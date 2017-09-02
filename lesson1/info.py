name = input('Enter your name:')
last_name = input('Enter your last name:')
user_info = {'first_name':name, 'last_name':last_name}
#print(user_info['first_name'])
for key in user_info:
	print(user_info[key])