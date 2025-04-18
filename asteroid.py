import pygame
import random
from constants import *
from circleshape import *

class Asteroid(CircleShape):
    def __init__(self, x, y, radius):
        super().__init__(x, y, radius)

    def draw(self, screen):
        pygame.draw.circle(screen, "white", (self.position.x, self.position.y), self.radius, 2)

    def update(self, dt):
        self.position += (self.velocity * dt)

    def split(self):
        self.kill()
        if self.radius <= ASTEROID_MIN_RADIUS:
            return
    
        # Generate random angle for splitting
        random_angle = random.uniform(20, 50)
    
        # Create copies of the original velocity vector
        new_velocity1 = pygame.math.Vector2(self.velocity)
        new_velocity2 = pygame.math.Vector2(self.velocity)
    
        # Rotate the new velocity vectors
        new_velocity1.rotate_ip(random_angle)
        new_velocity2.rotate_ip(-random_angle)
    
        # Scale up the velocities
        new_velocity1 *= 1.2
        new_velocity2 *= 1.2
    
        # Calculate new radius
        new_radius = self.radius - ASTEROID_MIN_RADIUS
    
        # Create new asteroids
        new_asteroid1 = Asteroid(pygame.math.Vector2(self.position), new_velocity1, new_radius)
        new_asteroid2 = Asteroid(pygame.math.Vector2(self.position), new_velocity2, new_radius)
    
        # Make sure the new asteroids are added to the same groups as the original
        for group in self.groups():
            group.add(new_asteroid1)
            group.add(new_asteroid2)