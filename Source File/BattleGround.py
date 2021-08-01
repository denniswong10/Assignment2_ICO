"""
    This is a script for creating battlefield to all object that need to grid their ship
"""

import Player as player
import AI

def generateMap():
    print("\n----1----2----3----4----5----6----7----8----9----    BOT Wins: " + str(AI.win))
    for i in range(9):
        print("\n" + str(i + 1) + "|                                             |" + str(i + 1), end = (("    Ship Left: " + ((str(AI.shipLeft)) if (i == 0) else str(player.shipLeft))) if ((i == 0) or (i == 8)) else ""))
        print()
    print("\n----1----2----3----4----5----6----7----8----9----    Player Wins: " + str(player.win) + "\n")
    
def goTo(x, y, text):
    print("\nHello")