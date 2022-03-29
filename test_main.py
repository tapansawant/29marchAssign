import main
import pytest


# @pytest.mark.skip()
@pytest.mark.xfail()
@pytest.mark.parametrize("num,output", [(5, False), (2, True), (10, False), (7, True)])
def test_CheckPrime(num, output):
    result = main.CheckPrime(num)
    assert result == output


@pytest.mark.parametrize("num,output", [(55, False), (2, True), (10, False), (77, True)])
def test_CheckPalindrome(num, output):
    result = main.CheckPalindrome(num)
    assert result == output

