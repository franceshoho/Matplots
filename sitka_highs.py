import csv
import matplotlib.pyplot as plt
from datetime import datetime

filename = 'Data/sitka_weather_2018_simple.csv'
with open(filename) as file:
    reader = csv.reader(file)  # get reader object
    header_row = next(reader)  # get next line in reader obj and returns a list

    for i, col_header in enumerate(header_row):
        print(i, col_header)
    # get min and max temp
    lows, highs, dates = [], [], []
    for row in reader:
        date = datetime.strptime(row[2], '%Y-%m-%d')
        high = int(row[5])
        low = int(row[6])
        dates.append(date)
        highs.append(high)
        lows.append(low)

    # print(f'Highs in Sitka: {highs}')
    # print(f'Lows in Sitka: {lows}')

# plot temp data
plt.style.use('seaborn')
fig, ax = plt.subplots()
# ax.plot(x, y, c, label, fontsize, etc.)
# if you don't specify x, you get default 0-#
ax.plot(dates, highs, c='red', label='High')
ax.plot(dates, lows, c='blue', label='Low')
ax.set_title('Daily High and Low Temp - 2018', fontsize = 24)
ax.set_xlabel('', fontsize=16)
fig.autofmt_xdate()         # print date diag. so no overlap
ax.set_ylabel("Temp (F)", fontsize=16)
ax.tick_params(axis='both', which='major', labelsize=16)
plt.legend()
plt.show()

