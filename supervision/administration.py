# -*- coding: utf-8 -*-

import psutil
import argparse
from time import sleep
from datetime import datetime
import json
from influxdb import InfluxDBClient

from logging_conf_administration import *


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
    args_parser.add_argument('--host', type=str, required=False,
                             default='localhost',
                             help='hostname of InfluxDB http API')
    args_parser.add_argument('--port', type=int, required=False, default=8086,
                             help='port of InfluxDB http API')

    args = args_parser.parse_args()

    show_output(args.interval)


def show_output(interval):
    save_to_influxdb()
    return
    interval = interval if interval is not None else 5
    console_print()
    while True:
        sleep(interval)
        console_print()


def save_to_influxdb():
    """Instantiate a connection to the InfluxDB."""
    user = 'root'
    password = 'root'
    dbname = 'psutils'
    dbuser = 'smly'
    host = '192.168.10.110'
    port = '8086'
    dbuser_password = 'my_secret_password'
    query = 'select Float_value from cpu_load_short;'
    metrics: Metrics = get_metrics()
    json_metrics = json.dumps(metrics.__dict__)
    json_payload = []
    object_payload = json.loads(
        '{ "measurement": "psutils", "tags": { "host": "psutils" }, '
        '"time": "' + str(datetime.now()) + '", "fields": ' + json_metrics + ' }')
    json_payload.append(object_payload)

    client = InfluxDBClient(host, port, user, password, dbname)

    print("Create database: " + dbname)
    client.create_database(dbname)

    print("Create a retention policy")
    client.create_retention_policy('awesome_policy', '3d', 3, default=True)

    print("Switch user: " + dbuser)
    client.switch_user(dbuser, dbuser_password)

    print("Write points: {0}".format(json_payload))
    client.write_points(json_payload)


def console_print():
    metrics: Metrics = get_metrics()
    print("")
    print("# SYSTEM METRICS ")
    mylogs.info(f"# Used Memory :  {metrics.memory_usage} % ")
    mylogs.info(f"# Network Usage :  {metrics.bytes_sent} ")
    mylogs.info(f"# CPU Usage :  {metrics.cpu_usage}  %")
    mylogs.info(f"# Battery :  {metrics.battery_percent} % ")


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
