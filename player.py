import pygame
from entity import entity
#class action:

class player(entity):
    def __init__(self, name, _coords):
      super().__init__(name, _coords) 
    
    def handle_input(self, event):
        if event.type == pygame.KEYUP:
            if event.key == pygame.K_d:
                self.direction = 0
        if event.type == pygame.KEYUP:
            if event.key == pygame.K_a:
                self.direction = 0
        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_a:
                self.direction = -1
        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_d:
                self.direction = 1
        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_SPACE:
                if self.falling == False:
                    self.isJumping = True
            if event.key == pygame.K_j:
                self.jAttack()
       

