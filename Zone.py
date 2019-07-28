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

