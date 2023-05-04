import pygame
import random


class PowerUpManager:
    def __init__(self, when_appears):
        self.power_ups = []
        self.when_appears = when_appears
        self.duration = random.randint(3, 5)

    def generate_power_up(self):
        pass

    #reconoce que tiene un poder
    def update(self, game):
        if len(self.power_ups) == 0 and self.when_appears == game.score:
            self.generate_power_up()


        for power_up in self.power_ups:
            power_up.update(game.game_speed, self.power_ups)
            if game.player.dino_rect.colliderect(power_up):
                power_up.start_time = pygame.time.get_ticks()
                game.player.type = power_up.type

    def draw(self, screen):
        for power_up in self.power_ups:
            power_up.draw(screen)

    def reset(self):
        self.power_ups = []
        self.when_appears = random.randint(100, 200)
