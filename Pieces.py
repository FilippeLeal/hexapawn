import pygame
class Pieces:
    def __init__(self,location,controlled,type="pawn"):
        self.location=location
        self.controlled=controlled
        self.type=type
        if controlled=="player":
            self.color=(0,0,255)
            self.front=-1
        else:
            self.color=(0,0,0)
            self.front=1

    def getLocation(self):
        return self.location

    def setLocation(self,newloc):
        self.location=newloc
        if self.controlled=="player":
            self.color=(0,0,255)
        else:
            self.color=(0,0,0)
    
    def validMoves(self,plist,board):
        #it gets a list of all pieces, and examinate the possible piece move with the vacancy of the square
        valid=[]
        loc=self.location
        listloc=[]
        listcontroller=[]
        for i in plist:
            listloc.append(i.location)
            listcontroller.append(i.controlled)
        if loc[1]+self.front in range(0,board): 
            if (loc[0],loc[1]+self.front) not in listloc:
                valid.append((loc[0],loc[1]+self.front))
            if loc[0]+1 in range(0,board) and (loc[0]+1,loc[1]+self.front) in listloc and plist[listloc.index((loc[0]+1,loc[1]+self.front))].controlled!=self.controlled:
                valid.append((loc[0]+1,loc[1]+self.front))
            if loc[0]-1 in range(0,board) and (loc[0]-1,loc[1]+self.front) in listloc and  plist[listloc.index((loc[0]-1,loc[1]+self.front))].controlled!=self.controlled :
                valid.append((loc[0]-1,loc[1]+self.front))
        return valid
     
    def getColor(self):
        return self.color

    def setColor(self,newColor):
        self.color=newColor
    
    def getController(self):
        return self.controlled

    def draw(self,screen,size,board,update=False):
        #not only draws the piece, but the square behind it too
        squareSize=int(size[0]/board)
        sqcolor=(255,255,0)
        corner=( int(self.location[0]*size[0]/board ), int(self.location[1]*size[0]/board ))
        bpawn = pygame.image.load('bpawn.png')
        bpawn2 = pygame.transform.scale(bpawn, (int(size[0]/board),int(size[0]/board)))
        wpawn = pygame.image.load('pawn.png')
        wpawn2 = pygame.transform.scale(wpawn, (int(size[0]/board),int(size[0]/board)))
        if self.color==(255,255,0):
            pygame.draw.rect(screen,self.color,(int(self.location[0]*squareSize),int(self.location[1]*squareSize),squareSize,squareSize))
        else:
            if (self.location[0]+self.location[1])%2==0:
                sqcolor=(185,122,87)
            else:
                sqcolor=(255,255,255)
        pygame.draw.rect(screen,sqcolor,(int(self.location[0]*squareSize),int(self.location[1]*squareSize),squareSize,squareSize))
        if self.controlled=="CPU":
            screen.blit(bpawn2, corner)
        elif self.controlled=="player":
            screen.blit(wpawn2, corner)
        if update==True:
            pygame.display.update()