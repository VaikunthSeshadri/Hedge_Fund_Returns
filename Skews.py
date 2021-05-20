import statistics as st
from scipy.stats import skew
from scipy.stats import skewnorm
from random import gauss
import pandas as pd
import numpy as np
import math

skewed = [-5, -4, -3, -2, -1, 0, 1, 2, 3, 4, 5]

data = []

y = False

while y == False:

    z = np.random.lognormal(0, 5, 60)

    if 4.99 < skew(z) < 5.01:

        mean_z = np.mean(z)
        std = st.stdev(z)

        goal_mean = 1

        ann_mean = mean_z*12
        ann_std = std*math.sqrt(12)


        goal_std = (goal_mean*12)/math.sqrt(12)

        p = goal_mean + (z - mean_z)*(goal_std/std)

        sharpe = (12*np.mean(p))/(st.stdev(p)*math.sqrt(12))

        if 0.99 < sharpe < 1.01:
            print(p)
            print("Details of P:", np.mean(p), st.stdev(p), skew(p))
            print("Details of Z: ", np.mean(z), st.stdev(z), skew(z))

            y = True
        else:
            print(skew(p))
            y = False
    else:
        False

