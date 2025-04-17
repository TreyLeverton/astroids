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

    print("Setting up containers")
    Player.container = (updatable, drawable)
    Asteroid.container = (asteroids, updatable, drawable)
    AsteroidField.containers = (updatable)

    print(f"Player created at {player.position}")
    
    print("Creating asteroid field")

    player = Player(x=SCREEN_WIDTH / 2, y=SCREEN_HEIGHT / 2)
    asteroid_field = AsteroidField()

    print("Asteroid field created")
    
    print(f"Asteroids count: {len(asteroids)}")
    print(f"Updatable count: {len(updatable)}")
    print(f"Drawable count: {len(drawable)}")

    clock = pygame.time.Clock()
    dt = 0

    while True:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                return 
            
        screen.fill("black")

        updatable.update(dt)
        drawable.draw(screen)

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
