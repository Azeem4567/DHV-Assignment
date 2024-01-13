import matplotlib.pyplot as plt
import seaborn as sns
import pandas as pd
import numpy as np

# Load the datasets
monthly_wages_2020_path = 'Country_Gross Average Monthly Wages in 2020.csv'
annual_wages_path = 'Development of average annual wages.csv'

monthly_wages_2020_df = pd.read_csv(monthly_wages_2020_path)
annual_wages_df = pd.read_csv(annual_wages_path)

# Data cleaning
monthly_wages_2020_df['Gross Average Monthly Wages in 2020 (US$, at current Exchange Rates)[4]'] = (
    monthly_wages_2020_df['Gross Average Monthly Wages in 2020 (US$, at current Exchange Rates)[4]']
    .str.replace(' USD', '').str.replace(',', '').astype(float)
)
annual_wages_df[['2020', '2022']] = annual_wages_df[['2020', '2022']].apply(pd.to_numeric, errors='coerce')

# Preparing data for visualizations

# 1. Top 10 Countries by Average Monthly Wages in 2020
top_10_wages_2020 = monthly_wages_2020_df.sort_values(by='Gross Average Monthly Wages in 2020 (US$, at current Exchange Rates)[4]', ascending=False).head(10)

# 2. Comparison of Average Wages in 2020 and 2022 for Selected Countries
selected_countries = ['United States', 'United Kingdom', 'Germany', 'Japan', 'China']
wages_comparison = annual_wages_df[annual_wages_df['Country'].isin(selected_countries)][['Country', '2020', '2022']]

# 3. Distribution of Average Monthly Wages in 2020 Across Countries
# Using the entire dataset for distribution

# 4. Average Annual Wages in 2020 vs 2022 for All Countries
# Using the entire dataset for comparison

# Creating the dashboard-style plot
plt.figure(figsize=(18, 12))
plt.suptitle("Wage Analysis Dashboard - Muhammad Azeem 22095075", fontsize=16)

# Subplot 1: Top 10 Countries by Average Monthly Wages in 2020
plt.subplot(2, 2, 1)
sns.barplot(x='Gross Average Monthly Wages in 2020 (US$, at current Exchange Rates)[4]', y='Country', data=top_10_wages_2020, palette='coolwarm')
plt.title("Top 10 Countries by Average Monthly Wages in 2020")
plt.xlabel("Average Monthly Wage (USD)")
plt.ylabel("Country")

# Subplot 2: Comparison of Average Wages in 2020 and 2022
plt.subplot(2, 2, 2)
wages_comparison_melted = wages_comparison.melt(id_vars=['Country'], var_name='Year', value_name='Average Wages')
sns.barplot(x='Country', y='Average Wages', hue='Year', data=wages_comparison_melted, palette='Set2')
plt.title("Average Wages Comparison: 2020 vs 2022")
plt.xlabel("Country")
plt.ylabel("Average Wages (USD)")

# Subplot 3: Distribution of Average Monthly Wages in 2020 Across Countries
plt.subplot(2, 2, 3)
sns.histplot(monthly_wages_2020_df['Gross Average Monthly Wages in 2020 (US$, at current Exchange Rates)[4]'], kde=True, color='green')
plt.title("Distribution of Average Monthly Wages in 2020")
plt.xlabel("Average Monthly Wage (USD)")
plt.ylabel("Number of Countries")

# Subplot 4: Average Annual Wages in 2020 vs 2022 for All Countries
plt.subplot(2, 2, 4)
sns.scatterplot(x='2020', y='2022', data=annual_wages_df, color='orange')
plt.title("Average Annual Wages: 2020 vs 2022")
plt.xlabel("2020 Wages (USD)")
plt.ylabel("2022 Wages (USD)")

# Save the plot
plt.savefig('Wage_Analysis_Dashboard_Muhammad_Azeem.png')

# Informing that the plot has been saved
print("Dashboard saved as 'Wage_Analysis_Dashboard_Muhammad_Azeem.png' in the current directory.")
