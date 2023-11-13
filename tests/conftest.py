import os
from pathlib import Path

import pytest

TEST_DIR = Path(__file__).parent


@pytest.fixture
def test_css_file():
    return TEST_DIR / "compiled.css"


@pytest.fixture
def default_compiled_css(test_css_file):
    return open(test_css_file, "r", encoding="utf-8").read()


@pytest.fixture
def percent_rule() -> str:
    return r"""
.uz {
  transform-origin: 100% 100%;
}
"""


@pytest.fixture
def var_rule() -> str:
    return r"""
.ux {
  border-spacing: var(--tw-border-spacing-x) var(--tw-border-spacing-y);
}
"""


@pytest.fixture
def size_rule() -> str:
    return r"""
.so {
  width: 150vw;
}

.to {
  width: 1px;
}

.tl {
  width: 90rem;
}

.bbf {
  opacity: 0.9;
}
"""


@pytest.fixture
def negative_rule() -> str:
    return r"""
.it {
  margin-top: -4rem;
}

.bbg {
  opacity: -0.45;
}
"""


@pytest.fixture
def color_rule() -> str:
    return r"""
.agy {
  border-color: #0000;
}

.aha {
  border-color: #ffffff1a;
}

.ahf {
  --tw-border-opacity: 1;
  border-bottom-color: rgb(229 231 235 / var(--tw-border-opacity));
}
"""


@pytest.fixture
def all_rules():
    return [percent_rule, var_rule, negative_rule, color_rule]
