from packer import Packer
import sys
import argparse


def create_arg_parser():
    parser = argparse.ArgumentParser()
    parser.add_argument('-o', '--output', default='')
    parser.add_argument('-e', '--epsilon')
    parser.add_argument('-n', '--length')
    return parser


if __name__ == '__main__':
    arg_parser = create_arg_parser()
    namespace = arg_parser.parse_args(sys.argv[1:])

    solver = Packer(namespace.output,
                    int(namespace.epsilon),
                    int(namespace.lenght))
