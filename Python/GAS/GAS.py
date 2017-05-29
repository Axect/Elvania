#-*- coding: utf-8 -*-
from collections import namedtuple
from collections import defaultdict
Grade = namedtuple('Grades',('score', 'weight'))


def fake():
    pass

class Subject(object):
    def __init__(self):
        self._grade = []
        self.count = 0
        
    def Gen(self):
        self.count += 1
        return self.count
    
    def Clear(self):
        self.count = 0
    
    def report_grade(self, score, weight):
        index = (self.Gen(),) # Auto index tuple
        tuples = Grade(score, weight) + index
        self._grade.append(tuples)
        
    def grade_recorder(self):
        total, total_weight = 0, 0
        for score, weight, _ in self._grade:
            total += score * weight
            total_weight += weight
        return [total / total_weight, total_weight]
    
    def Test(self):
        self.grade = self._grade
        print(self.grade)
        

class Year(object):
    def __init__(self):
        self._subjects = {}
    
    def subject(self, name):
        if name not in self._subjects:
            print('Insert %s is complete!' % name)
            self._subjects[name] = Subject() # All values in self._subjects are Subject class!
        return self._subjects[name]
    
    def average_grade(self):
        Fscore, Ftotal_weight = 0, 0
        for subject in self._subjects.values():
            Fscore += subject.grade_recorder()[0] * subject.grade_recorder()[1]
            Ftotal_weight += subject.grade_recorder()[1]
        return Fscore / Ftotal_weight
    
    
def weight_input(weight):
    if len(weight) == 3:
        return weight
    else:
        raise ValueError()

        
class UniV(object):
    def __init__(self):
        self._years = {}
        
    def year(self, level):
        if level not in self._years:
            print('Insert %s is complete!' % level)
            self._years[level] = Year() # All values in self._years are Year class!
        return self._years[level]
    
    def average_grade(self, weight):
        total = 0
        for i, year in enumerate(self._years.values()):
            total += year.average_grade() * weight[i]
        return total / sum(weight)