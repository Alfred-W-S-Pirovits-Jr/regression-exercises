import numpy as np
import pandas as pd
import os
from env import get_db_url

def wrangle_zillow():
    zillow = acquire.get_zillow_data()
    zillow = zillow.dropna()