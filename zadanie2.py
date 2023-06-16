import math

#zadanieIzy
def missingRectangleVertice(x1,y1,x2,y2,x3,y3):
    if x1 == x2 or x1==x3:
        if x1 == x2:
           x4=x3
        else:
           x4=x2
    else:
        x4=x1
    if y1 == y2 or y1==y3:
        if y1 == y2:
           y4=y3
        else:
           y4=y2
    else:
        y4=y1
    return(print(str(x4)+", "+str(y4)))

missingRectangleVertice(1,1,2,3,4,2)

#TODO zadaniePauliny
def missingTrinagleVertice(ax, ay, bx, by):

    # liczmy odleglośc miedzy punktami
    ab = math.pow(pow(bx - ax, 2) + pow(by - ay, 2), 1 / 2)
    print(ab)

    angle = math.atan2(by - ay, bx - ax)

    # calculate the coordinates of the third point (the first one)
    cx_1 = ax + ab * math.cos(angle - (1 * math.pi / 3))
    cy_1 = ay + ab * math.sin(angle - (1 * math.pi / 3))

    # calculate the coordinates of the third point (the second one)
    cx_2 = bx + ab * math.cos(angle + (1 * math.pi / 3))
    cy_2 = by + ab * math.sin(angle + (1 * math.pi / 3))

    return print('Wspołrzedne trójkąta to ', cx_1, " i ", cy_1, ' lub ', cx_2, ' i ', cy_2 )





#TODO testyMikolaja