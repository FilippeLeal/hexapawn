import pygame
class Pieces:
    def __init__(self,location,controled,type="pawn"):
        self.location=location
        self.controled=controled
        self.type=type
        if controled=="player":
            self.color=(0,0,255)
            self.front=-1
        else:
            self.color=(0,0,0)
            self.front=1

    def getLocation(self):
        return self.location

    def setLocation(self,newloc):
        self.location=newloc
        if self.controled=="player":
            self.color=(0,0,255)
        else:
            self.color=(0,0,0)
    
    def validMoves(self,plist,board):
        valid=[]
        loc=self.location
        listloc=[]
        for i in plist:
            listloc.append(i.location)
        if loc[1]+self.front in range(0,board): 
            if (loc[0],loc[1]+self.front) not in listloc:
                valid.append((loc[0],loc[1]+self.front))
            if loc[0]+1 in range(0,board) and (loc[0]+1,loc[1]+self.front) in listloc:
                valid.append((loc[0]+1,loc[1]+self.front))
            if loc[0]-1 in range(0,board) and (loc[0]-1,loc[1]+self.front) in listloc:
                valid.append((loc[0]-1,loc[1]+self.front))
        return valid
                            
                    

                


    def getColor(self):
        return self.color

    def setColor(self,newColor):
        self.color=newColor
    
    def getController(self):
        return self.controled

    def draw(self,screen,size,board,update=False):
        center=( int(self.location[0]*size[0]/board+size[0]/2/board),int(self.location[1]*size[0]/board+size[0]/2/board) )
        pygame.draw.circle(screen, self.color, center, int(size[0]/board/4))
        if update==True:
            pygame.display.update()