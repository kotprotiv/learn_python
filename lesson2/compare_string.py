def compare_strings(string1, string2):
	if len(string1) == len(string2):
		return 1
	elif len(string1) > len(string2):
		return 2
	elif len(string1) != len(string2) and string2 == 'learn':
		return 3
	else:
		return -1

input_str1 = input('Enter first string:')
input_str2 = input('Enter second string:')

print(compare_strings(input_str1, input_str2))