# import the pygame module, so you can use it
import pygame

#Change game directory and size accordingly
#direc = r"C:\Users\filip\Documents\python codes\hexapawn\local"     #desktop location
direc = r"C:\Users\Filippe\Documents\GitHub\hexapawn"              #notebook location
#size=(720,770,240,480,120,720,720,100,60,35)                   #default size
size=[360,385,120,240,60,360,360,50,30,17]                       #mini size
board=3
#Using "screen" here take some boot time for the game, but makes the code shorter

screen = pygame.display.set_mode((size[0],size[1]))
p=[]
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
        if x<board and y<=board and y>=0 and zone[x+y*board].hasPiece()==True:
            if zone[x+y*board].getPiece().isPlayer()!=self.isPlayer():
                valid.append((x,y))
        x=loc[0]-1
        y=loc[1]+direction
        if x>=0 and y<board and y>=0 and zone[x+y*board].hasPiece()==True:
            if zone[x+y*board].getPiece().isPlayer()!=self.isPlayer():
                valid.append((x,y))
        return valid

def drawBoard():
    screen.fill((250,250,250))
    pygame.draw.rect(screen,(185,122,87),(0,0,120,120))
    pygame.draw.rect(screen,(185,122,87),(240,0,120,120))
    pygame.draw.rect(screen,(185,122,87),(120,120,120,120))
    pygame.draw.rect(screen,(185,122,87),(0,240,120,120))
    pygame.draw.rect(screen,(185,122,87),(240,240,120,120))
    
def write(text,wait,size=size,screen=screen):
    screen.fill((250,250,0),(0,size[5],size[6],size[7]))
    screen.blit(pygame.font.SysFont('Arial', size[9]).render(text, False, (0, 0, 255)),(0,size[5]))
    pygame.display.update()
    pygame.time.wait(wait)
    
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

def movePiece(Piece,zone,zlist,sqSize,p,screen=screen):
    #zone=getZone(sqSize,click,z)
    validMove=Piece.validMoves(zlist)
    if zone.loc in validMove:
        if zone.hasPiece()==True:
            erase=zone.getPiece()
            zone.removePiece(erase)
            p.remove(erase)
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
    return moved

def checkVictory(z,p):
    for i in z:
        if i.loc[1]==0 and i.hasPiece() and i.getPiece().isPlayer():
            write("victory!!! Congratulations!!!  :D",3000)
            z,p=initiate(z)
        elif i.loc[1]==2 and i.hasPiece() and i.getPiece().isPlayer()==False:
            write("Defeat!!! Better luck next time!  :(",3000)
            z,p=initiate(z)
    return z,p

def initiate(z,black=(0,0,0),blue=(0,0,250),yellow=(250,250,0)):
    drawBoard()
    for i in z:
        if i.hasPiece():
            i.removePiece(i.getPiece())
        else:
            pass
    p=[]
    p.append(Piece(z,0,black,False))
    p.append(Piece(z,1,black,False))
    p.append(Piece(z,2,black,False))
    p.append(Piece(z,6,blue,True))
    p.append(Piece(z,7,blue,True))
    p.append(Piece(z,8,blue,True))
    
    for i in p:
        place(i,z)
    
    write("Choose the piece you want to move",0)
    return z,p

def PcTurn(p,z):
    pcPieces=[]
    pcMoves=[]
    for i in p:
        if i.isPlayer()==False:
            pcPieces.append(i)
    for i2 in pcPieces:
        pcMoves[pcPieces.index(i2)].append(i2.validMoves(z))
    print(len(pcMoves))
    print(pcMoves)

# define a main function
def main():
     
    # initialize the pygame module
    #pygame.init()
    # load and set the logo
    logo = pygame.image.load(direc+"\\pawn.png")
    pygame.display.set_icon(logo)
    pygame.display.set_caption("HexaPawn")
     
    # create a surface on screen that has the size of board
    
        
    sqSize=size[4]
    
    # Text at the bottom
    pygame.font.init()
    #create tiles objects
    z=[]
    for x in range (0,9):   
        z.append(Zone((x%board,int(x/board)),sqSize))
    
    z,p=initiate(z)
    
    
    
     
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
                            print("valid=",selectedPiece.validMoves(z))
                            write("choose where you want to move the selected piece",0)
                        else:
                            write("That's not your piece! Your's are BLUE!",1500) 
                            write("choose the piece you want to move",0) 
                    else:
                        write("There's no piece at this location!!!",1500) 
                        write("choose the piece you want to move",0)    
                else:
                    moved=movePiece(selectedPiece,getZone(sqSize,click,z),z,sqSize,p)
                    if moved==True:                        
                        write("wait for your turn",0)
                        selectedPiece=[]
                        z,p=checkVictory(z,p)
                        PcTurn(p,z)
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