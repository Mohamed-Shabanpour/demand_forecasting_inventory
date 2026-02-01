# Figures and Results Interpretation

This document provides an operational interpretation of the figures generated in the project, focusing on inventory cost, service level, and shortage trade-offs.

---

## Figure 1: Forecast Accuracy Comparison

**Description**  
This figure compares MAE, RMSE, and MAPE across forecasting models using rolling-origin evaluation.

**Insights**
- ETS achieves the lowest MAE (10.21) and MAPE (8.97), indicating stable short-term performance.
- ARIMA performs competitively but does not dominate across all metrics.
- Naïve forecasting exhibits the highest forecast error across all measures.

**Operational Implication**  
Lower forecast error improves safety stock estimation but does not fully determine inventory efficiency.

---

## Figure 2: Inventory Cost Comparison Across Forecast Models

**Description**  
This bar chart compares total inventory cost under a base-stock policy for each forecasting model.

**Insights**
- ETS achieves the lowest total cost (471.89).
- ARIMA incurs the highest cost (1321.75) despite superior service performance.
- Moving Average outperforms Naïve forecasting but remains cost-dominated by ETS.

**Operational Interpretation**  
Cost efficiency arises from balanced forecast variance rather than maximum service protection.

---

## Figure 3: Service Level Comparison

**Description**  
Achieved service levels are compared across forecasting models.

**Insights**
- ARIMA achieves the highest service level (97.22%).
- ETS maintains a lower service level (86.11%) but remains economically efficient.
- Naïve and Moving Average methods cluster around 91.67%.

**Managerial Trade-off**  
Higher service levels require disproportionate inventory investment and may not be cost-optimal.

---

## Figure 4: Average Inventory and Average Shortage

**Description**  
This figure contrasts average on-hand inventory with average shortage levels.

**Insights**
- ARIMA holds the highest inventory (27.97 units) and also exhibits the highest average shortage (1.75).
- ETS maintains low inventory (9.46) with moderate shortage (0.73).
- Moving Average achieves the lowest shortage (0.31) among mid-cost policies.

**Key Observation**  
High service level does not eliminate shortages under stochastic demand; variability dominates outcomes.

---

## Figure 5: Sensitivity Analysis Heatmaps

**Description**  
Heatmaps illustrate total cost sensitivity to safety stock factor (z) and shortage cost (p).

**Insights**
- Total cost increases nonlinearly with z across all models.
- ETS remains cost-dominant across most parameter combinations.
- ARIMA is highly sensitive to safety stock inflation due to forecast variance.

**Strategic Implication**  
Forecast-informed safety stock decisions are critical leverage points in inventory optimization.

---

## Figure 6: Inventory Levels Over Time by Forecast Model

**Description** 
This figure illustrates the dynamic evolution of inventory levels.

ETS exhibits the most stable inventory trajectory, avoiding extreme peaks and deep stockouts. ARIMA shows pronounced oscillations, frequently switching between surplus and shortage, indicating unstable forecast signals being amplified by the inventory policy.

Naïve and Moving Average models demonstrate moderate fluctuations but exhibit delayed responsiveness to demand changes.

**Operational insight:**  
Inventory stability is a critical determinant of operational robustness, working-capital control, and service reliability.

---

## Figure 7: Orders Placed Over Time by Forecast Model

**Description** 
This figure compares replenishment order quantities over time.

ARIMA induces large and frequent order spikes, increasing coordination costs and supplier strain. ETS generates smoother and more predictable order patterns, aligning better with capacity and procurement constraints.

**Operational insight:**  
Forecast-driven order volatility directly impacts supply chain coordination and execution risk.

---

## Integrated Results and Managerial Conclusions

Across all evaluated dimensions — cost efficiency, service reliability, inventory stability, and order smoothness — **Exponential Smoothing emerges as the most operationally robust forecasting model**.

While ARIMA achieves high service levels, it does so through unstable and costly operational behavior, making it unsuitable for most practical inventory systems.

**Managerial recommendation:**
- Use ETS for cost-efficient, stable, and scalable operations.
- Avoid complex models that amplify volatility unless service levels are mission-critical and operational costs are secondary.
- Evaluate forecasting models based on their downstream operational consequences, not accuracy metrics alone.

