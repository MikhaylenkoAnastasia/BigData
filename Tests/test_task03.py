import pytest

import HW4.hw4_task_03


@pytest.mark.parametrize(["data"],
                         [
                             ["error: file not found"]
                         ])
def test_stderr(data, capsys):
    HW4.hw4_task_03.my_precious_logger(data)
    err = capsys.readouterr()
    assert 'error: file not found' in err.err


@pytest.mark.parametrize(["data"],
                         [
                             ["Solnishko is beautiful"]
                         ])
def test_stderr(data, capsys):
    HW4.hw4_task_03.my_precious_logger(data)
    out = capsys.readouterr()
    assert 'Solnishko is beautiful' in out.out
