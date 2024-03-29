#importing pygame and random module
import pygame
from random import randint
from Pieces import *
from win32api import GetSystemMetrics


#size refers to: width and height of window
definition=GetSystemMetrics(1)
#size=[200,0]
size=[int(definition/1.5),0]
size[1]=int(size[0]*1.1)                     #mini size
board=3     #number of tiles on the side

def makeBoard(size,board):
    logo = pygame.image.load("pawn.png")
    pygame.display.set_icon(logo)
    pygame.display.set_caption("HexaPawn")
    
    #creating the surface for the screen
    screen = pygame.display.set_mode((size[0],size[1]))
    drawBoard(size,board,screen)
    pygame.display.update()
    return screen

def drawBoard(size,board,screen):
    #drawing tiles:
    brown=(185,122,87)
    white=(255,255,255)
    squareSize=int(size[0]/board)
    screen.fill(white)
    for i in range(0,board):
        for i2 in range(0,board):
            if (i+i2)%2==0:
                pygame.draw.rect(screen,brown,(int(i*squareSize),int(i2*squareSize),squareSize,squareSize))


def write(text,wait,size,screen):
    screen.fill((255,255,255),(0,size[0],size[0],(size[1]-size[0])))
    screen.blit(pygame.font.SysFont('Arial', int(size[0]/15)).render(text, False, (0, 0, 255)),(0,size[0]))
    pygame.display.update()
    pygame.time.wait(wait)

def startGame(screen,board=board,size=size):
    drawBoard(size,board,screen)
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

def selectPiece(target,size,screen,board): 
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

def movePiece(selectedPiece,target,size,screen,board,plist):
    done=False
    squareSize=int(size[0]/board)
    brown=(185,122,87)
    white=(255,255,255)
    oldLoc=selectedPiece.getLocation()
    if (oldLoc[0]+oldLoc[1])%2==0:
        color=brown
    else:
        color=white
    if target in selectedPiece.validMoves(plist,board):
        pygame.draw.rect(screen,color,(int(oldLoc[0]*squareSize),int(oldLoc[1]*squareSize),squareSize,squareSize))
        selectedPiece.setLocation(target)
        selectedPiece.draw(screen,size,board)
        pygame.display.update()
        done=True
    return done

def isGameOver(plist,size,board,screen,winner="no one"):
    isOver=False
    if winner!="no one":
        isOver=True
    for i in plist:
        if i.getController()=="player" and i.getLocation()[1]==0:
            winner="player"
            isOver=True
        elif i.getController()=="CPU" and i.getLocation()[1]==board-1:
            winner="CPU"
            isOver=True
    return isOver,winner

def checkImmobilization(plist,size,board,screen,turn,roundMoves,badMoves):
    GameOver=False
    winner="no one"
    noMoves=False
    validChoice=False
    availablePieces=[]
    chosenMove=0
    chosenPiece=0
    didItBefore=roundMoves.copy()
    if turn=="CPU":
        opponent="player"
    elif turn=="player":
        opponent="CPU"
    for i in plist:
            if i.getController()==turn:
                availablePieces.append(i)
    while validChoice==False and noMoves==False:
        if len(availablePieces)>0:
            chosenPiece=randint(0,len(availablePieces)-1)
            if len(availablePieces[chosenPiece].validMoves(plist,board))>=1:
                chosenMove=randint(0,len(availablePieces[chosenPiece].validMoves(plist,board))-1)
                validChoice=True
                didItBefore.append(availablePieces[chosenPiece].validMoves(plist,board)[chosenMove])
                for i in badMoves:    
                    if didItBefore==i:
                        validChoice=False
                        didItBefore.remove(didItBefore[-1])

            else:
                availablePieces.remove(availablePieces[chosenPiece])
        else:
            noMoves=True
            GameOver,winner=isGameOver(plist,size,board,screen,opponent)
    return noMoves,chosenMove,chosenPiece,availablePieces,GameOver,winner