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

    def animationChange(self,event):
        if not self.player.spellCasting:
            if event.type == pygame.KEYDOWN:
                if event.key == K_w:
                    self.player.changeAnimation(4)
                elif event.key == K_s:
                    self.player.changeAnimation(1)
                elif event.key == K_a:
                    self.player.changeAnimation(3)
                elif event.key == K_d:
                    self.player.changeAnimation(2)
            elif event.type == pygame.KEYUP:
                self.player.changeAnimation(0)

    def checkAnimation(self,animID):
        if not self.player.currentAnimation == animID and not self.player.spellCasting:
            self.player.changeAnimation(animID)

    def move(self,pressed_keys):
        if pressed_keys[K_w]:
            self.player.rect.move_ip(0, -self.speed)
            self.checkAnimation(4)
            if self.wallCollision:
                self.player.rect.move_ip(0, self.speed)
        elif pressed_keys[K_s]:
            self.player.rect.move_ip(0, self.speed)
            self.checkAnimation(1)
            if self.wallCollision:
                self.player.rect.move_ip(0, -self.speed)
        elif pressed_keys[K_a]:
            self.player.rect.move_ip(-self.speed, 0)
            self.checkAnimation(3)
            if self.wallCollision:
                self.player.rect.move_ip(self.speed, 0)
        elif pressed_keys[K_d]:
            self.player.rect.move_ip(self.speed, 0)
            self.checkAnimation(2)
            if self.wallCollision:
                self.player.rect.move_ip(-self.speed, 0)
        else:
            self.checkAnimation(0)

        