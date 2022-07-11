import pygame

class entities:
    def __init__(self):
        self._entities = []

    def checkCollision(self, subject):
        res = []
        for x in self._entities:
            if x != subject:
                if (subject.coords[0] <= x.coords[0] + x.width) and (subject.coords[0] >= x.coords[0]):
                    res.append(x)
                elif (subject.coords[0] + subject.width <= x.coords[0] + x.width) and (subject.coords[0] + subject.width >= x.coords[0]):
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
        self.falling = False
        self.isJumping = False
        self.atackNum = 0
        self.atackTime = 0
        doneList = []
        self.hitbox = pygame.Rect(self.coords[0], self.coords[1], self.width, 50)
        self.sprite_name = name
        self.current_action = 'idle'
        self.frame_queue = []
        self.health = 100
        self.dmg = 0

    def handle_dmg(dmg):
        return #TODO
    #def handle_animations()
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
            self.isJumping = False


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
        
        pygame.draw.rect(WIN, (255, 255, 255), self.hitbox)