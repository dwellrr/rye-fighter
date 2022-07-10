import pygame
import os
import ctypes
import core



class fighter:

    user32 = ctypes.windll.user32
    WIDTH, HEIGHT = user32.GetSystemMetrics(0)/1.2, user32.GetSystemMetrics(1)/1.2
    WIN = pygame.display.set_mode((WIDTH, HEIGHT))
    pygame.display.set_caption("Rye Fighter")
    game = core.core(WIN)
    game.loop()



def main():
    _fighter = fighter()
        

if __name__ == "__main__":
    main()

