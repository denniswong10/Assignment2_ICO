"""
    This is the main script where everything are been implemented here and execute it
    Making the game flow by calling function and module
"""
def main():
    #For testing only:
    import BattleGround as battleGround
    
    AI_Win = 1
    playerWin = 2
    AI_ShipLeft = 3
    playerShipLeft = 2
    
    battleGround.printMap(AI_Win, playerWin, AI_ShipLeft, playerShipLeft)
    battleGround.goTo(20, 20, "A")
    
main()