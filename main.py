class Student:

    def __init__(self, name, surname, gender):
        self.courses_in_prorgess = None
        self.name = name
        self.surname = surname
        self.gender = gender
        self.finished_courses = []
        self.courses_in_progress = []
        self.grades = {}


    def __str__(self):
        grades_count = 1
        courses_in_progress_string = ','.join(self.courses_in_progress)
        finished_courses_string = ','.join(self.finished_courses)
        for k in self.grades:
            grades_count += len(self.grades[k])
            self.average_rating = sum(map(sum, self.grades.values())) / grades_count
        res = f'Имя: {self.name}\n' \
              f'Фамилия: {self.surname}\n' \
              f'Средняя оценка за домашнее задание: {self.average_rating}\n' \
              f'Курсы в процессе обучения: {courses_in_progress_string}\n' \
              f'Завершенные курсы: {finished_courses_string}'
        return res

    def rate_hw(self, lecturer, course, grade):
        if isinstance(lecturer, Lecturer) and course in self.courses_attached and course in lecturer.courses_in_progress:
            if course in lecturer.grades:
                lecturer.grades[course] += [grade]
            else:
                lecturer.grades[course] = [grade]
        else:
            return 'Ошибка'

    def __lt__(self, other):
        if not isinstance(other, Student):
            print('Такое сравнение некорректно')
            return
        return self.average_rating < other.average_rating
    def __eq__(self, other):
        if not isinstance(other, Student):
            raise Exception('Такое сравнение некорректно')
        return self.average_rating == other.average_rating

    def __le__(self, other):
        if not isinstance(other, Student):
            raise Exception('Такое сравнение некорректно')
        return self.average_rating <= other.average_rating

class Mentor:
    def __init__(self):
        self.grades = {}
        super(Mentor, self).__init__()

    def __str__(self):
        grades_count = 1
        for k in self.grades:
            grades_count += len(self.grades[k])
        self.average_rating = sum(map(sum, self.grades.values())) / grades_count
        res = f'Имя: {self.name}\nФамилия: {self.surname}\nСредняя оценка за лекции: {self.average_rating}'
        return res


class Lecturer(Mentor):
    def __init__(self):
        super(Mentor, self).__init__()
        self.average_rating = float()
        self.grades = {}

    def __repr__(self):
        grades_count = 0
        if not self.grades:
            return 0
        k=[]
        for k in grades.values():
            grades_count += len(self.grades[k])
        self.average_rating = sum(map(sum, self.grades.values())) / grades_count
        res = f'Имя: {self.name}\nФамилия: {self.surname}\nСредняя оценка за лекции: {self.average_rating}'
        return res

    def __lt__(self, other):
        if not isinstance(other, Lecturer):
            print('Такое сравнение некорректно')
            return
        return self.average_rating < other.average_rating

    def __eq__(self, other):
        if not isinstance(other, Student):
            raise Exception('Такое сравнение некорректно')
        return self.average_rating == other.average_rating

    def __le__(self, other):
        if not isinstance(other, Student):
            raise Exception('Такое сравнение некорректно')
        return self.average_rating <= other.average_rating

class Reviewer(Mentor):
    def __init__(self, name, surname):
        super().__init__(name, surname)
        self.courses_attached = []

    def rate_hw(self, student, course, grade):
        if isinstance(student, Student) and course in self.courses_attached and course in student.courses_in_progress:
            if course in student.grades:
                student.grades[course] += [grade]
            else:
                student.grades[course] = [grade]
        else:
            return 'Ошибка'

    def __str__(self):
        res = f'Имя: {self.name}\nФамилия: {self.surname}'
        return res

best_student = Student('Ruoy', 'Eman', 'your_gender')
best_student.courses_in_progress += ['Python']
best_student.finished_courses += ['Введение в программирование']

best_student_1 = Student('Ivan', 'Sidorova', 'your_gender')
best_student_1.courses_in_progress += ['Python']
best_student_1.finished_courses += ['Введение в программирование']

best_lecturer = Lecturer('Bob', 'Ivanov')
best_lecturer.courses_attached += ['Python']

best_lecturer_1 = Lecturer('Mit', 'Petrov')
best_lecturer_1.courses_attached += ['Python']

cool_reviewer_1 = Reviewer('Some', 'Buddy')
cool_reviewer_1.courses_attached += ['Python']

cool_reviewer = Reviewer('Bot', 'Roy')
cool_reviewer.courses_attached += ['Python']

best_student.rate_hw(best_lecturer, 'Python', 10)
best_student.rate_hw(best_lecturer, 'Python', 9)
best_student.rate_hw(best_lecturer, 'Python', 8)

best_student_1.rate_hw( best_lecturer_1, 'Python', 10)
best_student_1.rate_hw( best_lecturer_1, 'Python', 9)
best_student_1.rate_hw( best_lecturer_1, 'Python', 8)

cool_reviewer.rate_hw(best_student, 'Python', 10)
cool_reviewer.rate_hw(best_student, 'Python', 9)
cool_reviewer.rate_hw(best_student, 'Python', 8)

cool_reviewer_1.rate_hw(best_student_1, 'Python', 10)
cool_reviewer_1.rate_hw(best_student_1, 'Python', 9)
cool_reviewer_1.rate_hw(best_student_1, 'Python', 8)

print(f'Перечень студентов:\n\n{best_student}\n\n{best_student_1}')
print()
print()

print(f'Перечень лекторов:\n\n{best_lecturer}\n\n{best_lecturer_1}')
print()
print()

print(f"Результат сравнения студентов (по средним оценкам за ДЗ): "
      f"{best_student.name} {best_student.surname} < {best_student_1.name} {best_student_1.surname}" == min('{best_student > best_student_1}'))
print()

print(f'Результат сравнения лекторов (по средним оценкам за лекции): '
      f'{best_lecturer.name} {best_lecturer.surname} < {best_lecturer_1.name} {best_lecturer_1.surname}' == min('{best_lecturer>  best_lecturer_1}'))
print()

student_list = [best_student, best_student_1]
lecturer_list = [best_lecturer, best_lecturer_1]

def average_grade_on_the_course(persons, course):
    if not isinstance(persons, list):
        return "Not list"
    all_average_grade = []
    for person in persons:
        all_average_grade.extend(person.average_grade_course.get(course, []))
    if not all_average_grade:
        return "По такому курсу ни у кого нет оценок"
    return round(sum(all_average_grade) / len(all_average_grade)
                 
print(f"Средняя оценка для всех студентов по курсу {'Python'}: {student_rating(student_list, 'Python')}")
print()

print(f"Средняя оценка для всех лекторов по курсу {'Python'}: {student.gradesg(lecturer_list, 'Python')}")
print()
Footer

