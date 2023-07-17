import pygame
import defineWindow
import math
import random
import tkinter as tk
from tkinter import messagebox


global WINDOW_WIDTH, WINDOW_HEIGHT
WINDOW_WIDTH = defineWindow.defineWindow()[0]    #I went ahead and threw the functions that I use for variable screen dimensions into its own reusable file
WINDOW_HEIGHT = defineWindow.defineWindow()[1]

class cube(object):
    rows = 20
    w = 500
    def __init__(self, start, dirnx=1, dirny=0, color=(255,0,0)):
        self.pos = start
        self.dirnx = 1
        self.dirny = 0
        self.color = color

    def move(self, dirnx, dirny):
        self.dirnx = dirnx
        self.dirny = dirny
        self.pos = (self.pos[0] + self.dirnx, self.pos[1] + self.dirny)

    def draw(self, surface, eyes=False):
        dis = self.w // self.rows
        i = self.pos[0]
        j = self.pos[1]

        pygame.draw.rect(surface, self.color, (i*dis+1,j*dis+1, dis-2, dis-2))
        if eyes:
            centre = dis//2
            radius = 3
            circleMiddle = (i*dis+centre-radius, j*dis+8)
            circleMiddle2 = (i*dis + dis - radius*2, j*dis+8)
            pygame.draw.circle(surface, (0,0,0), circleMiddle, radius)
            pygame.draw.circle(surface, (0,0,0), circleMiddle2, radius) #This whole mess determines where the eyes are placed
        

class snake(object):
    body = []
    turns = []
    def __init__(self, color, pos):
        self.color = color
        self.head = cube(pos)
        self.body.append(self.head) #Creates the snake, attaches head to the body
        self.dirnx = 0
        self.dirny = 1 #Keeps track of the direction that the snake is faceing / moving

    def move(self):
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
            
            keys = pygame.key.get_pressed()
            #for key in keys:
            if keys[pygame.K_LEFT]:
                self.dirnx = -1 
                self.dirny = 0 #We need to set the opposite x or y value to zero because the snake only moves one direction and not diagonally
                self.turns[self.head.pos[:]] = [self.dirnx, self.dirny] #Grabs the position of the head and stores that in the turns table. This will be used for the rest of the body to follow the path that the head took

            
            elif keys[pygame.K_RIGHT]:
                self.dirnx = 1
                self.dirny = 0
                self.turns[self.head.pos[:]] = [self.dirnx, self.dirny]

            elif keys[pygame.K_UP]:
                self.dirnx = 0 
                self.dirny = 1
                self.turns[self.head.pos[:]] = [self.dirnx, self.dirny]
            
            elif keys[pygame.K_DOWN]:
                self.dirnx = 0 
                self.dirny = -1
                self.turns[self.head.pos[:]] = [self.dirnx, self.dirny]
            
        for i, c in enumerate(self.body):
            p = c.pos[:]                    #Grabs the (P)osition of each (C)ube object in the body
            if p in self.turns:             
                turn = self.turns[p]        #Tells the body where it needs to turn to match what the head did
                c.move(turn[0],turn[1])
                if i == len(self.body) - 1:
                    self.turns.pop(p)       #If we are on the last cube of the body, delete that turn value, we don't need or want it anymore

            else:
                if c.dirnx == -1 and c.pos[0] <= 0: c.pos = (c.rows-1, c.pos[1]) #If we're moving left and x position of cube is less than or equal to zero, then change that position to the right side of the screen
                elif c.dirnx == 1 and c.pos[0] >= c.rows-1: c.pos = (0, c.pos[1]) #If we're moving right, put us on left side of screen
                elif c.dirnx == 1 and c.pos[1] >= c.rows-1: c.pos = (c.pos[0], 0) #If we're moving down, put us at top
                elif c.dirnx == -1 and c.pos[1] <= 0: c.pos = (c.pos[0], c.rows-1) #If moving up, put us at bottom
                else: c.move(c.dirnx, c.dirny) #If we're doing none of the above, just keep moving


def reset(self, pos):
    self.head = cube(pos)
    self.body = []
    self.body.append(self.head)
    self.turns = {}
    self.dirnx = 0
    self.dirny = 1


def addCube(self):
    tail = self.body[-1]
    dx, dy = tail.dirnx, tail.dirny

    if dx == 1 and dy == 0:
        self.body.append(cube((tail.pos[0]-1, tail.pos[1])))
    elif dx == -1 and dy == 0:
        self.body.append(cube((tail.pos[0]+1, tail.pos[1])))
    elif dx == 0 and dy == 1:
        self.body.append(cube((tail.pos[0], tail.pos[1]-1)))
    elif dx == 0 and dy == -1:
        self.body.append(cube((tail.pos[0], tail.pos[1]+1))) #This whole block chooses where to add the tail on the body, determined by where the current tail is moving

    self.body[-1].dirnx = dx
    self.body[-1].dirny = dy

def draw(self, surface):
    for i, c in enumerate(self.body):
        if i==0:
            c.draw(surface, True)  #If it is the first cube in the list, draw eyes
        else:
            c.draw(surface)

def drawGrid(w, rows, surface):
    sizeBetween = w // rows
    x = 0
    y = 0
    for i in range(rows):
        x = x + sizeBetween
        y = y + sizeBetween

        pygame.draw.line(surface, (255,255,255), (x,0), (x,w))
        pygame.draw.line(surface, (255,255,255), (0,y), (w,y)) #These two lines draw a horizontal and vertical line every loop / every row


def redrawWindow(surface):
    global rows, width, s, snack          #The tutorial used global s to represent a snake, please do not do this
    surface.fill((0,0,0))
    s.draw(surface)
    snack.draw(surface)
    drawGrid(width, rows, surface)
    pygame.display.update()

def randomSnack(rows, item):
    positions = item.body

    while True:
        x = random.randrange(rows)
        y = random.randrange(rows)
        if len(list(filter(lambda z:z.pos == (x,y), positions))) > 0: #This checks if new position "z" is equal to current positions "x,y" so that it doesn't place a snack on top of another snack
            continue
        else:
            break

def messageBox(subject, content):
    root = tk.Tk()
    root.attributes("-topmost", True) #This places the message box window over top of everything
    root.withdraw()
    messagebox.showinfo(subject, content)
    try:
        root.destroy()
    except:
        pass                 #Narrator does not know what this does

def main():
    global width, rows, s, snack
    width = 500
    rows = 20
    win = pygame.display.set_mode((WINDOW_WIDTH, WINDOW_HEIGHT)) #Creates the window for the app
    s = snake((255,0,0), (rows/2,rows/2)) #Creates the Snake, defines its color, and where to spawn it
    snack = cube(randomSnack(rows, s), color=(0,255,0))
    flag = True
    clock = pygame.time.Clock()
    while flag:
        pygame.time.delay(50) #Defines the 'tick' of the game
        clock.tick(10) #Sets the speed of the game at no more than 10 FPS
        s.move()
        if s.body[0].pos == snack.pos:
            s.addCube()
            snack = cube(randomSnack(rows, s), color=(0,255,0))

        for x in range(len(s.body)):
            if s.body[x].pos in list(map(lambda z:z.pos, s.body[x+1:])):
                print('Score: ', len(s.body))
                messageBox('You lost!', 'Play again...')
                s.reset((10,10))
                break

        redrawWindow(win)


main()

#Created with this tutorial https://www.youtube.com/watch?v=5tvER0MT14s
#Ultimately can't get it working, this tutorial is older so Tim was likely much more inexperienced
#I've used his newer stuff and it's much more refined, but this was pretty rough to follow