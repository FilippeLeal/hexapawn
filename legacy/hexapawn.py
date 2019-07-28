# import the pygame module, so you can use it
import pygame
import random
#Change game directory and size accordingly
#direc = r"C:\Users\filip\Documents\python codes\hexapawn\local"     #desktop location
direc = r"C:\Users\Filippe\Documents\GitHub\hexapawn"              #notebook location
#size=(720,770,240,480,120,720,720,100,60,35)                   #default size
size=[360,385,120,240,60,360,360,50,30,17]                       #mini size
board=3
sqSize=size[4]
#Using "screen" here take some boot time for the game, but makes the code shorter
screen = pygame.display.set_mode((size[0],size[1]))
p=[]
movesHistory=[]
defeatHistory=[]
### Implementar métodos gerais usando métodos de cada classe separadamente para as ações

class Zone:
    def __init__(self,loc,sqSize):
        self.loc=loc
        self.occupied=False
        self.sqSize=sqSize
        self.center=((1+loc[0])*2*sqSize-sqSize,(1+loc[1])*2*sqSize-sqSize)
        self.piece=[]
    
    def hasPiece(self):
        return self.occupied
    
    def getLoc(self):
        return self.loc

    def getPiece(self):
        return self.piece[0] 
    
    def addPiece(self,piece):
        self.piece.append(piece)
        self.occupied=True

    
    def removePiece(self,piece):
        self.piece.clear()
        self.occupied=False

    def zoneColor(self):
        if (self.loc[0]+self.loc[1])%2 == 0:
            return (185,122,87)
        else:
            return (255,255,255)


class Piece:
    def __init__(self,zone,sqr,color,controled):
        self.zone=zone[sqr]
        self.sqr=sqr
        self.color=color
        self.selected=False
        self.player=controled

    def draw(self,screen=screen,size=size):
        pygame.draw.circle(screen, self.color, self.zone.center, size[8])
    
    def changeColor(self,color):
        self.color=color
    
    def isPlayer(self):
        return self.player
    
    def getZone(self):
        return self.zone

    def changePlace(self,zone,newZone):
        self.zone=newZone
        zone.removePiece(self)
        newZone.addPiece(self)

    def validMoves(self,zone,board=board):
        valid=[]
        loc=self.getZone().getLoc()
        direction=0
        if self.isPlayer()==False:
            direction=1
        elif self.isPlayer()==True:
            direction=-1
        x=loc[0]
        y=loc[1]+direction
        type(zone)
        if y<board and y>=0 and zone[x+y*board].hasPiece()==False:
            valid.append((x,y))
        x=loc[0]+1
        y=loc[1]+direction
        if x<board and y<board and y>=0 and zone[x+y*board].hasPiece()==True:
            if zone[x+y*board].getPiece().isPlayer()!=self.isPlayer():
                valid.append((x,y))
        x=loc[0]-1
        y=loc[1]+direction
        if x>=0 and y<board and y>=0 and zone[x+y*board].hasPiece()==True:
            if zone[x+y*board].getPiece().isPlayer()!=self.isPlayer():
                valid.append((x,y))
        return valid

def drawBoard():
    screen.fill((255,255,255))
    pygame.draw.rect(screen,(185,122,87),(0,0,120,120))
    pygame.draw.rect(screen,(185,122,87),(240,0,120,120))
    pygame.draw.rect(screen,(185,122,87),(120,120,120,120))
    pygame.draw.rect(screen,(185,122,87),(0,240,120,120))
    pygame.draw.rect(screen,(185,122,87),(240,240,120,120))
    
def write(text,wait,size=size,screen=screen):
    screen.fill((250,250,0),(0,size[5],size[6],size[7]))
    screen.blit(pygame.font.SysFont('Arial', size[9]).render(text, False, (0, 0, 255)),(0,size[5]))
    pygame.display.update()
    #pygame.time.wait(wait)
    
