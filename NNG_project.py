import numpy as np
import pandas as pd
#import math 
#import streamlit as st      Implement at end


def nelson_siege_formula (B_0, B_1, B_2, L, T):
    # B_0   level =  
    # B_1   slope = 
    # B_2   shape = 
    # L     lambda= 
    # T     time  = Maturity
    yield_pct = B_0 + B_1((1 - np.exp(-L * T))/ L * T) + B_2((1 - np.exp(-L * T))/(L * T) - np.exp(-L * T))
    T_nsf = T
    return yield_pct, T_nsf


def money(maturity, cupon, yield_pct, price, T_nsf): 
    value = 100/((1 + yield_pct ) ** maturity) + (cupon/T_nsf)
    return value

#Hard coded values for now
B_0 = 0.0000
B_1 = 0.0000
B_2 = 0.0000
L   = 0.0000
T   = 0

dict_yield = {}
for i in range (1, 31):
    dict_yield [i] = 0.0000



#for v in range (1, 31):
#    print (f"{v}      {dict_yield[v]}")

print(np.__version__)