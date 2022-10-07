import random
from dino_runner.utils.constants import CLOUD, SCREEN_WIDTH


class Cloud:
    def __init__(self):
        self.x = SCREEN_WIDTH + random.randint(800, 1000)
        self.y = random.randint(50, 100)
        self.image = CLOUD
        self.width = self.image.get_width()

    def update(self, game):
        self.x -= game.game_speed
        if self.x < -(SCREEN_WIDTH + 1000):
            self.x = SCREEN_WIDTH + random.randint(2500, 3000)
            self.y = random.randint(50, 100)

    def draw(self, screen):
        screen.blit(self.image, (self.x, self.y))
        screen.blit(self.image, (self.x - 200, self.y + 100))
        screen.blit(self.image, (self.x - 1000, self.y - 50))
        screen.blit(self.image, (self.x - 100, self.y + 100))
        screen.blit(self.image, (self.x + 500, self.y + 50))
        screen.blit(self.image, (self.x + 200, self.y + 100))
