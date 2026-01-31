import numpy as np
import pandas as pd
from statsmodels.tsa.holtwinters import ExponentialSmoothing
from statsmodels.tsa.arima.model import ARIMA

# -----------------------------
# 1. Load synthetic demand data
# -----------------------------
data = pd.read_csv("data/demand_history.csv")["demand"].values

# -----------------------------
# 2. Forecasting utility functions
# -----------------------------
def rolling_origin_forecast(data, forecast_func, start):
    forecasts = []
    actuals = []
    for t in range(start, len(data)):
        history = data[:t]
        forecast = forecast_func(history)
        forecasts.append(forecast)
        actuals.append(data[t])
    return np.array(forecasts), np.array(actuals)

def forecast_accuracy(forecasts, actuals):
    mae = np.mean(np.abs(actuals - forecasts))
    rmse = np.sqrt(np.mean((actuals - forecasts)**2))
    mape = np.mean(np.abs((actuals - forecasts)/actuals)) * 100
    return mae, rmse, mape

# -----------------------------
# 3. Forecasting models
# -----------------------------
def naive_forecast(history):
    return history[-1]

def moving_average_forecast(history, window=3):
    if len(history) < window:
        return np.mean(history)
    return np.mean(history[-window:])

def ets_forecast(history):
    model = ExponentialSmoothing(
        history,
        trend="add",
        seasonal="add",
        seasonal_periods=12
    )
    fit = model.fit(optimized=True)
    return fit.forecast(1)[0]

def arima_forecast(history):
    model = ARIMA(history, order=(1,1,1))
    fit = model.fit()
    return fit.forecast(1)[0]

# -----------------------------
# 4. Rolling-origin evaluation
# -----------------------------
start = len(data) - 12  # evaluate last 12 periods

models = {
    "Naive": naive_forecast,
    "Moving Average": moving_average_forecast,
    "ETS": ets_forecast,
    "ARIMA": arima_forecast
}

results = {}

for name, model in models.items():
    forecasts, actuals = rolling_origin_forecast(data, model, start)
    mae, rmse, mape = forecast_accuracy(forecasts, actuals)
    results[name] = {"MAE": mae, "RMSE": rmse, "MAPE": mape}

results_df = pd.DataFrame(results).T
print("Forecast Evaluation Table (last 12 periods):")
print(results_df)
