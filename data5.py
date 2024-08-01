import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns
import folium
from folium.plugins import HeatMap
# data = {
#     'Time': ['12:00', '13:00'],
#     'Date': ['2024-07-29', '2024-07-30']
# }
# accidents = pd.DataFrame(data)
# Load data
accidents = pd.read_csv('C:/Users/kanch/Downloads/AccidentsBig.csv.zip')  # Replace with your dataset file path
print(accidents.columns)

# Display the first few rows of the dataset
print(accidents.head())
# Convert date and time columns to datetime objects

accidents['datetime'] = pd.to_datetime(accidents['Date'] + ' ' +accidents['Time'],format='%d-%m-%Y %H:%M')

# Extract relevant time features
accidents['hour'] = accidents['datetime'].dt.hour
accidents['day_of_week'] = accidents['datetime'].dt.day_name()
accidents['month'] = accidents['datetime'].dt.month_name()
# accidents['datetime'] = pd.to_datetime(accidents['Date'] + ' ' + accidents['Time'])

# Check data types and values
print(accidents.info())
required_columns = ['road_conditions', 'weather_conditions']
if 'Road_Conditions' in accidents.columns:
    accidents = accidents.dropna(subset=['Road_Conditions', 'Weather_Conditions'])
else:
    print("Column 'Road_Conditions' does not exist in the DataFrame")

# print(accidents['road_conditions'].unique())
# print(accidents['weather_conditions'].unique())
plt.figure(figsize=(12, 6))
sns.countplot(data=accidents, x='hour')
plt.title('Accident Frequency by Hour of Day')
plt.xlabel('Hour of Day')
plt.ylabel('Number of Accidents')
plt.show()
plt.figure(figsize=(12, 6))
sns.countplot(data=accidents, x='weather_conditions', order=accidents['weather_conditions'].value_counts().index)
plt.title('Accident Frequency by Weather Conditions')
plt.xlabel('Weather Conditions')
plt.ylabel('Number of Accidents')
plt.xticks(rotation=45)
plt.show()
plt.figure(figsize=(12, 6))
sns.countplot(data=accidents, x='road_conditions', order=accidents['road_conditions'].value_counts().index)
plt.title('Accident Frequency by Road Conditions')
plt.xlabel('Road Conditions')
plt.ylabel('Number of Accidents')
plt.xticks(rotation=45)
plt.show()
# Initialize the map centered around a midpoint (latitude, longitude)
m = folium.Map(location=[accidents['latitude'].mean(), accidents['longitude'].mean()], zoom_start=12)

# Prepare data for heatmap
heat_data = [[row['latitude'], row['longitude']] for index, row in accidents.iterrows()]

# Add HeatMap layer
HeatMap(heat_data).add_to(m)

# Save to an HTML file
m.save('heatmap.html')
plt.figure(figsize=(12, 6))
sns.boxplot(data=accidents, x='hour', y='severity')
plt.title('Accident Severity by Hour of Day')
plt.xlabel('Hour of Day')
plt.ylabel('Severity')
plt.show()
plt.figure(figsize=(12, 6))
sns.scatterplot(data=accidents, x='longitude', y='latitude', hue='road_conditions', palette='viridis', alpha=0.5)
plt.title('Accident Hotspots by Road Conditions')
plt.xlabel('Longitude')
plt.ylabel('Latitude')
plt.show()


