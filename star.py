import pygame
import random
from pygame.sprite import Sprite

class Star(Sprite):
    """A class to represent a single star in the fleet."""

    def __init__(self, ai_settings, screen):
        """Initialize star and set its starting position.""" 
        super(Star, self).__init__()
        self.screen = screen
        self.ai_settings = ai_settings
        star = pygame.image.load('/Users/usnahakimi/Desktop/python_3/aliens_game/star.bmp')
        self.image = pygame.transform.scale(star, (20, 25)) 
        self.rect = self.image.get_rect()

        self.x = float(self.rect.x)

    def blitme(self):
        """Draw the star at its current location.""" 
        positions = [(10, -10), (70, 10), (130, 40), (190, 90), (20, 110), (50, 250), (100, 150), (210, 180), 
        (260, 310), (300, 370), (360, 430), (420, 500), (490, 560), (550, 610), (235, 680), (330, 730), (385, 800),
        (475, 800), (10, -20), (700, 10), (630, 450), (770, 100), (720, 400), (800, 200), (580, 300), (720, 0), 
        (600, 70), (500, 250), (200, 10), (350, 40), (500, 70), (450, 600), (650, 500), (200, 500), (270, 550), 
        (100, 450), (30, 530), (100, 350), (400, 200), (680, 170), (780, 200)]
        for position in positions:
            self.screen.blit(self.image, position)
