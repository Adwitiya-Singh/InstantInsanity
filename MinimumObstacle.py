import typing
from math import floor, pi, e
from typing import List

coloursOne: List[List[int]] = []
coloursTwo: List[List[int]] = []
coloursThree: List[List[int]] = []
coloursFour: List[List[int]] = []

for n in range(1, 301, 3):
    coloursOne.append([1+(floor(n*pow(pi,10)))%100, 1+(floor(n+1*pow(pi,10)))%100, 1+(floor(n+2*pow(pi,10)))%100])
    coloursTwo.append([1 + (floor(n * pow(e, 10))) % 100, 1 + (floor(n+1 * pow(e, 10))) % 100, 1 + (floor(n+2 * pow(e, 10))) % 100])
    coloursThree.append([1 + (n * 51) % 100, 1 + (n+1 * 51) % 100, 1 + (n+2 * 51) % 100])
    coloursFour.append([1 + (n * 24) % 100, 1 + (n+1 * 24) % 100, 1 + (n+2 * 24) % 100])


print(coloursOne)