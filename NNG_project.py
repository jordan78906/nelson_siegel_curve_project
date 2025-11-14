import numpy as np
import pandas as pd
from scipy import stats

import seaborn as sns
import plotly.express as px
import matplotlib.pyplot as plt


#import math 
#import streamlit as st      Implement at end


def nelson_siege_formula (B_0, B_1, B_2, L, T):
    # B_0   level =  
    # B_1   slope = 
    # B_2   shape = 
    # L     lambda= 
    # T     time  = Maturity
    yield_pct = B_0 + B_1((1 - np.exp(-L * T))/ L * T) + B_2((1 - np.exp(-L * T))/(L * T) - np.exp(-L * T))
    return yield_pct, T


def buy_price(maturity, cupon, yield_pct, price, T): 
    value = 100/((1 + yield_pct ) ** maturity) + (cupon/T)
    return value

#Hard coded values for now
B_0 = 0.0000
B_1 = 0.0000
B_2 = 0.0000
L   = 0.0000
T   = 30
T_bond   = 10
###########################

test_raw = pd.read_csv('./nelson_siegel_curve_project/Test_data.csv')

print (f'\nShape:{test_raw.shape}\n')
print (test_raw.head(10))

#dict_yield = {}
#for i in range (1, 31):
#    dict_yield [i] = 0.0000

#print (data_df)

#for v in range (1, 31):
#    print (f"{v}      {dict_yield[v]}")

print(np.__version__)