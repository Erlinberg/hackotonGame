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
# ----------------------------------------------------------------------------------------#

pygame.init()

WIDTH, HEIGHT = 720,406
clock = pygame.time.Clock()

renderer = Renderer(WIDTH, HEIGHT)
imageLoader = ImageLoader()
level = Level("level",imageLoader.imageStorage["level"],imageLoader.imageStorage["deco"],(30,30),(23,18))

player = Player((WIDTH, HEIGHT),imageLoader.imageStorage["player"],[(0,2),(2,5),(5,8),(8,11),(11,14),(14,22),(22,37)])

# TEST
boss = SnowBoss((105,105),imageLoader.imageStorage['snowBoss'])
enemy = pygame.sprite.Group([boss])
# TEST

playerMovement = PlayerMovement(player,3,level)
mouseController = MouseController()
spellController = SpellController(mouseController,imageLoader.imageStorage,renderer, player,enemy)

running = True
while running:
    pressed_keys = pygame.key.get_pressed()
    
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
        playerMovement.animationChange(event)
        spellController.checkOnMouseClick(event.type)

    if not spellController.spellSquareActive:
        playerMovement.move(pressed_keys)
        player.update()
        spellController.spellGroup.update()
        level.decorationsGroup.update()

    mouseController.update()

    renderer.cameraUpdate(player.rect)

    renderer.fillBackground()

    renderer.blitGroup(level.levelBlocks)
    renderer.blitGroup(level.decorationsGroup)
    renderer.blitGroup(enemy)

    renderer.blitSprite(player)

    renderer.blitGroup(spellController.spellGroup)
    
    clock.tick(60)

    # FPS Counter ----------------------------------------------------------------------------#
    #fps = font.render(str(int(clock.get_fps())), True, pygame.Color('purple'))
    #renderer.display.blit(fps, (50, 50))
    #-----------------------------------------------------------------------------------------#

    # IN-GAME RENDER -------------------------------------------------------------------------#
    renderer.update(spellController.spellSquareActive)
    #-----------------------------------------------------------------------------------------#

    # UI RENDER ------------------------------------------------------------------------------#
    spellController.drawSpellSquare(renderer)
    #-----------------------------------------------------------------------------------------#

    
    pygame.display.update()

# Done! Time to quit.
pygame.quit()