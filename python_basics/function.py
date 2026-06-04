import numpy as np
import pandas as pd

print("NumPy:", np.__version__)
print("Pandas:", pd.__version__)


def twoSum(a,b):
    sum = a + b
    print("The sum of", a, "and", b, "is", sum)

twoSum(2,3)

print(__name__)
