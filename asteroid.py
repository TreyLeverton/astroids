import pygame
from circleshape import CircleShape

class Asteroid(CircleShape):
    def __init__(self, x, y, radius):
        super().__init__(x, y, radius)

        self.image = pygame.Surface((radius * 2, radius * 2), pygame.SRCALPHA)
        pygame.draw.circle(self.image, (255, 255, 255), (radius, radius), radius)

        self.rect = self.image.get_rect(center=(self.position.x, self.position.y))

    def draw(self, screen):
        pygame.draw.circle(screen, "white", (self.x, self.y), self.radius, 2)
        self.rect.center = (self.position.x, self.position.y)

    def update(self, dt):
        movement = self.velocity * dt
        self.position += movement
        self.rect.center = (self.position.x, self.position.y)