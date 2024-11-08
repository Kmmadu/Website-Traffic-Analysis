import matplotlib.pyplot as plt
import seaborn as sns

# Setting up a general style for the plots
sns.set(style="whitegrid")

# Time Series Plot
plt.figure(figsize=(12, 6))
plt.plot(traffic_data_cleaned['Date'], traffic_data_cleaned['Visits'], color='blue', linewidth=1.5)
plt.title('Daily Website Traffic Over Time')
plt.xlabel('Date')
plt.ylabel('Visits')
plt.show()

# Moving Average Plot (7-day moving average)
traffic_data_cleaned['7-Day MA'] = traffic_data_cleaned['Visits'].rolling(window=7).mean()
plt.figure(figsize=(12, 6))
plt.plot(traffic_data_cleaned['Date'], traffic_data_cleaned['Visits'], color='blue', label='Daily Visits')
plt.plot(traffic_data_cleaned['Date'], traffic_data_cleaned['7-Day MA'], color='red', label='7-Day Moving Average')
plt.title('Website Traffic with 7-Day Moving Average')
plt.xlabel('Date')
plt.ylabel('Visits')
plt.legend()
plt.show()

# Histogram
plt.figure(figsize=(10, 6))
sns.histplot(traffic_data_cleaned['Visits'], bins=20, color='purple')
plt.title('Distribution of Daily Visits')
plt.xlabel('Number of Visits')
plt.ylabel('Frequency')
plt.show()
