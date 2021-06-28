import random

class Student:
    def __init__(self, name, surname, gender):
        self.name = name
        self.surname = surname
        self.gender = gender
        self.finished_courses = []
        self.courses_in_progress = []
        self.grades = {}
    def rate_lecturer(self, lecturer, grade, course):
        if isinstance(lecturer, Lecturer) and grade in range(1,11) and (course in self.courses_in_progress or course in self.finished_courses):
            if course in lecturer.courses_attached:
                lecturer.grades.setdefault(course, []).append(grade)
            else:
                return 'Ошибка'
        else:
            return 'Ошибка'
    def get_middle_rate(self, course = 'all'):
        if course == 'all':
            grades_list = []
            for value in self.grades.values():
                grades_list += value
            if len(grades_list) == 0:
                return 0
            else:
                return round(sum(grades_list) / len(grades_list) ,2)
        else:
            if course not in self.grades.values():
                return 0
            else:
                if len(self.grades[course]) == 0:
                    return 0
                else:
                    return round(sum(self.grades[course]) / len(self.grades[course]), 2)

    def __str__(self):
        middle_rate_homework = self.get_middle_rate()
        current_courses = ', '.join(self.courses_in_progress)
        last_courses = ','.join(self.finished_courses)
        return f'Имя: {self.name}\nФамилия: {self.surname}\nСредняя оценка за домашние задания: {self.get_middle_rate()}\nКурсы в процессе изучения: {current_courses}\nЗавершенные курсы: {last_courses}'
    # and course in lecturer.courses_attached and course in student.courses_in_progress:

    def __lt__(self, other):
        if isinstance(other, Student):
            self_middle_grade = self.get_middle_rate()
            other_middle_grade = other.get_middle_rate()
            return self_middle_grade < other_middle_grade
        else:
            return 'Achtung!!! Ошибка!!!'

    def __le__(self, other):
        if isinstance(other, Student):
            self_middle_grade = self.get_middle_rate()
            other_middle_grade = other.get_middle_rate()
            return self_middle_grade <= other_middle_grade
        else:
            return 'Achtung!!! Ошибка!!!'

    def __eq__(self, other):
        if isinstance(other, Student):
            self_middle_grade = self.get_middle_rate()
            other_middle_grade = other.get_middle_rate()
            return self_middle_grade == other_middle_grade
        else:
            return 'Achtung!!! Ошибка!!!'

    def __ne__(self, other):
        if isinstance(other, Student):
            self_middle_grade = self.get_middle_rate()
            other_middle_grade = other.get_middle_rate()
            return self_middle_grade != other_middle_grade
        else:
            return 'Achtung!!! Ошибка!!!'
    def __gt__(self, other):
        if isinstance(other, Student):
            self_middle_grade = self.get_middle_rate()
            other_middle_grade = other.get_middle_rate()
            return self_middle_grade > other_middle_grade
        else:
            return 'Achtung!!! Ошибка!!!'
    def __ge__(self, other):
        if isinstance(other, Student):
            self_middle_grade = self.get_middle_rate()
            other_middle_grade = other.get_middle_rate()
            return self_middle_grade >= other_middle_grade
        else:
            return 'Achtung!!! Ошибка!!!'

class Mentor:
    def __init__(self, name, surname):
        self.name = name
        self.surname = surname
        self.courses_attached = []
    def __str__(self):
        return f'Имя: {self.name} \nФамилия: {self.surname}'
    # def rate_hw(self, student, course, grade):
    #     if isinstance(student, Student) and course in self.courses_attached and course in student.courses_in_progress:
    #         if course in student.grades:
    #             student.grades[course] += [grade]
    #         else:
    #             student.grades[course] = [grade]
    #     else:
    #         return 'Ошибка'

class Lecturer(Mentor):
    def __init__(self, name, surname):
        super().__init__(name, surname)
        self.grades = dict()

    def middle_grade(self, current_course = 'all'):
        if current_course == 'all':
            grades_list = []
            for value in self.grades.values():
                grades_list += value
            if len(grades_list) == 0:
                return 0
            else:
                return round(sum(grades_list) / len(grades_list),2)
        else:
            if current_course in self.grades.keys():
                grades_number = len(self.grades[current_course])
                if grades_number == 0:
                    return 0
                else:
                    return round(sum(self.grades[current_course]) / grades_number, 2)
            else:
                return 0
    def __str__(self):
        return(f'Имя: {self.name} \nФамилия: {self.surname} \nСредняя оценка за лекции: {self.middle_grade()}')

    def __lt__(self, other):
        if isinstance(other, Lecturer):
            self_middle_grade = self.middle_grade()
            other_middle_grade = other.middle_grade()
            return self_middle_grade < other_middle_grade
        else:
            return 'Achtung!!! Ошибка!!!'
    def __le__(self, other):
        if isinstance(other, Lecturer):
            self_middle_grade = self.middle_grade()
            other_middle_grade = other.middle_grade()
            return self_middle_grade <= other_middle_grade
        else:
            return 'Achtung!!! Ошибка!!!'
    def __eq__(self, other):
        if isinstance(other, Lecturer):
            self_middle_grade = self.middle_grade()
            other_middle_grade = other.middle_grade()
            return self_middle_grade == other_middle_grade
        else:
            return 'Achtung!!! Ошибка!!!'
    def __ne__(self, other):
        if isinstance(other, Lecturer):
            self_middle_grade = self.middle_grade()
            other_middle_grade = other.middle_grade()
            return self_middle_grade != other_middle_grade
        else:
            return 'Achtung!!! Ошибка!!!'
    def __gt__(self, other):
        if isinstance(other, Lecturer):
            self_middle_grade = self.middle_grade()
            other_middle_grade = other.middle_grade()
            return self_middle_grade > other_middle_grade
        else:
            return 'Achtung!!! Ошибка!!!'
    def __ge__(self, other):
        if isinstance(other, Lecturer):
            self_middle_grade = self.middle_grade()
            other_middle_grade = other.middle_grade()
            return self_middle_grade >= other_middle_grade
        else:
            return 'Achtung!!! Ошибка!!!'


