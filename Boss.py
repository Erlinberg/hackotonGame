import pygame
import math
from Animator import Animation

class Snowflake(pygame.sprite.Sprite):
    def __init__(self, pos, image, player, direction, distance, damage, group):
        super(Snowflake, self).__init__()
        self.image = image
        self.rect = pygame.Rect(pos, self.image.get_size())

        self.speed = 3
        self.player = player
        self.direction = (direction[0]*self.speed, direction[1]*self.speed)
        self.distanceMax = distance
        self.damage = damage

        self.distancePassed = 0

        group.add(self)

    @property
    def collidesPlayer(self):
        return self.rect.colliderect(self.player.rect)

    def update(self):
        self.rect.move_ip(self.direction)
        self.distancePassed += math.sqrt(self.direction[0]**2 + self.direction[1]**2)
        if self.distancePassed >= self.distanceMax:
            self.kill()

        if self.collidesPlayer:
            self.player.dealDamage(self.damage)
            self.kill()


class SnowBoss(pygame.sprite.Sprite):
    def __init__(self, pos, images,snowflakeImage, lives, player, attackdist, timerController):
        super(SnowBoss, self).__init__()
        self.images = images
        self.image = images[0]
        self.rect = pygame.Rect(pos, self.image.get_size())

        self.lives = lives
        self.defaultHP = lives 

        self.player = player
        self.atackdis = attackdist
        self.snowflakeImage = snowflakeImage
        self.timerController = timerController

        self.noticed = False
        self.snowflakes = pygame.sprite.Group()
        self.speed = 2.5
        self.currentlyAttack = False
        self.approaching = True
        self.animationController = Animation(2,self)
    
    def dealDamage(self,damage):
        self.lives -= damage
        if self.lives <= 0:
            self.kill()

    @property
    def xDistance(self):
        return self.player.rect.centerx - self.rect.centerx 

    @property
    def yDistance(self):
        return self.player.rect.centery - self.rect.centery

    def approach(self, untilDist=60):
        sign = lambda x: x and (1, -1)[x < 0]

        direction = (sign(self.xDistance)*self.speed, sign(self.yDistance)*self.speed)
        distance = math.sqrt((self.xDistance)**2 + (self.yDistance)**2)

        if distance <= untilDist:
            if not self.currentlyAttack:
                self.timerController.createTimer(1, self.iceFreeze, False)
                self.currentlyAttack = True
            return True
        
        self.rect.move_ip(direction)
        return False

    def checkPlayer(self):
        distance = math.sqrt((self.xDistance)**2 + (self.yDistance)**2)
        if distance <= self.atackdis:
            self.noticed = True
            self.snowBall()
            
    def snowBall(self):
        sign = lambda x: x and (1, -1)[x < 0]
        direction = (sign(self.xDistance), sign(self.yDistance))
        snowflake = Snowflake(self.rect.center, self.snowflakeImage, self.player, direction, 400, 15, self.snowflakes)
        self.currentlyAttack = False

    def snowRing(self):
        diresctions = [(-1,1),(0,1),(1,1),(-1,0),(1,0),(-1,-1),(0,-1),(1,-1)]
        for direction in diresctions:
            snowFlake = Snowflake(self.rect.center, self.snowflakeImage, self.player, direction, 300, 5, self.snowflakes)
        self.currentlyAttack = False


    def iceFreeze(self):
        radius = pygame.Rect(self.rect.center,(75,75))
        if radius.colliderect(self.player.rect):
            self.player.freeze()
            self.timerController.createTimer(1, self.snowBall, False)
        else:
            self.timerController.createTimer(1, self.snowRing, False)

    def aproachVar(self):
        self.approaching = True

    def update(self):
        if not self.noticed:
            self.checkPlayer()
        else:
            if self.approaching:
                if self.approach():
                    self.approaching = False
                    self.timerController.createTimer(3, self.aproachVar, False)

        self.snowflakes.update()

        self.timerController.updateTimers()

        self.animationController.animateRepeat(self.images,2)

