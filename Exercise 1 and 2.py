import numpy as np
import matplotlib.pyplot as plt
import pandas as pd
import statistics as st
from scipy.stats import skew
from scipy.stats import skewnorm

# Exercise 1: Creating 36 data points for two hedge fund returns with a positive and negative skew
# Sharpe ratio is essentially (Expected Returns)/(std dev of the returns)

z = np.random.normal(0,1, 36)

print(z)
print("Mean of Z: ", np.mean(z))

x = 1 + (z-np.mean(z))
print(x)
print("New Mean: ", np.mean(x))

'''
hedge1 = [0.76067099, -0.34415261, 1.5590077, -0.6023836, 1.07053833, 1.55489211,
          0.33662995, 0.70074729, -0.53373151, 3.594786, 0.30559619, 0.86485373,
          3.0049461, 0.33146944, 0.74384919, 2.44891398, 0.53207805, 0.35706731,
          1.80297669, 0.41893983, 0.66728789, -0.33158523, 2.06469472, 0.42270256,
          2.05964915, 0.17558543, 0.69573737, 0.70279793, 2.38557095, 0.31164943,
          0.36827956, 1.13979982, 2.26418595, 1.81539974, 1.47814737, 0.51032934]

hedgefund1 = []

for i in hedge1:
    x = i - 1
    hedgefund1.append(x)

print(hedgefund1)

expected_return1 = st.mean(hedge1)
std_dev1 = st.stdev(hedge1)
sharpe_ratio1 = expected_return1/std_dev1

print('Skew ' + str(skew(hedge1)))
print('Expected Returns ' + str(expected_return1))
print('Standard Dev ' + str(std_dev1))
print('Sharpe Ratio ' + str(sharpe_ratio1))

hedge1.sort()

plt.hist(hedgefund1, bins = 15, alpha = 0.65, edgecolor='k')
plt.xlabel('Returns')
plt.title('Histogram of returns of Hedge Fund 1 over 36 months')
plt.show()

hedge2 = [0.7138284, 1.19760027, 0.22349955, 1.09293669, 1.05156734, 0.53603039,
          1.40332843, 0.27643514, 0.4770598, 0.75069786, 0.1187825, 1.58332748,
          0.75459974, 0.73277956, 1.22210995, 1.61657888, 0.76500628, 1.39220507,
          -1.12128455, 2.46151686, 0.96956774, -0.18037703, 0.41323886, 1.63663789,
          1.11243398, 1.1565854, 0.80401109, 1.5937056, -0.47903869, 0.25200797,
          1.32599345, 1.74444004, 0.42669569, -1.48462914, 1.13346345, 0.5541033 ]


print("X =", len(hedge1), len(hedge2))
expected_return2 = st.mean(hedge2)
std_dev2 = st.stdev(hedge2)
sharpe_ratio2 = expected_return2/std_dev2

print('Skew ' + str(skew(hedge2)))
print('Expected Returns ' + str(expected_return2))
print('Standard Dev ' + str(std_dev2))
print('Sharpe Ratio ' + str(sharpe_ratio2))

hedge2.sort()

plt.hist(hedge2, bins = 15, alpha = 0.65, edgecolor='k')
plt.xlabel('Returns')
plt.title('Histogram of returns of Hedge Fund 2 over 36 months')
plt.show()
'''