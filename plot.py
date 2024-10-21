import csv
import matplotlib.pyplot as plt
import numpy as np
from scipy import interpolate

TS_RANGE = (30, 130)
TS_RANGE_OG = (10, 110)
Y_LIM_FOR_SOME_REASON = (0.305, 0.342)

ROLLING_AVG_PTS = 2

timestamps = []
values = []

with open("test-27.6v-wrench.csv") as f:
    f.readline()
    csv_read = csv.reader(f)
    for row in csv_read:
        timestamps.append(float(row[0]))
        values.append(float(row[1]))

timestamps_og = []
values_og = []

with open("test-27.6v.csv") as f:
    f.readline()
    csv_read = csv.reader(f)
    for row in csv_read:
        timestamps_og.append(float(row[0]))
        values_og.append(float(row[1]))


fig, ((ax1, ax2), (ax3, ax4), (ax5, ax6)) = plt.subplots(3, 2)
ax1.plot(timestamps, values)
ax2.plot(timestamps_og, values_og)

rolling_avg = np.convolve(np.array(values), np.ones(ROLLING_AVG_PTS)/ROLLING_AVG_PTS, mode="same")
rolling_avg_og = np.convolve(np.array(values_og), np.ones(ROLLING_AVG_PTS)/ROLLING_AVG_PTS, mode="same")

ax3.plot(timestamps, rolling_avg)
ax4.plot(timestamps_og, rolling_avg_og)

x_spline = np.array(timestamps)
y_spline = np.array(values)

x_spline_og = np.array(timestamps_og)
y_spline_og = np.array(values_og)

t, c, k = interpolate.splrep(x_spline, y_spline, s=0.0015, k=3)
spline = interpolate.BSpline(t, c, k)

t, c, k = interpolate.splrep(x_spline_og, y_spline_og, s=0.001, k=3)
spline_og = interpolate.BSpline(t, c, k)

ax5.plot(timestamps, spline(timestamps))
ax6.plot(timestamps_og, spline_og(timestamps_og))

ax1.set_xlim(TS_RANGE)
ax3.set_xlim(TS_RANGE)
ax5.set_xlim(TS_RANGE)

ax2.set_xlim(TS_RANGE_OG)
ax4.set_xlim(TS_RANGE_OG)
ax6.set_xlim(TS_RANGE_OG)

ax3.set_ylim(Y_LIM_FOR_SOME_REASON)
ax5.set_ylim(Y_LIM_FOR_SOME_REASON)

ax4.set_ylim(Y_LIM_FOR_SOME_REASON)
ax6.set_ylim(Y_LIM_FOR_SOME_REASON)


plt.show()