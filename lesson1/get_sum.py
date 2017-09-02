def get_summ(one, two, delimeter=' '):
	c = str(one) + str(delimeter) + str(two)
	c = c.upper()
	return c

print(get_summ('Hello', 'nothing!'))