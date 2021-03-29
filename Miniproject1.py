# PROJECT 1 - BASIC STATISTICS
import numpy as np

sample = list(range(1, 101))
# Mean
average = lambda x: sum(x) / len(sample)
# Standard Deviation
standard_deviation = lambda x: np.std(x)
# Median
Median = lambda x: np.median(x)
# Range
range_of_list = lambda x: max(x)-min(x)
# Variance
Variance_val = lambda x: np.var(x)
print("The Mean of first 100 Natural Numbers is {}".format(average(sample)))
print("The Standard Deviation of first 100 Natural Numbers is {}".format(standard_deviation(sample)))
print("The Median of first 100 Natural Numbers is {}".format(Median(sample)))
print("The Range of first 100 Natural Numbers is {}".format(range_of_list(sample)))
print("The Variance of first 100 Natural Numbers is {}".format(Variance_val(sample)))



