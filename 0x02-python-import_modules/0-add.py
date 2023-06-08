#!/usr/bin/python3

import sys
from add_0 import add

# My addition var
a = 1
b = 2

if 'add_0' in sys.modules:
     del sys.modules['add_0'] 
# Output of addition
print("{} + {} = {}".format(a, b, add(a, b)))
