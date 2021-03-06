# -*- coding: utf-8 -*-

import psutil
import argparse
from time import sleep
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
    """
    Create arguments
    """
    args_parser = argparse.ArgumentParser('show system information')

    args_parser.add_argument("-i", "--interval", help="choose interval output in second", type=int, action="store")
    args_parser.add_argument('-ho', '--host', type=str, required=False, help='hostname of InfluxDB http API', action="store")
    args_parser.add_argument('-p', '--port', type=int, required=False, help='port of InfluxDB http API', action="store")

    args = args_parser.parse_args()

    show_output(args.interval, args.host, args.port)


def show_output(interval, host, port):
    """
    Program logic
    Args:
        interval: in second
        host: host of InfluxBD
        port: port of InfluxBD
    """
    interval = interval if interval is not None else 5
    logging()
    while True:
        sleep(interval)
        logging()
        save_to_influxdb(host, port)


def save_to_influxdb(host, port):
    """Instantiate a connection to the InfluxDB.
    Args:
        host: host of InfluxBD
        port: port of InfluxBD
    """
    user = 'root'
    password = 'root'
    dbname = 'psutils'
    host = host if host is not None else 'localhost'
    port = port if port is not None else 8086

    metrics: Metrics = get_metrics()
    json_metrics = json.dumps(metrics.__dict__)
    json_payload = []
    object_payload = json.loads(
        '{ "measurement": "psutils", "tags": { "host": "psutils" }, "fields": ' + json_metrics + ' }')
    json_payload.append(object_payload)

    client = InfluxDBClient(host, port, user, password, dbname)

    print("Create database: " + dbname)
    client.create_database(dbname)

    print("Create a retention policy")
    client.create_retention_policy('awesome_policy', '3d', 3, default=True)

    print("Write points: {0}".format(json_payload))
    client.write_points(json_payload)


def logging():
    """
    Display logs
    """
    metrics: Metrics = get_metrics()
    mylogs.info("")
    mylogs.info("# SYSTEM METRICS ")
    mylogs.info(f"# Used Memory :  {metrics.memory_usage} % ")
    mylogs.info(f"# Network Usage :  {metrics.bytes_sent} ")
    mylogs.info(f"# CPU Usage :  {metrics.cpu_usage}  %")
    mylogs.info(f"# Battery :  {metrics.battery_percent} % ")


def get_metrics():
    """
    Retrieve metrics
    Returns:

    """
    cpu = psutil.cpu_percent()
    memory = psutil.virtual_memory()
    net = psutil.net_io_counters(pernic=True)
    sensors = psutil.sensors_battery()
    key = ""

    for k in net.keys():
        key = k
        break

    megabytes_sent = f"{key} : {net[key].bytes_sent / float(1 << 20):,.0f} MB"

    return Metrics(float(memory.percent), megabytes_sent, float(sensors.percent), float(cpu))


if __name__ == '__main__':
    main()
