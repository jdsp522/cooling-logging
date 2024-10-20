import serial
from datetime import datetime


def log(fp, port):
    with open(fp, "w") as f:
        f.write("Time (s),Ch0,Ch1,Ch2")

        with serial.Serial(port) as ser:
            line = ser.readline.decode()
            start = datetime.now()

            f.write("0.000000",{line_raw_to_v(line)})
            

def line_raw_to_v(r):
    return ",".join([str(int(x.split(",")) * (5 / 1024)) for x in r])

if __name__ == "__main__":
    fp = input("Output file name: ")
    port = input("Arduino serial port: ")

    log(fp, port)
