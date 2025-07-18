from random import randint
computador=randint(0,5)
usuario= int(input('Guess a number between 0 and 5: '))
if computador==usuario:
	print('You won!')
else:
	print(f'Wrong, the number is:  {computador}')