import os
import numpy as np
import pandas as pd

# -----------------------------
# 1. Set random seed
# -----------------------------
np.random.seed(42)

# -----------------------------
# 2. Define parameters
# -----------------------------
T = 36
mu = 100
beta = 0.5
A = 15
season_length = 12
sigma = 10

# -----------------------------
# 3. Generate demand
# -----------------------------
t = np.arange(1, T + 1)
seasonality = A * np.sin(2 * np.pi * t / season_length)
noise = np.random.normal(0, sigma, T)

demand = mu + beta * t + seasonality + noise
demand = np.maximum(demand, 0)

# -----------------------------
# 4. Create DataFrame
# -----------------------------
demand_df = pd.DataFrame({
    "period": t,
    "demand": demand
})

# -----------------------------
# 5. Ensure data directory exists
# -----------------------------
os.makedirs("data", exist_ok=True)

# -----------------------------
# 6. Save to CSV
# -----------------------------
demand_df.to_csv("data/demand_history.csv", index=False)

print(demand_df.head())
