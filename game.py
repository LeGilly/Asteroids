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
    
    def draw_lives_remaining(self, screen, center, size=PLAYER_RADIUS, color=WHITE_COLOR):
        cx, cy = center
        half_base = size * 0.5

        tip = (cx, cy - size * 0.6)
        left = (cx - half_base, cy + size * 0.4)
        right = (cx + half_base, cy + size * 0.4)

        pygame.draw.polygon(screen, color, [tip, left, right], DRAW_LINE_WIDTH)

    def update(self, dt):
        self.time_elapsed += dt
        if self.time_elapsed > self.next_time_bonus:
            self.add_score(10)
            self.next_time_bonus += 1
    
    def reset(self):
        self.__init__()