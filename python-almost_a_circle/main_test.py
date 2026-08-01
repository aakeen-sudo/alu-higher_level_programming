#!/usr/bin/python3
from models.base import Base

b1 = Base()
b2 = Base()
b3 = Base(12)

print(b1.id)
print(b2.id)
print(b3.id)
