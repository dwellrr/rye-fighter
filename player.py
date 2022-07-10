import pygame
from entity import entity
#class action:

class player(entity):
    def __init__(self, name, _coords):
      super().__init__(name, _coords) 
    
    def handle_input(self, event):
        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_a:
                self.acceleration -= 2
        if event.type == pygame.KEYUP:
            if event.key == pygame.K_a:
                self.acceleration = 0

