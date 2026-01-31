import os
import pickle
import matplotlib.pyplot as plt
import seaborn as sns
import numpy as np

# -----------------------------
# 0. Load data
# -----------------------------
with open("data/results_summary.pkl", "rb") as f:
    results_summary = pickle.load(f)

with open("data/sensitivity_df.pkl", "rb") as f:
    sensitivity_df = pickle.load(f)

# -----------------------------
# 1. Ensure figures folder exists
# -----------------------------
os.makedirs("figures", exist_ok=True)

# -----------------------------
# 2. Sensitivity Heatmaps
# -----------------------------
for name in results_summary.keys():
    model_df = sensitivity_df[sensitivity_df["Forecast Model"] == name]
    heatmap_data = model_df.pivot(index="Shortage Cost (p)", columns="Safety Stock (z)", values="Total Cost")
    
    plt.figure(figsize=(6,4))
    sns.heatmap(heatmap_data, annot=True, fmt=".0f", cmap="YlGnBu", cbar_kws={'label': 'Total Cost'})
    plt.title(f"Total Cost Sensitivity Heatmap - {name}")
    plt.xlabel("Safety Stock Factor (z)")
    plt.ylabel("Shortage Cost (p)")
    
    plt.savefig(f"figures/heatmap_total_cost_{name}.png", dpi=300, bbox_inches='tight')
    plt.close()

# -----------------------------
# 3. Inventory Levels
# -----------------------------
plt.figure(figsize=(12,6))
for name in results_summary:
    plt.plot(results_summary[name]["Inventory Levels"], label=name)
plt.xlabel("Period")
plt.ylabel("Inventory Level")
plt.title("Inventory Levels Over Time by Forecast Model")
plt.legend()
plt.grid(True)
plt.savefig("figures/inventory_levels.png", dpi=300, bbox_inches='tight')
plt.close()

# -----------------------------
# 4. Orders Placed
# -----------------------------
plt.figure(figsize=(12,6))
for name in results_summary:
    plt.plot(results_summary[name]["Orders"], label=name)
plt.xlabel("Period")
plt.ylabel("Order Quantity")
plt.title("Orders Placed Over Time by Forecast Model")
plt.legend()
plt.grid(True)
plt.savefig("figures/orders_placed.png", dpi=300, bbox_inches='tight')
plt.close()

# -----------------------------
# 5. Average Inventory & Shortage
# -----------------------------
plt.figure(figsize=(10,5))
x = np.arange(len(results_summary))
avg_inventory = [results_summary[m]["Average Inventory"] for m in results_summary]
avg_shortage = [results_summary[m]["Average Shortage"] for m in results_summary]

plt.bar(x-0.15, avg_inventory, width=0.3, label="Average Inventory")
plt.bar(x+0.15, avg_shortage, width=0.3, label="Average Shortage")
plt.xticks(x, list(results_summary.keys()))
plt.ylabel("Units")
plt.title("Average Inventory and Shortage by Forecast Model")
plt.legend()
plt.grid(axis="y")
plt.savefig("figures/avg_inventory_shortage.png", dpi=300, bbox_inches='tight')
plt.close()

print("All figures saved in 'figures/' folder.")
