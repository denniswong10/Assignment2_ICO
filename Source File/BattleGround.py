"""
    This is a script for creating battlefield to all object that need to grid their ship
"""

def printMap(AI_Win, playerWin, AI_ShipLeft, playerShipLeft):
    print("---------1------2-----3-----4-----5-----6-----7-----8-----9-------      BOT Wins: " + str(AI_Win) + "\n")
    for i in range(9):
        print(str(i + 1) + "|                                                              |" + str(i + 1), end = (("      Ship Left: " + (str(AI_ShipLeft) if (i == 0) else (str(playerShipLeft) if (i == 8) else "")) + " \n") if ((i == 0) or (i == 8)) else "\n"))
        print()
    print("---------1------2-----3-----4-----5-----6-----7-----8-----9-------      Player Wins: " + str(playerWin) + "\n")