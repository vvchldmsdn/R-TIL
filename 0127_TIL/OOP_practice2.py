from random import random


import random

class ClassHelper:

    def __init__(self, students):
        self.students = students

    def pick(self, n):
        return random.sample(self.students, n)

    def match_pair(self):
        pair = []
        while len(self.students) > 3:
            tmp = ClassHelper.pick(self, 2)
            pair.append(tmp)
            for student in tmp:
                self.students.remove(student)
        pair.append(self.students)
        return pair

ch = ClassHelper(['김싸피', '이싸피', '조싸피', '박싸피', '정싸피'])
print(ch.match_pair())
print(ch.pick(1))