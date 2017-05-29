
# coding: utf-8

# # 2016 08 11 Study

# ## Read and Write

# In[1]:




# In[12]:

from sys import argv
import numpy as np


# In[ ]:

script, filename = argv

print "%r 파일을 지우려 합니다." % filename
print "취소하려면 CTRL-C(^C)를 누르세요."
print "진행하려면 리턴을 누르세요."

raw_input("?")

print "파일 여는 중..."
target = open(filename, 'w')

print "파일 내용을 지웁니다. 안녕히!"
target.truncate()

print "이제 세 줄에 들어갈 내용을 묻겠습니다."
for i in range(0,3):
    locals()['line'+str(i+1)] = raw_input(str(i)+'> ')

print "이 내용을 파일에 씁니다."

for i in range(0,3):
    target.write(locals()['line'+str(i+1)])
    target.write('\n')

print "마지막으로 닫습니다."
target.close()

