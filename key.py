import pygame
from pygame.locals import *
import time
from random import randint

class Apple:
    x = 0
    y = 0
    def newCoord(self):
        self.x = randint(0,self.windowWidth-self.blockSize)
        self.y = randint(0,self.windowHeight-self.blockSize)
        if(divmod(self.x,self.blockSize)[1]>0):
            print(self.x)
            self.x -= (divmod(self.x,self.blockSize)[1])

        if(divmod(self.y,self.blockSize)[1]>0):
            self.y -= (divmod(self.y,self.blockSize)[1])

    def __init__(self,w,h,b):
        self.windowWidth = w
        self.windowHeight = h
        self.blockSize = b
        self.newCoord()


class Player:

    x = 0
    y = 0
    speed = 0
    isDead = False
    score = 0
    def __init__(self,w,h,b):
        self.windowWidth = w
        self.windowHeight = h
        self.blockSize = b
        self.x = w/2 - b/2
        self.y = h/2 - b/2
        self.speed=b


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

    windowWidth = 816
    windowHeight = 624
    blockSize = 16
    player = 0
    direction = 0
    apple = 0
    gameOver = False
    def __init__(self):
        self._running = True
        self._display = None
        self._image = None
        self._food = None
        self.player = Player(self.windowWidth,self.windowHeight,self.blockSize) 
        self.apple = Apple(self.windowWidth,self.windowHeight,self.blockSize)
        self.t = time.time()

    def on_init(self):
        pygame.init()
        self._display = pygame.display.set_mode((self.windowWidth,self.windowHeight))
        
        pygame.display.set_caption('Snake game')
        self._running = True
        self._image = pygame.image.load("snake_16.jpeg").convert()
        self._food = pygame.image.load("apple_16.jpeg").convert()
    
    def on_render(self):
        self._display.fill((0,0,0))
        self._display.blit(self._image,(self.player.x,self.player.y))
        self._display.blit(self._food,(self.apple.x,self.apple.y))
        pygame.display.update()
 
    def on_cleanup(self):
        pygame.quit()
 
    def on_execute(self):
        self.on_init()
 
        while( self._running ):
            pygame.event.pump()
            keys = pygame.key.get_pressed() 
            
            if (keys[K_RIGHT]):
                if(self.direction!=2):
                    self.direction=2
                    # self.player.x+=self.blockSize - divmod(self.player.x,self.blockSize)[1]
                    # self.player.y+=self.blockSize - divmod(self.player.y,self.blockSize)[1]

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

                time.sleep(0.125)


            if (self.player.x == self.apple.x and self.player.y == self.apple.y):
                self.apple.newCoord()
                self.player.score += 1
            sec = divmod(time.time()-self.t,1)[0]
            min_cap = divmod(sec,60)[0]
            sec_cap = divmod(sec,60)[1]
            if (not self.player.isDead):
                caption = "SNAKE: " + "Съедено яблок: " \
                + str(self.player.score) + " | " + "Время: " + str(min_cap)[:-2] + "m " + str(sec_cap)[:-2] + "s"
                pygame.display.set_caption(caption)


            self.on_render()
        self.on_cleanup()
 
if __name__ == "__main__" :
    theApp = App()
    theApp.on_execute()