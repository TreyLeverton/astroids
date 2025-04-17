import sys
import pygame
from constants import *
from circleshape import *
from player import *
from asteroid import Asteroid
from asteroidfield import *


def main():
    pygame.init()

    screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))
    
    updatable = pygame.sprite.Group()
    drawable = pygame.sprite.Group()
    asteroids = pygame.sprite.Group()
      
    Shot.containers = (drawable, updatable)
    Player.containers = (updatable, drawable)
    Asteroid.containers = (asteroids, updatable, drawable)
    AsteroidField.containers = (updatable)

    player = Player(x=SCREEN_WIDTH / 2, y=SCREEN_HEIGHT / 2)
    asteroid_field = AsteroidField()
    pygame.display

    clock = pygame.time.Clock()
    dt = 0

    while True:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                return 
            
        screen.fill("black")

        updatable.update(dt)

        for asteroid in asteroids:
            for shot in player.shots:
                if asteroid.rect.colliderect(shot.rect):
                    asteroid.kill()
                    shot.kill()

        for asteroid in asteroids:
            if player.collision(asteroid):
                print("Game over!")
                sys.exit()

        for entity in drawable:
            entity.draw(screen)

        dt = clock.tick(60) / 1000
        
        pygame.display.flip()
        
if __name__ == "__main__":
    main()
