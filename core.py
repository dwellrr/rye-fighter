import pygame
import os
import ctypes

class core:

    def __init__(self, _win):
        self.WIN = _win

    user32 = ctypes.windll.user32
    WIDTH, HEIGHT = user32.GetSystemMetrics(0) - 100, user32.GetSystemMetrics(1) -100
    FPS = 60
    fullscreen = False
    run = True


    def draw(self):
        pygame.draw.rect(self.WIN, (0, 0, 0), (pygame.Rect(self.WIDTH//2 - 5, 0, 10, self.HEIGHT)))
        pygame.display.update()

    def update(self):
        return

    def handle_events(self, event):
        if event.type == pygame.QUIT:
                    self.run = False
                    pygame.quit()
        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_f:
                self.fullscreen = not self.fullscreen
                if self.fullscreen:
                    self.WIN = pygame.display.set_mode((self.WIN.get_width(), self.WIN.get_height()), pygame.FULLSCREEN)
                else:
                    self.WIN = pygame.display.set_mode((self.WIDTH, self.HEIGHT))


    def loop(self):
        clock = pygame.time.Clock()
        run = True
        while run:
            clock.tick(self.FPS)
            for event in pygame.event.get():
                self.handle_events(event)
            self.update()
            self.draw()

                


