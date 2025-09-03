print("Input: ")
numOfShapes = int(input())
shapes = ["cube","sphere","cylinder","cone"]

compareShapes = []
for x in range(numOfShapes):
    shape = input()
    compareShapes.append(shape.lower())

shapeTypes = []
for y in range(len(compareShapes)):
    temp = compareShapes[y]
    x = 0
    newTemp = ""
    while temp[x] != " ":
        newTemp += temp[x]
        x += 1
    shapeTypes.append(newTemp)

lengths = []
for z in range(len(shapeTypes)):
    if compareShapes[z] == "cube"

volumes = []
for z in range(len(shapeTypes)):
    if shapeTypes[z] == "cube":
        volumes.append()

#should have used .split which I did not know about at the time