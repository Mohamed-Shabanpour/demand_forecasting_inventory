import os
import numpy as np
import pandas as pd
from statsmodels.tsa.holtwinters import ExponentialSmoothing
from statsmodels.tsa.arima.model import ARIMA
from tabulate import tabulate

# -----------------------------
# 0. Ensure data and figures folders exist
# -----------------------------
os.makedirs("data", exist_ok=True)
os.makedirs("figures", exist_ok=True)

# -----------------------------
# 1. Set random seed and parameters
# -----------------------------
np.random.seed(42)
T = 36
mu = 100
beta = 0.5
A = 15
season_length = 12
sigma = 10

# -----------------------------
# 2. Generate synthetic demand
# -----------------------------
t = np.arange(1, T + 1)
seasonality = A * np.sin(2 * np.pi * t / season_length)
noise = np.random.normal(0, sigma, T)
demand = np.maximum(mu + beta * t + seasonality + noise, 0)

# -----------------------------
# 3. Save demand to CSV
# -----------------------------
demand_df = pd.DataFrame({"period": t, "demand": demand})
demand_df.to_csv("data/demand_history.csv", index=False)

# -----------------------------
# 4. Load demand
# -----------------------------
data = pd.read_csv("data/demand_history.csv")["demand"].values

# -----------------------------
# 5. Forecasting models
# -----------------------------
def naive_forecast(history):
    return history[-1]

def moving_average_forecast(history, window=3):
    if len(history) < window:
        return np.mean(history)
    return np.mean(history[-window:])

def ets_fitted(series):
    model = ExponentialSmoothing(series, trend="add", seasonal="add", seasonal_periods=12)
    fit = model.fit(optimized=True)
    return fit.fittedvalues

def arima_fitted(series):
    model = ARIMA(series, order=(1,1,1))
    fit = model.fit()
    return fit.fittedvalues

def rolling_forecast_out_of_sample(series, model_func, **kwargs):
    forecasts = []
    for t in range(len(series)):
        if t == 0:
            forecasts.append(series[0])
        else:
            history = series[:t]
            forecasts.append(model_func(history, **kwargs) if kwargs else model_func(history))
    return np.array(forecasts)

# -----------------------------
# 6. Inventory simulation function
# -----------------------------
def simulate_inventory(forecast_series, demand, h=1, p=5, z=1.28, initial_inventory=50):
    T = len(demand)
    residuals = demand - forecast_series
    sigma = np.std(residuals)

    I = initial_inventory
    inventory_levels = []
    orders = []
    holding_costs = []
    shortage_costs = []

    for t in range(T):
        S_t = forecast_series[t] + z * sigma
        Q_t = max(0, S_t - I)
        I = I + Q_t - demand[t]

        inventory_levels.append(I)
        orders.append(Q_t)
        holding_costs.append(h * max(I,0))
        shortage_costs.append(p * max(-I,0))

    total_cost = sum(holding_costs) + sum(shortage_costs)
    service_level = sum([1 if i>=0 else 0 for i in inventory_levels]) / T
    avg_inventory = np.mean([max(0,i) for i in inventory_levels])
    avg_shortage = np.mean([max(0,-i) for i in inventory_levels])

    return total_cost, service_level, inventory_levels, orders, avg_inventory, avg_shortage

# -----------------------------
# 7. Generate forecasts & simulate inventory
# -----------------------------
forecast_models = {
    "Naive": lambda s: rolling_forecast_out_of_sample(s, naive_forecast),
    "Moving Average": lambda s: rolling_forecast_out_of_sample(s, moving_average_forecast, window=3),
    "ETS": ets_fitted,
    "ARIMA": arima_fitted
}

results_summary = {}
for name, func in forecast_models.items():
    forecast_series = func(data)
    total_cost, service_level, inventory_levels, orders, avg_inventory, avg_shortage = simulate_inventory(forecast_series, data)
    results_summary[name] = {
        "Total Cost": total_cost,
        "Service Level": service_level*100,
        "Inventory Levels": inventory_levels,
        "Orders": orders,
        "Average Inventory": avg_inventory,
        "Average Shortage": avg_shortage
    }

# -----------------------------
# 8. Main comparison table
# -----------------------------
comparison_df_clean = pd.DataFrame({
    "Forecast Model": list(results_summary.keys()),
    "Total Cost": [results_summary[m]["Total Cost"] for m in results_summary],
    "Service Level (%)": [results_summary[m]["Service Level"] for m in results_summary],
    "Average Inventory": [results_summary[m]["Average Inventory"] for m in results_summary],
    "Average Shortage": [results_summary[m]["Average Shortage"] for m in results_summary]
}).round(2)

comparison_df_clean["Best Cost"] = ""
comparison_df_clean.loc[comparison_df_clean["Total Cost"].idxmin(), "Best Cost"] = "✅"
comparison_df_clean["Best Service"] = ""
comparison_df_clean.loc[comparison_df_clean["Service Level (%)"].idxmax(), "Best Service"] = "✅"

comparison_df_clean = comparison_df_clean[[
    "Forecast Model", "Total Cost", "Best Cost",
    "Service Level (%)", "Best Service",
    "Average Inventory", "Average Shortage"
]]

print("\nInventory Simulation Comparison (Single Table):\n")
print(tabulate(comparison_df_clean, headers='keys', tablefmt='fancy_grid', showindex=False))

# -----------------------------
# 9. Sensitivity Analysis
# -----------------------------
z_values = [1.0, 1.28, 1.65]       # 84%, 90%, 95% service levels
p_values = [2, 5, 10]              # shortage cost variations
sensitivity_results = []

for z_val in z_values:
    for p_val in p_values:
        for name, func in forecast_models.items():
            forecast_series = func(data)
            total_cost, service_level, _, _, avg_inventory, avg_shortage = simulate_inventory(
                forecast_series, data, h=1, p=p_val, z=z_val, initial_inventory=50
            )
            sensitivity_results.append({
                "Forecast Model": name,
                "Safety Stock (z)": z_val,
                "Shortage Cost (p)": p_val,
                "Total Cost": round(total_cost,2),
                "Service Level (%)": round(service_level*100,2),
                "Average Inventory": round(avg_inventory,2),
                "Average Shortage": round(avg_shortage,2)
            })

sensitivity_df = pd.DataFrame(sensitivity_results)
print("\nSensitivity Analysis: Inventory Performance under Different z and p Values\n")
print(tabulate(sensitivity_df, headers='keys', tablefmt='fancy_grid', showindex=False))

# -----------------------------
# 10. Save results for plotting
# -----------------------------
results_summary_file = "data/results_summary.pkl"
sensitivity_df_file = "data/sensitivity_df.pkl"
os.makedirs("data", exist_ok=True)

import pickle
with open(results_summary_file, "wb") as f:
    pickle.dump(results_summary, f)

with open(sensitivity_df_file, "wb") as f:
    pickle.dump(sensitivity_df, f)

print("\nResults saved to 'data/' folder. You can now run generate_figures.py to save all plots.")
