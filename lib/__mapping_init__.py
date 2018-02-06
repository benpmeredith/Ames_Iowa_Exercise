import matplotlib.pyplot as plt
import matplotlib.cm
 
import pandas as pd
import geopandas as gpd
import numpy as np
from geopandas.tools import sjoin
import folium
from folium.plugins import MarkerCluster
from folium.element import IFrame
import shapely
from shapely.geometry import Point
import unicodedata
import pysal as ps

print('GeoPandas and Folium mapping modules initiated')
print('Please initiate "%matplotlib inline".')
