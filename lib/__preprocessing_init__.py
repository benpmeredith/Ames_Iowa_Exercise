import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns
import tqdm
import warnings
warnings.filterwarnings('ignore')
from sklearn.preprocessing import StandardScaler
from sklearn.preprocessing import MinMaxScaler
from sklearn.preprocessing import RobustScaler
from sklearn.preprocessing import Normalizer
from sklearn.linear_model import LogisticRegression
from sklearn.linear_model import LinearRegression
from sklearn.feature_selection import SelectKBest, SelectFromModel, RFE, SelectPercentile
from sklearn.linear_model import Ridge, Lasso, ElasticNet
from sklearn.model_selection import train_test_split, StratifiedKFold, KFold
from IPython.display import display
import csv
from itertools import combinations


print('StandardScaler Initiated')
print('MinMaxscaler Initiated')
print('RobustScaler Initiated')
print('Normalizer Initiated')
print('Logistic Regression Initiated')
print('Linear Regression Initiated')
print('train_test_split Initiated')
print('SelectKBest Initiated')
print('SelectFromModel Initiated')
print('RFE Initiated')
print('SelectPercentile Initiated')
print('StratifiedKFold Initiated')
print('Ridge Regression Initiated')
print('Lasso Regression Initiated')
print('ElasticNet Initiated')
print('KFold Initiated')
print('Please initiate "%matplotlib inline"')
