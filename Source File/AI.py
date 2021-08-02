"""
    Make a script that can make a bot to plot ship and fire cannon
"""

AI_ship1 = {"Pos":[0, 0], "Can":[0, 0]}
AI_ship2 = {"Pos":[0, 0], "Can":[0, 0]}
AI_ship3 = {"Pos":[0, 0], "Can":[0, 0]}
AI_Ships = [AI_ship1, AI_ship2, AI_ship3]

win = 0
shipLeft = 3

def AI_ShipPosXY():
    import random
    import Player as player
    
    for i in range(3):
        
        posX = random.randint(1, 9)
        posY = random.randint(1, 9)
        
        # Checking if the positions generated are the same as the ones player inputted, if yes then generate again
        for playerShip in (player.playerShips):
            while (playerShip["Pos"][0] == posX):
                posX = random.randint(1, 9)
            while (playerShip["Pos"][1] == posY):
                posY = random.randint(1, 9)
                    
        if (i == 0):
            AI_ship1["Pos"][0] = posX
            AI_ship1["Pos"][1] = posY
        elif(i == 1):
            AI_ship2["Pos"][0] = posX
            AI_ship2["Pos"][1] = posY
        else:
            AI_ship3["Pos"][0] = posX
            AI_ship3["Pos"][1] = posY
            
def AI_CannonPosXY():
    import random

    shipNum = random.randint(1, len(AI_Ships))
    posX = random.randint(1, 9)
    posY = random.randint(1, 9)
    
    if (shipNum == 1):
        AI_ship1["Can"][0] = posX
        AI_ship1["Can"][1]= posY
    elif (shipNum == 2):
        AI_ship2["Can"][0] = posX
        AI_ship2["Can"][1] = posY
    else:
        AI_ship3["Can"][0] = posX
        AI_ship3["Can"][1] = posY
        
    return shipNum, posX, posY