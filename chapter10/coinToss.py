import random
guess = ''

while guess not in ('heads', 'tails'):
    print('Guess the coin toss! Enter heads or tails:')
    guess = input()
toss = random.randint(0, 1) # 0 is tails, 1 is heads
if toss == 1:
    convert = 'heads'
else:
    convert = 'tails'
if convert == guess:
    print('You got it!')
else:
    print('Nope! Guess again!')
    guesses = input()
    if convert  == guesses:
        print('You got it!')
    else:
        print('Nope. You are really bad at this time')