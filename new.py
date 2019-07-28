
from GameFunctions import *
from Pieces import *


# define a main function 
def main():
    # load and set the window and board
    screen=makeBoard(size,board)
    pygame.font.init()

    
   
    
    
    
    # variables to control the main loop
    running = True
    isgameset=False
    turn = "player"
    selectPiece=[]

    #the main Loop
    while running==True:
        plist=startGame(screen)  ##start a game from turn 1
        while isgameset==False:  ##so the game will only restart if the previous is finished
            for event in pygame.event.get():
                if turn=="player":
                    if pygame.mouse.get_pressed()[0]==1:
                        click=pygame.mouse.get_pos()
                        target=getTileLocation(click,plist)
                        if selectPiece=[]:
                            selectedPiece=SelectPiece(target)
                            write("Select the location that you want to move the piece!",0,size,screen)
                        if selectedPiece!=[]:
                            
                            
                            

                            
                if event.type == pygame.QUIT:
                    # change the value to False, to exit the main loop
                    running = False
                    isgameset= True
        


if __name__=="__main__":
    # call the main function
    main()