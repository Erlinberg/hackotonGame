import pygame

class SoundController():
    def __init__(self,backgroundMusic,SFXs,bgVol):
        self.backgroundMusic = pygame.mixer.music.load(backgroundMusic)
        pygame.mixer.music.set_volume(bgVol)
        pygame.mixer.music.play()


        self.SFX = self.loadSFX(SFXs)
        # spell 1
        # spell 2
        # hit

    def loadSFX(self,SFXs):
        result = {}
        for SFX in SFXs:
            result[SFX[0]] = pygame.mixer.Sound("Sounds/{0}{1}".format(SFX[0], ".ogg"))
            result[SFX[0]].set_volume(SFX[1])
        return result

    def playSFXOnce(self,soundName):
        if soundName in self.SFX:
            self.SFX[soundName].play()