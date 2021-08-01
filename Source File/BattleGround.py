"""
    This is a script for creating battlefield to all object that need to grid their ship
"""

def generateMap(playerWin, playerShipLeft, AI_win, AI_shipLeft):
    print("----1----2----3----4----5----6----7----8----9----    BOT Wins: " + str(AI_win) + "\n")
    for i in range(9):
        print(str(i + 1) + "|                                             |" + str(i + 1), end = (("    Ship Left: " + ((str(AI_shipLeft) + "\n") if (i == 0) else (str(playerShipLeft) + " \n"))) if ((i == 0) or (i == 8)) else "\n"))
        print()
    print("----1----2----3----4----5----6----7----8----9----    Player Wins: " + str(playerWin) + "\n")
    
def goTo(x, y, text):
    #Not done
    print("Hello World")