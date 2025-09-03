sentence = "The quick brown fox jumps over the lazy dog."
print(sentence)
sentence = sentence.lower()

letters = ["a","b","c","d","e","f","g","h","i","j","k","l","m","n","o","p","q","r","s","t","u","v","w","x","y","z"]
occurences = [0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0]

for x in range(len(sentence)):
    for y in range(26):
        if sentence[x] == letters[y]:
            occurences[y] += 1

isPangram = "Pangram"
used = []
notUsed = []
for z in range(26):
    if occurences[z] == 0:
        isPangram = "Not a pangram"
        notUsed.append(letters[z])
    elif occurences[z] > 1:
        used.append(letters[z])

def printList(list):
    newList = ""
    for a in list:
        newList += a + " "
    return newList

print(isPangram)
if isPangram == "Pangram":
    print(printList(used),end=" ")
else:
    print(printList(notUsed),end=" ")