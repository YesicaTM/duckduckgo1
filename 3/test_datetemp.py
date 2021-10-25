# test_datetemp.py

import pytest
from datetemp import sorted_by_date
from datetemp import sorted_by_temp
from datetemp import DateTemp

# testing ability to create instance of date temp class from normal date and temp


def test_instance():
    dt = DateTemp(20091212, 99)

# test to_string returns expected string so when printed out, the outcome is correct


def test_tostring():
    dt = DateTemp(20091212, 99)
    assert str(dt) == f'The temperature on {dt.date} was {dt.temperature} F'

# test set_date_from_ints
def test_set_date1():
    # testing ability to change date from initial creation and have it displayed as new date in str
    # for ability to change the date for a temperature
    dt = DateTemp(20091212, 99)
    dt.set_date_from_ints(2011, 12, 12)
    assert str(dt) == f'The temperature on 2011-12-12 was {dt.temperature} F'

# test sort by temp and date function and that they work
def test_sort_date():
    a = DateTemp(20091212, 99)
    b = DateTemp(20081011, 95)
    c = DateTemp(20100201, 96)
    list1 = [a, b, c]
    assert str(sorted_by_date(list1)) == '[The temperature on 20081011 was 95 F, The temperature on 20091212 was 99 F, The temperature on 20100201 was 96 F]'

def test_sort_date():
    a = DateTemp(20091212, 99)
    b = DateTemp(20081011, 95)
    c = DateTemp(20100201, 96)
    list1 = [a, b, c]
    assert str(sorted_by_temp(list1)) == "[The temperature on 20081011 was 95 F, The temperature on 20100201 was 96 F, The temperature on 20091212 was 99 F]"

