import csv
import matplotlib.pyplot as plt
import math

CONVERT_CSVS = False
CONVERT_CSVS_HEADER = ("Time (s)", "Upstream Thermistor (C)", "Downstream Thermistor (C)")

DATA_FLOW_RATES = ("0.0667", "0.0692", "0.0933", "0.1020")
DATA_FAN_VOLTAGES = ("20.4", "24.0", "27.6")

DATA_SOURCE_FOLDER = "tests"
DATA_OUTPUT_FOLDER = "tests_c"

DATA_FILEPATHS = ("tests-airspeed/1.1lpm/12v-1.34m-s.csv",)
NUM_CHANNELS = 2

THERM_DIVIDER_RESISTANCES = (10010, 10060)
DIVIDER_V_SUPPLY = 3.309

K_C_CONSTANT = 273.15

THERM_BETA = 3435
THERM_R25 = 10000
THERM_T25 = 25 + K_C_CONSTANT

def calc_resistance(v_thermistor, resistor_ohms):
    # v_divider = v_thermistor + i(resistor_ohms)
    current_a = (DIVIDER_V_SUPPLY - v_thermistor) / resistor_ohms
    return v_thermistor / current_a

def calc_temp(resistance):
    return 1 / ((math.log(resistance / THERM_R25) / THERM_BETA) + (1 / THERM_T25))

def calc_temp_c(resistance):
    return calc_temp(resistance) - K_C_CONSTANT

def plot_data(path):
    timestamps = []
    values = [[] for i in range(NUM_CHANNELS)]

    with open(path, "r") as f:
        f.readline()
        csv_read = csv.reader(f)
        for row in csv_read:
            timestamps.append(float(row[0]))
            print(row)
            for i in range(NUM_CHANNELS): 
                resistance = calc_resistance(float(row[i + 1]), THERM_DIVIDER_RESISTANCES[i])
                values[i].append(calc_temp_c(resistance))

    for channel in values: plt.plot(timestamps, channel)

    plt.show()

def convert_csv(input_path, output_path):
    #  timestamps = []
    # values = [[] for i in range(NUM_CHANNELS)]

    with open(input_path, "r") as f:
        with open(output_path, "w") as f_out:
            f.readline()
            csv_read = csv.reader(f)
            csv_write = csv.writer(f_out)

            rows_out = [CONVERT_CSVS_HEADER]
            # csv_write.writerow(CONVERT_CSVS_HEADER)
            for row in csv_read:
                rows_out.append([float(row[0])])

                for i in range(NUM_CHANNELS): 
                    resistance = calc_resistance(float(row[i + 1]), THERM_DIVIDER_RESISTANCES[i])
                    rows_out[-1].append(calc_temp_c(resistance))
            
            csv_write.writerows(rows_out)

if __name__ == "__main__":
    if not CONVERT_CSVS:
        for path in DATA_FILEPATHS: plot_data(path)
    else:
        for rate in DATA_FLOW_RATES:
            for voltage in DATA_FAN_VOLTAGES:
                sub = f"/{rate}/{rate}-{voltage}v.csv"
                convert_csv(DATA_SOURCE_FOLDER + sub, DATA_OUTPUT_FOLDER + sub)