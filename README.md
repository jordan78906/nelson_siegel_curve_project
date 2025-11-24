# Bond Yield Curve using Nelson Siegel Svensson Formula

A Python application that visualizes the bond yield curve using the Nelson Siegel Svensson (NSS) model. Using the NSS formula, the app calculates bond yield curve based on user-adjustable parameters. The user-friendly Streamlit interface allows for easy adjustments to model parameters.

## Live Demo on Streamlit
[Access the application on Streamlit](https://nngproject.streamlit.app/)

<img width="1170" height="908" alt="image" src="https://github.com/user-attachments/assets/bf52634e-1c02-4432-8266-2838a7847166" />

## Features
- **Nelson Siegel Svensson Formula**:
$`(t) = \beta_0 + \beta_1 \left( \frac{1 - e^{ \text{-} \lambda t} }{ \lambda t } \right) + \beta_2 \left( \frac{1 - e^{ \text{-} \lambda t}}{ \lambda t} - e^{\text{-} \lambda t} \right) + \beta_3 \left( \frac{ 1 - e^{\text{-} \mu t} }{ \mu t } - e^{ \text{-} \mu t} \right) `$
- **Interactive 2D Nelson Siegel Svensson Graph**:
  - Real-time 2D plot of the NSS yield curve.
  - Visualizes yield (%) across time to maturity.
  - Parameters can be adjusted via up/down buttons or direct input.
- **CSV Input Support**: The app can ingest a CSV data file.
- **Adjustable $`\beta_0`$**: Long-term level of rates.
- **Adjustable $`\beta_1`$**: Short-term slope (controls whether the curve starts inverted or normal).
- **Adjustable $`\beta_2`$**: Curvature parameter controlling the medium-term “hump.”
- **Adjustable $`\beta_3`$**: Additional curvature parameter for a second hump at longer maturities.
- **Adjustable $`\lambda`$**: Decay factor for β₁ and β₂ (controls how fast the hump occurs).
- **Adjustable $`\mu`$**: Decay factor for β₃ (controls the long-horizon hump).
- **Adjustable $`t`$**: Time to maturity.
- **User-Friendly Design**: Built with Streamlit for an accessible and responsive interface.

## Libraries Used
- **Streamlit**: Frontend interface for web-based interaction.
- **NumPy**: Numerical computations and array handling.
- **Pandas**: Data management and manipulation.
- **SciPy**: Root-finding and normal distribution functions for calculating implied volatility.
- **Plotly**: 3D plotting and visualization of the implied volatility surface.
