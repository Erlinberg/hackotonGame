import pygame

# External Classes -----------------------------------------------------------------------#
from PlayerMovement import PlayerMovement
from Player import Player
from Boss import SnowBoss
from Level import Level
from renderer import Renderer
from ImageLoader import ImageLoader
from SpellController import SpellController
from MouseController import MouseController
from SoundController import SoundController
# ----------------------------------------------------------------------------------------#

pygame.mixer.pre_init(44100, -16, 2, 2048)
pygame.mixer.init()
pygame.init()

class Game():
    def __init__(self):
        self.currentProgram = 'snow' # Current main loop

        WIDTH, HEIGHT = 720,406 # Output video quality

        self.clock = pygame.time.Clock()

        self.renderer = Renderer(WIDTH, HEIGHT)
        self.imageLoader = ImageLoader()
        self.soundController = SoundController('bgMusic.ogg',[('cutSpell',0.1)],0.1)
        self.mouseController = MouseController()

        self.player = Player((WIDTH, HEIGHT),self.imageLoader.imageStorage["player"],[(0,2),(2,5),(5,8),(8,11),(11,14),(14,22),(22,37)])
        self.spellController = SpellController(self.mouseController,self.imageLoader.imageStorage,self.renderer, self.player,self.soundController)


        self.enemy = pygame.sprite.Group()
        self.spellController.enemies = self.enemy

        self.level = None
        self.playerMovement = None

    

    def snowLevelInit(self):
        # TEST
        self.enemy.empty()
        boss = SnowBoss((105,105),self.imageLoader.imageStorage['snowBoss'])
        self.enemy.add(boss)
        # TEST

        self.spellController.enemies = self.enemy

        self.level = Level("level",self.imageLoader.imageStorage["snowLevel"],self.imageLoader.imageStorage["snowDeco"],(30,30),(23,18))
        self.playerMovement = PlayerMovement(self.player,2,self.level)


    def snowLevelRun(self):
        pressed_keys = pygame.key.get_pressed()
            
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                return False
            self.playerMovement.animationChange(event)
            self.spellController.checkOnMouseClick(event.type)

        if not self.spellController.spellSquareActive:
            self.playerMovement.move(pressed_keys)
            self.player.update()
            self.spellController.updateSpells()
            self.level.decorationsGroup.update()

        self.mouseController.update()

        self.renderer.cameraUpdate(self.player.rect)

        self.renderer.fillBackground()

        self.renderer.blitGroup(self.level.levelBlocks)
        self.renderer.blitGroup(self.level.decorationsGroup)
        self.renderer.blitGroup(self.enemy)

        self.renderer.blitSprite(self.player)

        self.spellController.blitSpells()
            
        self.clock.tick(60)

        # IN-GAME RENDER -------------------------------------------------------------------------#
        self.renderer.update(self.spellController.spellSquareActive)
        #-----------------------------------------------------------------------------------------#

        # UI RENDER ------------------------------------------------------------------------------#
        self.spellController.drawSpellSquare()
        #-----------------------------------------------------------------------------------------#

            
        pygame.display.update()

        return True

    def main(self):
        self.snowLevelInit()
        running = True
        while running:
            if self.currentProgram == 'menu':
                pass
            elif self.currentProgram == 'snow':
                running = self.snowLevelRun()

        pygame.quit()

game = Game()
game.main()