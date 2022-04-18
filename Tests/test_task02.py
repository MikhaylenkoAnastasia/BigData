import pytest
import HW6.hw6_task_02 as T2

opp_teacher = T2.Teacher('Daniil', 'Shadrin')
advanced_python_teacher = T2.Teacher('Aleksandr', 'Smetanin')

lazy_student = T2.Student('Roman', 'Petrov')
good_student = T2.Student('Lev', 'Sokolov')

oop_hw = opp_teacher.create_homework('Learn OOP', 1)
docs_hw = opp_teacher.create_homework('Read docs', 5)

result_1 = good_student.do_homework(oop_hw, 'I have done this hw')
result_3 = lazy_student.do_homework(docs_hw, 'done')


def test_classname_teacher():
    assert opp_teacher.__class__.__name__ == 'Teacher'


def test_classname_student():
    assert lazy_student.__class__.__name__ == 'Student'


def test_classname_homework():
    assert oop_hw.__class__.__name__ == 'Homework'


def test_classname_homeworkresult():
    assert result_1.__class__.__name__ == 'HomeworkResult'


def test_homework_task():
    assert oop_hw.text == 'Learn OOP'


def test_homework_deadline():
    assert oop_hw.deadline == 1


def test_homework_deadline_ok():
    assert result_3.__class__ == T2.HomeworkResult


def test_homework_deadline_fail():
    result_2 = advanced_python_teacher.create_homework('write a text', 0)
    try:
        fail_hw = good_student.do_homework(result_2, "Done hw")
    except Exception as e:
        assert e.__class__.__name__ == T2.DeadlineError.__name__
