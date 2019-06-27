import pygame
from pygame.locals import *
import time
from random import randint
'''
TODO:
Меню:
    Скоростные сложности
    Локации
    Рекорды
    Выход
Идентифкация игрока после смерти змейки
Видимые барьеры
Новые картинки
'''
class Apple:
    x = 0
    y = 0
    def newCoord(self):
        self.x = randint(0,self.windowWidth-self.blockSize)
        self.y = randint(0,self.windowHeight-self.blockSize)
        if(divmod(self.x,self.blockSize)[1]>0):
            self.x -= (divmod(self.x,self.blockSize)[1])

        if(divmod(self.y,self.blockSize)[1]>0):
            self.y -= (divmod(self.y,self.blockSize)[1])

    def __init__(self,w,h,b):
        self.windowWidth = w
        self.windowHeight = h
        self.blockSize = b
        self.newCoord()


class Player:

    x = [0]
    y = [0]
    speed = 0
    isDead = False
    score = 0
    size = 3
    def __init__(self,w,h,b):
        self.windowWidth = w
        self.windowHeight = h
        self.blockSize = b
        self.x=[0]*self.size
        self.y=[0]*self.size
        # print(x)
        for i in range(self.size): 
            self.x[i] = w/2 - b/2 -self.blockSize * i
            self.y[i] = h/2 - b/2
        self.speed=b


    def moveRight(self):
        for i in range(self.size-1,0,-1):
            self.x[i] = self.x[i-1]
            self.y[i] = self.y[i-1]
        self.x[0] = self.x[0] + self.speed
        if (self.x[0]>self.windowWidth-self.blockSize):
            self.isDead=True
        for i in range(self.size-1,0,-1):
            if(self.x[i]==self.x[0] and self.y[i]==self.y[0]):
                self.isDead=True



    def moveLeft(self):
        for i in range(self.size-1,0,-1):
            self.x[i] = self.x[i-1]
            self.y[i] = self.y[i-1]
        self.x[0] = self.x[0] - self.speed
        if (self.x[0]<0):
            self.isDead=True
        for i in range(self.size-1,0,-1):
            if(self.x[i]==self.x[0] and self.y[i]==self.y[0]):
                self.isDead=True

    def moveDown(self):
        for i in range(self.size-1,0,-1):
            self.y[i] = self.y[i-1]
            self.x[i] = self.x[i-1]
        self.y[0] = self.y[0] + self.speed 
        if (self.y[0]>self.windowHeight-self.blockSize):
            self.isDead=True
        for i in range(self.size-1,0,-1):
            if(self.x[i]==self.x[0] and self.y[i]==self.y[0]):
                self.isDead=True


    def moveUp(self):
        for i in range(self.size-1,0,-1):
            self.y[i] = self.y[i-1]
            self.x[i] = self.x[i-1]
        self.y[0] = self.y[0] - self.speed 
        if (self.y[0]<0):
            self.isDead=True
        for i in range(self.size-1,0,-1):
            if(self.x[i]==self.x[0] and self.y[i]==self.y[0]):
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
        for i in range(self.player.size):
            self._display.blit(self._image,(self.player.x[i],self.player.y[i]))
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
                if (not((self.player.x[0] != self.player.x[1]) and (self.player.y[0] != self.player.y[1]))):
                    if (self.direction != 4):
                        if(self.direction!=2):
                            self.direction=2
                    # self.player.x+=self.blockSize - divmod(self.player.x,self.blockSize)[1]
                    # self.player.y+=self.blockSize - divmod(self.player.y,self.blockSize)[1]

            if (keys[K_LEFT]):
                if (not((self.player.x[0] != self.player.x[1]) and (self.player.y[0] != self.player.y[1]))):
                    if(self.direction != 2 and self.direction != 0):
                        self.direction=4

            if (keys[K_DOWN]):
                if (not((self.player.x[0] != self.player.x[1]) and (self.player.y[0] != self.player.y[1]))):
                    if(self.direction != 1):
                        self.direction=3

            if (keys[K_UP]):
                if (not((self.player.x[0] != self.player.x[1]) and (self.player.y[0] != self.player.y[1]))):
                    if(self.direction != 3):
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


            if (self.player.x[0] == self.apple.x and self.player.y[0] == self.apple.y):
                self.apple.newCoord()
                self.player.score += 1
                self.player.size += 1
                self.player.x.insert(self.player.size,self.player.x[len(self.player.x)-1])
                self.player.y.insert(self.player.size,self.player.y[len(self.player.y)-1])
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