from __future__ import print_function
import argparse
import pandas as pd
__author__ = 'mlg'


def getparser():
    parser = argparse.ArgumentParser()
    parser.add_argument('targetfile')
    parser.add_argument('btecfile')
    return parser


def getargs():
    parser = getparser()
    args = parser.parse_args()
    return args


def main(args):
    df = pd.read_csv(args.targetfile)
    df = df[['name', 'y11_ap5', '3lop_3', 'fftd_2']]
    print(df.info())
    print(df)
    dfb = pd.read_csv(args.btecfile, usecols=['candidate', 'option',
                                              'result_2'])
    dfb = dfb[dfb['option'] == 'GEOGRAPHY (SPE CASH IN (LINEAR)']
    print(dfb.info())
    print(dfb)

if __name__ == '__main__':
    _args = getargs()
    main(_args)
