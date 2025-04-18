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
        else:
            random_angle = random.uniform(20, 50)

            new_radius = self.radius - ASTEROID_MIN_RADIUS

            new_velocity1 = self.velocity.rotate(random_angle) * 1.2
            new_velocity2 = self.velocity.rotate(-random_angle) * 1.2
            
            new_asteroid1 = Asteroid(self.position, new_velocity1, new_radius)
            new_asteroid2 = Asteroid(self.position, new_velocity2, new_radius)

            