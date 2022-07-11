import pygame
from entity import entity
#class action:

class player(entity):
    def __init__(self, name, _coords, config):
      super().__init__(name, _coords) 
      self.config = config
      

    def handle_input(self, event):
        if self.config == "wasd":
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
                if event.key == pygame.K_w:
                    if self.falling == False:
                        self.isJumping = True
                if event.key == pygame.K_LSHIFT:
                    self.jAttack()

        if self.config == "arrows":
            if event.type == pygame.KEYUP:
                if event.key == pygame.K_RIGHT:
                    self.direction = 0
            if event.type == pygame.KEYUP:
                if event.key == pygame.K_LEFT:
                    self.direction = 0
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_LEFT:
                    self.direction = -1
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_RIGHT:
                    self.direction = 1
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_UP:
                    if self.falling == False:
                        self.isJumping = True
                if event.key == pygame.K_RSHIFT:
                    self.jAttack()

            
            
       

