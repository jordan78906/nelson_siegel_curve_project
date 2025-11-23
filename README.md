# Bond Yield Curve using Nelson Siegel Svensson Formula

A Python application that visualizes the bond yield curve using the nelson siegel svensson formula. Using nelson siegel svensson formula, the app calculates bond yield curve based on nelson siegel svensson inputs. The user-friendly Streamlit interface allows for easy adjustments to model parameters.

## Live Demo on Streamlit
[Access the application on Streamlit](https://nngproject.streamlit.app/)

<img width="1170" height="908" alt="image" src="https://github.com/user-attachments/assets/bf52634e-1c02-4432-8266-2838a7847166" />

## Features
- **Nelson Siegel Svensson Formula**:
$`(t) = \beta_0 + \beta_1 \left( \frac{1 - e^{ \text{-} \lambda t} }{ \lambda t } \right) + \beta_2 \left( \frac{1 - e^{ \text{-} \lambda t}}{ \lambda t} - e^{\text{-} \lambda t} \right) + \beta_3 \left( \frac{ 1 - e^{\text{-} \mu t} }{ \mu t } - e^{ \text{-} \mu t} \right) `$
- **Interactive 2D Nelson Siegel Svensson Graph**: View bond yield percentage over varying inputs and time to maturity.
- **Real-Time Data**: The app allows for csv input data file.
- **Adjustable $`\beta_0`$**: Long term value 
- **User-Friendly Design**: Built with Streamlit for an accessible and responsive interface.

## Libraries Used
- **Streamlit**: Frontend interface for web-based interaction.
- **NumPy**: Numerical computations and array handling.
- **Pandas**: Data management and manipulation.
- **SciPy**: Root-finding and normal distribution functions for calculating implied volatility.
- **Plotly**: 3D plotting and visualization of the implied volatility surface.
