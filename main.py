import sys
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
    
    #variables to get the moves registered for the AI
    roundMoves=[]
    #clean Start
    badMoves=[]
    #load 
    try:
        file=open("GameMemory.txt","r")
        moves=int(file.readline())
        for i in range(0,moves):
            roundMoves=[]
            line=file.readline()
            for i2 in range(0,(len(line)-2),2):
                roundMoves.append((int(line[i2]),int(line[i2+1])))
            badMoves.append(roundMoves)
        file.close()
    except:
        #print("Oops!",sys.exc_info()[0],"occured.")
        print("no File loaded")
    # AI final form
    #badMoves=[[(2, 1), (0, 1)], [(2, 1), (1, 1)], [(2, 1), (2, 1), (1, 1), (0, 1)], [(2, 1), (2, 1), (1, 1), (1, 1), (1, 1), (0, 1)], [(0, 1), (1, 1)], [(0, 1), (2, 1)], [(0, 1), (0, 1), (1, 1),(2, 1)], [(1, 1), (1, 1), (1, 1), (0, 1), (2, 1), (2, 1)], [(1, 1), (2, 1)], [(1, 1), (1, 1), (1, 1), (2, 1), (0, 1), (0, 1)], [(1, 1), (0, 1)], [(1, 1), (1, 1), (1, 1), (1, 1)], [(1, 1), (1, 1), (0, 1), (2, 1)], [(1, 1), (1, 1), (2, 1), (0, 1)], [(1, 1), (1, 1), (2, 1), (2, 1), (1, 1), (0, 1)], [(1, 1), (1, 1), (0, 1), (0, 1), (1, 1), (2, 1)], [(0, 1), (0, 1),(1, 1), (1, 1), (1, 1), (2, 1)]]
    #the main Loop
    while running==True:
        plist=startGame(screen)  ##start a game from turn 1
        GameOver=False 
        turn="player"
        scoreBoard.append(winner)
        if winner=="player": #CPU only remember moves that made it lose
            roundMoves.remove(roundMoves[-1])
            badMoves.append(roundMoves)

        print(roundMoves)    
        print(scoreBoard)
        roundMoves=[]
        while GameOver==False:  ##so the game will only restart if the previous is finished
            if turn=="player":
                #the checkImmobilization check all valid moves and brings a random possible move as return
                noMoves,chosenMove,chosenPiece,availablePieces,GameOver,winner=checkImmobilization(plist,size,board,screen,turn,roundMoves,badMoves)
                for event in pygame.event.get():
                    if pygame.mouse.get_pressed()[0]==1:
                        click=pygame.mouse.get_pos()
                        target=getTileLocation(click,plist) 
                        #target return the location if the tile is empty or the Piece obj occupying it
                        if selectedPiece!=[]:
                            if type(target)!=tuple:#therefore, if the taget is not a location, it is a piece obj
                                hadPiece.append(target)
                                target=target.getLocation()     

                            done=movePiece(selectedPiece,target,size,screen,board,plist) #return false if the move was unsuccessfull
                            if done==False:
                                write("Invalid move!",1000,size,screen)
                                write("Select the piece you want to move!",0,size,screen)
                                selectedPiece.setLocation(selectedPiece.getLocation())
                                selectedPiece.setColor((0,0,0))
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
                    for i in plist:
                        if i.getLocation()==target and i.getController()=="player":
                            plist.remove(i)
                    GameOver,winner=isGameOver(plist,size,board,screen) 
                
                        
                turn="player"
                            
            if GameOver==True:
                write((winner+" WINS!!!"),1500,size,screen)
                            
            if event.type == pygame.QUIT:
                file=open("GameMemory.txt","w")
                file.write(str(len(badMoves))+"\n")
                for i in range(0,len(badMoves)):
                    for i2 in range(0,len(badMoves[i])):
                        file.write(str(badMoves[i][i2][0]))
                        file.write(str(badMoves[i][i2][1]))
                    file.write("\n")

                file.close()
                print(scoreBoard)
                if "player" not in scoreBoard:
                    print("HEXAPAWN HAS NO WEAKNESS")
                # change both following variables to exit the main loops
                running = False
                GameOver= True
        


if __name__=="__main__":
    # call the main function
    main()
