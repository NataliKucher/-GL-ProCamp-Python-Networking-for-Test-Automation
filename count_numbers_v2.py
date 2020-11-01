import random
import string
from math import fsum

file_name = "numbers2.txt"


def random_data():
    data = [str(random.uniform(0, 1000)) for i in range(10)] + \
           ["#" + "".join(string.digits) for i in range(5)] + \
           ["" for i in range(5)]
    random.shuffle(data)
    return data


with open(file_name, "w") as f:
    list(map(lambda i: f.write(str(i) + '\n'), random_data()))


with open(file_name) as file:
    full_data = file.read().splitlines()
    el = [i for i in full_data if i != "" and not i.startswith("#")]
    float_numbers = list(map(lambda i: float(i), el))

calc = fsum(float_numbers)
print(round(calc, 2))
