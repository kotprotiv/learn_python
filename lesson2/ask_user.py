answers = {"привет": "И тебе привет!"
,"как дела": "Лучше всех"
,"пока": "Увидимся"}

def get_answer(question):
	return answers.get(question.lower(), 'Я не понял!')

def ask_user():
    while True:
        user_input = input('Скажи что-нибудь: ')
        answer = get_answer(user_input)
        print(answer)
        if answer == 'Увидимся':
        	break

try:
	ask_user()
except KeyboardInterrupt:
	print('\nКак жаль, что вы уходите!')