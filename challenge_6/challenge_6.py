import csv
import numpy as np

data = []
with open('BTC-USD.csv', 'r') as file:
    csv_reader = csv.reader(file)
    for row in csv_reader:
        data.append(row)

header = data[0]
close_prices_index = header.index('Close')
volumes_index = header.index('Volume')

close_prices = np.array([float(row[close_prices_index]) for row in data[1:]])
volumes = np.array([float(row[volumes_index]) for row in data[1:]])

threshold_price = 30000
threshold_volume = 16000000000

filtered_days = np.where((close_prices > threshold_price) & (volumes >= threshold_volume))

selected_days = [data[i+1] for i in filtered_days[0]]
for day in selected_days:
    print(*day)
