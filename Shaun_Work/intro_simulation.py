import random
from random import sample
from datetime import date, datetime
from pydbgen import pydbgen

list = [1,2,3,4,5]
print(sample(list, 5))

def calculate_age(born):
    born = datetime.strptime(born, '%Y-%m-%d').date()
    today = date.today()
    return today.year - born.year - ((today.month,
                                      today.day) < (born.month,
                                                    born.day))
DB = pydbgen.pydb()
name_date = DB.gen_dataframe(251, fields=['name','date'])
# date = DB.gen_data_series(251, data_type='date')
name_date['age'] = name_date['date'].apply(calculate_age)

