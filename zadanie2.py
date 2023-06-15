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






#TODO testyMikolaja