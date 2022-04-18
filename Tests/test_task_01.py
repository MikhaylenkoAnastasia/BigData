import pytest
import HW5.hw5_task_01 as T1

teacher = T1.Teacher('Daniil', 'Shadrin')
student = T1.Student('Roman', 'Petrov')
homework = teacher.create_homework('create 2 simple classes', 5)


# Test Teacher
def test_teacher_classname():
    assert teacher.__class__.__name__ == T1.Teacher.__name__


def test_teacher_firstname():
    assert teacher.first_name == 'Daniil'


def test_teacher_secondname():
    assert teacher.last_name == 'Shadrin'


# Test Student
def test_student_classname():
    assert student.__class__.__name__ == T1.Student.__name__


def test_student_firstname():
    assert student.first_name == 'Roman'


def test_student_secondname():
    assert student.last_name == 'Petrov'


# Test Homework
def test_homework_classname():
    assert homework.__class__.__name__ == T1.Homework.__name__


def test_homework_task():
    assert homework.text == 'create 2 simple classes'


def test_homework_deadline():
    assert homework.deadline == 5


def test_homework_deadline_ok():
    assert student.do_homework(homework) == homework


def test_homework_deadline_fail(capsys):
    homework2 = teacher.create_homework('write a text', 0)
    student.do_homework(homework2)
    message = capsys.readouterr()
    assert message.out == 'You are late\n'
