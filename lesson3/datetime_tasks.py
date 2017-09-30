import datetime
from calendar import monthrange

a = datetime.datetime.now()
b = datetime.timedelta(days=1)
days_r = monthrange(a.year, a.month - 1)
c = datetime.timedelta(days=days_r[1])
print(a)
print(a - b)
print(a - c)
