# import the pygame module, so you can use it
import pygame
direc = r"C:\Users\Filippe\Documents\GitHub\hexapawn" 

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
        return self.piece
    
    def addPiece(self,piece):
        self.piece.append(piece)
        self.occupied=True
        return self.piece


class Piece:
    def __init__(self,zone,sqr,color):
        self.zone=zone[sqr]
        self.sqr=sqr
        self.color=color
        self.selected=False

    def draw(self,screen):
        pygame.draw.circle(screen, self.color, self.zone.center, 60)
    
    def changeColor(self,color):
        self.color=color
    
    def isPlayer(self):
        if self.color==(0,0,0):
            return False
        else:
            return True

        

def write(text,screen,wait):
    screen.fill((255,255,255),(0,725,720,100))
    screen.blit(pygame.font.SysFont('Arial', 35).render(text, False, (0, 0, 255)),(0,725))
    pygame.display.update()
    pygame.time.wait(wait)
    
def getZone(sqSize, where,listloc,z):
    xZone=int(where[0]/sqSize/2)
    yZone=int(where[1]/sqSize/2)
    return z[listloc.index((xZone,yZone))]

def selectPiece(z,piece,screen):
    piece.changeColor((255,255,0))
    piece.draw(screen)
    return 0
    
def place(piece,zoneList,screen):
    zoneList[piece.sqr].addPiece(piece)
    piece.draw(screen)    



def movePiece(Piece,zoneList,screen):
    if pygame.mouse.get_pressed()[0]==1:
        click=pygame.mouse.get_pos()
        zone=getZone(sqSize,click,listloc,z)
        if zone.pos==Piece.zone.pos+(1,-1) or zone.pos==Piece.zone.pos+(-1,-1):
            write("deu bom",screen,2)
        else:
            write('quase bom',screen,2)
    



# define a main function
def main():
     
    # initialize the pygame module
    pygame.init()
    # load and set the logo
    logo = pygame.image.load(direc+"\\pawn.png")
    pygame.display.set_icon(logo)
    pygame.display.set_caption("HexaPawn")
     
    # create a surface on screen that has the size of board
    screen = pygame.display.set_mode((720,770))
    screen.fill((255,255,255))
    image = pygame.image.load(direc+"\\tiles.png")
    image.convert()
    pos=[(120),(360),(600)]
    sqSize=120
    black=(0,0,0)
    blue=(0,0,250)
    yellow=(250,250,0)
    screen.blit(image,(0,0))
    listloc=[(0,0),(1,0),(2,0),(0,1),(1,1),(2,1),(0,2),(1,2),(2,2)]
    write("Choose the piece you want to move",screen,0)
    
    
    #create tiles objects
    z=[]
    for x in range (0,9):   
        z.append(Zone(listloc[x],sqSize))
    

    # Text at the bottom
    pygame.font.init()
    

    pc0=Piece(z,0,black)
    pc1=Piece(z,1,black)
    pc2=Piece(z,2,black)
    pl0=Piece(z,6,blue)
    pl1=Piece(z,7,blue)
    pl2=Piece(z,8,blue)
    
    place(pc0,z,screen)
    place(pc1,z,screen)
    place(pc2,z,screen)
    place(pl0,z,screen)
    place(pl1,z,screen)
    place(pl2,z,screen)
    
     
    # define a variable to control the main loop
    running = True
     
    # main loop
    while running:
        # event handling, gets all event from the event queue
        for event in pygame.event.get():
            if pygame.mouse.get_pressed()[0]==1:
                click=pygame.mouse.get_pos()
                if getZone(sqSize,click,listloc,z).hasPiece():
                    zone=getZone(sqSize,click,listloc,z)
                    if zone.getPiece()[0].isPlayer():
                        selectPiece(zone,zone.getPiece()[0],screen)
                        write("choose where you want to move the selected piece",screen,0)
                        click=pygame.mouse.get_pos()
                    else:
                        write("That's not your piece! Your's are BLUE!",screen,1500) 
                        write("choose the piece you want to move",screen,0) 
                        #movePiece()
                else:
                    write("There's no piece at this location!!!",screen,1500) 
                    write("choose the piece you want to move",screen,0)    
                    
                    
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