import pygame
from pygame.locals import (K_w,
    K_s,
    K_a,
    K_d,
)

class PlayerMovement():
    def __init__(self,player,speed, level):
        self.player = player
        self.speed = speed

        self.walls = level.walls

    @property
    def wallCollision(self):
        return pygame.sprite.spritecollide(self.player, self.walls, False)

    def check(self,pressed_keys):
        self.player.currentState = self.player.ends[0]
        self.player.animationController.animCount = self.player.currentState[1]-self.player.currentState[0]

        if pressed_keys[K_w]:
            self.player.rect.move_ip(0, -self.speed)
            self.player.currentState = self.player.ends[4]
            self.player.animationController.animCount = self.player.currentState[1]-self.player.currentState[0]
            if self.wallCollision:
                self.player.rect.move_ip(0, self.speed)
        elif pressed_keys[K_s]:
            self.player.rect.move_ip(0, self.speed)
            self.player.currentState = self.player.ends[1]
            self.player.animationController.animCount = self.player.currentState[1]-self.player.currentState[0]
            if self.wallCollision:
                self.player.rect.move_ip(0, -self.speed)
        elif pressed_keys[K_a]:
            self.player.rect.move_ip(-self.speed, 0)
            self.player.currentState = self.player.ends[3]
            self.player.animationController.animCount = self.player.currentState[1]-self.player.currentState[0]
            if self.wallCollision:
                self.player.rect.move_ip(self.speed, 0)
        elif pressed_keys[K_d]:
            self.player.rect.move_ip(self.speed, 0)
            self.player.currentState = self.player.ends[2]
            self.player.animationController.animCount = self.player.currentState[1]-self.player.currentState[0]
            if self.wallCollision:
                self.player.rect.move_ip(-self.speed, 0)

        