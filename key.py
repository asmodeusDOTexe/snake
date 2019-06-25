import pygame
from pygame.locals import *
import time

class Player:

    x = 400-16
    y = 300-16
    speed = 10
    isDead = False
    def __init__(self,w,h,b):
        self.windowWidth = w
        self.windowHeight = h
        self.blockSize = b
        self.speed=self.blockSize


    def moveRight(self):
        self.x = self.x + self.speed
        if (self.x>self.windowWidth-self.blockSize):
            self.isDead=True
        



    def moveLeft(self):
        self.x = self.x - self.speed
        if (self.x<0):
            self.isDead=True

    def moveDown(self):
        self.y = self.y + self.speed 
        if (self.y>self.windowHeight-self.blockSize):
            self.isDead=True


    def moveUp(self):
        self.y = self.y - self.speed 
        if (self.y<0):
            self.isDead=True



class App:

    windowWidth = 800
    windowHeight = 600
    blockSize = 32
    player = 0
    direction = 0
    gameOver = False
    def __init__(self):
        self._running = True
        self._display = None
        self._image = None
        self.player = Player(self.windowWidth,self.windowHeight,self.blockSize) 

    def on_init(self):
        pygame.init()
        self._display = pygame.display.set_mode((self.windowWidth,self.windowHeight))
        
        pygame.display.set_caption('Snake game')
        self._running = True
        self._image = pygame.image.load("snake.jpeg").convert()
 
    
    def on_render(self):
        self._display.fill((0,0,0))
        self._display.blit(self._image,(self.player.x,self.player.y))
        pygame.display.update()
 
    def on_cleanup(self):
        pygame.quit()
 
    def on_execute(self):
        self.on_init()
 
        while( self._running ):
            pygame.event.pump()
            keys = pygame.key.get_pressed() 
            
            if (keys[K_RIGHT]):
                self.direction=2

            if (keys[K_LEFT]):
                self.direction=4

            if (keys[K_DOWN]):
                self.direction=3

            if (keys[K_UP]):
                self.direction=1

            if (keys[K_ESCAPE]):
                self._running = False

            if (self.gameOver!=True):


                if (self.direction>0):

                    if (self.direction==1):
                        self.player.moveUp()

                    elif (self.direction==2):
                        self.player.moveRight()

                    elif (self.direction==3):
                        self.player.moveDown()

                    elif (self.direction==4):
                        self.player.moveLeft()

                if (self.player.isDead):
                    self.direction=0
                    print("Game Over")
                    self.gameOver=True

                time.sleep(0.175)


            self.on_render()
        self.on_cleanup()
 
if __name__ == "__main__" :
    theApp = App()
    theApp.on_execute()