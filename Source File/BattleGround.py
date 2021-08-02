"""
    This is a script for creating battlefield to all object that need to grid their ship
"""

import Player as player
import AI

playerWin = player.win
AI_Win = AI.win
playerShipLeft = player.shipLeft
AI_ShipLeft = AI.shipLeft

def plotPlayerShip(text):
    ship1_SpaceCount = (player.playerShip1["Pos"][0] * 5) - 3
    ship2_SpaceCount = (player.playerShip2["Pos"][0] * 5) - 3
    ship3_SpaceCount = (player.playerShip3["Pos"][0] * 5) - 3
            
    for i in range(9):
        if ((i + 1) == player.playerShip1["Pos"][1]): print("\n" + str(i + 1) + "|" + (" " * ship1_SpaceCount) + text + (" " * (45 - ship1_SpaceCount - 1)) + "|" + str(i + 1), end = (("    Ship Left: " + ((str(AI_ShipLeft)) if (i == 0) else str(playerShipLeft))) if ((i == 0) or (i == 8)) else ""))
        elif ((i + 1) == player.playerShip2["Pos"][1]): print("\n" + str(i + 1) + "|" + (" " * ship2_SpaceCount) + text + (" " * (45 - ship2_SpaceCount - 1)) + "|" + str(i + 1), end = (("    Ship Left: " + ((str(AI_ShipLeft)) if (i == 0) else str(playerShipLeft))) if ((i == 0) or (i == 8)) else ""))
        elif ((i + 1) == player.playerShip3["Pos"][1]): print("\n" + str(i + 1) + "|" + (" " * ship3_SpaceCount) + text + (" " * (45 - ship3_SpaceCount - 1)) + "|" + str(i + 1), end = (("    Ship Left: " + ((str(AI_ShipLeft)) if (i == 0) else str(playerShipLeft))) if ((i == 0) or (i == 8)) else ""))
        else: print("\n" + str(i + 1) + "|" + (" " * 45) + "|" + str(i + 1), end = (("    Ship Left: " + ((str(AI_ShipLeft)) if (i == 0) else str(playerShipLeft))) if ((i == 0) or (i == 8)) else ""))
        print()
        
def plotPlayerCannon(text):
    print("Hello")
    

def generateMap(text):
    print("\n----1----2----3----4----5----6----7----8----9----    BOT Wins: " + str(AI_Win))
    
    if (text == "S"): plotPlayerShip(text)
    else: plotPlayerShip(text); plotPlayerCannon(text)
        
    print("\n----1----2----3----4----5----6----7----8----9----    Player Wins: " + str(playerWin) + "\n")