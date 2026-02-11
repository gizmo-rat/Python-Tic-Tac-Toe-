import numpy as np
import matplotlib.pyplot as plt
import os
#from matplotlib.patches import Circle

class Game:
    player1 = ""
    player2 = ""
    x = []
    y = []
    result = 0 #still don't know what type i want this to be, should have three results, player 1 win, player 2 win, draw (so boolean is out of the question)


def play(game):
    game.player1 = input("Player 1, please enter your name " )
    game.player2 = input("Player 2, please enter your name " )
    i=0
    end = False
    while (i<9 and end==False):
        if(i%2 == 0):
            print(game.player1,"it is your turn \n Please choose where to place your 'X' in x-y coordinates from 1-3 :) \n")
        else:
            print(game.player2,"it is your turn \n Please choose where to place your 'O' in x-y coordinates from 1-3 :) \n")
        xIn = int(input(" enter an x value: ")) 
        yIn = int(input(" enter a y value: ")) 
        game.x.append(xIn)
        game.y.append(yIn)
        show(game)
        i+=1
    return
        

def show(game): 
    xpoints = np.array([1,1])
    ypoints = np.array([.5,3.5])
    print("The newest point is at x:",type(game.x[len(game.x)-1])," and  y:",type(game.y[len(game.y)-1]))
    for i in range(len(game.x)): #is there a way for x in game.x and y in game.y at the same time?
        print(i)
        if (i%2==0):
            print("entered if \n")
            crosspointsx = np.array([-.4,.4]) + game.x[i] #x coords for the crosss
            crosspointsy1 = np.array([-.4,.4]) + game.y[i] #y coords for cross line from bl to tr
            crosspointsy2 = np.array([.4,-.4]) + game.y[i] #y coords for cross line from tl to br
            plt.figure(figsize=(5,5))
            plt.plot(xpoints+.5, ypoints, color = 'white') #vert line 1
            plt.plot(xpoints+1.5,ypoints, color = 'white') #vert line 2
            plt.plot(ypoints,xpoints+.5, color = 'white') #hori line 1
            plt.plot(ypoints,xpoints+1.5, color = 'white') #hori line 2
            plt.plot(crosspointsx,crosspointsy1, color = 'b')
            plt.plot(crosspointsx,crosspointsy2, color = 'b')
        else:
            print("entered else \n")
            theta = np.linspace(0, 2*np.pi, 100)
            r= .45
            x = r*np.cos(theta) + game.x[i] 
            y = r*np.sin(theta) + game.y[i] 
            plt.plot(x,y, color = 'red')
    plt.gca().set_facecolor('black') 
    plt.xticks([1,2,3], ['1', '2', '3'])
    plt.yticks([1,2,3], ['1', '2', '3'])
    plt.show()
    os.system('cls')
exit = False

matchhistory = []

while (exit==False): 
    currentGame = Game()
    play(currentGame)
    
    exit = True




show()

