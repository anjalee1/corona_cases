import pandas as pd
data= pd.read_csv('data.csv')
data['Active'] = data['Confirmed'] - data['Deaths'] - data['Recovered']
result = data.groupby('Country/Region')[['Confirmed', 'Deaths', 'Recovered', 'Active']].sum().reset_index()
print(result)
