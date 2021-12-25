from typing import Counter
import pygame

from time import sleep

from pygame.draw import circle

pygame.init()

color = (0,0,150)
surface = pygame.display.set_mode((400,300))
surface.fill(color)
pygame.display.set_caption("Pepcoding Connect4")
font = pygame.font.Font("freesansbold.ttf", 40)
font_black = (0,0,0)
font_white = (255,255,255)


black_color = (0,0,0)
player_color = ((0,255,170))
isPlayerColor = True
playerWins = False

redColorXCoordinate = 0
redColorYCoordinate = 0

#cordinate of circle
X = 40
Y = 30

listOfCircles = [
                  [[X,Y] , [X+60,Y], [X+120,Y], [X+180,Y], [X+240,Y],[X+300,Y]],
                  [[X,Y+60] , [X+60,Y+60], [X+120,Y+60], [X+180,Y+60], [X+240,Y+60],[X+300,Y+60]],
                  [[X,Y+120] , [X+60,Y+120], [X+120,Y+120], [X+180,Y+120], [X+240,Y+120],[X+300,Y+120]],
                  [[X,Y+180] , [X+60,Y+180], [X+120,Y+180], [X+180,Y+180], [X+240,Y+180],[X+300,Y+180]],
                  [[X,Y+240] , [X+60,Y+240], [X+120,Y+240], [X+180,Y+240], [X+240,Y+240],[X+300,Y+240]]                 
                  
                ] 

connect4List = []



for i in range(len(listOfCircles)):
    col = []
    for j in range(len(listOfCircles[0])):
        col.append(-1)
    connect4List.append(col)


pygame.draw.circle(surface, black_color, (X,Y), 20,0)
pygame.draw.circle(surface, black_color, (X + 60 ,Y), 20,0)
pygame.draw.circle(surface, black_color, (X + 120,Y), 20,0)
pygame.draw.circle(surface, black_color, (X + 180,Y), 20,0)
pygame.draw.circle(surface, black_color, (X + 240,Y), 20,0)
pygame.draw.circle(surface, black_color, (X + 300,Y), 20,0) 

pygame.draw.circle(surface, black_color, (X,Y + 60), 20,0)
pygame.draw.circle(surface, black_color, (X + 60 ,Y +60), 20,0)
pygame.draw.circle(surface, black_color, (X + 120,Y + 60), 20,0)
pygame.draw.circle(surface, black_color, (X + 180,Y + 60), 20,0)
pygame.draw.circle(surface, black_color, (X + 240,Y + 60), 20,0)
pygame.draw.circle(surface, black_color, (X + 300,Y + 60), 20,0)

pygame.draw.circle(surface, black_color, (X,Y + 120), 20,0)
pygame.draw.circle(surface, black_color, (X + 60 ,Y + 120), 20,0)
pygame.draw.circle(surface, black_color, (X + 120,Y + 120), 20,0)
pygame.draw.circle(surface, black_color, (X + 180,Y + 120), 20,0)
pygame.draw.circle(surface, black_color, (X + 240,Y + 120), 20,0)
pygame.draw.circle(surface, black_color, (X + 300,Y + 120), 20,0)

pygame.draw.circle(surface, black_color, (X,Y + 180), 20,0)
pygame.draw.circle(surface, black_color, (X + 60 ,Y + 180), 20,0)
pygame.draw.circle(surface, black_color, (X + 120,Y + 180), 20,0)
pygame.draw.circle(surface, black_color, (X + 180,Y + 180), 20,0)
pygame.draw.circle(surface, black_color, (X + 240,Y + 180), 20,0)
pygame.draw.circle(surface, black_color, (X + 300,Y + 180), 20,0)

pygame.draw.circle(surface, black_color, (X,Y + 240), 20,0)
pygame.draw.circle(surface, black_color, (X + 60 ,Y + 240), 20,0)
pygame.draw.circle(surface, black_color, (X + 120,Y + 240), 20,0)
pygame.draw.circle(surface, black_color, (X + 180,Y + 240), 20,0)
pygame.draw.circle(surface, black_color, (X + 240,Y + 240), 20,0)
pygame.draw.circle(surface, black_color, (X + 300,Y + 240), 20,0)

