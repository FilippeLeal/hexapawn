
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
    roundMoves=[]
    badMoves=[]
    #the main Loop
    while running==True:
        plist=startGame(screen)  ##start a game from turn 1
        GameOver=False
        turn="player"
        scoreBoard.append(winner)
        if winner=="player":
            roundMoves.remove(roundMoves[-1])
            badMoves.append(roundMoves)

        print(scoreBoard)
        roundMoves=[]
        while GameOver==False:  ##so the game will only restart if the previous is finished
            if turn=="player":
                noMoves,chosenMove,chosenPiece,availablePieces,GameOver,winner=checkImmobilization(plist,size,board,screen,turn,roundMoves,badMoves)
                for event in pygame.event.get():
                    if pygame.mouse.get_pressed()[0]==1:
                        click=pygame.mouse.get_pos()
                        target=getTileLocation(click,plist) 
                        #target returns as the location if the tile is empty or the Piece obj occupying it
                        if selectedPiece!=[]:
                            if type(target)!=tuple:#therefore, if the taget is not a location, it is a piece obj
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
                                roundMoves.append(target)
                                turn="CPU"  
                                selectedPiece=[]
                                if hadPiece!=[]:
                                    plist.remove(hadPiece[0])
                                    hadPiece=[]
                        elif selectedPiece==[]:
                            selectedPiece=selectPiece(target,size,screen,board)
                            write("Select the location that you want to move the piece!",0,size,screen)
                    GameOver,winner=isGameOver(plist,size,board,screen)        
            elif turn=="CPU":
                noMoves,chosenMove,chosenPiece,availablePieces,GameOver,winner=checkImmobilization(plist,size,board,screen,turn,roundMoves,badMoves)

                if noMoves==False:
                    target=availablePieces[chosenPiece].validMoves(plist,board)[chosenMove]
                    done=movePiece(availablePieces[chosenPiece],target,size,screen,board,plist)
                    roundMoves.append(target)
                    print(roundMoves)
                    for i in plist:
                        if i.getLocation()==target and i.getController()=="player":
                            plist.remove(i)
                    GameOver,winner=isGameOver(plist,size,board,screen) 
                
                        
                turn="player"
                            

                            
            if event.type == pygame.QUIT:
                # change the value to False, to exit the main loop
                print(badMoves)
                running = False
                GameOver= True
        


if __name__=="__main__":
    # call the main function
    main()