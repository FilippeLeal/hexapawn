
from GameFunctions import *
from Pieces import *
from random import randint

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
        turn="player"
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
                                turn="CPU"  
                                selectedPiece=[]
                                if hadPiece!=[]:
                                    plist.remove(hadPiece[0])
                                    hadPiece=[]
                                    print("piece number=",len(plist))
                        elif selectedPiece==[]:
                            selectedPiece=selectPiece(target,size,screen,board)
                            write("Select the location that you want to move the piece!",0,size,screen)
                    GameOver,winner=isGameOver(plist,size,board)        
                elif turn=="CPU":
                    noMoves=False
                    validChoice=False
                    cpulist=[]
                    for i in plist:
                            if i.getController()=="CPU":
                                cpulist.append(i)
                    while validChoice==False and noMoves==False:
                        if len(cpulist)>0:
                            chosenPiece=randint(0,len(cpulist)-1)
                            print("cpu piece id",chosenPiece)
                            if len(cpulist[chosenPiece].validMoves(plist,board))>=1:
                                chosenMove=randint(0,len(cpulist[chosenPiece].validMoves(plist,board))-1)
                                print("chosen=",cpulist[chosenPiece].validMoves(plist,board))
                                validChoice=True
                            else:
                                print("check1")
                                cpulist.remove(cpulist[chosenPiece])
                        else:
                            print("check2")
                            noMoves=True
                            GameOver,winner=isGameOver(plist,size,board,"player")
                            


                    if validChoice==True:
                        target=cpulist[chosenPiece].validMoves(plist,board)[chosenMove]
                        done=movePiece(cpulist[chosenPiece],target,size,screen,board,plist)
                        for i in plist:
                            if i.getLocation()==target and i.getController()=="player":
                                plist.remove(i)
                        GameOver,winner=isGameOver(plist,size,board) 
                    turn="player"
                            

                            
                if event.type == pygame.QUIT:
                    # change the value to False, to exit the main loop
                    running = False
                    GameOver= True
        


if __name__=="__main__":
    # call the main function
    main()