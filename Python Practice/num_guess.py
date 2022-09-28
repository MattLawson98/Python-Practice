import random

def guess(x):
 random_number = random.randint(1,x)
 guess = 0
while guess != random_number:  
  guess = int(input(f'Guess a number between 1 and {X}:'))
  if guess < random_number:
    print('Sorry, guess again. Too low')
  elif guess > random_number:
    print('Sorry, guess again. Too High')

  print(f'You have guessed the number, {random_number}, correctly')

guess(10)