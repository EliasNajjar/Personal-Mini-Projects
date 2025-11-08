from random import randint

wins = [0,0,0,0,0,0,0,0,0,0,0]

while True:
    places = [0,0,0,0,0,0,0,0,0,0,0]
    while True:
        roll = randint(1,6) + randint(1,6)
        places[roll-2] += 180 // (18 - 3*abs(roll-7))
        if max(places) == 180:
            wins[places.index(180)] += 1
            break

    for h in range(11):
        print(h+2,": ",wins[h])

    print()
    if max(wins) == 1000:
        break