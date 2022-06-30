# system modules
import argparse

# user modules
from base64_decoder import *
from base64_encoder import *
from logging_conf_base64 import *


def main(command_line=None):
    parser = argparse.ArgumentParser('base64 encoder/decoder')

    subparsers = parser.add_subparsers(dest='command')

    decode_parser = subparsers.add_parser('decode', help='decode base64')

    decode = decode_parser.add_mutually_exclusive_group()

    decode.add_argument("-s", "--string", help="handle a string", type=str, action="store")
    decode_parser.add_argument("-o", "--output", help="output to a file", type=str, action="store")
    decode_parser.add_argument("-l", "--log", help="logging level", type=str, action="store")
    decode.add_argument("-f", "--filename", help="handle a file", type=str, action="store")

    encode_parser = subparsers.add_parser('encode', help='encode into base64')

    encode = encode_parser.add_mutually_exclusive_group()

    encode.add_argument("-s", "--string", help="handle a string", type=str, action="store")
    encode_parser.add_argument("-o", "--output", help="output to a file", type=str, action="store")
    encode_parser.add_argument("-l", "--log", help="logging level", type=str, action="store")
    encode.add_argument("-f", "--filename", help="handle a file", type=str, action="store")

    args = parser.parse_args(command_line)

    if args.command == 'decode' or args.command == 'encode':
        args_handler(args)


def args_handler(args):
    mode = args.command
    result = ""

    if args.string is not None:
        if args.log is not None:
            if args.log.upper() == "DEBUG":
                logging_conf(logging_level=logging.DEBUG)
            elif args.log.upper() == "INFO":
                logging_conf(logging_level=logging.INFO)
            elif args.log.upper() == "WARNING":
                logging_conf(logging_level=logging.WARNING)
            elif args.log.upper() == "ERROR":
                logging_conf(logging_level=logging.ERROR)
            elif args.log.upper() == "CRITICAL":
                logging_conf(logging_level=logging.CRITICAL)
        else:
            logging_conf(logging_level=logging.DEBUG)
        result = base64_encode(args.string, args.log) if mode == "encode" else 'not implemented yet'
    if args.filename is not None:
        f = open(args.filename, "r")
        if args.log is not None:
            if args.log.upper() == "DEBUG":
                logging_conf(logging_level=logging.DEBUG)
            elif args.log.upper() == "INFO":
                logging_conf(logging_level=logging.INFO)
            elif args.log.upper() == "WARNING":
                logging_conf(logging_level=logging.WARNING)
            elif args.log.upper() == "ERROR":
                logging_conf(logging_level=logging.ERROR)
            elif args.log.upper() == "CRITICAL":
                logging_conf(logging_level=logging.CRITICAL)
        else:
            logging_conf(logging_level=logging.DEBUG)
        result = base64_encode(f.read(), args.log) if mode == "encode" else 'not implemented yet'
    if args.output is not None and (args.filename is not None or args.output is not None):
        f = open(args.output, "x")
        f.write(result)
    else:
        print(result)


if __name__ == '__main__':
    main()
