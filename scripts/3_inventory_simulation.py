import numpy as np
import pandas as pd
from statsmodels.tsa.holtwinters import ExponentialSmoothing

# -----------------------------
# 1. Load demand
# -----------------------------
data = pd.read_csv("data/demand_history.csv")["demand"].values
T = len(data)

# -----------------------------
# 2. ETS fitted values function
# -----------------------------
def ets_fitted(series):
    model = ExponentialSmoothing(
        series,
        trend="add",
        seasonal="add",
        seasonal_periods=12
    )
    fit = model.fit(optimized=True)
    return fit.fittedvalues

# -----------------------------
# 3. Compute fitted values and forecast error
# -----------------------------
fitted_values = ets_fitted(data)
residuals = data - fitted_values
sigma = np.std(residuals)

# -----------------------------
# 4. Inventory simulation parameters
# -----------------------------
h = 1
p = 5
z = 1.28
initial_inventory = 50

# -----------------------------
# 5. Initialize simulation
# -----------------------------
I = initial_inventory
inventory_levels = []
orders = []
holding_costs = []
shortage_costs = []

for t in range(T):
    S_t = fitted_values[t] + z * sigma
    Q_t = max(0, S_t - I)
    I = I + Q_t - data[t]

    inventory_levels.append(I)
    orders.append(Q_t)
    holding_costs.append(h * max(I, 0))
    shortage_costs.append(p * max(-I, 0))

# -----------------------------
# 6. Compute total cost and service level
# -----------------------------
total_cost = sum(holding_costs) + sum(shortage_costs)
service_achieved = sum([1 if i>=0 else 0 for i in inventory_levels]) / T

# -----------------------------
# 7. Print results
# -----------------------------
print("Simulation Results:")
print(f"Total cost: {total_cost:.2f}")
print(f"Service level achieved: {service_achieved*100:.1f}%")
