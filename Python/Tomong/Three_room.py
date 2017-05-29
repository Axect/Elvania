
# -*- coding: utf-8 -*-

import random

class Room(object): # 일단 가장 큰 단위를 만듭니다. 나중에 상속시켜서 쓸 것입니다.

    door_list = ['Aroom', 'Broom', 'Croom'] # 일단은 모든 방 목록. 방마다 움직일 수 있는 방 목록으로 변경할 것입니다.
    
    def __init__(self):
        # 여기서는 모든방이지만 각각의 방에서 Override할 예정.
        # class의 variable은 클래스를 instance화 시키지 않아도 사용가능!
        self.door_list = Room.door_list
        
    
    def enter(self):
        print self.door_list # 어디로 갈 수 있는지 보여줌.
            
    def move(self):
        self.door = raw_input('>') # 일단, 텍스트로 움직일 방을 받음.
        
        if self.door in self.door_list:
            # 텍스트로 받은 방을 Map의 사전으로 방 객체를 호출 (이미 인스턴스화)
            self.next_door = Map.room_dict[self.door] 
            
            print "%s으로 이동하였습니다." % self.door
            return self.next_door
        else:
            print "이동하지 않았습니다."
            return Map.room_dict[self.door] # 이거 에러임!

class Engine(object):
    
    def shuffle(self, x): # self는 클래스의 기본 인스턴스, x는 리스트
        self.x = list(x) # 즉, self.x란 Engine.x를 의미함.
        random.shuffle(self.x) # 셔플셔플!
        return self.x

    def init_point(self): # 시작위치를 랜덤으로 지정할것임.
        self.door_list = Room.door_list # 모든 방 목록.
        # Engine 내에 함수가 있기에 self.shuffle을 사용해야함.(self는 기본 인스턴스)
        self.shuffle_list = self.shuffle(self.door_list)
        return self.shuffle_list[0] # 즉, 반환값은 텍스트입니다. (Map은 텍스트를 Class로 바꾸어줍니다.)
        
        
class Aroom(Room):
    
    door_list = ['Broom']
    def __init__(self):
        self.door_list = Aroom.door_list # Room의 init을 Override함.

class Broom(Room):
    
    door_list = ['Aroom', 'Croom']
    def __init__(self):
        self.door_list = Broom.door_list # Room의 init을 Override함.

class Croom(Room):
    
    door_list = ['Broom']
    def __init__(self):
        self.door_list = Croom.door_list # Room의 init을 Override함.

class Map(object):
    # Room class들을 인스턴스화시키고 사전에 저장.
    a = Aroom()
    b = Broom()
    c = Croom()
    
    # 텍스트로 받을 input을 객체로 변경시켜주기 위한 사전.
    room_dict = {
        'Aroom': a,
        'Broom': b,
        'Croom': c
    }