def getZone(sqSize, where,z):
    xZone=int(where[0]/sqSize/2)
    yZone=int(where[1]/sqSize/2)
    index=xZone+yZone*board
    return z[index]

def selectPiece(z,piece,screen=screen):
    piece.changeColor((255,255,0))
    piece.draw(screen)
    return 0
    
def place(piece,zoneList,screen=screen):
    zoneList[piece.sqr].addPiece(piece)
    piece.draw(screen)    

def movePiece(Piece,zone,zlist,sqSize,p,movesHistory=movesHistory,screen=screen):
    #zone=getZone(sqSize,click,z)
    validMove=Piece.validMoves(zlist)
    if zone.loc in validMove:
        movesHistory.append(zone.loc)
        print("moves",movesHistory)
        if zone.hasPiece()==True:
            erase=zone.getPiece()
            p.remove(erase)
            zone.removePiece(erase)
            
            Piece.changeColor(Piece.getZone().zoneColor())
            Piece.draw()
            Piece.changePlace(Piece.zone,zone)
            if Piece.isPlayer():
                Piece.changeColor((0,0,250))
            else:
                Piece.changeColor((0,0,0))
            Piece.draw()
            moved=True
            write("Moved!",1000)
        else:
            Piece.changeColor(Piece.getZone().zoneColor())
            Piece.draw()
            Piece.changePlace(Piece.zone,zone)
            if Piece.isPlayer():
                Piece.changeColor((0,0,250))
            else:
                Piece.changeColor((0,0,0))
            Piece.draw()
            moved=True
            write("Moved!",1000)
    else:
        moved=False
        write("Invalid Move!",2000)
    return moved,movesHistory

def checkVictory(z,p,winner="no one",defeatHistory=defeatHistory,movesHistory=movesHistory):
    gameOver=False
    for i in z:
        if i.loc[1]==0 and i.hasPiece() and i.getPiece().isPlayer():
            winner="player"
        elif i.loc[1]==2 and i.hasPiece() and i.getPiece().isPlayer()==False:
            winner="CPU"
    if winner!="no one":
        gameOver=True
        if winner=="player":
            write("victory!!! Congratulations!!!  :D",3000)
            defeatHistory.append(movesHistory)
            print(defeatHistory)
            print(len(defeatHistory))
        elif winner=="CPU":
            write("Defeat!!! Better luck next time!  :(",3000)
        z,p,movesHistory=initiate(z)
        print("moves history:",movesHistory)
    return gameOver,defeatHistory,movesHistory

def initiate(z,p=p,black=(0,0,0),blue=(0,0,250),yellow=(250,250,0)):
    drawBoard()
    movesHistory=[]
    print("initiate",movesHistory)
    for i in z:
        if i.hasPiece():
            i.removePiece(i.getPiece())
    
    p.clear()
    p.append(Piece(z,0,black,False))
    p.append(Piece(z,1,black,False))
    p.append(Piece(z,2,black,False))
    p.append(Piece(z,6,blue,True))
    p.append(Piece(z,7,blue,True))
    p.append(Piece(z,8,blue,True))
    for i in p:
        place(i,z)
    
    write("Choose the piece you want to move",0)
    return z,p,movesHistory

