from hashlib import sha256
from typing import Dict, Literal, Tuple

from bs4 import BeautifulSoup, Tag
from bs4.formatter import Formatter

from retailwind.parser import Stylesheet, parse_css
from retailwind.tailwind import CSS


def hash_rule(props: Dict[str, str]) -> str:
    buffer = " ".join(f"{k}:{props[k]}" for k in sorted(props.keys()))
    return sha256(buffer.encode()).hexdigest()[:10]


def reverse_index(style: Stylesheet, hash_as_key: bool = True):
    hm = {}
    for cl, rules in style.items():
        h = hash_rule(rules)
        if h in hm:
            pass
            # print("warning: key already exist", cl, rules, h)
        if hash_as_key:
            hm[h] = cl
        else:
            hm[cl] = h

    return hm


class Translator:
    pseudo_classes = ["hover", "focus", "focus-visible"]

    def __init__(
        self,
        compiled: str,
        tailwind: str = CSS,
        on_error: Literal["raise", "mark", "ignore"] = "mark",
    ) -> None:
        self.tailwind_css = parse_css(tailwind)
        self.compiled_css = parse_css(compiled)

        self.ht = reverse_index(self.tailwind_css)
        self.hc = reverse_index(self.compiled_css, False)

        self.on_error = on_error

    def __raw_single_key(
        self,
        key: str,
    ) -> str:
        cl = key
        pc = ""

        if not cl.startswith("."):
            cl = "." + key

        if cl not in self.hc:
            for pc in self.pseudo_classes:
                if f"{cl}:{pc}" in self.hc:
                    cl = f"{cl}:{pc}"
                    pc = f"{pc}:"
                    break

        if cl not in self.hc:
            if self.on_error == "raise":
                raise KeyError(f"unknown class {key}")
            elif self.on_error == "mark":
                return f"!{key}"
            elif self.on_error == "ignore":
                return key
        try:
            return pc + self.ht[self.hc[cl]].removeprefix(".")
        except KeyError as err:
            if self.on_error == "raise":
                raise err
            elif self.on_error == "mark":
                return f"?{key}"
            elif self.on_error == "ignore":
                return key

    def raw(
        self,
        key_or_class: str,
        *others: str,
    ) -> str | Tuple[str, ...]:
        """Translate input class(es)

        The translator may fail. In this case, three behaviors can be used:
        - raise: the program raises an exception
        - mark: classes not found in the input css are prepend with a '!' (kind of error, it probably means that the provided stylesheet is not complete).
                Classes not found in tailwind.css are prepend with a '?' (it means that some classes are missing in the reference stylesheet).
        - ignore: initial classes are kept
        """
        keys = key_or_class.strip().split(" ")
        out = " ".join(self.__raw_single_key(k) for k in keys if len(k) > 0)
        if len(others) > 0:
            return out, *self.raw(*others)
        return out

    def html(self, html_or_str_input: str) -> str:
        """Replace obfuscated classes with tailwind ones on a HTML fragment"""
        soup = BeautifulSoup(html_or_str_input, "html.parser")
        if not soup.find():
            return "".join(self.raw(soup.get_text()))

        def recursive_re(tag: Tag):
            if "class" in tag.attrs:
                tag.attrs["class"] = [self.raw(c) for c in tag.attrs["class"]]  # type: ignore
            for c in tag.children:
                if isinstance(c, Tag):
                    recursive_re(c)

        recursive_re(soup)
        return str(soup)

    def prettify(self, html: str) -> str:
        """ """
        soup = BeautifulSoup(html, "html.parser")
        return soup.prettify(formatter=Formatter(indent=4))
