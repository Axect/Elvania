# coding: utf-8

# # 2016 08 11 Study

# ## Function & File

# In[1]:

from sys import argv


# In[2]:

script, input_file = argv

def print_all(f):
    print f.read()
    
def rewind(f):
    f.seek(0)
    
def print_a_line(line_count, f):
    print line_count, f.readline()

current_file = open(input_file)

print "파일 전체를 출력해 봅시다.\n"

print_all(current_file)

print "이번에는 테이프처럼 되감아 봅시다."

rewind(current_file)

print "세 줄을 출력해 봅시다."

current_line = 1

for i in range(1,4):
    print_a_line(current_line,current_file)
    current_line = current_line + 1



