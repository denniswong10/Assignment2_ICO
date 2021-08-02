"""
    This is a script for player that need to be control and make a plot of the cannon fire.
"""

playerShip1 = {"Pos":[0, 0]}
playerShip2 = {"Pos":[0, 0]}
playerShip3 = {"Pos":[0, 0]}
playerShips = [playerShip1, playerShip2, playerShip3]

win = 0
<<<<<<< Updated upstream
shipLeft = 3
=======
shipLeft = 3

def playerShipPosXY(isQuit):
    ship1_string = "Ship 1: -"
    ship2_string = "Ship 2: -"
    ship3_string = "Ship 3: -"
    
    for i in range(3):
        
        print("\n<Press 'q' to exit>")
        
        if (i == 0): 
            ship1_string = "> Ship 1: <"
        elif (i == 1):
            ship1_string = "Ship 1: (" + str(playerShip1["Pos"][0]) + ", " + str(playerShip1["Pos"][1]) + ")"
            ship2_string = "> Ship 2: <"
        else:
            ship1_string = "Ship 1: (" + str(playerShip1["Pos"][0]) + ", " + str(playerShip1["Pos"][1]) + ")"
            ship2_string = "Ship 1: (" + str(playerShip2["Pos"][0]) + ", " + str(playerShip2["Pos"][1]) + ")"
            ship3_string = "> Ship 3: <"
        
        print("\n" + ship1_string + "\n\n" + ship2_string + "\n\n" + ship3_string)
        print("\nBattlefield Size (9x9) -> Please enter between 1 to 9")
                
        validValue = False
        while (validValue == False):
            posX = input("\nPlace ship " + str(i + 1) + " to (PosX): ")
            if (posX.lower() == "q"): isQuit = True; break
            if (not posX.isdecimal()): print("\nInvalid Input!"); continue
            if (not (1 <= int(float(posX)) <= 9)): print("\nInvalid Input!"); continue
            validValue = True
        if (isQuit == False): posX = int(float(posX))
        if (isQuit == True): break
    
        validValue = False    
        while (validValue == False):
            posY = input("\nPlace ship " + str(i + 1) + " to (PosY): ")
            if (posY.lower() == "q"): isQuit = True; break
            if (not posY.isdecimal()): print("\nInvalid Input!"); continue
            if (not (1 <= int(float(posY)) <= 9)): print("\nInvalid Input!"); continue
            validValue = True
        if (isQuit == False): posY = int(float(posY))
        if (isQuit == True): break
        
        if (i == 0):
            playerShip1["Pos"][0] = posX
            playerShip1["Pos"][1] = posY
        elif(i == 1):
            playerShip2["Pos"][0] = posX
            playerShip2["Pos"][1] = posY
        else:
            playerShip3["Pos"][0] = posX
            playerShip3["Pos"][1] = posY
            
    return isQuit

def playerCannonPosXY(x, y):
    'When player input defined'
    
    'Check if any of the AI ship is equal to the player input'
    '    Update AI ship remain'
        
    'Otherwise skip this step'
    '    Goto AI cannon fire'
>>>>>>> Stashed changes
