#importing requirements
import requests
import pandas as pd

#pulling data from api
r = requests.get('https://datausa.io/api/data?drilldowns=Nation&measures=Population')
data = r.json()['data']
df = pd.DataFrame(data=data)


#print(df.head(5))

#find and print two descriptive statistics
recent_year = df['Year'].max()
oldest_record = df['Year'].min()


print("Most recent year in record ",recent_year)
print("Oldest year in record ", oldest_record)

#use pandas.query to create two subsets of data. print statements are
#commented out but were used to test that the query worked.

df['Year'] = pd.to_datetime(df['Year'])
newer_df = df.query('Year >= "2016-01-01"')
#print(newer_df.head())

older_df = df.query('Year < "2016-01-01"')
#print(older_df.head())

#print the second and third columns of the df

selected_columns = df.iloc[:, 1:3]
print(selected_columns)

#print the first four rows of the df

first_four = df.head(4)
print(first_four)