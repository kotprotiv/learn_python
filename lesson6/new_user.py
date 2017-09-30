from db import db_session, User
import sqlalchemy

user = User('Ivan', 'Ivanov', 'ii@mail.ru')

print(user)

db_session.add(user)
db_session.commit()