def isInside(equation_x, equation_y, equation_h, equation_k):

    # h, k are the centre of the given cirle
    # x, y are the points that we have to check

    radius = 20
    circleEquation = (equation_x - equation_h) * (equation_x - equation_h) + (equation_y - equation_k) * (equation_y - equation_k)

    if(circleEquation <= radius * radius):  
        return True
    
    else:
        return False


def isFourdots0Connected(row, column, player):
    
    dots0 = 0
    dots1 = 0

    dictionary = {
        "player" : -1,
        "dots" : False
    }


    # BOTTOM TO TOP => 
    r = row - 3
    mainRow = row
    mainColumn = column

    while(mainRow >= r and mainRow >= 0):
        element = connect4List[mainRow][mainColumn]
        
        if(element == 0):
            dots0 += 1
            # print(dots0)

        
        if(element == 1):
            dots1 += 1
            # print(dots1)

        mainRow -= 1
    
    if(dots0 == 4):
        dictionary["player"] = 0
        dictionary["dots"] = True
        return dictionary
    
    elif(dots1 == 4):
        dictionary["player"] = 1
        dictionary["dots"] = True
        return dictionary
    
    else:
        dots0 = 0
        dots1 = 0


    # TOP RIGHT =>

    r = row - 3
    c = column + 3
    mainRow = row
    mainColumn = column

    while(mainRow >= r and mainColumn <= c and mainRow >= 0 and mainColumn < len(connect4List[0])):
        element = connect4List[mainRow][mainColumn]

        if(element == 0):
            dots0 += 1

        elif(element == 1):
            dots1 += 1


        mainRow -= 1
        mainColumn += 1
    
    if(dots0 == 4):
        dictionary["player"] = 0
        dictionary["dots"] = True
        return dictionary

    elif(dots1 == 4):
        dictionary["player"] = 1
        dictionary["dots"] = True
        return dictionary
    
    else:
        dots0 = 0
        dots1 = 0




    # TOP LEFT =>
    
    r = row-3
    c = column-3
    mainRow = row
    mainColumn = column

    while(mainRow>=r and mainColumn>=c):
        element = connect4List[mainRow][mainColumn]

        if(element == 0):
            dots0 += 1
        
        elif(element == 1):
            dots1 += 1


        mainRow -= 1
        mainColumn -= 1

    if(dots0 == 4):
        dictionary["player"] = 0
        dictionary["dots"] = True
        return dictionary

    elif(dots1 == 4):
        dictionary["player"] = 1
        dictionary["dots"] = True
        return dictionary
    
    else:
        dots0 = 0
        dots1 = 0

    
    # TO LEFT =>

    mainRow = row
    mainColumn = column
    c = column-3

    while(mainColumn>=c):
        element = connect4List[mainRow][mainColumn]

        if(element == 0):
            dots0 += 1
        
        elif(element == 1):
            dots1 += 1


        mainColumn -= 1

    if(dots0 == 4):
        dictionary["player"] = 0
        dictionary["dots"] = True
        return dictionary

    elif(dots1 == 4):
        dictionary["player"] = 1
        dictionary["dots"] = True
        return dictionary

    else:
        dots0 = 0
        dots1 = 0

    # TO RIGHT =>
    
    mainRow = row
    mainColumn = column
    c = column + 3

    while(mainColumn <= c and mainColumn < len(connect4List[0])):
        element = connect4List[mainRow][mainColumn]
        mainColumn += 1

        if(element == 0):
            dots0 += 1
        
        elif(element == 1):
            dots1 += 1

        
    if(dots0 == 4):
        dictionary["player"] = 0
        dictionary["dots"] = True
        return dictionary
    
    elif(dots1 == 4):
        dictionary["player"] = 1
        dictionary["dots"] = True
        return dictionary

    else:
        dots0 = 0
        dots1 = 0

    
    # TO BOTTOM =>

    mainRow = row
    mainColumn = column
    r = row + 3

    while(mainRow <= r and mainRow < len(connect4List)):
        element = connect4List[mainRow][mainColumn]

        if(element == 0):
            dots0 += 1

        elif(element == 1):
            dots1 += 1

        mainRow += 1
    
    if(dots0 == 4):
        dictionary["player"] = 0
        dictionary["dots"] = True
        return dictionary
    
    elif(dots1 == 4):
        dictionary["player"] = 1
        dictionary["dots"] = True
        return dictionary

    else:
        dots0 = 0
        dots1 = 0
    
    #BOTTOM LEFT =>

    mainRow = row
    mainColumn = column

    r = row + 3
    c = column - 3

    while(mainRow <= r and mainColumn >= c and mainRow < len(listOfCircles) and mainColumn>=0):
        element = connect4List[mainRow][mainColumn]

        if(element == 0):
            dots0 += 1

        elif(element == 1):
            dots1 += 1

        
        mainRow += 1
        mainColumn -= 1
    
    if(dots0 == 4):
        dictionary["player"] = 0
        dictionary["dots"] = True
        return dictionary
    
    elif(dots1 == 4):
        dictionary["player"] = 1
        dictionary["dots"] = True
        return dictionary

    else:
        dots0 = 0
        dots1 = 0

    #BOTTOM RIGHT =>

    mainRow = row
    mainColumn = column
    r = row + 3
    c = column + 3

    while(mainRow <= r and mainColumn <= c and mainRow < len(connect4List) and mainColumn < len(connect4List[0])):
        element = connect4List[mainRow][mainColumn]

        if(element == 0):
            dots0 += 1

        elif(element == 1):
            dots1 += 1

        mainRow += 1
        mainColumn += 1

    if(dots0 == 4):
        dictionary["player"] = 0
        dictionary["dots"] = True
        return dictionary
    
    elif(dots1 == 4):
        dictionary["player"] = 1
        dictionary["dots"] = True
        return dictionary

    else:
        dots0 = 0
        dots1 = 0
    


