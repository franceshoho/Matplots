import csv
import matplotlib.pyplot as plt
from datetime import datetime

filename = 'Data/death_valley_2018_full.csv'
with open(filename) as file:
    reader = csv.reader(file)
    header_row = next(reader)
    # for i, header in enumerate(header_row):
    #     print(i, header)

    lows, highs, dates = [], [], []
    for row in reader:
        date = datetime.strptime(row[2], "%Y-%m-%d")
        try:
            low = int(row[7])
            high = int(row[6])
        except ValueError:
            print("Missing data for", date)
        else:
            dates.append(date)
            lows.append(low)
            highs.append(high)
#
# print(f'Highs in dead valley: {highs}')
# print(f'Lows in dead valley: {lows}')

# plot 2 graphs side by side
plt.style.use('classic')
fig, (ax1, ax2) =  plt.subplots(1, 2, sharey=True, sharex=True, figsize=(20,10))
ax1.plot(dates, lows, c='blue', label='Low', alpha=0.5)
ax2.plot(dates, highs, c='red', label='High', alpha=0.5)
# # Fine-tune figure; make subplots close to each other and hide x ticks for
# # all but bottom plot.
# fig.subplots_adjust(hspace=0)
# plt.setp([a.get_xticklabels() for a in fig.axes[:-1]], visible=False)

#set title, axis label, legend
ax1.set_title('Daily Low Temp - 2018', fontsize = 16)
ax1.set_xlabel('', fontsize=16)
ax1.set_ylabel('Temp (F)', fontsize=16)
ax1.set_title('Daily Low Temp - 2018', fontsize=16)

ax2.set_title('Daily High Temp - 2018', fontsize = 16)
ax1.tick_params(axis='both', which='major', labelsize=16)
ax2.tick_params(axis='both', which='major', labelsize=16)

fig.suptitle('Dead Valley - 2018', fontsize=24)
fig.autofmt_xdate()
fig.legend()
fig.tight_layout()  # will adj spacing btw subplots
plt.show()

# plot in one line with area between
plt.style.use('seaborn')
fig, ax = plt.subplots()
# ax.plot(x, y, c, label, fontsize, etc.)
# if you don't specify x, you get default 0-#
ax.plot(dates, highs, c='red', label='High', alpha=0.5)
ax.plot(dates, lows, c='blue', label='Low', alpha=0.5)  # half transparency
# fill between 2 lines
ax.fill_between(dates, highs, lows, facecolor="blue", alpha=0.1)
ax.set_title('Daily High and Low Temp - 2018', fontsize = 24)
ax.set_xlabel('', fontsize=16)
fig.autofmt_xdate()         # print date diag. so no overlap
ax.set_ylabel("Temp (F)", fontsize=16)
ax.legend(loc='upper left')
ax.tick_params(axis='both', which='major', labelsize=16)
# save plot to file
cur_dir = f'./Data/'  # parent directory
plt.savefig(cur_dir+'deadvalley-high-low.png')
plt.show()
