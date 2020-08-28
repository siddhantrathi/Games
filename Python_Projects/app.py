import random

#Ghost Game

door = random.randint(1, 4)
no.ofdoor = 3


ans = int(input('Which no. do you choose: '))

if ans > no.ofdoor:
    print('invalid door')

if ans == door:
    print('Ghost')
else:
    print('No Ghost')