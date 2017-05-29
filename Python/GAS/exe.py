from Tool import *
from GAS import *
a = text_importer('sample.txt')
arxiv = auto_grader(a)
weight = [3, 3, 4]
print(arxiv.average_grade(weight))
