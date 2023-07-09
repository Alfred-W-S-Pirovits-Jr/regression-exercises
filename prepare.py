from env import get_db_url
import numpy as np
import pandas as pd
import os
import acquire
import matplotlib.pyplot as plt
from scipy import stats
import sklearn.preprocessing
from sklearn.model_selection import train_test_split
import pandas as pd


def scale_zillow():
    # Split the Data
    train_validate, test = train_test_split(zillow, test_size = .2, random_state=823)
    train, validate = train_test_split(train_validate, test_size= .25, random_state=823)
    
    #Set the Scaler
    scaler = sklearn.preprocessing.MinMaxScaler()
    # Note that we only call .fit with the training data,
    # but we use .transform to apply the scaling to all the data splits.
    scaler.fit(train)

    # Turn all the sets inot the scaled np data array
    train_scaled = scaler.transform(train)
    validate_scaled = scaler.transform(validate)
    test_scaled = scaler.transform(test)
    
    # Create a dictionary so that I can take the np arrays back to a labelled pd DataFrame
    columns = train.columns #List of Columns
    numbers = [0,1,2,3,4,5,6] #List of numbers for the scaled np array I'm converting into a dataframe
    zipped= dict(zip(numbers, columns))

    
    #turn the Train Validate and Test arrays back into labelled DataFrames
    train_scaled = pd.DataFrame(train_scaled).rename(columns=zipped)
    validate_scaled = pd.DataFrame(validate_scaled).rename(columns=zipped)
    test_scaled = pd.DataFrame(test_scaled).rename(columns=zipped)
    
    #Return the three scaled DataFrames
    return train_scaled, validate_scaled, test_scaled