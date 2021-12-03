import random
from random import sample

list = [1,2,3,4,5]
print(sample(list, 5))

from pydbgen import pydbgen
DB = pydbgen.pydb()
name_date = DB.gen_dataframe(251, fields=['name','date'])
date = DB.gen_data_series(251, data_type='date')
