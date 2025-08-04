from circleshape import CircleShape
import pygame
import random


from constants import ASTEROID_MIN_RADIUS

class Asteroid(CircleShape):
    def __init__(self, x, y, radius):
        super().__init__(x, y, radius)
    def draw(self, screen):
        pygame.draw.circle(screen, color="white",center=self.position, radius=self.radius, width=2)
    def update(self, dt):
        self.position += self.velocity * dt
    def split(self):
        self.kill()
        if self.radius <= ASTEROID_MIN_RADIUS:
            return
        random_angle = random.uniform(20, 50)
        pos_vec = self.velocity.rotate(random_angle)
        neg_vec = self.velocity.rotate(-random_angle)
        new_radius = self.radius - ASTEROID_MIN_RADIUS
        pos_asteroid = Asteroid(self.position[0], self.position[1], new_radius)
        neg_asteroid = Asteroid(self.position[0], self.position[1], new_radius)
        pos_asteroid.velocity = pos_vec * 1.2
        neg_asteroid.velocity = neg_vec * 1.2
