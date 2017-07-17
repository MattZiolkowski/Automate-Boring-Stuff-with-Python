import random

result = ('heads', 'tails')
guess = ''
while guess not in result:
    print('Guess the coin toss! Enter heads or tails:')
    guess = input()

toss = result[random.randrange(0, 2)]
if toss == guess:
    print('You got it!')
else:
    print('Nope! Guess again!')
    guess = input()
    if toss == guess:
        print('You got it!')
    else:
        print('Nope. You are really bad at this game.')