import pygame
import os
import ctypes
import entity
from player import player

class core:

    def __init__(self, _win):
        self.WIN = _win

    user32 = ctypes.windll.user32
    absolute_res = [user32.GetSystemMetrics(0), user32.GetSystemMetrics(1)]
    WIDTH, HEIGHT = absolute_res[0]/1.2, absolute_res[1]/1.2
    FPS = 60
    fullscreen = False
    run = True
    entities = []
    player = player("Rye", [(WIDTH)/1.5, (HEIGHT)/1.5])


    def draw(self):
        
        #pygame.draw.rect(self.WIN, (0, 0, 0), (pygame.Rect(self.WIDTH//2 - 5, 0, 10, self.HEIGHT)))
        self.WIN.fill((0, 0, 0))
        for e in self.entities:
            e.draw(self.WIN)
        self.player.draw(self.WIN)
        pygame.display.update()

    def update(self):
        for e in self.entities:
            e.update()
        self.player.update()

    def handle_events(self, event):
        if event.type == pygame.QUIT:
                    self.run = False
                    pygame.quit()
                    
        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_f:
                prev = [self.WIN.get_width(), self.WIN.get_height()]
                self.fullscreen = not self.fullscreen
                if self.fullscreen:
                    self.WIDTH, self.HEIGHT = self.absolute_res[0], self.absolute_res[1]
                    self.WIN = pygame.display.set_mode((self.WIDTH, self.HEIGHT), pygame.FULLSCREEN)
                    self.update_resolution(prev, [self.WIDTH, self.HEIGHT])
                else:
                    self.WIDTH, self.HEIGHT = self.WIDTH/1.2, self.HEIGHT/1.2
                    self.WIN = pygame.display.set_mode((self.WIDTH, self.HEIGHT))
                    self.update_resolution(prev, [self.WIDTH, self.HEIGHT])
        self.player.handle_input(event)
    
    def update_resolution(self, previous, new):
        for e in self.entities:
            x_prop = e.coords[0]/previous[0]
            y_prop = e.coords[1]/previous[1]
            e.coords[0] = new[0] * x_prop 
            e.coords[1] = new[1] * y_prop 

    
    def start_game(self):
        self.entities.append(entity.entity("Rye", [(self.WIDTH)/1.5, (self.HEIGHT)/1.5]))
        
        

    def loop(self):
        clock = pygame.time.Clock()
        run = True
        self.start_game()
        while run:
            clock.tick(self.FPS)
            for event in pygame.event.get():
                self.handle_events(event)
            self.update()
            self.draw()

                


