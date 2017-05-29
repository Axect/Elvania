
# -*- coding: utf-8 -*-

from sys import exit
from random import randint
from time import sleep

def start():
    print "띠리리리링"
    for i in range(0,4):
        print '.' * 3
        sleep(1)
    print "띠리리리.."
    print "퍽!"
    sleep(1)
    print "꿍?"
    sleep(1)
    print "(시계를 보니 9시다.) 꾸꿍?!"
    sleep(1)
    print "늦어뚜 꾸힝 빨리 띴구 나가야 행."
    sleep(1)
    print "지금부터 튜토리얼을 시작합니다. 스킵하시려면 Skip을, 진행하시려면 Tutorial을 입력해주십시오."
    tutorial = raw_input('>')
    
    if tutorial == 'Skip':
        print "튜토리얼을 스킵합니다."
        print "맵을 불러옵니다.",
        for i in range(0,5):
            sleep(0.5)
            print '.',
        print '.'
        print '-' * 20
        clean_boll = False
        current_map = Map('Home')
        Load = Engine(current_map)
        Let = Load.play()
        Next, boll = Let.enter(clean_boll)
        for i in range(0,len(Map.scenes)+1):
            current_map = Map(Next)
            clean_boll = boll
            Load = Engine(current_map)
            Let = Load.move()
            Next, boll = Let.enter(clean_boll)
        
    else:
        print "아직 만들지 않았습니다."

class Engine(object):
    
    def __init__(self, scene_map):
        self.scene_map = scene_map
    
    def play(self):
        current_scene = self.scene_map.opening_scene()
        return current_scene
    
    def move(self):
        for i in range(0,5):
            print "아장 아장"
            sleep(1)
        current_scene = self.scene_map.opening_scene()
        return current_scene
        
class Scene(object):
    
    def enter(self, time):
        self.time = time
        print "아직 만들지 않았습니다."
        pass
        
class Home(Scene):
    
    def enter(self, clean_boll):
        self.cleanboll = clean_boll
        if not self.cleanboll:
            print "집에 들어왔습니다."
            sleep(1)
            print "무엇을 하시겠습니까?"
            print "-" * 20
            print "Wash"
            Hmethod = raw_input('>')
            print "-" * 20
            
            if Hmethod == "Wash":
                HAct = Wash()
                HAct.enter(self.cleanboll)
                sleep(1)
                print "볼이 깨끗하므로 밖으로 나갑니다."
                sleep(1)
                return 'Subway', True
            else:
                print "Error"
        
        else:
            print "볼이 깨끗하므로 밖으로 나갑니다."
            return 'Subway', True

        
class Wash(Scene):
    
    def enter(self, clean_boll):
        self.cleanboll = clean_boll
        
        if not self.cleanboll:
            print "흠.. 어제 샤워했는데 오늘은 어떻게 하지?"
            print "-" * 20
            print "Shower"
            print "Wash the Face"
            wmethod = raw_input('>')
            print "-" * 20
            
            if wmethod == "Shower":
                self.Shower()
                self.cleanboll = True
        
        else:
            print "이미 깨끗한 볼입니다. 더 씻을 필요가 없습니다."
    
    def Shower(self):
        print "토디는 즐겁게 노래를 부르며 샤워를 합니다."
        sleep(1)
        print "뚱가 뚱가 춤까지 흥겹게 춥니다."
        sleep(1)
        print "아주 귀여워서 몽몽이가 보고있다면 덕통사고를 당할 것만 같습니다. (꾸왕!)"

    
    def WTF(self):
        pass
    
    

class Subway(Scene):
    
    def enter(self, clean_boll):
        self.clean_boll = clean_boll
        print "토디는 아장아장 걸어서 지하철에 들어왔습니다."
        sleep(1)
        print "우리 아가 토디는 힘들디만 학교에 가야합니다."
        sleep(1)
        print "지하철 노선은 2개가 있으니 선택해야 합니다!"
        sleep(1)
        print "토디: 꾸우..?"
        sleep(1)
        print "-" * 20
        print "line 2"
        print "line 9"
        smethod = raw_input('>')
        print "-" * 20
        
        if smethod == "line 2":
            SAct = Line2()
            SAct.enter(self.clean_boll)
            print "볼은 아직 탱탱합니다. 몽몽이가 보면 좋아하겠네요!"
            return "Sinchon", True
        elif smethod == "line 9":
            pass
        else:
            print "Error"

class Line2(Scene):
    
    def enter(self, clean_boll):
        self.clean_boll = clean_boll
        print "토디는 2호선을 탔습니다."
        
        if self.clean_boll:
            print "토디는 자리에 앉았습니다. 기분이 좋아집니다."
            print "볼도 깨끗합니다. 몽몽이 보여줄 생각에 기분이 더 좋아집니다."
            print "토디는 이제 할 행동을 선택할 수 있습니다."
            print "-" * 20
            print "Between"
            print "Sleep"
            lmethod = raw_input('>')
            print "-" * 20
            
            if lmethod == "Between":
                self.Between()
            elif lmethod == "Sleep":
                self.Sleep()
    
    def Between(self):
        print "토디는 비트윈을 켜서 몽몽이에게 스티커를 보냅니다."
        sleep(1)
        print "하이룽 몽몽! (로빈에그_하이룽)"
        sleep(1)
        print "그리고 페이스북을 켜려는 찰나, 몽몽이에게 답장이 옵니다."
        sleep(1)
        print "하이ㄹㅜㅇ토ㅓ디? (로빈에그_하이룽)"
        sleep(1)
        print "그렇습니다. 비몽사몽몽이었던 것입니다."
        sleep(1)
        print "토디는 로빈에그의 자장자장 스티커를 보내곤 빰빰이를 구하러 갑니다."
        for i in range(0,5):
            print '.',
            sleep(0.75)
        print "\n"
        print "빰빰이를 구하다 보니 어느새 신촌역에 도착했습니다. 이제 내립니다."
    
    def Sleep(self):
        pass


class Sinchon(Scene):
    pass
            

class Map(object):
    
    scenes = {
        'Home': Home(),
        'Subway': Subway(),
        'Sinchon': Sinchon()
    }
    
    def __init__(self, start_scene):
        self.start_scene = start_scene
        print "현재 장소는 %s입니다." % self.start_scene
        print '-' * 20
        
    def next_scene(self, scene_name):
        val = Map.scenes[scene_name]
        return val
        
    def opening_scene(self):
        return self.next_scene(self.start_scene)