def PcTurn(p,zlist,movesHistory=movesHistory,defeatHistory=defeatHistory,sqsize=sqSize,screen=screen,board=board):
    pcPieces=[]
    pcMoves=[]
    noMoves=True
    valid=False
    dejavu=True
  
    for i in p:
        if i.isPlayer()==False:
            pcPieces.append(i)
    for i2 in pcPieces:
        pcMoves.append(i2.validMoves(zlist))
    while dejavu==True:
        testmove=movesHistory.copy()
        for i3 in pcMoves:
            if pcMoves[pcMoves.index(i3)]!=[]:
                noMoves=False
        if noMoves==True:
            print("victory by immobilization")
            gameOver,defeatHistory,movesHistory=checkVictory(zlist,p,"player")
            dejavu=False
        else:
            while valid==False:
                a=random.randrange(len(pcMoves))
                if pcMoves[a]!=[]:
                    valid=True
            b=random.randrange(len(pcMoves[a]))
            testmove.append(pcMoves[a][b])
            if defeatHistory in testmove:
                print("dejavu")
                dejavu=True
                pcMoves[a].remove(b)
            else:
                dejavu=False
                print("pc target=",pcMoves[a][b])
            print(pcMoves)
            targetZone=zlist[pcMoves[a][b][0]+pcMoves[a][b][1]*board]
            moved,movesHistory=movePiece(pcPieces[a],targetZone,zlist,sqSize,p)
    return zlist,p,movesHistory,defeatHistory

def checkNoMoves(zlist,plist):
    noMoves=True
    playerPieces=[]
    playerMoves=[]
    for i in p:
        if i.isPlayer()==True:
            playerPieces.append(i)
    for i2 in playerPieces:
        playerMoves.append(i2.validMoves(zlist))
    for i3 in playerMoves:
        if playerMoves[playerMoves.index(i3)]!=[]:
            noMoves=False
    return noMoves

# define a main function
def main():
     
    # initialize the pygame module
    pygame.init()
    # load and set the logo
    logo = pygame.image.load(direc+"\\pawn.png")
    pygame.display.set_icon(logo)
    pygame.display.set_caption("HexaPawn")
     
    # create a surface on screen that has the size of board
    
        
    
    
    # Text at the bottom
    pygame.font.init()
    #create tiles objects
    z=[]
    for x in range (0,9):   
        z.append(Zone((x%board,int(x/board)),sqSize))
    
    z,p,movesHistory=initiate(z)
    
    clock=pygame.time.Clock()
    
     
    # define a variable to control the main loop
    running = True
    selectedPiece=[] 
    # main loop
    while running: 
        # event handling, gets all event from the event queue
        for event in pygame.event.get():
            if pygame.mouse.get_pressed()[0]==1:
                click=pygame.mouse.get_pos()
                if selectedPiece==[]:
                    if getZone(sqSize,click,z).hasPiece():
                        zone=getZone(sqSize,click,z)
                        if zone.getPiece().isPlayer():
                            selectPiece(zone,zone.getPiece())
                            selectedPiece=zone.getPiece()
                            write("choose where you want to move the selected piece",0)
                        else:
                            write("That's not your piece! Your's are BLUE!",1500) 
                            write("choose the piece you want to move",0) 
                    else:
                        write("There's no piece at this location!!!",1500) 
                        write("choose the piece you want to move",0)    
                else:
                    print("MOVE",movesHistory)
                    moved,movesHistory=movePiece(selectedPiece,getZone(sqSize,click,z),z,sqSize,p)
                    if moved==True:                        
                        write("wait for your turn",0)
                        selectedPiece=[]
                        gameOver,defeatHistory,movesHistory=checkVictory(z,p)
                        print("aiai",movesHistory)
                        if gameOver==False:
                            clock.tick()
                            z,p,movesHistory,defeatHistory=PcTurn(p,z)
                            clock.tick()
                            print("pcturntime:",clock.get_time())
                            gameOver,defeatHistory,movesHistory=checkVictory(z,p)
                            noMoves=checkNoMoves(z,p)
                            if noMoves==True:
                                print("defeat by immobilization")
                                gameOver,defeatHistory,movesHistory=checkVictory(z,p,"CPU")
                    else:
                        write("choose where you want to move the selected piece",0)
                        

            
                    
            # only do something if the event is of type QUIT
            if event.type == pygame.QUIT:
                # change the value to False, to exit the main loop
                running = False
        
        
        pygame.display.update()
     
     
# run the main function only if this module is executed as the main script
# (if you import this as a module then nothing is executed)
if __name__=="__main__":
    # call the main function
    main()