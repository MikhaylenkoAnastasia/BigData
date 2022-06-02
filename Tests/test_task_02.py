from HW7.hw6_task_02 import backspace_compare
import pytest


@pytest.mark.parametrize(('first', 'second', 'result'), (('a#d', 'a#d#b#d', 'd'),
                                                         ('a#d', 'a##d', 'd'),
                                                         ('aaa##d', 'a#d#b#ad', 'ad'),
                                                         ('###ok#k', '##bla###o#okk#', 'ok')))
def test_backspace_compare_positive(first, second, result):
    assert backspace_compare(first, second) == f"Output: True\nExplanation: both s and t become '{result}'"
