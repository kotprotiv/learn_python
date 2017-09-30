from flask import Flask
from flask import request
import requests

api_key = '0cbf7d274d6b13d3665fa44992a4d526'

got_data = requests.get('http://api.data.mos.ru/v1/datasets/2009/rows?api_key={}'.format(api_key))
newborn_json = got_data.json()


app = Flask(__name__)

@app.route("/")
def index():
    html = '''<a href="http://127.0.0.1:5000/names">Перейти к рейтингу имен!</a>'''
    return html

@app.route("/names")
def names():
    year = request.args.get('year', default = 2017)
    html = '''<table>
                <tr>
                    <th>Имя</th>
                    <th>Год</th>
                    <th>Месяц</th>
                    <th>Количество</th>
                </tr>
            '''
    for row in newborn_json:
        if row['Cells']['Year'] == int(year):
            html += ('<tr>')
            html += ('<td>' + row['Cells']['Name'] + '</td>')
            html += ('<td>' + str(row['Cells']['Year']) + '</td>')
            html += ('<td>' + str(row['Cells']['Month']) + '</td>')
            html += ('<td>' + str(row['Cells']['NumberOfPersons']) + '</td>')         
            html += ('</tr>')
    html += ('</table>')
    return html

if __name__ == "__main__":
    app.run()