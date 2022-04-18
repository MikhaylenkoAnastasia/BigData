import pytest
import HW6.hw6_task_01 as T1

user = T1.User()


def test_classname():
    assert user.__class__.__name__ == 'Counter'


def test_instances():
    assert user.counter == 1


def test_instances_up():
    _, _, _ = T1.User(), T1.User(), T1.User()
    assert user.counter == 4


def test_instances_reset():
    user.reset_instances_counter()
    assert user.counter == 0
