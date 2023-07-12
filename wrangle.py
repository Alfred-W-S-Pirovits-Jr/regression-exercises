import numpy as np
import pandas as pd
import os
from env import get_db_url
import acquire

def wrangle_zillow():
    zillow = acquire.get_zillow_data()
    zillow = zillow.dropna()
    zillow = zillow.rename(columns = {'bedroomcnt': 'bedrooms',
                                 'bathroomcnt': 'bathrooms',
                                 'calculatedfinishedsquarefeet': 'sqft',
                                 'taxvaluedollarcnt': 'tax_value',
                                 'yearbuilt': 'year_built',
                                 'taxamount': 'tax_amount'})
    zillow.drop_duplicates(inplace=True)
    return zillow

def wrangle_zillow_predictions():
    zillow = acquire.get_zillow_predictions()
    zillow = zillow.dropna()
    zillow = zillow.rename(columns = {'bedroomcnt': 'bedrooms',
                                 'bathroomcnt': 'bathrooms',
                                 'calculatedfinishedsquarefeet': 'sqft',
                                 'taxvaluedollarcnt': 'tax_value',
                                 'yearbuilt': 'year_built',
                                 'taxamount': 'tax_amount'})
    zillow.drop_duplicates(inplace=True)
    return zillow