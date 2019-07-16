# import the pygame module, so you can use it
import pygame

#Change game directory and size accordingly
#direc = r"C:\Users\filip\Documents\python codes\hexapawn\local"     #desktop location
direc = r"C:\Users\Filippe\Documents\GitHub\hexapawn"              #notebook location
#size=(720,770,120,360,600,120,725,720,100,60,35)                   #default size
size=[360,385,60,180,300,60,365,360,50,30,17]                       #mini size

#Using "screen" here take some boot time for the game, but makes the code shorter

screen = pygame.display.set_mode((size[0],size[1]))
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
    
    def getPiece(self):
        return self.piece[0]
    
    def addPiece(self,piece):
        self.piece.append(piece)
        self.occupied=True

    
    def removePiece(self,piece):
        self.piece.remove(piece)
        self.occupied=False

    def zoneColor(self):
        if (self.loc[0]+self.loc[1])%2 == 0:
            return (185,122,87)
        else:
            return (250,250,250)


class Piece:
    def __init__(self,zone,sqr,color):
        self.zone=zone[sqr]
        self.sqr=sqr
        self.color=color
        self.selected=False

    def draw(self,screen=screen,size=size):
        pygame.draw.circle(screen, self.color, self.zone.center, size[9])
    
    def changeColor(self,color):
        self.color=color
    
    def isPlayer(self):
        if self.color==(0,0,0):
            return False
        else:
            return True
    
    def getZone(self):
        return self.zone

    def changePlace(self,zone,newZone):
        self.zone=newZone
        zone.removePiece(self)
        newZone.addPiece(self)

        

def write(text,wait,size=size,screen=screen):
    screen.fill((255,255,255),(0,size[6],size[7],size[8]))
    screen.blit(pygame.font.SysFont('Arial', size[10]).render(text, False, (0, 0, 255)),(0,size[6]))
    pygame.display.update()
    pygame.time.wait(wait)
    
def getZone(sqSize, where,listloc,z):
    xZone=int(where[0]/sqSize/2)
    yZone=int(where[1]/sqSize/2)
    return z[listloc.index((xZone,yZone))]

def selectPiece(z,piece,screen=screen):
    piece.changeColor((255,255,0))
    piece.draw(screen)
    return 0
    
def place(piece,zoneList,screen=screen):
    zoneList[piece.sqr].addPiece(piece)
    piece.draw(screen)    



def movePiece(Piece,listloc,click,z,sqSize,screen=screen):
    zone=getZone(sqSize,click,listloc,z)
    validMove=[]
    if Piece.isPlayer()==False:
        validMove.append((Piece.zone.loc[0],Piece.zone.loc[1]+1))
        validMove.append((Piece.zone.loc[0]+1,Piece.zone.loc[1]+1))
        validMove.append((Piece.zone.loc[0]-1,Piece.zone.loc[1]+1))
    else:
        validMove.append((Piece.zone.loc[0],Piece.zone.loc[1]-1))
        validMove.append((Piece.zone.loc[0]+1,Piece.zone.loc[1]-1))
        validMove.append((Piece.zone.loc[0]-1,Piece.zone.loc[1]-1))
    if (zone.loc==validMove[1] or zone.loc==validMove[2]) and zone.hasPiece():
        zone.removePiece(zone.getPiece())
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
    elif (zone.loc==validMove[0]) and zone.hasPiece()==False:
        #Piece.zone.removePiece(Piece)
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

def checkVictory(z):
    for i in z:
        if i.loc[1]==0 and i.hasPiece() and i.getPiece().isPlayer():
            write("victory :D Congratulations!!!",3000)
            initiate(z)
        elif i.loc[1]==2 and i.hasPiece() and i.getPiece().isPlayer()==False:
            write("Defeat :( Better luck next time!",3000)
            initiate(z)

def initiate(z,black=(0,0,0),blue=(0,0,250),yellow=(250,250,0)):
    for i in z:
        if i.hasPiece():
            i.removePiece(i.getPiece())
        else:
            pass

    pc0=Piece(z,0,black)
    pc1=Piece(z,1,black)
    pc2=Piece(z,2,black)
    pl0=Piece(z,6,blue)
    pl1=Piece(z,7,blue)
    pl2=Piece(z,8,blue)
    
    place(pc0,z)
    place(pc1,z)
    place(pc2,z)
    place(pl0,z)
    place(pl1,z)
    place(pl2,z)
    write("Choose the piece you want to move",0)
    return z

# define a main function
def main():
     
    # initialize the pygame module
    pygame.init()
    # load and set the logo
    logo = pygame.image.load(direc+"\\pawn.png")
    pygame.display.set_icon(logo)
    pygame.display.set_caption("HexaPawn")
     
    # create a surface on screen that has the size of board
    
    
    screen.fill((255,255,255))
    image = pygame.image.load(direc+"\\tiles.png")
    image=pygame.transform.scale(image,(size[0],size[1]))
    #image.convert()
    pos=[size[2],size[3],size[4]]
    sqSize=size[5]
    
    screen.blit(image,(0,0))
    listloc=[(0,0),(1,0),(2,0),(0,1),(1,1),(2,1),(0,2),(1,2),(2,2)]
    
    
    
    # Text at the bottom
    pygame.font.init()
    #create tiles objects
    z=[]
    for x in range (0,9):   
        z.append(Zone(listloc[x],sqSize))
    
    initiate(z)
    
    
     
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
                    if getZone(sqSize,click,listloc,z).hasPiece():
                        zone=getZone(sqSize,click,listloc,z)
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
                    moved=movePiece(selectedPiece,listloc,click,z,sqSize)
                    if moved==True:                        
                        write("wait for your turn",0)
                        selectedPiece=[]
                        checkVictory(z)
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