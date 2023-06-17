import math

#zadanieIzy
def missingRectangleVertice(x1,y1,x2,y2,x3,y3):
    if x1 == x2 or x1 == x3:
        if x1 == x2:
           x4 = x3
        else:
           x4 = x2
    else:
        x4 = x1
    if y1 == y2 or y1 == y3:
        if y1 == y2:
           y4 = y3
        else:
           y4 = y2
    else:
        y4 = y1
    return x4, y4

missingRectangleVertice(1,1,2,3,4,2)

#TODO zadaniePauliny
def missingTriangleVertice(ax, ay, bx, by):

    # liczmy odleglośc miedzy punktami
    ab = math.pow(pow(bx - ax, 2) + pow(by - ay, 2), 1 / 2)
    print(ab)

    angle = math.atan2(by - ay, bx - ax)

    # calculate the coordinates of the third point (the first one)
    cx_1 = ax + ab * math.cos(angle + math.pi/3)
    cy_1 = ay + ab * math.sin(angle + math.pi/3)

    # calculate the coordinates of the third point (the second one)
    cx_2 = ax + ab * math.cos(angle - math.pi/3)
    cy_2 = ay + ab * math.sin(angle - math.pi/3)

    return [(cx_1, cy_1), (cx_2, cy_2)]




#TODO testyMikolaja
#almost_equal - rounding numbers due to precission issues
def almost_equal(t1, t2, rel_tol=1e-9):
    return all(abs(x-y) <= max(rel_tol * max(abs(x), abs(y)), rel_tol) for x, y in zip(t1, t2))

assert almost_equal(missingTriangleVertice(0, 0, 1, 0)[0], (0.5, math.sqrt(3)/2))
assert almost_equal(missingTriangleVertice(0, 0, 1, 0)[1], (0.5, -math.sqrt(3)/2))

assert missingRectangleVertice(0, 0, 5, 0, 0, 5) == (5, 5)
assert missingRectangleVertice(2, 3, 5, 3, 2, 6) == (5, 6)



