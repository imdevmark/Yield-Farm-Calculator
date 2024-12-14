# Re-import necessary libraries
import pandas as pd

# Define the action table data
data = {
    "Input": [
        "Investment Amount", "DPR (%)", "WPR (%)", "Active TVL", "Weekly Rewards ($)",
        "Harvest Fee (%)", "Compound Fee (%)", "Rebalance Fee <=0.05%",
        "Rebalance Fee <=0.3%", "Rebalance Higher Fee", "Auto-Harvest Fee (%)",
        "Auto-Compound Fee (%)", "Auto-Rebalance Fee"
    ],
    "Value": [
        1000, 3.98, 27.89, 804241.08, 224331.08, 0.9, 0.9, 0.01, 0.03, 0.05, 1.2, 1.8, "Same as manual"
    ],
    "Output": [
        "Daily Yield", "Weekly Yield", "Monthly Yield (Compounded)",
        "Yearly Yield (Compounded)", "Proportion of Weekly Rewards", "Net Harvest Yield",
        "Net Compound Yield", "Rebalance <=0.05% Fee", "Rebalance <=0.3% Fee",
        "Rebalance Higher Fee", "Net Auto-Harvest Yield", "Net Auto-Compound Yield",
        "Auto-Rebalance Fee"
    ],
    "Formula": [
        "=B2 * (B3 / 100)", "=B2 * (B4 / 100)", "=B2 * ((1 + (B3 / 100))^30 - 1)",
        "=B2 * ((1 + (B3 / 100))^365 - 1)", "=B6 * (B2 / B5)", "=Yield * (1 - C2)",
        "=Yield * (1 - C3)", "=Position * C4", "=Position * C5", "=Position * C6",
        "=Yield * (1 - C7)", "=Yield * (1 - C8)", "Refer to corresponding manual formula."
    ]
}

# Convert to DataFrame
df = pd.DataFrame(data)

# Save to an Excel file
file_path = "/Users/skizzy/Downloads/Cryptocurrency_Yield_Calculator_2.xlsx"
df.to_excel(file_path, index=False)

file_path