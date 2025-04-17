import sys
import pygame
from constants import *
from circleshape import *
from player import Player
from asteroid import Asteroid
from asteroidfield import *

def main():
    pygame.init
    print("Starting Asteroids!")
    print(f"Screen width: {SCREEN_WIDTH}")
    print(f"Screen height: {SCREEN_HEIGHT}")

    screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))

    updatable = pygame.sprite.Group()
    drawable = pygame.sprite.Group()
    asteroids = pygame.sprite.Group()

    Asteroid.containers = (asteroids, updatable, drawable)
    Player.containers = (updatable, drawable)
    AsteroidField.containers = (updatable)

    player = Player(x=SCREEN_WIDTH / 2, y=SCREEN_HEIGHT / 2)
    updatable.add(player)
    drawable.add(player)

    clock = pygame.time.Clock()
    dt = 0
    
    asteroid_field = AsteroidField()

    while True:

        print("Player in drawable:", player in drawable)
        
        for asteroid in asteroids:
            if player.collides_with(asteroid):
                print("Game over!")
                sys.exit()
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                return
            
            
        screen.fill("black")

        player.draw(screen)
        drawable.draw(screen)
        
        dt = clock.tick(60) / 1000
        updatable.update(dt)

        pygame.display.flip()
        
if __name__ == "__main__":
    main()
