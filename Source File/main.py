"""
    This is the main script where everything are been implemented here and execute it
    Making the game flow by calling function and module
"""

def shipTest():
    # Doesn't Work!
    import Ship as Ship1
    import Ship as Ship2
    import Ship as Ship3
    
    Ship1.posX = 4
    print(Ship2.posX) # 4
    print(Ship3.posX) # 4


playerShip1 = {"Pos":[0, 0]}
playerShip2 = {"Pos":[0, 0]}
playerShip3 = {"Pos":[0, 0]}

AI_ship1 = {"Pos":[0, 0]}
AI_ship2 = {"Pos":[0, 0]}
AI_ship3 = {"Pos":[0, 0]}

def playerInput():
    for i in range(3):
        
        ship1_string = "Ship 1: -"
        ship2_string = "Ship 2: -"
        ship3_string = "Ship 3: -"
        
        if (i == 0): ship1_string = "> Ship 1: <"
        elif (i == 1): ship2_string = "> Ship 2: <"
        else: ship3_string = "> Ship 3: <"
        
        print(ship1_string + "\n\n" + ship2_string + "\n\n" + ship3_string + "\n")
        print("Battlefield Size (9x9) -> Please enter between 1 to 9\n")
        
        posX = input("Place ship " + str(i + 1) + " to (PosX): "); print()
        posY = input("Place ship " + str(i + 1) + " to (PosY): "); print()
        
        if (i == 0):
            playerShip1["Pos"][0] = posX
            playerShip1["Pos"][1] = posY
        elif(i == 1):
            playerShip2["Pos"][0] = posX
            playerShip2["Pos"][1] = posY
        else:
            playerShip3["Pos"][0] = posX
            playerShip3["Pos"][1] = posY
            
def AI_PosXY():
    import random
    
    for i in range(3):
        
        posX = random.randrange(1, 10)
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

def main():
    import BattleGround as battleGround
    import Player as player
    import AI
    
    while True:
        
        print("Welcome To Battle-Ship War Game\n")
        
        playerInput()
        AI_PosXY()
        battleGround.printMap(player.win, player.shipLeft, AI.win, AI.shipLeft)
        
        break
    
main()