import xlwt
from xlwt import Workbook
import json

filename = 'readable_eq_data.json'

with open(filename, encoding='UTF-8') as f:
    all_eq_data = json.load(f)

wb = Workbook()
eq_sheet = wb.add_sheet('Earthquakes')
headers =list(all_eq_data['features'][0]['properties'].keys()) + list(all_eq_data['features'][0]['geometry'].keys()) + ['id'] #all_eq_data['features'][0]['id']
#print(headers)
i = 0
for header in headers:
    eq_sheet.write(0, i, header.title())
    i += 1

for i in range(1, len(all_eq_data['features'])):
    for j in range(len(headers[:26])):
        if all_eq_data['features'][i-1]['properties'][headers[:26][j]] == None:
            eq_sheet.write(i, j, 'null')
        else:
            eq_sheet.write(i, j, str(all_eq_data['features'][i-1]['properties'][headers[:26][j]]))
    for k in range(len(headers[26:28])):
        eq_sheet.write(i, k + 26, str(all_eq_data['features'][i-1]['geometry'][headers[26:28][k]]))
    for l in range(1):
        eq_sheet.write(i, l + 28, str(all_eq_data['features'][i-1]['id']))
wb.save('world_earthquake_data.xls')