class Reviewer(Mentor):

    def __init__(self, name, surname):
        super().__init__(name, surname)

    def rate_hw(self, student, course, grade):
        if isinstance(student, Student) and course in self.courses_attached and course in student.courses_in_progress:
            if course in student.grades:
                student.grades[course] += [grade]
            else:
                student.grades[course] = [grade]
        else:
             return 'Ошибка'

def get_common_homework_middle_rate_(students_list, course):
    common_grade_list = []
    for student in students_list:
        if isinstance(student, Student):
            common_grade_list += student.get_middle_rate(course)
        else:
            return 'error'
    if len(common_grade_list) != 0:
        return round(sum(common_grade_list) / len(common_grade_list), 2)
    else:
        return 0

def get_common_lectures_middle_grade(lecturers_list, course):
    common_grade_list = []
    for lecturer in lecturers_list:
        if isinstance(lecturer, Lecturer):
            common_grade_list += lecturer.middle_grade(course)
        else:
            return 'error'

    if len(common_grade_list) != 0:
        return round(sum(common_grade_list) / len(common_grade_list) ,2)
    else:
        return 0


def create_random_student(name_list, surname_list):
    rand_name = random.choice(name_list)
    rand_surname = random.choice(surname_list)
    random_student = Student(rand_name, rand_surname, 'Male')

    random_student.finished_courses = ['Java', 'English']
    random_student.courses_in_progress = ['Python']
    for i in range(1,11):
        random_student.grades.setdefault('Java', []).append(random.randint(1, 10))
        random_student.grades.setdefault('English', []).append(random.randint(1, 10))
        random_student.grades.setdefault('Python', []).append(random.randint(1, 10))
    return random_student

def create_random_lecturer(name_list, surname_list, courses_list):
    rand_name = random.choice(name_list)
    rand_surname = random.choice(surname_list)
    random_lecturer = Lecturer(rand_name, rand_surname)
    for i in range(1,4):
        rand_course = random.choice(courses_list)
        random_lecturer.courses_attached.append(rand_course)
        for grade in range(1,10):
            random_lecturer.grades.setdefault(rand_course,[]).append(random.randint(1,10))
    return random_lecturer

def create_random_reviewer(name_list, surname_list, courses_list):
    rand_name = random.choice(name_list)
    rand_surname = random.choice(surname_list)
    random_reviewer = Reviewer(rand_name, rand_surname)
    for i in range(1,4):
        rand_course = random.choice(courses_list)
        random_reviewer.courses_attached.append(rand_course)

    return random_reviewer



if __name__ == '__main__':

    name_list = ['Dima', 'Kolya', 'Petya', 'Vasya', 'Andrey', 'Nikita', 'Oleg', 'Sasha', 'Karen', 'Homer', 'Liza',
                 'Bart', 'Sub-zero', 'Vova', 'Anton', 'Terminator']
    surname_list = ['Petrov', 'Simpson', 'Ivanov', 'Sidorov', 'Popov', 'Glushkov', 'Maksimov', 'Aleksandrov', 'Belyaev',
                    'Shatov']
    courses_list = ['Java', 'Fighting', 'Python', 'English', 'Cooking']
    student1 = create_random_student(name_list, surname_list)
    student2 = create_random_student(name_list, surname_list)
    lecturer1 = create_random_lecturer(name_list, surname_list, courses_list)
    lecturer2 = create_random_lecturer(name_list, surname_list, courses_list)
    mentor1 = create_random_reviewer(name_list, surname_list, courses_list)
    mentor2 = create_random_reviewer(name_list, surname_list, courses_list)
    print(f'============================\nStudents')
    print(student1)
    print(student2)

    print(f'============================\nLecturers')
    print(lecturer1)
    print(lecturer2)

    print(f'============================\nMentors')
    print(mentor1)
    print(mentor2)



