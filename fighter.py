import pygame
import os
import ctypes

user32 = ctypes.windll.user32
WIDTH, HEIGHT = user32.GetSystemMetrics(0), user32.GetSystemMetrics(1)
FPS = 60
WIN = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption("Rye Fighter")


def draw_window():
    pygame.draw.rect(WIN, (0, 0, 0), (pygame.Rect(WIDTH//2 - 5, 0, 10, HEIGHT)))

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

