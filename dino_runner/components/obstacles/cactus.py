import random

from dino_runner.components.obstacles.obstacle import Obstacle
from dino_runner.utils.constants import SMALL_CACTUS, LARGE_CACTUS

class Cactus(Obstacle):
    def __init__(self, image):
        self.type = random.randint(0, 2)
        super().__init__(image, self.type)
        if self.image == SMALL_CACTUS:
            self.rect.y = 325   #small
        if self.image == LARGE_CACTUS:
            self.rect.y = 300   #Large
        

    