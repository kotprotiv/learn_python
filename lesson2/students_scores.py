students_scores = [{'school_class':'4a', 'scores':[2,3,4,3,4]}
, {'school_class':'4b', 'scores':[4,3,5,5,2]}
, {'school_class':'4c', 'scores':[2,5,2,2,2]}]

sum_all = 0
count_all = 0
sum_class = 0
temp_sum = 0

for class_n in students_scores:
	for scores in class_n['scores']:
		sum_all += scores
		count_all += 1
	sum_class = sum_all - temp_sum
	print('{0} class average is {1}'.format(class_n['school_class'], sum_class / len(class_n['scores'])))
	temp_sum += sum_class

print('school average is: {0}'.format(sum_all / count_all))
