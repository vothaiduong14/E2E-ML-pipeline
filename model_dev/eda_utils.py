# helper functions for EDA
import pandas as pd 
import numpy as np
import matplotlib.pyplot as plt
import seaborn as sns
from sklearn.ensemble import IsolationForest

def load_data(file_name):
    """
    Load data from a file
    """
    return pd.read_csv(file_name)

def count_values(df, col_name):
    """
    Given a dataframe, show number and percentage of value count by each column
    """
    new_df = df[col_name].value_counts().rename_axis(col_name).reset_index(name='count')
    new_df['percentage'] = round(new_df['count'] / len(df) * 100, 2)
    return new_df

def count_nan(df):
    """
    Given a dataframe, show the number and percentage of NaN values by each column
    """
    new_df = df.isnull().sum().rename_axis('column').reset_index(name='count')
    new_df['percentage'] = round(new_df['count'] / len(df) * 100, 2)
    return new_df

def show_heatmap(data, figsize=(12,8), 
                 highest_only=False, 
                 thresold=0.7, # Look at only highly correlated pairs
                 annot=False):
    correlation_matrix = data.corr()
    high_corr = correlation_matrix[np.abs(correlation_matrix )>= thresold]
    plt.figure(figsize=figsize)

    if highest_only:
        sns.heatmap(high_corr, annot=annot, cmap="Greens", 
                    linecolor='black', linewidths=0.1)
    else:
        sns.heatmap(correlation_matrix, annot=annot)

def show_pairplot(data, 
                  highest_only=False, 
                  thresold=0.7 # Look at only highly correlated pairs
                  ): 
    correlation_matrix = data.corr()
    high_corr = correlation_matrix[np.abs(correlation_matrix )>= thresold]
    plt.figure()  

    if highest_only:
        sns.pairplot(data, hue='Response', palette='coolwarm',
                     vars=high_corr.columns)
    else:
        sns.pairplot(data, hue='Response', palette='coolwarm')

def check_outlier(data, col_names):
    """
    Given a dataframe, show the number and percentage of outliers by each column
    input:
        data: dataframe
        col_names: list of column names
    """
    clf = IsolationForest(n_estimators=100, max_samples=100, contamination=0.01, random_state=42)
    clf.fit(data[col_names].values)
    return clf.predict(data[col_names].values)
