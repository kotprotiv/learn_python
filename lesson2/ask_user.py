def get_answer(question):
	answers = {"привет": "И тебе привет!"
    ,"как дела": "Лучше всех"
    ,"пока": "Увидимся"}
	return answers.get(question.lower())

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
	print()
	print('Как жаль, что вы уходите!')