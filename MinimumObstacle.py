import typing
from math import floor, pi, e
from typing import List

coloursOne: List[int] = []
coloursTwo: List[int] = []
coloursThree: List[int] = []
coloursFour: List[int] = []

for n in range(1, 301):
    coloursOne.append(1+(floor(n*pow(pi,10)))%100)
    coloursTwo.append(1 + (floor(n * pow(e, 10))) % 100)
    coloursThree.append(1 + (n * 51) % 100)
    coloursFour.append(1 + (n * 24) % 100)


print(coloursOne)