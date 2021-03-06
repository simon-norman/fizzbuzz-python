import pytest
from fizzbuzz import fizzbuzz


@pytest.mark.unittest
def test_returns_number():
    assert fizzbuzz(4) == 4


@pytest.mark.unittest
def test_returns_fizz_on_3():
    assert fizzbuzz(3) == 'fizz'


@pytest.mark.unittest
def test_returns_fizz_on_mult_of_3():
    assert fizzbuzz(36) == 'fizz'


@pytest.mark.unittest
def test_returns_buzz_on_5():
    assert fizzbuzz(5) == 'buzz'


@pytest.mark.unittest
def test_returns_buzz_on_mult_of_5():
    assert fizzbuzz(25) == 'buzz'


@pytest.mark.unittest
def test_returns_fizzbuzz_on_mult_3_and_5():
    assert fizzbuzz(15) == 'fizzbuzz'