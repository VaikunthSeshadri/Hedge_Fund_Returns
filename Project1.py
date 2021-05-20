import pandas as pd
import datetime
from datetime import datetime
import statistics as st
import math

'''
This program imports a dataframe with information about the returns of various hedge funds over time as well as other
information as provided by Kapil Rastogi. Using the information provided, this program attempts to analyze the 
performance of funds active from 01/01/2008 to 12/31/2017. Funds that start after the first date and funds that end
before the latter are not counted. For funds that exist during and beyond this timeframe, only their performance over 
these 10 years will be counted. This program analyzes the performance of the fund by calculating annualized returns,
annualized volatility, maximum drawdown, the duration of that drawdown as well as the Sharpe and Calmar ratios.
'''

'''import dataset'''

dataset = pd.read_csv(r'C:\Users\vaiku\PycharmProjects\KapilProjects\Kapil_Data.csv', parse_dates=['Date'], index_col=0)
dataset = pd.DataFrame(dataset)

'''capture a list of funds that were active between 01/01/2008 and 12/31/2017 by comparing a list of funds
that reported returns on 01/31/2008 and funds that reported returns on 12/31/2017. Funds that are in both lists were 
active in the time period.'''

start_fund = list(dataset.loc['2008-01-31'].iloc[:, 4])
end_fund = list(dataset.loc['2017-12-31'].iloc[:, 4])
relevant_funds = []

for i in end_fund:
    if i in start_fund:
        relevant_funds.append(int(i))

def max_dd(df):

    '''This function attempts to find the maximum drawdown of a fund from its returns. It takes in a dataframe with
    a column called Rate of Return and uses the returns to calculate maximum drawdown.'''

    df["total_return"] = df["Rate of Return"].cumsum()
    df["drawdown"] = df["total_return"] - df["total_return"].cummax()
    maxdd = df["drawdown"].min()
    return -1*maxdd/100


def duration(x):

    '''This function attempts to find the duration of the drawdown associated with the maximum drawdown. If the peak
    corresponding to the max DD was never exceeded anymore (i.e. the time adds to the duration of drawdown), the
    difference between the end-date and the time of the peak was used. '''

    y = x.loc[x['drawdown'] == x['drawdown'].min()]
    b = y.index[0]
    z = x.loc[x['drawdown'] == 0]
    start = datetime.strptime(str(z.index[0]), '%Y-%m-%d %H:%M:%S')
    end = datetime.strptime("2017-12-31 00:00:00", '%Y-%m-%d %H:%M:%S')
    g = datetime.strptime(str(y.index[0]), '%Y-%m-%d %H:%M:%S')
    start_diff = (g - start).days
    end_diff = max((end - g).days, 0)

    for i in range(1, len(z) - 1):
        f = datetime.strptime(str(z.index[i]), '%Y-%m-%d %H:%M:%S')
        h = datetime.strptime(str(z.index[i + 1]), '%Y-%m-%d %H:%M:%S')

        diff = max((g - f).days, 0)
        diff_1 = max((h - g).days, 0)
        if (f < g) and (f > start):
            start = f

        if (h < end) and (h > g):
            end = h

    return ((end - start).days / 365)


def ann_ret(x_return):

    '''This function attempts to find the annualized returns for a fund from a list of returns'''

    x_return = [((num / 100) + 1) for num in x_return]
    m = 1
    for i in x_return:
        m = m * i
    return (m ** (12 / len(x_return))) - 1

def ann_vol(x_return):

    '''This function attempts to find the annualized volatility for a fund from a list of its returns'''

    return st.stdev(x_return) * math.sqrt(12)

def sharpe(x_return):

    '''This function attempts to find the Sharpe ratio for a fund from a list of its returns
    Sharpe Ratio = (annualized returns - risk-free rate)/(annualized volatility), with risk-free rate assumed to be 0.
    '''

    return ann_ret(x_return)/ann_vol(x_return)

def calmar(x, x_return):

    '''This function attempts to find the Calmar ratio for a fund from its dataframe and a list of returns
    Calmar Ratio = (annualized returns - risk-free rate)/(maximum drawdown), with risk-free rate assumed to be 0.
    '''

    if max_dd(x) > 0:
        return ann_ret(x_return)/max_dd(x)
    else:
        return 0

ann_returns = []
ann_volatility = []
max_drawdown = []
duration_drawdown = []
calmar_ratio = []
sharpe_ratio = []

'''Computation of the various figures from the functions defined above for all the relevant funds'''


for q in relevant_funds:
    a = dataset.loc[dataset['Product Reference'] == int(q)]
    a = a.loc['2008-01-31':'2017-12-31']
    a_return = list(a.loc[:, 'Rate of Return'])
    ann_returns.append(float(ann_ret(a_return)))
    ann_volatility.append(float(ann_vol(a_return)))
    max_drawdown.append(float(max_dd(a)))
    duration_drawdown.append(float(duration(a)))
    sharpe_ratio.append(float(sharpe(a_return)))
    calmar_ratio.append(float(calmar(a, a_return)))

'''Presentation of results in a dataframe'''

col_names = ["Fund ID", 'Annualized Returns', 'Annualized Volatility', 'Maximum Drawdown', 'Duration of Drawdown', 'Sharpe Ratio', 'Calmar Ratio']
data = [relevant_funds, ann_returns, ann_volatility, max_drawdown, duration_drawdown, sharpe_ratio, calmar_ratio]

results = pd.DataFrame(data)
results = results.transpose()
results.columns = col_names
print(results)


