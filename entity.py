from queue import Empty
import queue
import pygame

class entities:
    def __init__(self):
        self._entities = []

    def checkCollision(self, subject):
        res = []
        for x in self._entities:
            if x != subject:
                if (subject.coords[0] <= x.coords[0] + x.width) and (subject.coords[0] >= x.coords[0]):
                    if ((subject.coords[1] <= x.coords[1] + x.height) and (subject.coords[1] >= x.coords[1])) or ((subject.coords[1] + subject.height <= x.coords[1] + x.height) and (subject.coords[1] + subject.height >= x.coords[1])):
                        res.append(x)
                elif (subject.coords[0] + subject.width <= x.coords[0] + x.width) and (subject.coords[0] + subject.width >= x.coords[0]):
                    if ((subject.coords[1] <= x.coords[1] + x.height) and (subject.coords[1] >= x.coords[1])) or ((subject.coords[1] + subject.height <= x.coords[1] + x.height) and (subject.coords[1] + subject.height >= x.coords[1])):
                        res.append(x)
        return res

    def update(self, WIDTH, HEIGHT):
        for x in self._entities:
            x.update(WIDTH, HEIGHT)
            if x.atackNum == 1 and x.atackTime > 0:
                for a in self.checkCollision(x):
                    if a not in x.doneList:
                        a.getHurt(20)
                        a.acceleration[0] += int(x.acceleration[0]/3)
                        x.doneList.append(a)
                x.atackTime -= 1
            if x.atackTime == 0:
                x.atackNum = 0
                x.doneList = []

            if x.health <= 0:
                self._entities.remove(x)
    def draw(self, WIN):
        for x in self._entities:
            x.draw(WIN)
            

class entity:
    coords = [0, 0]
    acceleration = 0
    hitbox = pygame.Rect(0, 0, 50, 50)
    sprite_name = ""
    current_action = ""
    frame_queue = []
    health = 0
    dmg = 0
    def __init__(self, name, _coords):
        self.speed = 15
        self.direction = 0
        self.acceleration = [0, 0]
        self.coords = _coords
        self.width = 50
        self.height = 50
        self.falling = False
        self.isJumping = False
        self.atackNum = 0
        self.atackTime = 0
        doneList = []
        self.hitbox = pygame.Rect(self.coords[0], self.coords[1], self.width, 50)
        self.sprite_name = name
        self.current_action = 'idle'
        self.frame_count = 0
        self.health = 100
        self.action = ""
        self.runF = [pygame.image.load("res/r1.png"), pygame.image.load("res/r2.png"), pygame.image.load("res/r3.png"), pygame.image.load("res/r4.png")]
        self.idleF = [pygame.image.load("res/i1.png"), pygame.image.load("res/i2.png"), pygame.image.load("res/i3.png"), pygame.image.load("res/i4.png")]
        self.attackF = [pygame.image.load("res/a1.png"), pygame.image.load("res/a2.png"), pygame.image.load("res/a3.png"), pygame.image.load("res/a4.png")]
        self.jumpF = [pygame.image.load("res/j1.png"), pygame.image.load("res/j2.png"), pygame.image.load("res/j3.png"), pygame.image.load("res/j4.png"), pygame.image.load("res/f1.png"), pygame.image.load("res/f2.png")]
        self.current_frame = self.runF[0]
        self.current_frame = self.runF[0]
        self.current_frame_alpha = self.current_frame.copy()
        self.anim_offset = 0


    def update(self, WIDTH, HEIGHT):
        if self.direction == -1 and self.acceleration[0] > -self.speed:
            self.acceleration[0] -= 1
        elif self.direction == 0 and self.acceleration[0] < 0:
            self.acceleration[0] += 1
        elif self.direction == 1 and self.acceleration[0] < self.speed:
            self.acceleration[0] += 1
        elif self.direction == 0 and self.acceleration[0] > 0:
            self.acceleration[0] -= 1

        self.coords[0] += self.acceleration[0]
        if (self.coords[0] <= 0):
            self.coords[0] = 0
        elif (self.coords[0] + self.width >= WIDTH):
            self.coords[0] = WIDTH - self.width

        if self.acceleration[0] > self.speed:
            self.acceleration[0] -= 1
        if self.acceleration[0] < -self.speed:
            self.acceleration[0] += 1


   
        if (self.coords[1] < HEIGHT/1.2):
            self.falling = True
        else:
            self.falling = False
        if (self.coords[1] > HEIGHT/1.2):
            self.coords[1] = HEIGHT/1.2
        
        if self.falling:
            self.acceleration[1] += 1
        else:
            self.acceleration[1] = 0

        if(self.isJumping):
            self.acceleration[1] -= 30
            self.frame_count = 0
            self.isJumping = False
        
        if(self.acceleration[0] > 0):
            self.action = "r_r"
        elif(self.acceleration[0] < 0):
            self.action = "r_l"
        else:
            self.action = "idle"

        if(self.falling):
            self.action = "jump"
        
        if(self.atackTime > 0):
            self.action = "attack"

        if(self.anim_offset == 9):
            self.frame_count += 1
            self.anim_offset = 0

        if(self.action == "r_l"):
            if (self.frame_count >= 4):
                self.frame_count = 0
            self.current_frame = self.runF[self.frame_count]
        elif(self.action == "r_r"):
            if (self.frame_count >= 4):
                self.frame_count = 0
            self.current_frame = (pygame.transform.flip(self.runF[self.frame_count], True, False))
        elif(self.action == "idle"):
            if (self.frame_count >= 4):
                self.frame_count = 0
            self.current_frame = self.idleF[self.frame_count]
        elif(self.action == "jump") and (self.acceleration[0] < 0):
            if (self.frame_count >= 6):
                self.frame_count = 5
            self.current_frame = self.jumpF[self.frame_count]
        elif(self.action == "jump") and (self.acceleration[0] > 0):
            if (self.frame_count >= 6):
                self.frame_count = 5
            self.current_frame = pygame.transform.flip(self.jumpF[self.frame_count], True, False)
        elif(self.action == "attack") and (self.acceleration[0] < 0):
            if (self.frame_count >= 4):
                self.frame_count = 0
            self.current_frame = self.attackF[self.frame_count]
        elif(self.action == "attack") and (self.acceleration[0] > 0):
            if (self.frame_count >= 4):
                self.frame_count = 0
            self.current_frame = pygame.transform.flip(self.attackF[self.frame_count], True, False)
        


        self.current_frame_alpha = self.current_frame.copy()
        alpha = 128
        self.current_frame_alpha.fill((225, 225, 255, alpha), None, pygame.BLEND_RGBA_MULT)
        self.anim_offset += 1

        self.coords[1] += self.acceleration[1]
        
        self.hitbox = pygame.Rect(self.coords[0], self.coords[1], 50, 50)

     


        if self.dmg != 0:
            self.handle_dmg()
        #self.handle_animations()
    #def jump(self):
        #while (self.acceleration[1] < 20):
            #self.acceleration[1] += 4

        
    def jAttack(self):
        if self.acceleration[0] > 0:
            self.acceleration[0] += 20
        elif self.acceleration[0] < 0:
            self.acceleration[0] -= 20
        else:
            self.acceleration[1] += 20
        self.atackNum = 1
        self.atackTime = 20
    
    def getHurt(self, dmg):
        self.health -= dmg

    def draw(self, WIN):
        
      
        WIN.blit(self.current_frame_alpha, (self.coords[0], self.coords[1]))