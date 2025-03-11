def intSort(array):
    dupArray = array[:]
    arraySorted = []
    for x in range(len(dupArray)):
        currentMin = array[0]
        for y in range(1,len(dupArray)):
            if dupArray[y] < currentMin:
                currentMin = dupArray[y]
        dupArray.remove(currentMin)
        arraySorted.append(currentMin)
    return arraySorted

a = [5,4,3,2,1]
print(intSort(a))
print(a)