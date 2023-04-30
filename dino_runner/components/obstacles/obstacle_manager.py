import pygame
import random

from dino_runner.components.obstacles.cactus import Cactus
from dino_runner.components.obstacles.bird import Bird
from dino_runner.utils.constants import SMALL_CACTUS, LARGE_CACTUS, BIRD


class ObstacleManager:
    def __init__(self):
        self.obstacles = []

    def generate_obstacle(self, oType):
        if oType == 0:
           obstacle = Cactus(SMALL_CACTUS)            #Small_cactus
        elif oType == 1:
           obstacle = Cactus(LARGE_CACTUS)            #Large_cactus
        elif oType == 2:
           obstacle = Bird(BIRD)                      #ave
        return obstacle    

    def update(self, game):
        if len(self.obstacles) == 0:
            oType = random.randint(0,2)
            obstacle = self.generate_obstacle(oType)
            self.obstacles.append(obstacle)

        for obstacle in self.obstacles:
            obstacle.update(game.game_speed, self.obstacles)
            if game.player.dino_rect.colliderect(obstacle.rect):
                game.playing = False
                pygame.time.delay(1000)
                break


    def draw(self, screen):
        for obstacle in self.obstacles:
            obstacle.draw(screen)