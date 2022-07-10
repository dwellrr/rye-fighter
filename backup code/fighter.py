import pygame
import os
import player
import ctypes

class fighter:

    user32 = ctypes.windll.user32
    WIDTH, HEIGHT = user32.GetSystemMetrics(0) - 100, user32.GetSystemMetrics(1) -100
    FPS = 60
    WIN = pygame.display.set_mode((WIDTH, HEIGHT))
    fullscreen = False
    pygame.display.set_caption("Rye Fighter")
    user_player = player.player("Rye", [WIDTH/2, HEIGHT/2])



    def draw():
        pygame.draw.rect(WIN, (0, 0, 0), (pygame.Rect(WIDTH//2 - 5, 0, 10, HEIGHT)))
        user_player.draw(WIN)
        pygame.display.update()

    def update():
        user_player.update()


    def main():
        clock = pygame.time.Clock()
        run = True
        while run:
            clock.tick(FPS)
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    run = False
                    pygame.quit()
                if event.type == pygame.KEYDOWN:
                    if event.key == pygame.K_f:
                        fullscreen = not fullscreen
                        if fullscreen:
                            WIN = pygame.display.set_mode((WIN.get_width(), WIN.get_height(), pygame.display.set_mode(pygame.FULLSCREEN)))
                        else:
                            WIN = pygame.display.set_mode((WIN.get_width(), WIN.get_height(), pygame.display.set_mode(pygame.SHOWN)))
            draw()

    if __name__ == "__main__":
    main()

