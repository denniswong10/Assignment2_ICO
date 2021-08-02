"""
    This is the main script where everything are been implemented here and execute it
    Making the game flow by calling function and module
"""
import Player as player
import AI

isQuit = False

def playerPosXY():
    ship1_string = "Ship 1: -"
    ship2_string = "Ship 2: -"
    ship3_string = "Ship 3: -"
    
    for i in range(3):
        
        print("\n<Press 'q' to exit>")
        
        if (i == 0): 
            ship1_string = "> Ship 1: <"
        elif (i == 1):
            ship1_string = "Ship 1: (" + str(player.playerShip1["Pos"][0]) + ", " + str(player.playerShip1["Pos"][1]) + ")"
            ship2_string = "> Ship 2: <"
        else:
            ship1_string = "Ship 1: (" + str(player.playerShip1["Pos"][0]) + ", " + str(player.playerShip1["Pos"][1]) + ")"
            ship2_string = "Ship 1: (" + str(player.playerShip2["Pos"][0]) + ", " + str(player.playerShip2["Pos"][1]) + ")"
            ship3_string = "> Ship 3: <"
        
        print("\n" + ship1_string + "\n\n" + ship2_string + "\n\n" + ship3_string)
        print("\nBattlefield Size (9x9) -> Please enter between 1 to 9")
        
        global isQuit
        
        validValue = False
        while (validValue == False):
            posX = input("\nPlace ship " + str(i + 1) + " to (PosX): ")
            if (posX.lower() == "q"): isQuit = True; break
            if ((not posX.isdecimal()) and (not (1 <= int(float(posX)) <= 9))): print("\nInvalid Input!"); continue
            validValue = True
        if (isQuit == False): posX = int(float(posX))
        if (isQuit == True): break    
    
        validValue = False    
        while (validValue == False):
            posY = input("\nPlace ship " + str(i + 1) + " to (PosY): ")
            if (posY.lower() == "q"): isQuit = True; break
            if ((not posY.isdecimal()) and (not (1 <= int(float(posY)) <= 9))): print("\nInvalid Input!"); continue
            validValue = True
        if (isQuit == False): posY = int(float(posY))
        if (isQuit == True): break
        
        if (i == 0):
            player.playerShip1["Pos"][0] = posX
            player.playerShip1["Pos"][1] = posY
        elif(i == 1):
            player.playerShip2["Pos"][0] = posX
            player.playerShip2["Pos"][1] = posY
        else:
            player.playerShip3["Pos"][0] = posX
            player.playerShip3["Pos"][1] = posY
            
def AI_PosXY():
    import random
    
    posX = random.randrange(1, 10)
    posY = random.randrange(1, 10)
    
    for i in range(3):
        
        # Checking if the positions generated are the same as the ones player inputted, if yes then generate again
        for playerShip in (player.playerShips):
            for index in range(2):
                while (playerShip["Pos"][index] == posX):
                    posX = random.randrange(1, 10)
                while (playerShip["Pos"][index] == posY):
                    posY = random.randrange(1, 10)
                    
        if (i == 0):
            AI.AI_ship1["Pos"][0] = posX
            AI.AI_ship1["Pos"][1] = posY
        elif(i == 1):
            AI.AI_ship2["Pos"][0] = posX
            AI.AI_ship2["Pos"][1] = posY
        else:
            AI.AI_ship3["Pos"][0] = posX
            AI.AI_ship3["Pos"][1] = posY

def main():
    global isQuit
    
    while ((isQuit == False) and (player.shipLeft != 0) and (AI.shipLeft != 0)):
        
        import BattleGround as battleGround
        
        print("Welcome To Battle-Ship War Game")
        
        playerPosXY()
        if (isQuit == True): break
        AI_PosXY()
        battleGround.generateMap()
        
        break
        
    if (player.shipLeft == 0): print("\nYou Lost :(")
    elif (AI.shipLeft == 0): print("\nYou Won!")
    
main()

def CheckForShipRemain():
    'If any of the player remain ship is 0'
    '   Display win to the player have won'
    
    'Otherwise the game will continue'
    
'Break loop when any ship remain is 0'
while (AI.shipLeft != 0 or player.shipLeft != 0):
    'Call the player cannon fire first and check for ship remain'
    CheckForShipRemain()
    'Call the AI cannon fire then go back to ship remain'
    CheckForShipRemain()
    
'Display win message!'
if (AI.shipLeft == 0): 
    print("Player Win!")
    
elif (player.shipLeft == 0): 
    print("AI Win!")