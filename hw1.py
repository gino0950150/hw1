# Part. 1
#=======================================
# Import module
#  csv -- fileIO operation
import csv
#=======================================

# Part. 2
#=======================================
# Read cwb weather data
cwb_filename = '107000105.csv'
data = []
header = []
target_station = ['C0A880', 'C0F9A0', 'C0G640', 'C0R190', 'C0X260']
ans = []

with open(cwb_filename) as csvfile:
   mycsv = csv.DictReader(csvfile)
   header = mycsv.fieldnames
   for row in mycsv:
      if(row['HUMD'] != '-99.000' and row['HUMD'] != '-999.000'):
        data.append(row)

for station in target_station:
    sum = 0
    haveNone = 0
    target_data = list(filter(lambda item: item['station_id'] == station, data))
    for row in target_data:
        if row['HUMD'] == '':
            print('!')
        else:
            sum = sum + float(row['HUMD'])
    ans.append([station, sum])



#=======================================


# Part. 3
#=======================================

# target_data = data[:10]

#=======================================

# Part. 4
#=======================================
# Print result
print(ans)
#========================================