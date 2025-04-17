from circleshape import CircleShape
from constants import PLAYER_RADIUS, PLAYER_TURN_SPEED, PLAYER_SPEED
import pygame

class Player(pygame.sprite.Sprite, CircleShape):
    def __init__(self, x, y):
        pygame.sprite.Sprite.__init__(self)
        CircleShape.__init__(self, x, y, PLAYER_RADIUS)
        self.rotation = 0
        
        # Create an appropriately sized surface
        size = int(self.radius * 2.5)  # Make it a bit larger to fit the triangle
        self.image = pygame.Surface((size, size), pygame.SRCALPHA)
        self.rect = self.image.get_rect(center=(self.position.x, self.position.y))
        
        # Initial drawing
        self.redraw()

    def redraw(self):
        # Clear the surface
        self.image.fill((0, 0, 0, 0))  # Transparent black
        
        # Get triangle points
        tri_points = self.triangle()
        
        # Convert world coordinates to surface-relative coordinates
        center = pygame.Vector2(self.rect.width // 2, self.rect.height // 2)
        adjusted_points = [(p.x - self.position.x + center.x, 
                           p.y - self.position.y + center.y) for p in tri_points]
        
        # Draw the triangle
        pygame.draw.polygon(self.image, (255, 255, 255), adjusted_points, 2)

    def rotate(self, dt):
        self.rotation += PLAYER_TURN_SPEED * dt
        self.redraw()  # Redraw after rotation changes

    # in the player class
    def triangle(self):
        forward = pygame.Vector2(0, 1).rotate(self.rotation)
        right = pygame.Vector2(0, 1).rotate(self.rotation + 90) * self.radius / 1.5
        a = self.position + forward * self.radius
        b = self.position - forward * self.radius - right
        c = self.position - forward * self.radius + right
        return [a, b, c]
    
    def move(self, dt):
        forward = pygame.Vector2(0, 1).rotate(self.rotation)
        self.position += forward * PLAYER_SPEED * dt
    
    def update(self, dt):
        keys = pygame.key.get_pressed()

        if keys[pygame.K_a]:
            self.rotate(-dt)
        if keys[pygame.K_d]:
            self.rotate(dt)
        if keys[pygame.K_w]:
            self.move(dt)
        if keys[pygame.K_s]:
            self.move(-dt)
