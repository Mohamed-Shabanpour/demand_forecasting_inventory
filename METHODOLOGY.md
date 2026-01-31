# Methodology

## Demand Generation
Synthetic demand data is generated to include trend, seasonality, and stochastic noise. This allows controlled experimentation under known data-generating processes.

## Forecasting
The following models are evaluated:
- Naïve benchmark
- Moving Average
- Exponential Smoothing (ETS)
- ARIMA

Forecast accuracy is assessed using rolling-origin evaluation with MAE, RMSE, and MAPE.

## Inventory Policy
A base-stock (order-up-to) policy is applied. Safety stock is calculated using the estimated standard deviation of forecast errors and a service-level factor.

## Simulation
Inventory dynamics are simulated over time, tracking:
- Inventory levels
- Order quantities
- Holding costs
- Shortage costs

## Sensitivity Analysis
The robustness of results is tested by varying:
- Safety stock factor (z)
- Shortage cost parameters
- Forecasting model choice
