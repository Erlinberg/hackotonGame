import pygame

class AmountBars():
    def __init__(self, player, boss, images, center):
        self.hp = images[0]
        self.mana = images[1]
        self.bossHP = images[2]

        self.hpRect = pygame.Rect((0,0),self.hp.get_size())
        self.hpRect.center = center
        self.hpRect.y = 10

        self.manaRect = pygame.Rect((0,0),self.mana.get_size())
        self.manaRect.center = center
        self.manaRect.y = 25

        self.bossHPRect = pygame.Rect((0,0),self.bossHP.get_size())
        self.bossHPRect.center = center
        self.bossHPRect.y = 360

        self.player = player
        self.boss = boss

    def updateHP(self, renderer):
        color = (255,61,96)
        filling = self.player.lives/self.player.defaultHP
        size = (int(filling*679), 4)
        renderer.drawUIRect(color,pygame.Rect((self.hpRect.x+4,self.hpRect.y+4),size))

    def updateMana(self, renderer):
        color = (51,157,198)
        filling = self.player.mana/self.player.defaultMana
        size = (int(filling*195), 6)
        renderer.drawUIRect(color,pygame.Rect((self.manaRect.x+6,self.manaRect.y+4),size))

    def updateBossHP(self, renderer):
        color = (175,17,46)
        filling = self.boss.lives/self.boss.defaultHP
        size = (int(filling*705), 4)
        renderer.drawUIRect(color,pygame.Rect((self.bossHPRect.x+6,self.bossHPRect.y+4),size))


    def drawBars(self,renderer):
        self.updateHP(renderer)
        self.updateBossHP(renderer)
        self.updateMana(renderer)
        renderer.blitUISeparate(self.hp,self.hpRect)
        renderer.blitUISeparate(self.mana,self.manaRect)
        renderer.blitUISeparate(self.bossHP,self.bossHPRect)
