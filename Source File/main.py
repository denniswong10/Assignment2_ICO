"""
    This is the main script where everything are been implemented here and execute it
    Making the game flow by calling function and module
"""
import Player as player
import AI

isQuit = False

def comparePos(text, shipNum):
    if (str(shipNum).lower() != 'q'):
        if (text == "P"):
            for i in range(len(AI.AI_Ships)):
                if ((player.playerShips[shipNum - 1]["Can"][0] == AI.AI_Ships[i]["Pos"][0]) and (player.playerShips[shipNum - 1]["Can"][1] == AI.AI_Ships[i]["Pos"][1])): return "AI_Ships", i
        else:
            for i in range(len(player.playerShips)):
                if ((AI.AI_Ships[shipNum - 1]["Can"][0] == player.playerShips[i]["Pos"][0]) and (AI.AI_Ships[shipNum - 1]["Can"][1] == player.playerShips[i]["Pos"][1])): return "Player_Ships", i
        
    return "", -1

def removeShip(shipStr, shipNum):
    if (shipStr == "AI_Ships"):
        AI.AI_Ships[shipNum] = {"Destroyed":[shipNum + 1]}
        AI.AI_Ships.remove(AI.AI_Ships[shipNum])
        AI.shipLeft -= 1
        if (AI.shipLeft == 0): player.win += 1
    else:
        player.playerShips[shipNum] = {"Destroyed":[shipNum + 1]}
        player.playerShips.remove(player.playerShips[shipNum])
        player.shipLeft -= 1
        if (player.shipLeft == 0): AI.win += 1
    
def main():
    import BattleGround as battleGround
    
    global isQuit
    
    print("Welcome To Battle-Ship War Game")
    
    _Quit = player.playerShipPosXY(isQuit)
    isQuit = _Quit
    if (isQuit == True): return
    AI.AI_ShipPosXY()
    battleGround.generateMap("S") # Generate map with only player's ships plotted
    
    while ((isQuit == False) and (player.shipLeft != 0) and (AI.shipLeft != 0)):
        
        _Quit, _playerShipNum = player.playerCannonPosXY(isQuit)
        isQuit = _Quit
        if (isQuit == True): break
        shipStr, _AI_ShipNum = comparePos("P", _playerShipNum) # Compare player's cannon position with AI's ship position
        if ((shipStr != "") and (_AI_ShipNum != -1)): removeShip(shipStr, _AI_ShipNum)
        battleGround.generateMap("C") # Generate map with player's ships and cannon plotted
        
        if (len(AI.AI_Ships) == 0): break
        
        AI_ShipNum, cannonPosX, cannonPosY = AI.AI_CannonPosXY() # Remove cannonPosX, cannonPosY when done testing
        shipStr, player_ShipNum = comparePos("A", AI_ShipNum) # Compare AI's cannon position with player's ship position
        if ((shipStr != "") and (player_ShipNum != -1)): removeShip(shipStr, player_ShipNum)
        battleGround.generateMap("S") # Generate map with only player's ships plotted
        
        if (len(player.playerShips) == 0): break
    
        print("\nAI Ship " + str(AI_ShipNum) + " Cannon Last Pos: " + str(cannonPosX) + ", " + str(cannonPosY) + " -- For Testing Only!")
        print("\nAI Ship 1 Pos X: " + str(AI.AI_ship1["Pos"][0]) + ", Pos Y: " + str(AI.AI_ship1["Pos"][1]) + " -- For Testing Only!")
        print("AI Ship 2 Pos X: " + str(AI.AI_ship2["Pos"][0]) + ", Pos Y: " + str(AI.AI_ship2["Pos"][1]) + " -- For Testing Only!")
        print("AI Ship 3 Pos X: " + str(AI.AI_ship3["Pos"][0]) + ", Pos Y: " + str(AI.AI_ship3["Pos"][1]) + " -- For Testing Only!")
    
    if (player.shipLeft == 0): print("\nYou Lost :(")
    elif (AI.shipLeft == 0): print("\nYou Won!")
    
main()