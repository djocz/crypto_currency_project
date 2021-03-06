# %load q03_lag_plots/build.py
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
from pandas.plotting import lag_plot, autocorrelation_plot
from sklearn.model_selection import train_test_split
plt.switch_backend('agg')

def q03_lag_plots(path, n_lags):
    df = pd.read_csv(path,index_col=['Date']).iloc[:,1:]
    plt.figure(figsize=(20,10))
    for i in range(1,len(df.columns.values)+1):
        plt.subplot(2,4,i)
        pd.plotting.lag_plot(df.iloc[:,i-1],lag=n_lags)
