import pygame
from constants import *
from circleshape import *
from player import Player
from asteroid import Asteroid

def main():
    pygame.init
    print("Starting Asteroids!")
    print(f"Screen width: {SCREEN_WIDTH}")
    print(f"Screen height: {SCREEN_HEIGHT}")

    screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))
    player = Player(x=SCREEN_WIDTH / 2, y=SCREEN_HEIGHT / 2)

    updatable = pygame.sprite.Group()
    drawable = pygame.sprite.Group()
    asteroid = pygame.sprite.Group()

    Player.container = (updatable, drawable)
    Aster
    clock = pygame.time.Clock()
    dt = 0

    while True:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                return 
            
        screen.fill("black")

        dt = clock.tick(60) / 1000
        updatable.update(dt)
        for entity in drawable:
            entity.draw(screen)

        
        pygame.display.flip()
        
if __name__ == "__main__":
    main()