while True:

    player_one = 0
    player_two = 1

    for event in pygame.event.get():
        
        if(isPlayerColor):
            player_color = (255,0,0)
        
        else:
            player_color = ((0,255,0))

        if event.type == pygame.MOUSEBUTTONUP:

            equation_x, equation_y = pygame.mouse.get_pos()

            isInsideTrue = False
            
            for i in listOfCircles:

               for j in i:

                   equation_h, equation_k = j

                   if(isInside(equation_x, equation_y, equation_h, equation_k)):
                        print("It is inside the cirle")

                        column = int(equation_h/60)
                        row = len(listOfCircles)

                        redColorXCoordinate = 0
                        redColorYCoordinate = 0
                        
                        for x in reversed(range(len(connect4List))):
                            if(connect4List[x][column] == -1):
                                
                                if(isPlayerColor):  
                                    connect4List[x][column] = player_one
                                    redColorXCoordinate, redColorYCoordinate =listOfCircles[x][column]
                                
                                else:
                                    connect4List[x][column] = player_two
                                    redColorXCoordinate, redColorYCoordinate =listOfCircles[x][column]

                                dictionary = isFourdots0Connected(x,column,isPlayerColor)
                                
                                if(dictionary):
                                    if(dictionary["player"] == 0):
                                        print("Player 1 wins (Red Player)")

                                        text = font.render("Player 1 Wins", True, font_white, font_black)
                                        textRect = text.get_rect()
                                        surface.fill(font_black)
                                        textRect.center = (200, 150)
                                        surface.blit(text, textRect)
                                        playerWins = True

                                    
                                    elif(dictionary["player"] == 1):
                                        print("Player 2 Wins (Green Color)")
                                        text = font.render("Player 2 Wins", True, font_white, font_black)
                                        textRect = text.get_rect()
                                        surface.fill(font_black)
                                        textRect.center = (200, 150)
                                        surface.blit(text, textRect)
                                        playerWins = True
                                
                               
                                break

                        if(playerWins == True):
                            break    

                        for x in connect4List:
                            print(x)


                        pygame.draw.circle(surface, player_color, (redColorXCoordinate, redColorYCoordinate) , 20, 0)
                        if(isPlayerColor):
                            isPlayerColor = False
                        else:
                            isPlayerColor = True


                        isInsideTrue = True
                        break
            
                   else:    
                        pass

               if(isInsideTrue or playerWins):
                   break
            

        if event.type == pygame.QUIT:
            quit()


    pygame.display.flip()

    