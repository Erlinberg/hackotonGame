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
from Menu import Menu
from AmountBars import AmountBars
from Timer import TimerController
# ----------------------------------------------------------------------------------------#

pygame.mixer.pre_init(44100, -16, 2, 2048)
pygame.mixer.init()
pygame.init()

class Game():
    def __init__(self):
        self.currentProgram = 'menu' # Current main loop

        WIDTH, HEIGHT = 720,406 # Output video quality

        self.clock = pygame.time.Clock()
        self.timerController = TimerController()

        self.renderer = Renderer(WIDTH, HEIGHT)
        self.imageLoader = ImageLoader()
        self.soundController = SoundController('bgMusic.ogg',[('cutSpell',0.1),('lightingSpell',0.1),('explosionSpell',0.1)],0.05)
        self.mouseController = MouseController()
        self.menu = Menu(self.imageLoader.imageStorage['menu'],self)

        self.player = Player((WIDTH, HEIGHT),self.imageLoader.imageStorage["player"],[(0,2),(2,5),(5,8),(8,11),(11,14),(14,22),(22,37)])
        self.spellController = SpellController(self.mouseController,self.imageLoader.imageStorage,self.renderer, self.player,self.soundController)

        self.amountBars = AmountBars(self.player, None, self.imageLoader.imageStorage['bars'],(WIDTH//2,HEIGHT//2))

        self.boss = None

        self.level = None
        self.playerMovement = None

    def menuRun(self):
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                return False

        self.renderer.fillBackground()

        self.menu.update(self.mouseController, self.renderer)

        pygame.display.update()
        return True

    def snowLevelInit(self):
        # TEST
        self.boss = SnowBoss((105,105),self.imageLoader.imageStorage['snowBoss'],pygame.image.load('snow.png'), 1000, self.player, 300, self.timerController)
        # TEST

        self.amountBars.boss = self.boss

        self.spellController.enemy = self.boss

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
            self.boss.update()

        self.mouseController.update()

        self.renderer.cameraUpdate(self.player.rect)

        self.renderer.fillBackground()

        self.renderer.blitGroup(self.level.levelBlocks)
        self.renderer.blitGroup(self.level.decorationsGroup)
        self.renderer.blitSprite(self.boss)

        self.renderer.blitSprite(self.player)

        self.renderer.blitGroup(self.boss.snowflakes)

        self.spellController.blitSpells()
            
        self.clock.tick(60)

        # IN-GAME RENDER -------------------------------------------------------------------------#
        self.renderer.update(self.spellController.spellSquareActive)
        #-----------------------------------------------------------------------------------------#

        # UI RENDER ------------------------------------------------------------------------------#
        self.spellController.drawSpellSquare()
        self.amountBars.drawBars(self.renderer)
        #-----------------------------------------------------------------------------------------#

            
        pygame.display.update()

        return True

    def main(self):
        self.snowLevelInit()
        running = True
        while running:
            if self.currentProgram == 'menu':
                running = self.menuRun()
            elif self.currentProgram == 'snow':
                running = self.snowLevelRun()

        pygame.quit()

game = Game()
game.main()