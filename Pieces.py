import pygame
class Pieces:
    def __init__(self,location,controled,type="pawn"):
        self.location=location
        self.controled=controled
        self.type=type
        if controled=="player":
            self.color=(0,0,255)
            self.front=1
        else:
            self.color=(0,0,0)
            self.front=-1

    def getLocation(self):
        return self.location
    
    def validMoves(self,plist,board):
        valid=[( self.location[0],(self.location[1]+self.front) ), ( (self.location[0]-1) , (self.location[1]+self.front) ), ( (self.location[0]+1), (self.location[1]+self.front) )]
        for i in valid:
            if i[0] not in range(0,board) or i[1] not in range(0,board):
                valid.remove(i)
            else:
                for i2 in plist:
                    if i2.getLocation()==i:
                        if i==0:
                            valid.remove(i)
                        elif i==1:
                            valid1=True
                        elif i==2:
                            valid2=True
                if valid1=False:
                    valid.remove(1)
                            
                    

                


    def getColor(self):
        return self.color

    def setColor(self,newColor):
        self.color=newColor

    def getController(self):
        return self.controled

    def draw(self,screen,size,board):
        center=( int(self.location[0]*size[0]/board+size[0]/2/board),int(self.location[1]*size[0]/board+size[0]/2/board) )
        pygame.draw.circle(screen, self.color, center, int(size[0]/board/4))
        