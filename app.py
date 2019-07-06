import pandas as pd
columns = ['City_ID','City','Cloudiness','Country',	'Date',	'Humidity',	'Lat',	'Lng',	'Max Temp',	'Wind Speed']

df_cities = pd.read_csv('Resources\cities.csv')


# , names=columns

# Save to file
df_cities.to_html('cities.htm')

