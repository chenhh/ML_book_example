# -*- coding: utf-8 -*-

import pandas as pd
import numpy as np

"""
ts object of R
y <- ts(c(123,39,78,52,110), start=2012)
"""
samples = [123, 39, 78, 52, 110]
first_year = 2012
#
period_range = pd.period_range(first_year, periods=len(samples), freq='Y')
y = pd.Series(samples, index=period_range)
print(y)
"""
2012    123
2013     39
2014     78
2015     52
2016    110
Freq: A-DEC, dtype: int64
"""

"""
y <- ts(z, start=2003, frequency=12)
"""
number_samples = 12
first_month = '01/2003'
period_range = pd.period_range(str(first_month),
                   periods=number_samples, freq='M')
yy = pd.Series(np.random.randint(0, 200, size=(number_samples,)),
               index=period_range)
print(yy)
"""
2003-01     21
2003-02     81
2003-03     30
2003-04     26
2003-05     88
2003-06    193
2003-07     20
2003-08    101
2003-09    117
2003-10     24
2003-11     86
2003-12    173
Freq: M, dtype: int32
"""