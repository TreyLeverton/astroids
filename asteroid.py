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
        # Store the original groups before killing
        original_groups = self.groups()
    
        # Kill the asteroid
        self.kill()
    
        # Don't split if too small
        if self.radius <= ASTEROID_MIN_RADIUS:
            return
    
        # Generate random angle for splitting
        random_angle = random.uniform(20, 50)
    
        # Create new velocity vectors by rotating the original
        # Note: rotate() returns a new vector and doesn't modify the original
        new_velocity1 = self.velocity.rotate(random_angle) * 1.2
        new_velocity2 = self.velocity.rotate(-random_angle) * 1.2
    
        # Calculate new radius
        new_radius = self.radius - ASTEROID_MIN_RADIUS
    
        # Create new asteroids with copied position vectors to avoid reference issues
        new_position = pygame.Vector2(self.position)
        new_asteroid1 = Asteroid(new_position, new_velocity1, new_radius)
        new_asteroid2 = Asteroid(new_position, new_velocity2, new_radius)
    
        # Add the new asteroids to all groups the original was in
        for group in original_groups:
            group.add(new_asteroid1)
            group.add(new_asteroid2)