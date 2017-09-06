def find_person(name):
	name_list = ["Вася", "Маша", "Петя", "Валера", "Саша", "Даша"]
	for name_c in name_list:
		if name_c == name:
			return('{0} нашелся'.format(name))


input_name = input('Введите имя: ')
print(find_person(input_name))