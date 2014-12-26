from __future__ import print_function
import argparse
import pandas as pd
__author__ = 'mlg'


def getparser():
    parser = argparse.ArgumentParser()
    parser.add_argument('infile')
    # parser.add_argument('outfile')
    return parser


def getargs():
    parser = getparser()
    args = parser.parse_args()
    return args


def main(args):
    df = pd.read_csv(args.infile)
    df = df[['name', 'y11_ap5', '3lop_3', 'fftd_2']]
    print(df.info())
    print(df)

if __name__ == '__main__':
    _args = getargs()
    main(_args)
