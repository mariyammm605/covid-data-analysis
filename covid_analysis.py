# COVID-19 Data Analysis 
import pandas as pd
import matplotlib.pyplot as plt

# Load data (public dataset from GitHub)
url = "https://raw.githubusercontent.com/CSSEGISandData/COVID-19/master/csse_covid_19_data/csse_covid_19_time_series/time_series_covid19_confirmed_global.csv"
df = pd.read_csv(url)

# Process data
india_data = df[df['Country/Region'] == 'India'].iloc[:, 4:].sum()
dates = india_data.index
cases = india_data.values

# Create plot
plt.figure(figsize=(12,6))
plt.plot(dates[::30], cases[::30], 'r-')  # Show monthly data
plt.title('COVID-19 Cases in India (2020-2023)')
plt.xlabel('Date')
plt.ylabel('Confirmed Cases')
plt.xticks(rotation=45)
plt.tight_layout()
plt.savefig('covid_india.png')  
