# PROJECT 2 - Print Euler's number to the nth digit
import sys
import numpy as np

euler_number = np.exp(1)
euler_decimals = lambda precision: sys.stdout.write('%.*f' % (precision, euler_number)) if precision <= 50 \
    else sys.stdout.write("Number too large, Please select a number less than 50")
euler_decimals(int(input("How many decimals do you want to display ? ")))
