"""
    This is the main script where everything are been implemented here and execute it
    Making the game flow by calling function and module
"""
import Player as player
import AI

isQuit = False

def comparePos(text):
    if (text == "S"):
        print("LOL")
    else:
        print("LOL")
    
def main():
    global isQuit
    
    while ((isQuit == False) and (player.shipLeft != 0) and (AI.shipLeft != 0)):
        
        import BattleGround as battleGround
        
        print("Welcome To Battle-Ship War Game")
        
        _Quit = player.playerShipPosXY(isQuit)
        isQuit = _Quit
        if (isQuit == True): break
        AI.AI_ShipPosXY()
        battleGround.generateMap("S") # Generate map with only player's ships plotted
        
        _Quit = player.playerCannonPosXY(isQuit)
        isQuit = _Quit
        if (isQuit == True): break
        comparePos("S") # Compare player's ship position with AI's ship
        battleGround.generateMap("C") # Genearte map with player's ships and cannon plotted
        AI.AI_CannonPosXY()
        comparePos("A") # Compare AI's ship position with player's ship
        battleGround.generateMap("S")
        
    if (player.shipLeft == 0): print("\nYou Lost :(")
    else: print("\nYou Won!")
    
main()