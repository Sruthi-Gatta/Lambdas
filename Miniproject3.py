# PROJECT 3 - Print Pi to the nth digit

import math
import sys

Decimals = lambda precision: sys.stdout.write('%.*f' % (precision, math.pi)) if precision <= 50 else sys.stdout.write(
    "Number too large, Please select a number less than 50")
Decimals(int(input("How many decimals do you want to display ? ")))