

from random import randrange
from datetime import timedelta


def random_date(start, end):
    """
    This function will return a random datetime between two datetime
    objects.
    """
    delta = end - start
    int_delta = (delta.days * 24 * 60 * 60) + delta.seconds
    random_second = randrange(int_delta)
    return start + timedelta(seconds=random_second)

from datetime import datetime

d1 = datetime.strptime('1/1/2018 1:30 PM', '%m/%d/%Y %I:%M %p')
d2 = datetime.strptime('1/1/2019 4:50 AM', '%m/%d/%Y %I:%M %p')

patient_data = []

for _ in range(10):

    patient_data.append(
        {
            'name': 'Patient ' + str(_+1),
            'id': 'ID ' + str(_ + 1),
            'city': 'Amsterdam',
            'last_visit': random_date(d1, d2)
        }
    )