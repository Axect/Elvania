# -*- coding: utf-8 -*-

from Three_room import *
from time import sleep

def start():
    print "시작 위치를 지정합니다."
    E = Engine()
    init_point = E.init_point()
    print "시작 위치는"
    print "%s 입니다." % init_point
    print "%s 로 들어갑니다." % init_point
    # first point 는 A,B,C 클래스 중의 하나를 객체화 시킨 객체.
    first_point = Map.room_dict[init_point] 
    print "움직일 수 있는 방은 다음과 같습니다."    
    first_point.enter() # 고로 enter를 상속받았음.
    
    for i in range(0,5):
        print "이동하시겠습니까? Y or N"
        OK = raw_input('>')
        
        if OK == 'Y':
            print "어디로 움직이시겠습니까?"
            # move도 상속되었기에 역시 가능. move의 반환값이 A~C의 
            # 객체이므로 또 지정 가능.
            first_point = first_point.move() 
            print "움직일 수 있는 방은 다음과 같습니다."   
            first_point.enter() # 같은 이유로 enter도 상속됨.
        elif OK == 'N':
            print "편안히 쉬십시오."
            sleep(3)
            print "현재 위치는"
            first_point.enter()
        else:
            print "Error"
            break

start()
