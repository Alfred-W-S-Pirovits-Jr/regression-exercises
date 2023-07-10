from env import get_db_url
import numpy as np
import pandas as pd
import os
import acquire
import prepare
import wrangle
import matplotlib.pyplot as plt
from scipy import stats
import sklearn.preprocessing
from sklearn.model_selection import train_test_split
import pandas as pd
import seaborn as sns



def plot_variable_pairs(df, sample_size=10000):
    
    if sample_size < len(df):
        df_sample = df.sample(n=sample_size, random_state=823)
    else:
        df_sample = df

    
    for col in df.columns:
        for col2 in df.columns:
            if col == col2:
                continue
            else:
                sns.lmplot(x=col, y=col2, data=df_sample, line_kws={'color': 'red'})
                plt.show()
            

            
def plot_categorical_and_continuous_vars(df, discrete_list, continuous_list, sample_size=10000):# lists of discrete and continuous columns:
    if sample_size < len(df):
        df_sample = df.sample(n=sample_size, random_state=823)
    else:
        df_sample = df
    
    for discrete_col in discrete_list:
        for continuous_col in continuous_list:
            
            plt.figure(figsize=(11,6))
            
            plt.subplot(131)
            sns.boxplot(x=discrete_col, y=continuous_col, data=df_sample)
            plt.subplot(132)
            sns.violinplot(x=discrete_col, y=continuous_col, data=df_sample)
            plt.subplot(133)
            sns.barplot(x=discrete_col, y=continuous_col, data=df_sample)