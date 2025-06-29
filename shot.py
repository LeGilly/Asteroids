import pygame
from circleshape import CircleShape
from constants import *

class Shot(CircleShape):
    def __init__(self, x, y, radius):
        super().__init__(x, y, radius)
    
    def draw(self, screen):
        pygame.draw.circle(screen, WHITE_COLOR, self.position, self.radius, DRAW_LINE_WIDTH)
    
    def update(self, dt):
        self.position += (self.velocity * dt)