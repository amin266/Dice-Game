import random

while True:
    print('__________________________')
    print('Dice : 1,2,3,4,5,6')
    print('---------------------------')
    button = input('type (Go) to roll the dice : ')
    if button == 'Go':
        dice_list = [1, 2, 3, 4, 5, 6]
        print('random result:', random.choice(dice_list))
    else:
        break
