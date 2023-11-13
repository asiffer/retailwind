import pytest

from retailwind.interactive import ReTailwindApp
from retailwind.translator import Translator


@pytest.mark.asyncio
async def test_interactive(default_compiled_css):
    tr = Translator(compiled=default_compiled_css)
    async with ReTailwindApp(tr).run_test() as pilot:
        # leave key
        await pilot.press("ctrl+c")
