import sklearn.cluster
import scipy.cluster
import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
import pickle
import numpy as np
import scipy.stats as stats
import seaborn as sns
from IPython.display import display
from itertools import combinations
from sklearn.decomposition import PCA
from sklearn.linear_model import Ridge, Lasso
from sklearn.preprocessing import StandardScaler, RobustScaler, MinMaxScaler, PolynomialFeatures
from sklearn.model_selection import train_test_split
from sklearn.feature_selection import SelectKBest, SelectFromModel, RFE, SelectPercentile
from sklearn.datasets import make_classification, make_blobs
from sklearn.naive_bayes import GaussianNB
from sklearn.pipeline import Pipeline
from sklearn.linear_model import LogisticRegression
from ipywidgets import * 
from tqdm import tqdm

get_ipython().magic('matplotlib inline')

import warnings
warnings.filterwarnings("ignore")




