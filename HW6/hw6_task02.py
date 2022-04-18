import datetime
from collections import defaultdict

class Homework:

    def init(self, text: str, deadline: datetime.timedelta):
        self.text = text
        self.deadline = datetime.timedelta(days=deadline)
        self.created = datetime.datetime.today()

    def is_active(self) -> bool:
        if datetime.datetime.today() < self.created + self.deadline:
            return True
        else:
            return False

class HomeworkResult:
    def init(self, homework: Homework, solution: str, author):
        if not isinstance(homework, Homework):
            raise TypeError('You gave a not Homework object')
        self.homework = homework
        self.solution = solution
        self.author = author
        self.created = datetime.datetime.today()

class Human:
    def init(self, first_name: str, last_name: str):
        self.first_name = first_name
        self.last_name = last_name

class Student(Human):
    def do_homework(self, hw: Homework, solution: str):
        if hw.is_active():
            return HomeworkResult(hw, solution, self)
        else:
            raise DeadlineError('You are late')

class Teacher(Human):
    homework_done = defaultdict()

    @classmethod
    def create_homework(cls, text: str, deadline: datetime.timedelta.days = datetime.timedelta(days=1)):
        hw = Homework(text, deadline)
        return hw

    @classmethod
    def check_homework(cls, homework_result: HomeworkResult):
        if len(homework_result.solution) > 5:
            Teacher.homework_done[homework_result.homework] = homework_result.solution
            return True
        else:
            return False

    @classmethod
    def reset_results(cls, homework: Homework = None):
        if homework is not None:
            Teacher.homework_done[homework.text] = None
        else:
            Teacher.homework_done.clear()
class DeadlineError(Exception):
    pass


if name == 'main':
    opp_teacher = Teacher('Daniil', 'Shadrin')
    advanced_python_teacher = Teacher('Aleksandr', 'Smetanin')

    lazy_student = Student('Roman', 'Petrov')
    good_student = Student('Lev', 'Sokolov')

    oop_hw = opp_teacher.create_homework('Learn OOP', 1)
    docs_hw = opp_teacher.create_homework('Read docs', 5)

    result_1 = good_student.do_homework(oop_hw, 'I have done this hw')
    result_2 = good_student.do_homework(docs_hw, 'I have done this hw too')
    result_3 = lazy_student.do_homework(docs_hw, 'done')
    try:
        result_4 = HomeworkResult(good_student, "fff", "Solution")
    except Exception:
        print('There was an exception here')
    opp_teacher.check_homework(result_1)
    temp_1 = opp_teacher.homework_done

    advanced_python_teacher.check_homework(result_1)
    temp_2 = Teacher.homework_done
    assert temp_1 == temp_2

    opp_teacher.check_homework(result_2)
    opp_teacher.check_homework(result_3)

    print(Teacher.homework_done[oop_hw])
    Teacher.reset_results()