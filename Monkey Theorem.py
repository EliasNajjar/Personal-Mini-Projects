import random
import time

temp = ""
#charList = ["a","b","c","d","e","f","g","h","i","j","k","l","m","n","o","p","q","r","s","t","u","v","w","x","y","z"," "," "," "," "]
charList = ["m","o","h","a","n","d","a","s","s"]

ending = input("What would you like the text to end with? ")

goodInput = False # to check if input is valid in while loop

while True: # a break will end the loop when input is valid
    badChars = [] # to tell user what chars are not valid

    for i in ending:
        iIsGood = False # to check if char in ending is valid
        for j in charList:
            if i == j: # if the character is valid
                iIsGood = True # char in ending is in charList
                break # break j loop and go to the next char in ending
        if iIsGood == False: # if the char in ending was not in charList
            add_i = True # we expect to add the char
            for k in badChars:
                if k == i: # if the char is already in badChars, we do not need to add it again
                    add_i = False
            if add_i == True:
                badChars.append(i) # add that char to a list to tell the user it is not valid

    if badChars != []: # if the input is not valid
        if len(badChars) == 1:
            print(badChars[0] + " is not a valid character. ", end="") # tell user there was 1 invalid char
        else: # if there is more than one invalid char
            for i in range(len(badChars)-1):
                print(badChars[i] + ", ", end="")
            print("and " + badChars[-1] + " are not valid characters. ", end="") # tell the user each invalid char
        ending = input("What would you like the text to end with? ") # get new input
    else: # if input is valid
        break # input is good and while loop ends

count = 0 # to count the number of characters it takes to reach ending
while temp != ending:
    count += 1
    r = random.randint(0, len(charList)-1) # choose random index in charList
    print(charList[r], end="") # print that character
    temp = temp + charList[r] # update temp var to compare to ending
    if temp[len(temp)-1] != ending[len(temp)-1]: # if the next random character is not the next character in ending
        temp = "" # reset temp

print("\n", count, " characters.")