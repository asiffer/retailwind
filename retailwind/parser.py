import re
from typing import Dict

CLASSNAME_PATTERN = r"[.][a-z0-9-.:>~ )(\]\[]+"
KEY_PATTERN = r"[a-z-]+"
VALUE_PATTERN = r"[a-z0-9# )(-/%]+"
KEY_VALUE_PATTERN = rf"({KEY_PATTERN}):\s+({VALUE_PATTERN});"

# KEY_VALUE = re.compile(r"([a-z-]+):\s+([a-z0-9# )(-/%]+);")
# RULE = re.compile(
# r"([.][a-z0-9-.:>~ )(\]\[]+)\s+{(\s+[a-z-]+:[a-z0-9# )(-/%]+;)+\s*}"
# )
KEY_VALUE = re.compile(KEY_VALUE_PATTERN)
RULE = re.compile(
    rf"({CLASSNAME_PATTERN})"
    + r"\s*{"
    + rf"(\s*{KEY_PATTERN}:\s+{VALUE_PATTERN};)+"
    + r"\s*}"
)
DECIMAL = re.compile(r"0([.][0-9]+)")
SPACES = re.compile(r"\s+")

Stylesheet = Dict[str, Dict[str, str]]


def rgb_to_html(rgb_rule: str) -> str:
    rgb_rule = (
        rgb_rule.strip()
        .removeprefix("rgb(")
        .removesuffix(";")
        .removesuffix(")")
    )
    rgb_rule = rgb_rule.replace(",", " ").replace("/", " ")
    rgb_rule = SPACES.sub(" ", rgb_rule)

    args = rgb_rule.split(" ")
    if len(args) == 4:
        last = args.pop().strip()
        if last.endswith("%"):
            opacity = float(last.removesuffix("%")) / 100.0
        else:
            opacity = float(last)
    else:
        opacity = 1.0

    if len(args) != 3:
        raise RuntimeError("Bad color:", args)

    rgb = []
    for c in args:
        if c.endswith("%"):
            code = round(float(c.removesuffix("%")) * 2.55)
        else:
            code = int(c)
        rgb.append(code)

    # rgba
    rgb.append(round(opacity * 255))
    return "#" + "".join(hex(c).removeprefix("0x").rjust(2, "0") for c in rgb)


def normalize_key(key: str) -> str:
    if ">" in key:
        key = key.split(">")[0].strip()
    return key


def normalize_color(value: str) -> str:
    pattern = r"rgb("
    i = value.find(pattern)
    while i >= 0:
        j = value.find(")", i) + 1
        try:
            value = value[:i] + rgb_to_html(value[i:j]) + value[j:]
        except BaseException:  # pylint: disable=broad-exception-caught
            # do not replace
            pass
        i = value.find(pattern, j)
    return value


def normalize_size(value: str) -> str:
    if value.startswith("0."):
        value = value[1:]
    if value.startswith("-0."):
        value = "-" + value[2:]
    if value in ["0px", "0em", "0rem"]:
        value = "0"
    return value


def normalize_space(value: str) -> str:
    return SPACES.sub(" ", value)


def parse_css(raw: str) -> Stylesheet:
    # remove lines
    raw = raw.strip().replace("\n", "")
    css: Dict[str, Dict[str, str]] = {}
    for m in RULE.finditer(raw):
        key = m.group(1).strip()
        key = normalize_key(key)
        css[key] = {}
        for k in KEY_VALUE.finditer(m.group(0)):
            prop, value = k.groups()

            value = normalize_space(value)
            value = normalize_size(value)
            value = normalize_color(value)
            css[key][prop] = value

    return css
