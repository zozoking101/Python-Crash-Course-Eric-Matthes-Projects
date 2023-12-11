import pandas as pd
import json

# Replace 'your_json_file.json' with the actual path to your JSON file
with open('readable_eq_data.json', 'r', encoding='UTF-8') as file:
    data = json.load(file)

# Create a DataFrame from the 'features' list in the JSON data
df = pd.json_normalize(data['features'])

# Specify the columns you want in the desired order
selected_columns = ['properties.mag', 'properties.place', 'properties.time', 'properties.updated',
                    'properties.tz', 'properties.url', 'properties.detail', 'properties.felt',
                    'properties.cdi', 'properties.mmi', 'properties.alert', 'properties.status',
                    'properties.tsunami', 'properties.sig', 'properties.net', 'properties.code',
                    'properties.ids', 'properties.sources', 'properties.types', 'properties.nst',
                    'properties.dmin', 'properties.rms', 'properties.gap', 'properties.magType',
                    'properties.type', 'properties.title', 'geometry.type', 'geometry.coordinates',
                    'id']

# Extract the selected columns from the DataFrame
df_selected = df[selected_columns]

# Rename the columns for better readability
column_mapping = {'properties.mag': 'Mag', 'properties.place': 'Place', 'properties.time': 'Time',
                   'properties.updated': 'Updated', 'properties.tz': 'Tz', 'properties.url': 'Url',
                   'properties.detail': 'Detail', 'properties.felt': 'Felt', 'properties.cdi': 'Cdi',
                   'properties.mmi': 'Mmi', 'properties.alert': 'Alert', 'properties.status': 'Status',
                   'properties.tsunami': 'Tsunami', 'properties.sig': 'Sig', 'properties.net': 'Net',
                   'properties.code': 'Code', 'properties.ids': 'Ids', 'properties.sources': 'Sources',
                   'properties.types': 'Types', 'properties.nst': 'Nst', 'properties.dmin': 'Dmin',
                   'properties.rms': 'Rms', 'properties.gap': 'Gap', 'properties.magType': 'Magtype',
                   'properties.type': 'Type', 'properties.title': 'Title', 'geometry.type': 'Geometry_Type',
                   'geometry.coordinates': 'Coordinates', 'id': 'Id'}

df_selected = df_selected.rename(columns=column_mapping)

# Save the DataFrame to an Excel file
df_selected.to_excel('earthquake_data.xlsx', index=False)
