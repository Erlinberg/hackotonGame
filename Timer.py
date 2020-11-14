import pygame

class Timer():
    def __init__(self, secondsDuration, onend, repeat):
        self.milisecondsDuration = secondsDuration*1000
        self.onend = onend
        self.repeat = repeat

        self.timerStart = 0

        self.startTimer()

        self.finished = False

    def startTimer(self):
        self.timerStart = pygame.time.get_ticks()

    def update(self):
        milisecondsPassed = pygame.time.get_ticks()-self.timerStart
        
        if milisecondsPassed >= self.milisecondsDuration and not self.finished:
            self.onend()
            if self.repeat:
                self.timerStart = pygame.time.get_ticks()
            else:
                self.finished = True


class TimerController():
    def __init__(self):
        self.timers = []

    def updateTimers(self):
        for timer in self.timers:
            timer.update()

    def createTimer(self, seconds, onend, repeat=False):
        self.timers.append(Timer(seconds, onend, repeat))