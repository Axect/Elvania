
# -*- coding: utf-8 -*-

from sys import argv

script, filename = argv

print "%r 파일을 지우려 합니다." % filename
print "취소하려면 CTRL-C(^C)를 누르세요."
print "진행하려면 리턴을 누르세요."

raw_input("?")

print "파일 여는 중..."
target = open(filename, 'w')

print "파일 내용을 지웁니다. 안녕히!"
target.truncate() # 삭제입니다.

print "이제 세 줄에 들어갈 내용을 묻겠습니다."
line1 = raw_input('> ')
line2 = raw_input('> ')
line3 = raw_input('> ')

print "이 내용을 파일에 씁니다."

for i in range(0,3): # 파이썬은 index가 0부터 시작. 즉, 0부터 3미만까지 하라는 소리. 콜론과 들여쓰기는 필수입니다.
    target.write(locals()['line'+str(i+1)]) # 이건 몽몽이의 비밀병기!
    target.write('\n') # 줄 띄우기!

print "마지막으로 닫습니다."
target.close() # Close 하지 않으면 저장이 안됩니다.