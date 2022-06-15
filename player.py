import pygame

#class action:

class player:
    acceleration = 0
    hitbox = pygame.Rect(0, 0, 50, 50)
    sprite_name = ""
    current_action = ""
    frame_queue = []
    health = 0
    dmg = 0
    def __init__(self, name, coords):
        self.acceleration = 0
        self.hitbox = pygame.Rect(coords[0], coords[1], 50, 50)
        self.sprite_name = name
        self.current_action = 'idle'
        self.frame_queue = []
        self.health = 100
        self.dmg = 0

    def handle_input():
        return #TODO
    def handle_dmg(dmg):
        return #TODO
    #def handle_animations()
    def update(self):
        self.handle_input()
        if self.dmg != 0:
            self.handle_dmg()
        #self.handle_animations()
    def draw(self, WIN):
        pygame.draw.rect(WIN, (255, 255, 255), self.hitbox,  2)
        pygame.draw.rect(WIN, (255, 255, 255), self.hitbox)

