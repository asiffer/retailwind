from click.testing import CliRunner

from retailwind.__main__ import main


def test_main_raw(test_css_file):
    runner = CliRunner()
    result = runner.invoke(main, ["-c", test_css_file, "-r", "tz"])
    assert result.stdout.strip() == "max-w-6xl"


def test_main_interactive(test_css_file):
    runner = CliRunner()
    runner.invoke(main, ["-c", test_css_file, "-i"])
