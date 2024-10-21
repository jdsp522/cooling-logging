import serial
from datetime import datetime

def log(fp, port):
    with open(fp, "w") as f:
        f.write("Time (s),Pitot Tube (V),3V3 Supply (V, unused)\n")

        with serial.Serial(port, 115200) as ser:
            ser.reset_input_buffer()
            line = ser.readline().decode()
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
    fp = input("Output file name: ")
    port = input("Serial port: ")

    log(fp, port)
