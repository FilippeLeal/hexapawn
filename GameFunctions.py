#importing pygame and random module
import pygame
import random
from Pieces import *

#Change game directory and size accordingly
#direc = r"C:\Users\filip\Documents\python codes\hexapawn\local"     #desktop location
direc = r"C:\Users\Filippe\Documents\GitHub\hexapawn"              #notebook location
#size refers to: width and height of screen
size=[360,385]                     #mini size
board=5     #number of tiles on the side

def makeBoard(size,board):
    logo = pygame.image.load(direc+"\\pawn.png")
    pygame.display.set_icon(logo)
    pygame.display.set_caption("HexaPawn")
    
    #creating the surface for the screen
    screen = pygame.display.set_mode((size[0],size[1]))

    #drawing tiles:
    brown=(185,122,87)
    white=(255,255,255)
    squareSize=int(size[0]/board)
    screen.fill(white)
    for i in range(0,board):
        for i2 in range(0,board):
            if (i+i2)%2==0:
                pygame.draw.rect(screen,brown,(int(i*squareSize),int(i2*squareSize),squareSize,squareSize))

    pygame.display.update()
    return screen

def write(text,wait,size,screen):
    screen.fill((255,255,255),(0,size[0],size[0],(size[1]-size[0])))
    screen.blit(pygame.font.SysFont('Arial', int(size[0]/20)).render(text, False, (0, 0, 255)),(0,size[0]))
    pygame.display.update()
    pygame.time.wait(wait)

def startGame(screen,board=board,size=size):
    #create and draw pieces in place
        plist=[]        #piece list
        for i in range(0,board):
            plist.append(Pieces((i,0),"CPU",board))
            plist[-1].draw(screen,size,board)
        for i2 in range(0,board):
            plist.append(Pieces((i2,board-1),"player",board))
            plist[-1].draw(screen,size,board)
        # Text at the bottom
        write("Select the Piece you want to move",0,size,screen)
        pygame.display.update()
        
        return plist

def getTileLocation(click,plist,board=board,size=size):
    x=int((click[0]/(size[0]/board)))
    y=int((click[1]/(size[0]/board)))
    target=(x,y)
    for i in plist:
        if i.getLocation()==(x,y):
            target=i
    return target

def selectPiece(piece,size,screen,board): 
    selected=[]
    if type(target)==tuple:
        write("No Piece there!",1000,size,screen)
        write("Select the Piece you want to move",0,size,screen)
    elif target.getController()=="CPU":
        write("That's not your piece! yours are blue!",1000,size,screen)
        write("Select the Piece you want to move",0,size,screen)
    else:
        target.setColor((255,255,0))
        target.draw(screen,size,board)
        pygame.display.update()
        selected=target
    return selected