# Figures and Operational Analysis

This document provides an analytical interpretation of all figures generated in the project, emphasizing operational insights rather than descriptive statistics.

---

## Figure 1: Inventory Simulation Comparison (Summary Table)

This table compares forecasting models across total cost, service level, average inventory, and average shortage.

Exponential Smoothing (ETS) achieves the lowest total cost, reflecting an efficient balance between holding and shortage costs. ARIMA attains the highest service level but does so with the highest average inventory and shortage, indicating operational inefficiency rather than superiority.

**Operational insight:**  
High service levels achieved through excessive inventory volatility are not operationally desirable. Cost efficiency and stability must be evaluated jointly.

---

## Figure 2: Sensitivity Analysis – Total Cost under Different Safety Stock and Shortage Cost Parameters

The sensitivity heatmaps reveal that ETS maintains cost robustness across varying service-level targets and shortage cost scenarios. ARIMA’s cost escalates rapidly as safety stock or shortage penalties increase, highlighting its sensitivity to uncertainty.

**Operational insight:**  
Robust forecasting models should perform consistently across parameter changes, not only under calibrated conditions.

---

## Figure 3: Inventory Levels Over Time by Forecast Model

This figure illustrates the dynamic evolution of inventory levels.

ETS exhibits the most stable inventory trajectory, avoiding extreme peaks and deep stockouts. ARIMA shows pronounced oscillations, frequently switching between surplus and shortage, indicating unstable forecast signals being amplified by the inventory policy.

Naïve and Moving Average models demonstrate moderate fluctuations but exhibit delayed responsiveness to demand changes.

**Operational insight:**  
Inventory stability is a critical determinant of operational robustness, working-capital control, and service reliability.

---

## Figure 4: Orders Placed Over Time by Forecast Model

This figure compares replenishment order quantities over time.

ARIMA induces large and frequent order spikes, increasing coordination costs and supplier strain. ETS generates smoother and more predictable order patterns, aligning better with capacity and procurement constraints.

**Operational insight:**  
Forecast-driven order volatility directly impacts supply chain coordination and execution risk.

---

## Figure 5: Average Inventory and Average Shortage by Forecast Model

This comparison highlights structural differences in how forecasting models manage risk.

ETS maintains low average inventory while keeping shortages at acceptable levels. ARIMA simultaneously exhibits high inventory and high shortage, signaling inefficiency rather than robustness.

---

## Integrated Results and Managerial Conclusions

Across all evaluated dimensions — cost efficiency, service reliability, inventory stability, and order smoothness — **Exponential Smoothing emerges as the most operationally robust forecasting model**.

While ARIMA achieves high service levels, it does so through unstable and costly operational behavior, making it unsuitable for most practical inventory systems.

**Managerial recommendation:**
- Use ETS for cost-efficient, stable, and scalable operations.
- Avoid complex models that amplify volatility unless service levels are mission-critical and operational costs are secondary.
- Evaluate forecasting models based on their downstream operational consequences, not accuracy metrics alone.
