"""
    This is a script for creating battlefield to all object that need to grid their ship
"""

import Player as player
import AI

def plotPlayerShipAndCannon(text):
    if (text == "S"):
        
        playerShip_PosY = 0 
        
        for i in range(9):
            for playerShip in player.playerShips:
                if ((i + 1) == playerShip["Pos"][1]):
                    playerShip_PosY = playerShip["Pos"][1]
                    ship_SpaceCount = (playerShip["Pos"][0] * 5) - 3
                    
            if ((i + 1) == playerShip_PosY): print("\n" + str(i + 1) + "|" + (" " * ship_SpaceCount) + text + (" " * (45 - ship_SpaceCount - 1)) + "|" + str(i + 1), end = (("    Ship Left: " + ((str(AI.shipLeft)) if (i == 0) else str(player.shipLeft))) if ((i == 0) or (i == 8)) else ""))
            else: print("\n" + str(i + 1) + "|" + (" " * 45) + "|" + str(i + 1), end = (("    Ship Left: " + ((str(AI.shipLeft)) if (i == 0) else str(player.shipLeft))) if ((i == 0) or (i == 8)) else ""))
            print()
                
    else:
        
        playerShip_PosY = 0
        playerCannon_PosY = 0
        
        for i in range(9):
            for playerShip in player.playerShips:
                if ((i + 1) == playerShip["Pos"][1]):
                    playerShip_PosY = playerShip["Pos"][1]
                    ship_SpaceCount = (playerShip["Pos"][0] * 5) - 3
                elif ((i + 1) == playerShip["Can"][1]):
                    playerCannon_PosY = playerShip["Can"][1]
                    cannon_SpaceCount = (playerShip["Can"][0] * 5) - 3
                    
            if ((i + 1) == playerShip_PosY): print("\n" + str(i + 1) + "|" + (" " * ship_SpaceCount) + "S" + (" " * (45 - ship_SpaceCount - 1)) + "|" + str(i + 1), end = (("    Ship Left: " + ((str(AI.shipLeft)) if (i == 0) else str(player.shipLeft))) if ((i == 0) or (i == 8)) else ""))
            elif ((i + 1) == playerCannon_PosY): print("\n" + str(i + 1) + "|" + (" " * cannon_SpaceCount) + text + (" " * (45 - cannon_SpaceCount - 1)) + "|" + str(i + 1), end = (("    Ship Left: " + ((str(AI.shipLeft)) if (i == 0) else str(player.shipLeft))) if ((i == 0) or (i == 8)) else ""))
            else: print("\n" + str(i + 1) + "|" + (" " * 45) + "|" + str(i + 1), end = (("    Ship Left: " + ((str(AI.shipLeft)) if (i == 0) else str(player.shipLeft))) if ((i == 0) or (i == 8)) else ""))
            print()

def generateMap(text):
    print("\n----1----2----3----4----5----6----7----8----9----    BOT Wins: " + str(AI.win))
    
    if (text == "S"): plotPlayerShipAndCannon(text)
    else: plotPlayerShipAndCannon(text)
        
    print("\n----1----2----3----4----5----6----7----8----9----    Player Wins: " + str(player.win) + "\n")