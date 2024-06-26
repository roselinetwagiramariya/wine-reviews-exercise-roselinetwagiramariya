import pandas as pd

wine_data = pd.read_csv('data/winemag-data-130k-v2.csv.zip')


summary_data = wine_data.groupby('country').agg({
    'country': 'count',
    'points': 'mean'
}).rename(columns={'country': 'count', 'points': 'average_points'}).reset_index()


summary_data['average_points'] = summary_data['average_points'].round(1)

summary_data.to_csv('data/reviews-per-country.csv', index=False)

print("Summary data saved successfully!")


