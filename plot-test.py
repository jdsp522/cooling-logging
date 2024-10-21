import csv
import matplotlib.pyplot as plt
import numpy as np
from scipy import interpolate

timestamps = []
values = []

with open("test.csv") as f:
    f.readline()
    csv_read = csv.reader(f)
    for row in csv_read:
        timestamps.append(float(row[0]))
        values.append(float(row[1]))

ts_np = np.array(timestamps)
v_np = np.array(values)
# v_supply = np.array(values[2150:2250])
# v_onboard = np.array(values[350:450])


#430-450 -> supply 3v3
#70-90 -> stock 3v3



print(f"Supply: {np.std(v_np[2150:2250])}")
print(f"Onboard: {np.std(v_np[350:450])}")

# plt.plot(timestamps, values)


timestamps = []
values = []

with open("test3.csv") as f:
    f.readline()
    csv_read = csv.reader(f)
    for row in csv_read:
        timestamps.append(float(row[0]))
        values.append(float(row[1]))

ts_np = np.array(timestamps)
v_np = np.array(values)

print(f"bruh: {np.std(v_np[50:150])}")


plt.plot(timestamps, values)
plt.show()