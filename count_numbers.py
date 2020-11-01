import re
import random
import string
from math import fsum


def random_data():
    data = [str(random.uniform(0, 1000)) for i in range(10)] + \
           ["#" + "".join(string.digits) for i in range(5)] + \
           ["" for i in range(5)]
    random.shuffle(data)
    return data


def write_random_data(file):
    with open(file, "w") as f:
        list(map(lambda i: f.write(str(i) + '\n'), random_data()))


def read_data(file):
    with open(file) as f:
        data = f.read().splitlines()
        return data


def select_float_number(data):
    pattern = re.compile(r'(\d+\.\d+)')
    elem = [i for a in data for i in pattern.findall(a)]
    res = list(map(lambda i: float(i), elem))
    return res


file_name = "numbers2.txt"
write_random_data(file_name)

full_data = read_data(file_name)
float_numbers = select_float_number(full_data)
calc = fsum(float_numbers)
print(round(calc, 2))
