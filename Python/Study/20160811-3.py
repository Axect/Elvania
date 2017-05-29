
# coding: utf-8

# # 2016 08 11 Study

# ## Read

# In[1]:




# In[2]:

from sys import argv


# In[ ]:

script, filename = argv
prompt = '> '

txt = open(filename)

print "파일  %r의 내용:" % filename
print txt.read()

print "파일 이름을 다시 입력해 주세요."
file_again = raw_input(prompt)

txt_again = open(file_again)

print txt_again.read()

