answers = {"привет": "И тебе привет!"
    , "как дела": "Лучше всех"
    , "пока": "Увидимся"}


def get_answer(question, answers):
    return answers[question.lower()]
