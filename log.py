import serial
from datetime import datetime
import sys

def log(fp, port):
    with open(fp, "w") as f:
        f.write("Time (s),Pitot Tube (V),Unused (V)\n")

        with serial.Serial(port, 230400) as ser:
            while ser.in_waiting > 0:
                ser.readline()
            # line = ser.readline().decode()
            ser.reset_input_buffer()
            line = ser.readline().decode()
            start = datetime.now()

            f.write(f"0.000000,{line_raw_to_v(line)}\n")

            while True:
                ser_line = ser.readline().decode()
                line = f"{time_since_start(start)},{line_raw_to_v(ser_line)}\n"
                f.write(line)
                print(line)

# def line_raw_to_v(r):
#     return ",".join([str(int(x) * (5 / 1024)) for x in r.split(",")])

def line_raw_to_v(r):
    return ",".join([f"{int(x) * (3.3 / 65535):.6f}" for x in r.split(",")])

def time_since_start(start: datetime):
    delta = datetime.now() - start
    return f"{delta.seconds}.{delta.microseconds:06}"

if __name__ == "__main__":
    fp = sys.argv[2]
    port = sys.argv[1]

    log(fp, port)
