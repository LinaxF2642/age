driving = input('Have you ever tired to drive a car?')
age = input('How old are you？')
age = int(age)
if driving == 'yes':
	if age >= 18:
		print('It is legal')
	else:
		print('It is illegal')
elif driving == 'Never':
	if age >= 18:
		print('You are able to take the driving test')
	else:
		print('No worries. You can take the driving test after you are 18')