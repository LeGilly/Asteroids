import pygame
from constants import *

class Game():
    def __init__(self):
        self.score = 0
        self.time_elapsed = 0
        self.next_time_bonus = 1
        self.font = pygame.font.SysFont(None, 36)

    def add_score(self, points):
        self.score += points
    
    def draw_score(self, screen):
        score_surface = self.font.render(f"Score: {self.score}", True, WHITE_COLOR)
        screen.blit(score_surface, (10, 10))

    def update(self, dt):
        self.time_elapsed += dt
        if self.time_elapsed > self.next_time_bonus:
            self.add_score(10)
            self.next_time_bonus += 1
