def getUserCoordinate():
    x = float(input("Enter x coordinate: "))
    y = float(input("Enter y coordinate: "))
    return x, y

def coordinateToString(coordinate):
    x = str(coordinate[0])
    y = str(coordinate[1])

    return "( " + x + ", " + y + " )"

def findMidpoint(coordinates1, coordinates2):
    xm = (coordinates1[0]+coordinates2[0])/2
    ym = (coordinates1[1]+coordinates2[1])/2
    return([xm, ym])

coordinates1 = getUserCoordinate()
coordinates2 = getUserCoordinate()
midpoint = findMidpoint(coordinates1, coordinates2)
print("The midpoint of")
print(coordinateToString(coordinates1))
print("and")
print(coordinateToString(coordinates2))
print("is")
print(coordinateToString(midpoint))