# Data manipulation
import numpy as np
import pandas as pd
import scipy
from scipy import stats

# Visualization tools
import seaborn as sns
import plotly.express as px
import matplotlib.pyplot as plt

# Web App tool
import streamlit as st

st.title ('Nelson Siegel Svensson Model')


def nelson_siege_formula (B_0, B_1, B_2, B_3, L, mu, T):
    # B_0   level =  long term value (interest rates, ex: 5% = 0.050)
    # B_1   slope =  yield curve (0.01 = inverter curve/ -0.01 = normal curve)
    # B_2   shape =  max/min (hump) at a particular maturity
    # L     lambda=  decay, exponential decay, model flexible shape, later hump
    #yield_pct = B_0 + B_1((1 - np.exp(-L * T))/ L * T) + B_2((1 - np.exp(-L * T))/(L * T) - np.exp(-L * T))
    exp_input = ((-L) * T)
    mu_input = ((-mu) * T)
    yield_pct = B_0 + B_1 * ((1 - np.exp(exp_input))/(L * T)) + B_2 * ((1 - np.exp(exp_input))/(L * T) - np.exp(exp_input)) + B_3 * ((1 - np.exp(mu_input))/(mu * T) - np.exp(mu_input))
    #print (yield_pct)
    return yield_pct

def buy_price(maturity, cupon, yield_pct, price, T): 
    value = 100/((1 + yield_pct ) ** maturity) + (cupon/T)
    return value


###########################
#Hard coded values for now

T_bond   = 10
###########################

st.sidebar.header('Model Parameters')
st.sidebar.write('Adjust the parameters for the Nelson Siegel Svensson model.')

st.sidebar.write("--------------------")
st.sidebar.markdown("Created by Jordan Hernandez-Almache  |   [LinkedIn](https://www.linkedin.com/in/jordan-hernandez-almache/)")
st.sidebar.write("--------------------")


B_0 = st.sidebar.number_input(
    'B0 - Level (e.g., 0.015 for 1.5%)',
    value=0.050,
    format="%.4f"
)

B_1 = st.sidebar.number_input(
    'B1 - Slope (e.g., 0.013 for 1.3%)',
    value=0.013,
    format="%.4f"
)

B_2 = st.sidebar.number_input(
    'B2 - Shape (e.g., 0.015 for 1.5%)',
    value=0.050,
    format="%.4f"
)

B_3 = st.sidebar.number_input(
    'B3 - Shape (e.g., 0.013 for 1.3%)',
    value=0.013,
    format="%.4f"
)

L = st.sidebar.number_input(
    'Lambda - Decay (e.g., 0.015 for 1.5%)',
    value=0.050,
    format="%.4f"
)

mu = st.sidebar.number_input(
    'Mu - Decay (e.g., 0.013 for 1.3%)',
    value=0.013,
    format="%.4f"
)

T = st.sidebar.number_input(
    'Maturity (e.g., 1 for 1 year)',
    value=30,
    format="%d"
)

# Nelson Siegel Formula
# Graph: y-axis = yield | x-axis = maturity
x_values = []
y_values = []

for i in range (1, (T + 1)):
    x_values.append(nelson_siege_formula(B_0, B_1, B_2, B_3, L, mu, i))
    y_values.append(i)

fig , ax = plt.subplots()
ax.plot(y_values, x_values)
ax.set_xlabel('Maturity')
ax.set_ylabel('Yield')
ax.set_title('Yield Curve')

st.pyplot(fig)

st.title ('Price Data')
########################################################################################
# Upload File
uploaded_file = st.file_uploader("Upload your CSV file", type="csv")

#Check if file was uploaded
if uploaded_file is not None:
    try:
        test_raw = pd.read_csv(uploaded_file)
        # print (f'\nShape:{test_raw.shape}\n')
        st.write(test_raw.head(10))
        
        ### Price Curve
        # Seperating Column values into lists
        z_values = []
        maturity = test_raw.loc[:,'Maturity']
        coupon = test_raw.loc[:,'Coupon']
        price = test_raw.loc[:,'Price']

        # Iterating through column values to calculate Bond Value
        for v in range (0, T_bond):
            a = maturity[v]
            b = coupon[v]
            c = price[v]
            d = x_values[v]
            z_values.append(buy_price(a, b, d, c, v+1))

        # Bond Value Output
        st.title ('Bond Value')
        new_test = test_raw
        new_test['Value'] = z_values
        st.write(new_test.head(10))

    except Exception as e:
        st.error(f"Error loading CSV file: {e}")
else:
    st.info("Please upload a CSV file to begin.")

st.write("---")
st.markdown("Created by Jordan Hernandez-Almache  |   [LinkedIn](https://www.linkedin.com/in/jordan-hernandez-almache/)")
