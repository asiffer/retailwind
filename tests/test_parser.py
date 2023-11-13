from retailwind.parser import (
    normalize_color,
    normalize_size,
    normalize_space,
    parse_css,
    rgb_to_html,
)


def test_rgb_to_html():
    for rgb in [
        "rgb(253 224 71)",
        "rgb(253, 224, 71)",
        "rgb(253 224 71 / 1)",
        "rgb(253, 224, 71, 1)",
    ]:
        html = rgb_to_html(rgb)
        assert html == "#fde047ff"

    for rgb in [
        "rgb(253 224 71 / 0.8)",
        "rgb(253, 224, 71, 0.8)",
    ]:
        html = rgb_to_html(rgb)
        assert html == "#fde047cc"


def test_normalize_space():
    r = "sfkl  e dzf 999    à_u ioav'  ov"
    n = normalize_space(r)
    assert "  " not in n


def test_normalize_color():
    value0 = "0 1px 3px 0 #0000001a, 0 1px 2px -1px #0000001a"
    assert normalize_color(value0) == value0

    value1 = "0 1px 3px 0 rgb(0, 0, 0, 0.1), 0 1px 2px -1px rgb(0, 0, 0, 0.1)"
    assert normalize_color(value1) == value0


def test_normalize_size():
    assert normalize_size("0.5") == ".5"
    assert normalize_size("0px") == "0"
    assert normalize_size("0rem") == "0"
    assert normalize_size("-0.5") == "-.5"


def test_parser_percent(percent_rule):
    style = parse_css(percent_rule)
    assert len(style) == 1


def test_parser_var(var_rule):
    style = parse_css(var_rule)
    assert len(style) == 1


def test_parser_size(size_rule):
    style = parse_css(size_rule)
    assert len(style) == 4


def test_parser_negative(negative_rule):
    style = parse_css(negative_rule)
    assert len(style) == 2


def test_parser_color(color_rule):
    style = parse_css(color_rule)
    assert len(style) == 3
