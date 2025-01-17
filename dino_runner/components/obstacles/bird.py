import random

from dino_runner.components.obstacles.obstacle import Obstacle


class Bird(Obstacle):
    BIRD_HEIGHT = [220, 260, 320]

    def __init__(self, image):
        self.type = 0
        super().__init__(image, self.type)
        self.rect.y = random.choice(self.BIRD_HEIGHT)
        self.index = 0

    def draw(self, screen):
        self.index += 1
        if self.index >= 10:
            self.index = 0
        screen.blit(self.image[self.index // 5], self.rect)
        


   



