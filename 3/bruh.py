from datetemp import DateTemp
from datetemp import sorted_by_temp
from datetemp import sorted_by_date

dt = DateTemp(202120658833, 'hell')
print(dt.__str__())


a = DateTemp(20091212, 99)
b = DateTemp(20081011, 95)
c = DateTemp(20100201, 96)
list1 = [a, b, c]
print(sorted_by_temp(list1))