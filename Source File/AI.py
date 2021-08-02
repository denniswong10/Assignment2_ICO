"""
    Make a script that can make a bot to plot ship and fire cannon
"""

AI_ship1 = {"Pos":[0, 0]}
AI_ship2 = {"Pos":[0, 0]}
AI_ship3 = {"Pos":[0, 0]}

win = 0
shipLeft = 3

def AI_ShipPosXY():
    import random
    import Player as player
    
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
            AI_ship1["Pos"][0] = posX
            AI_ship1["Pos"][1] = posY
        elif(i == 1):
            AI_ship2["Pos"][0] = posX
            AI_ship2["Pos"][1] = posY
        else:
            AI_ship3["Pos"][0] = posX
            AI_ship3["Pos"][1] = posY