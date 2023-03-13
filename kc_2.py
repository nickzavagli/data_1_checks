import pandas as pd
import seaborn as sns

df = pd.read_csv('assets/banklist.csv', encoding='ISO-8859-1')

# Convert the Closing Date column to datetime and extract the year
df['Closing_Year'] = pd.to_datetime(df['Closing Date']).dt.year

# Create a count plot of bank closures by year
sns.countplot(x='Closing_Year', data=df, palette='Blues')