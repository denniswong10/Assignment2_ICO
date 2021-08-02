"""
    This is the main script where everything are been implemented here and execute it
    Making the game flow by calling function and module
"""
import Player as player
import AI

isQuit = False

def main():
    global isQuit
    
    while ((isQuit == False) and (player.shipLeft != 0) and (AI.shipLeft != 0)):
        
        import BattleGround as battleGround
        
        print("Welcome To Battle-Ship War Game")
        
        _Quit = player.playerShipPosXY(isQuit)
        isQuit = _Quit
        if (isQuit == True): break
        AI.AI_ShipPosXY()
        battleGround.generateMap()
        
        break
        
    if (player.shipLeft == 0): print("\nYou Lost :(")
    elif (AI.shipLeft == 0): print("\nYou Won!")
    
main()