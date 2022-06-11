import pygame
import os
import ctypes

user32 = ctypes.windll.user32
WIDTH, HEIGHT = user32.GetSystemMetrics(0), user32.GetSystemMetrics(1)
FPS = 60
WIN = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption("Rye Fighter")

class player:
    def __init__(self, name):
        hitbox = pygame.Rect(WIDTH/2, HEIGHT/2, 50, 50)
        sprite_name = name
        current_action = 'idle'
        frame_queue = []
        health = 100
        dmg = 0
        cooldown = 0

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



def draw_window():
    pygame.draw.rect(WIN, (0, 0, 0), (pygame.Rect(WIDTH//2 - 5, 0, 10, HEIGHT)))
    pygame.display.update()

def main():
    clock = pygame.time.Clock()
    run = True
    while run:
        clock.tick(FPS)
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                run = False
                pygame.quit()
        draw_window()

if __name__ == "__main__":
    main()

