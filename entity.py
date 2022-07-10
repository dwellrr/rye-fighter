import pygame

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
        self.acceleration = 0
        self.coords = _coords
        self.hitbox = pygame.Rect(self.coords[0], self.coords[1], 50, 50)
        self.sprite_name = name
        self.current_action = 'idle'
        self.frame_queue = []
        self.health = 100
        self.dmg = 0

    def handle_dmg(dmg):
        return #TODO
    #def handle_animations()
    def update(self):
        self.coords[0] += self.acceleration
        self.hitbox = pygame.Rect(self.coords[0], self.coords[1], 50, 50)

        if self.dmg != 0:
            self.handle_dmg()
        #self.handle_animations()
    def draw(self, WIN):
        
        pygame.draw.rect(WIN, (255, 255, 255), self.hitbox)