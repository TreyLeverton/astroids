from readline import redisplay
from textwrap import fill
import pygame
from constants import *

def main():
    pygame.init
    print("Starting Asteroids!")
    print(f"Screen width: {SCREEN_WIDTH}")
    print(f"Screen height: {SCREEN_HEIGHT}")
    screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))

    pygame.time.Clock
    dt = 0

    while True:
        for event in pygame.event.get():
            dt = pygame.clock.tick(60) / 1000
            if event.type == pygame.QUIT:
                return 
        fill("black")
        pygame.display.flip()


if __name__ == "__main__":
    main()
