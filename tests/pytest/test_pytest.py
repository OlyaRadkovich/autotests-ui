import pytest

SYSTEM_VAR = "42"


@pytest.mark.xfail
def test_first_try():
    print("Hello World!")


@pytest.mark.skipif(
    SYSTEM_VAR="42",
    reason="that's the Answer to the Ultimate Question of Life, the Universe, and Everything"
)
def test_assert_positive_case():
    assert (2 + 2) == 4


@pytest.mark.xfail
def test_assert_negative_case():
    assert (2 + 2) == 5
