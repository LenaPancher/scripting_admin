import psutil
import argparse
from time import time, sleep


class Metrics:
    def __init__(self, memory_usage, bytes_sent, battery_percent, cpu_usage):
        self.memory_usage = memory_usage
        self.bytes_sent = bytes_sent
        self.battery_percent = battery_percent
        self.cpu_usage = cpu_usage


def main():
    parser()


def parser():
    args_parser = argparse.ArgumentParser('show system information')

    args_parser.add_argument("-i", "--interval", help="choose interval output in second", type=int,
                             action="store")

    args = args_parser.parse_args()

    show_output(args.interval)


def show_output(interval):
    interval = interval if interval is not None else 5
    console_print()
    while True:
        sleep(interval)
        console_print()


def console_print():
    metrics: Metrics = get_metrics()
    print("")
    print("# SYSTEM METRICS ")
    print(f"# Used Memory :  {metrics.memory_usage} % ")
    print(f"# Network Usage :  {metrics.bytes_sent} ")
    print(f"# CPU Usage :  {metrics.cpu_usage}  %")
    print(f"# Battery :  {metrics.battery_percent} % ")


def get_metrics():
    cpu = psutil.cpu_percent()
    memory = psutil.virtual_memory()
    net = psutil.net_io_counters(pernic=True)
    sensors = psutil.sensors_battery()
    key = ""

    for k in net.keys():
        key = k
        break

    megabytes_sent = f"{key} : {net[key].bytes_sent / float(1 << 20):,.0f} MB"

    return Metrics(memory.percent, megabytes_sent, sensors.percent, cpu)


if __name__ == '__main__':
    main()
