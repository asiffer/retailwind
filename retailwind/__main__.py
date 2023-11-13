from typing import Optional

import click
import requests

from retailwind.interactive import ReTailwindApp
from retailwind.tailwind import CSS
from retailwind.translator import Translator


def get_css(src: str):
    """Open css file"""
    if src.startswith("http://") or src.startswith("https://"):
        response = requests.get(src, timeout=5)
        if response.status_code != 200:
            raise RuntimeError(response.content)
        return response.content.decode()
    return open(src, "r", encoding="utf-8").read()


@click.command()
@click.option(
    "-c",
    "--css",
    help="Stylesheet of the html page that contains the obfuscated classes",
    required=True,
)
@click.option(
    "-r",
    "--raw",
    help="Raw class(es) (or HTML fragment) to deobfuscate",
    type=str,
    default=None,
)
@click.option(
    "-t",
    "--tailwind-css",
    type=str,
    help="Tailwind stylesheet different from the builtin one",
)
@click.option(
    "-i",
    "--interactive",
    is_flag=True,
    help="Run in interactive mode",
)
def main(
    css: str = "",
    raw: Optional[str] = None,
    tailwind_css: Optional[str] = None,
    interactive: bool = False,
):
    """Command entrypoint"""
    compiled = get_css(css)

    tailwind = CSS
    if tailwind_css is not None:
        tailwind = get_css(tailwind_css)

    # build the translator
    translator = Translator(
        compiled=compiled,
        tailwind=tailwind,
        on_error="ignore",
    )

    # cli run
    if not interactive:
        assert isinstance(raw, str)
        print(translator.html(raw))
        return

    # interactive run
    ReTailwindApp(translator).run()


if __name__ == "__main__":
    main()
