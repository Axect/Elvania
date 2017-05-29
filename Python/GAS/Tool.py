# -*- coding: utf-8 -*-
from GAS import *
def text_importer(path):
    txt = open(path, 'r')
    copy = [line.strip() for line in txt]
    topy = [line.split(',') for line in copy]
    xopy = []
    cupy = []
    for List in topy:
        for word in List:
            cupy.append(word.strip())
        xopy.append(cupy)
        cupy = []   
    dopy_1 = {} 
    for List in xopy:
        dopy_1[List[0]] = List[1:]
    for i, key in enumerate(dopy_1):
        locals()['bopy_' + str(i)] = {}
        value = dopy_1[key]
        for word in value:
            k = word.split(':')
            for j, new in enumerate(k):
                t = new.strip()
                k[j] = t
            sw = k[1].split(';')
            for j, new in enumerate(sw):
                s = new.strip()
                sw[j] = s
            sw_tuple = (float(sw[0]), float(sw[1]))
            locals()['bopy_' + str(i)][k[0]] = sw_tuple
        dopy_1[key] = locals()['bopy_' + str(i)]
    return dopy_1


def auto_grader(dic):
    arxiv = UniV()
    for i, semester in enumerate(dic):
        locals()['sem_' + str(i)] = arxiv.year(semester)
        dic2 = dic[semester]
        for j, sub in enumerate(dic2):
            locals()['sub_' + str(j)] = locals()['sem_' + str(i)].subject(sub)
            dic3 = dic2[sub]
            score, weight = dic3[0], dic3[1]
            locals()['sub_' + str(j)].report_grade(score, weight)
    return arxiv