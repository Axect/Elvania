
# -*- coding: utf-8 -*-

from sys import exit

def gold_room():
    print "황금으로 가득 찬 방입니다. 얼마나 가져갈까요?"
    
    next = raw_input('>')
    if int(next) >= 0:
        how_much = int(next)
    else:
        dead("인간이여, 숫자 쓰는 법부터 배우세요.")
    
    if how_much < 50:
        print "좋아, 욕심부리지 않는군요. 당신이 이겼습니다!"
        exit(0)
    else:
        dead("욕심쟁이 얼간이 같으니!")

def bear_room():
    print """
    여기에는 곰이 한 마리 있습니다.
    곰은 꿀을 잔뜩 들고 있습니다.
    뚱뚱한 곰은 다른 쪽 문 앞에 있습니다.
    어떻게 곰을 움직이겠습니까?
    """
    
    bear_moved = False
    
    while True:
        next = raw_input(">")
        
        if next == "꿀 뺏기":
            dead("곰이 당신을 쳐다보더니 목이 떨어져라 따귀를 날립니다.")
        elif next == "곰 놀리기" and not bear_moved:
            print "곰이 문에서 비켜섰습니다. 이제 나갈 수 있습니다."
            bear_moved = True
        elif next == "곰 놀리기" and bear_moved:
            dead("곰이 머리 끝까지 열받아 당신의 다리를 씹어먹습니다.")
        elif next == "문 열기" and bear_moved:
            gold_room()
        else:
            print "무슨 말인지 모르겠네요."

def Todi_room():
    print """
    여기에는 토디 한 마리가 있습니다.
    토디는 아주 귀엽습니다.
    볼은 뽀똥하고 코는 귀여우며 팔은 뽀똥합니다.
    어디를 만지시겠습니까?
    """
    Todi_touched = False
    Todi_lock = True
    
    while True:
        next = raw_input(">")
        
        if next == "코" and not Todi_touched:
            print "토디가 깜짝 놀랍니다."
            Todi_touched = True
        elif next == "코" and Todi_touched and Todi_lock:
            print "토디가 좋아합니다."
            Todi_lock = False
        elif next == "코" and not Todi_lock:
            print "토디가 짜증냅니다."
            dead("토디가 토라졌습니다. 꾸!")
        elif next == "볼" and not Todi_lock:
            print "토디 잠금해제에 성공했습니다! 추카추카!"
            exit(0)
        elif next == "볼" and Todi_lock:
            print "토디가 좋아하지만 원하는 것이 아닙니다."
        elif next == "팔":
            print "토디가 분노합니다!"
            dead("꾸꾸꾸꾸꾸!")
        else:
            print "좋은 말 할때, 만지라는 데를 만지십시오."

def dead(why):
    print why, "Wasted"
    exit(0)

def start():
    print "어두운 방에 있습니다."
    print "오른쪽과 왼쪽에는 문이 있습니다."
    print "어느 쪽을 고를까요?"
    
    next = raw_input(">")
    
    if next == "왼쪽":
        bear_room()
    elif next == "오른쪽":
        Todi_room()
    else:
        dead("문 주위에서 맴돌기만 하다 굶어 죽었습니다.")