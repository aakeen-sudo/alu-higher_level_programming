#!/usr/bin/python3
from models.rectangle import Rectangle

r1 = Rectangle(3, 2)
print(r1.width)
print(r1.height)
print(r1.id)

r2 = Rectangle(4, 5, 9)
print(r2.id)

try:
    r3 = Rectangle(3, "hi")
except TypeError as e:
    print(e)
