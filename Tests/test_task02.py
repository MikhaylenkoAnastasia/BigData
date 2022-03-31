import os

import pytest

import HW4.hw4_task_02


@pytest.mark.parametrize(["data"],
                         [
                             [1.5], [2.0], [2.5], [1.0], [1.2], [2.4], [1.7]
                         ])
def test_positive(data):
    with open("data.txt", "w+") as file:
        file.write(str(data))
    assert HW4.hw4_task_02.read_magic_number("data.txt")
    os.remove("data.txt")
    assert not os.path.exists("data.txt")


@pytest.mark.parametrize(["data"],
                         [
                             [7.5], [22.5], [14.2]
                         ])
def test_negative(data):
    with open("data.txt", "w+") as file:
        file.write(str(data))
    assert not HW4.hw4_task_02.read_magic_number("data.txt")
    os.remove("data.txt")
    assert not os.path.exists("data.txt")


@pytest.mark.parametrize(["data"],
                         [
                             ["2.5"], [(1, 0)], [{"key1": "value1"}]
                         ])
def test_error(data):
    try:
        with open("data.txt", "w+") as file:
            file.write(str(data))
        HW4.hw4_task_02.read_magic_number("data.txt")
    except ValueError:
        assert ValueError
    os.remove("data.txt")
    assert not os.path.exists("data.txt")
