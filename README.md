# demand_forecasting_inventory
Demand forecasting and inventory optimization under forecast uncertainty

## Overview
This project integrates demand forecasting and inventory control to study how forecast accuracy affects inventory performance, service levels, and cost trade-offs under uncertainty.  
It combines classical time-series forecasting models with a base-stock inventory policy and evaluates their impact on operational performance.

---

## Problem Description
A single-item inventory system is considered with stochastic demand exhibiting:
- Trend
- Seasonality
- Random noise

The decision problem involves determining replenishment quantities over time while balancing:
- Holding costs
- Shortage costs
- Service level requirements

---

## Forecasting Models
The following forecasting approaches are evaluated:
- Naïve forecasting
- Moving average
- Exponential smoothing (ETS)
- ARIMA

Forecast accuracy is assessed using rolling-origin evaluation metrics such as MAE, RMSE, and MAPE.

---

## Inventory Control Policy
A base-stock (order-up-to) policy is implemented where safety stock is computed using forecast error variance and service-level targets.  

Inventory performance is evaluated based on:
- Total cost
- Achieved service level
- Average inventory
- Average shortage

---

## Sensitivity Analysis
Sensitivity analysis is conducted with respect to:
- Safety stock factor (z)
- Shortage cost parameters
- Forecast model choice

Heatmaps and comparative plots illustrate the interaction between forecasting accuracy and inventory outcomes.

---

## Key Insights
- Improved forecast accuracy reduces inventory costs and service-level volatility.
- The value of forecast improvements exhibits diminishing returns.
- Safety stock decisions are highly sensitive to forecast error estimation.
- Forecast model choice significantly affects downstream operational performance.

---

## Tools & Technologies
- Python
- Statsmodels
- NumPy, Pandas
- Matplotlib, Seaborn

---

## Author
[Mohamed_Shabanpour]
