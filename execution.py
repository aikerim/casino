from decouple import config
from home_work_5 import casino

my_money = config('MY_MONEY', default=0, cast=int)
print(casino(my_money))
