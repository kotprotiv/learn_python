import get_answer as ga
import csv

new_answers = []
for key in ga.answers:
    new_answers.append(dict(zip(['question', 'answer'], [key, ga.answers[key]])))
    #print(new_answers)

with open('answers.csv', 'w', encoding='UTF-8') as f:
    fields = ['question', 'answer']
    writer = csv.DictWriter(f, fields, delimiter=';')
    writer.writeheader()
    writer.writerows(new_answers)
