import pytest

import HW4.hw4_task_05


@pytest.mark.parametrize("data", "5")
def test_positive(data):
    expected_res = ["1", "2", "fizz", "4", "buzz"]
    assert list(HW4.hw4_task_05.fizzbuzz(int(data))) == expected_res


@pytest.mark.parametrize("data", "7")
def test_negative(data):
    expected_res = ["1", "2", "fizz", "4", "buzz"]
    assert not list(HW4.hw4_task_05.fizzbuzz(int(data))) == expected_res
