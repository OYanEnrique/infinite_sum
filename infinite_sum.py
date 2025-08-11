# Infinite Sum

sum = 0
counter = 0
greater = 0
lower = 0
answer = 'Y'


while True:
	number = int(input('Enter a number:\n'))
	sum += number
	counter +=1
	
	if counter == 1:
		greater = number
		lower = number
	else:
		if number > greater:
			greater = number
			
		elif number < lower:
			lower = number
			
	answer=str(input('Want to continue, Y or N? ')).strip().upper()
	
	if answer == 'N':
		break
	

average = sum/counter
print(f'The average is {average:.2f}')
print(f'The greater number was {greater}')
print(f'The lower number was {lower}')