def get_answer(question):
	answers = {"привет": "И тебе привет!"
	,"как дела": "Лучше всех"
	,"пока": "Увидимся"}
	return answers[question.lower()]

print(get_answer(input('Задай вопрос!')))