import csv
import matplotlib.pyplot as plt
import numpy as np

from scipy import interpolate
from matplotlib.ticker import AutoMinorLocator

ROLLING_AVG_PTS=200
# conv_kernel = np.array([(1 / (1.33 ** x)) for x in range(ROLLING_AVG_PTS)])
conv_kernel = np.array([(1 / (1 ** x)) for x in range(ROLLING_AVG_PTS)])
conv_kernel /= conv_kernel.sum()
print(conv_kernel)

to_plot = ("test-20.4v.csv", "test-24.0v.csv", "test-27.6v.csv")
# to_plot = ("test-20.4v.csv", "test-20.4v-5v.csv")

fig, ax = plt.subplots(2, 1)
for data_filepath in to_plot:
    timestamps = []
    values = []

    with open(data_filepath) as f:
        f.readline()
        csv_read = csv.reader(f)
        for row in csv_read:
            timestamps.append(float(row[0]))
            values.append(float(row[1]))

    # plt.plot(timestamps[:-1 * (ROLLING_AVG_PTS - 1)], np.convolve(np.array(values), np.ones(ROLLING_AVG_PTS)/ROLLING_AVG_PTS, mode="valid"), label=data_filepath)
    ax[0].plot(timestamps[(ROLLING_AVG_PTS - 1):], np.convolve(np.array(values), conv_kernel, mode="valid"), label=data_filepath)
    ax[1].plot(timestamps[:-1 * (ROLLING_AVG_PTS - 1)], values[:-1 * (ROLLING_AVG_PTS - 1)])


    # conv_kernel = np.array([(1 / (2 ** x)) for x in range(ROLLING_AVG_PTS)])
    # conv_kernel /= conv_kernel.sum()

    # plt.plot(timestamps[(ROLLING_AVG_PTS - 1):], np.convolve(np.array(values), conv_kernel, mode="valid"), label=data_filepath)

    # plt.plot(timestamps[:-1 * (ROLLING_AVG_PTS - 1)], values[:-1 * (ROLLING_AVG_PTS - 1)])


ax[0].legend()
ax[0].minorticks_on()
# ax[0].tick_params(which='minor', bottom=False, left=False)
ax[0].xaxis.set_minor_locator(AutoMinorLocator(2))
ax[0].yaxis.set_minor_locator(AutoMinorLocator(2))
ax[0].grid(which="major")
ax[0].grid(which="minor", color="#DDDDDD")
plt.show()

