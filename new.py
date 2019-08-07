
from GameFunctions import *
from Pieces import *


# define a main function 
def main():
    # load and set the window and board
    screen=makeBoard(size,board)
    pygame.font.init()

    # variables to control the main loop
    running = True
    GameOver=False
    winner="Game Start!"
    turn = "player"
    scoreBoard=[]
    selectedPiece=[]
    hadPiece=[]
    #the main Loop
    while running==True:
        plist=startGame(screen)  ##start a game from turn 1
        GameOver=False
        scoreBoard.append(winner)
        print(scoreBoard)
        while GameOver==False:  ##so the game will only restart if the previous is finished
            for event in pygame.event.get():
                if turn=="player":
                    if pygame.mouse.get_pressed()[0]==1:
                        click=pygame.mouse.get_pos()
                        target=getTileLocation(click,plist) 
                        #target returns as the location if the tile is empty or the Piece obj occupying it
                        if selectedPiece!=[]:
                            if type(target)!=tuple:
                                hadPiece.append(target)
                                target=target.getLocation()     

                            done=movePiece(selectedPiece,target,size,screen,board,plist)
                            if done==False:
                                write("Invalid move!",1000,size,screen)
                                write("Select the piece you want to move!",0,size,screen)
                                selectedPiece.setLocation(selectedPiece.getLocation())
                                selectedPiece.draw(screen,size,board,update=True)
                                selectedPiece=[]
                                hadPiece=[]

                            else:
                                selectedPiece=[]
                                if hadPiece!=[]:
                                    plist.remove(hadPiece[0])
                                    hadPiece=[]
                                    print("piece number=",len(plist))
                        elif selectedPiece==[]:
                            selectedPiece=selectPiece(target,size,screen,board)
                            write("Select the location that you want to move the piece!",0,size,screen)
                    GameOver,winner=isGameOver(plist,size,board)        
                                
                            

                            
                if event.type == pygame.QUIT:
                    # change the value to False, to exit the main loop
                    running = False
                    GameOver= True
        


if __name__=="__main__":
    # call the main function
    main()