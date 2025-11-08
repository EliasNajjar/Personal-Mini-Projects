solveFor = int(input("What do you need:\n1: find quota amount given random number\n2: find quota amount given rolls\n3: find rolls and random number given quotas\n"))
while solveFor != 1 and solveFor != 2 and solveFor != 3:
	solveFor = int(input("Please try again:\n1: find quota amount given random number\n2: find quota amount given rolls\n3: find rolls and random number given quotas\n"))

if solveFor == 1:
	quota = int(input("What quota number was just finished (not quota amount)? "))
	ranNum = float(input("What is the random number (-0.503 to 0.503)? "))
	previousQuotaAmount = int(input("What was the previous quota amount? "))
	result = "Next quota will be " + str(int(previousQuotaAmount + 100 * (1 + ranNum) * (quota**2/16 + 1)))
elif solveFor == 2:
	quota = int(input("What quota number was just finished (not quota amount)? "))
	rolls = float(input("What rolls are you expecting (0 to 1)? "))
	previousQuotaAmount = int(input("What was the previous quota amount? "))
	result = "Next quota will be " + str(int(previousQuotaAmount + 100 * (1 + (rolls * 1.006 - 0.503)) * (quota**2/16 + 1)))
elif solveFor == 3:
	quota = int(input("What quota number was just finished (not quota amount)? "))
	previousQuotaAmount = int(input("What was the previous quota amount? "))
	newQuotaAmount = int(input("What is the new quota amount? "))
	ranNum = round((newQuotaAmount - previousQuotaAmount) / (100 * (quota**2/16 + 1)) - 1, 3)
	result = "Random number was about " + str(ranNum) + " and rolls were about " + str(round((ranNum + 0.503) / 1.006, 2))

print(result)