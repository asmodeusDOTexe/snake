## -*- coding: utf-8 -*-.
import pygame
from pygame.locals import *
import time
from random import randint

clock = pygame.time.Clock()


def text_objects(text, font):
    textSurface = font.render(text, True, (0,0,0))
    return textSurface, textSurface.get_rect()

class Apple:
    x = -1
    y = -1
    def SetWall(self,v,n):
        self.appleX = v
        self.appleY = n
    def newCoord(self):
        appleOk = False
        while(not appleOk):
            self.x = randint(0,self.windowWidth-self.blockSize)
            self.y = randint(0,self.windowHeight-self.blockSize)
            self.x = self.x // self.blockSize
            self.y = self.y // self.blockSize   
            self.x *= self.blockSize
            self.y *= self.blockSize     
            appleOk = True

            for i in range(len(self.appleX)):
                if self.appleX[i] == self.x:
                    if self.appleY[i] == self.y:
                        appleOk = False

    def __init__(self,w,h,b):
        self.windowWidth = w
        self.windowHeight = h
        self.blockSize = b
        self.appleX = []
        self.appleY = []

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
        for i in range(self.size): 
            self.x[i] = w/2 - b/2 -self.blockSize * i
            self.y[i] = h/2 - b/2
        self.speed=b


    def moveRight(self):
        if (self.x[0] + self.speed>self.windowWidth-2*self.blockSize):
            self.isDead=True
        else:
            for i in range(self.size-1,0,-1):
                self.x[i] = self.x[i-1]
                self.y[i] = self.y[i-1]
            self.x[0] = self.x[0] + self.speed
        for i in range(self.size-1,0,-1):
            if(self.x[i]==self.x[0] and self.y[i]==self.y[0]):
                self.isDead=True



    def moveLeft(self):
        if (self.x[0]-self.speed<self.blockSize):
            self.isDead=True
        else:
            for i in range(self.size-1,0,-1):
                self.x[i] = self.x[i-1]
                self.y[i] = self.y[i-1]
            self.x[0] = self.x[0] - self.speed
        for i in range(self.size-1,0,-1):
            if(self.x[i]==self.x[0] and self.y[i]==self.y[0]):
                self.isDead=True

    def moveDown(self):
        if (self.y[0] + self.speed>self.windowHeight-2*self.blockSize):
            self.isDead=True
        else:
            for i in range(self.size-1,0,-1):
                self.y[i] = self.y[i-1]
                self.x[i] = self.x[i-1]
            self.y[0] = self.y[0] + self.speed 
        for i in range(self.size-1,0,-1):
            if(self.x[i]==self.x[0] and self.y[i]==self.y[0]):
                self.isDead=True


    def moveUp(self):
        if (self.y[0]-self.speed<self.blockSize):
            self.isDead=True
        else:
            for i in range(self.size-1,0,-1):
                self.y[i] = self.y[i-1]
                self.x[i] = self.x[i-1]
            self.y[0] = self.y[0] - self.speed 
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
    cur_screen = 0
    pause = False
    wall_x=[]
    wall_y=[]

    def __init__(self):
        self._running = True
        self._display = None
        self._image = None
        self._food = None
        self.wall = None
        
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
        self.wall = pygame.image.load("wall.jpeg").convert()
        self._image_head = pygame.image.load("snake_16 (head).jpeg").convert()

    def create_wall(self,x,y,x1,y1):
        if(x==x1):
            for i in range(y,y1,self.blockSize):
                self.wall_x.insert(len(self.wall_x),x)
                self.wall_y.insert(len(self.wall_y),i)
                self._display.blit(self.wall,(x,i))
        if(y==y1):
            for i in range(x,x1,self.blockSize):
                self.wall_x.insert(len(self.wall_x),i)
                self.wall_y.insert(len(self.wall_y),y)
                self._display.blit(self.wall,(i,y))




    def on_render(self):
        self._display.fill((0,0,0))
        if self.cur_screen == 1:
            
            for i in range(1,self.player.size):
                self._display.blit(self._image,(self.player.x[i],self.player.y[i]))
            self._display.blit(self._image_head,(self.player.x[0],self.player.y[0]))
            self._display.blit(self._food,(self.apple.x,self.apple.y))
            self.create_wall(0,0,0,self.windowHeight - self.blockSize + 1)
            self.create_wall(0,0,self.windowWidth - self.blockSize + 1,0)
            self.create_wall(self.windowWidth - self.blockSize,0,self.windowWidth - self.blockSize,self.windowHeight - self.blockSize + 1)
            self.create_wall(0,self.windowHeight - self.blockSize,self.windowWidth - self.blockSize + 1,self.windowHeight - self.blockSize)
        elif self.cur_screen == 0:
            self.pause = True
            mouse = pygame.mouse.get_pos()
            if 612 > mouse[0] > 204 and 290 > mouse[1] > 190:
                pygame.draw.rect(self._display, (200,200,200),(204,190,408,100))
                if pygame.mouse.get_pressed()[0] == 1:
                    self.cur_screen = 1
                    self.direction = 0
                    self.player.isDead = False
                    self._running = True
                    self.__init__()
                    self._display = pygame.display.set_mode((self.windowWidth,self.windowHeight))
                    
                    pygame.display.set_caption('Snake game')
                    self._running = True
                    self._image = pygame.image.load("snake_16.jpeg").convert()
                    self._food = pygame.image.load("apple_16.jpeg").convert()
                    self.wall = pygame.image.load("wall.jpeg").convert()
                    self._image_head = pygame.image.load("snake_16 (head).jpeg").convert()
                    self.pause = False
                    self.player.isDead = False
                    while(True):
                        self.apple.newCoord()
                        brk = True
                        for j in range(len(self.wall_x)):
                            if(self.wall_x[j] == self.apple.x):
                                if(self.wall_y[j] == self.apple.y):
                                    brk = False
                        for i in range(len(self.player.x)):
                            if(self.player.x[i] == self.apple.x):
                                if(self.player.y[i] == self.apple.y):
                                    brk = False
                        if(brk):
                            break
            else:
                pygame.draw.rect(self._display, (255,255,255),(204,190,408,100))
            if 612 > mouse[0] > 204 and (145 + 145 + 145) > mouse[1] > (45 + 145 + 145):
                pygame.draw.rect(self._display, (200,200,200),(204,335,408,100))
                if pygame.mouse.get_pressed()[0] == 1:
                    self._running = False
            else:
                pygame.draw.rect(self._display, (255,255,255),(204,335,408,100))

            largeText = pygame.font.Font('freesansbold.ttf',70)
            TextSurf, TextRect = text_objects("Новая Игра", largeText)
            TextRect.center = (408,240)
            
            self._display.blit(TextSurf, TextRect)
            
            
            largeText = pygame.font.Font('freesansbold.ttf',70)
            TextSurf, TextRect = text_objects("Выход", largeText)
            TextRect.center = (408,385)

            self._display.blit(TextSurf, TextRect)

        pygame.display.update()
        clock.tick(10)
    def on_cleanup(self):
        pygame.quit()
 
    def on_execute(self):
        self.on_init()
        self.create_wall(0,0,0,64)
        while( self._running ):
            pygame.event.pump()
            keys = pygame.key.get_pressed() 
            if(self.pause == False):
                
                
                if (keys[K_RIGHT]):
                    if (not((self.player.x[0] != self.player.x[1]) and (self.player.y[0] != self.player.y[1]))):
                        if (self.direction != 4):
                            if(self.direction!=2):
                                self.direction=2
                elif (keys[K_LEFT]):
                    if (not((self.player.x[0] != self.player.x[1]) and (self.player.y[0] != self.player.y[1]))):
                        if(self.direction != 2 and self.direction != 0):
                            self.direction=4

                elif (keys[K_DOWN]):
                    if (not((self.player.x[0] != self.player.x[1]) and (self.player.y[0] != self.player.y[1]))):
                        if(self.direction != 1):
                            self.direction=3

                elif (keys[K_UP]):
                    if (not((self.player.x[0] != self.player.x[1]) and (self.player.y[0] != self.player.y[1]))):
                        if(self.direction != 3):
                            self.direction=1

                if (keys[K_ESCAPE]):
                    self.cur_screen = 0

                for j in range(len(self.wall_x)):
                    if(self.wall_x[j] == self.player.x[0]):
                        if(self.wall_y[j] == self.player.y[0]):
                            self.player.isDead = True

                if (self.player.isDead!=True):


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
                        self.player.isDead=True



                if (self.player.x[0] == self.apple.x and self.player.y[0] == self.apple.y) or (self.apple.x == -1 and self.apple.y == -1):
                    while(True):
                        self.apple.newCoord()
                        brk = True
                        for j in range(len(self.wall_x)):
                            if(self.wall_x[j] == self.apple.x):
                                if(self.wall_y[j] == self.apple.y):
                                    brk = False
                        for i in range(len(self.player.x)):
                            if(self.player.x[i] == self.apple.x):
                                if(self.player.y[i] == self.apple.y):
                                    brk = False
                        if(brk):
                            break

                    if (self.apple.x != -1 and self.apple.y != -1):
                        self.player.score += 1
                        self.player.size += 1
                        self.player.x.insert(self.player.size,self.player.x[len(self.player.x)-1])
                        self.player.y.insert(self.player.size,self.player.y[len(self.player.y)-1])
                sec = divmod(time.time()-self.t,1)[0]
                min_cap = divmod(sec,60)[0]
                sec_cap = divmod(sec,60)[1]
                if (not self.player.isDead) and self.cur_screen == 1:
                    caption = "SNAKE: " + "Съедено яблок: " \
                    + str(self.player.score) + " | " + "Время: " + str(min_cap)[:-2] + "m " + str(sec_cap)[:-2] + "s"
                    pygame.display.set_caption(caption)


            self.on_render()
        self.on_cleanup()
 
if __name__ == "__main__" :
    theApp = App()
    theApp.on_execute()