# system modules
import argparse

# user modules
from base64_decoder import *
from base64_encoder import *


def main(command_line=None):
    parser = argparse.ArgumentParser('base64 encoder/decoder')

    subparsers = parser.add_subparsers(dest='command')

    decode_parser = subparsers.add_parser('decode', help='decode base64')

    decode = decode_parser.add_mutually_exclusive_group()

    decode.add_argument("-s", "--string", help="handle a string", type=str, action="store")
    decode_parser.add_argument("-o", "--output", help="output to a file", type=str, action="store")
    decode.add_argument("-f", "--filename", help="handle a file", type=str, action="store")

    encode_parser = subparsers.add_parser('decode', help='encode into base64')

    encode = encode_parser.add_mutually_exclusive_group()

    encode.add_argument("-s", "--string", help="handle a string", type=str, action="store")
    encode_parser.add_argument("-o", "--output", help="output to a file", type=str, action="store")
    encode.add_argument("-f", "--filename", help="handle a file", type=str, action="store")

    args = parser.parse_args(command_line)

    if args.command == 'decode' or args.command == 'encode':
        args_handler(args)


def args_handler(args):
    mode = args.command

    if args.string is not None:
        print(base64_encode(args.string))
    if args.filename is not None:
        print(args.filename)
    if args.output is not None and (args.filename is not None or args.output is not None):
        print(args.output)
    else:
        print(mode)


if __name__ == '__main__':
    main()
