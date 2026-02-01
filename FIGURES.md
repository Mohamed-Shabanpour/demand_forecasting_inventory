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

## Summary Insight
The figures collectively demonstrate that **forecast accuracy, service level, and inventory cost are structurally decoupled**. Optimal operational decisions arise from integrated forecast–inventory evaluation rather than isolated forecasting improvements.
