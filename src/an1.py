from __future__ import print_function
import argparse
import pandas as pd
__author__ = 'mlg'

GRADEMAP = {'E': 1, 'D': 2, 'C': 3, 'B': 4, 'A': 5, 'A*': 6}


def getparser():
    parser = argparse.ArgumentParser()
    parser.add_argument('targetfile')
    parser.add_argument('btecfile')
    return parser


def getargs():
    """

    :rtype : Namespace
    """
    parser = getparser()
    args = parser.parse_args()
    return args


def main(args):
    df = pd.read_csv(args.targetfile)
    df = df[['name', 'y11_ap5', '3lop_3', 'fftd_2']]
    # print(df.info())
    # print(df)
    dfb = pd.read_csv(args.btecfile, usecols=['candidate', 'option',
                                              'result_2'])
    dfb = dfb[dfb['option'] == 'GEOGRAPHY (SPE CASH IN (LINEAR)']
    # print(dfb.info())
    del dfb['option']
    dfb.rename(columns={'candidate': 'name'}, inplace=True)
    # print(dfb)
    mf = pd.merge(df, dfb, on='name')
    mf.rename(columns={'y11_ap5': 'ap5', '3lop_3': '3lop', 'fftd_2': 'fftd',
                       'result_2': 'result'}, inplace=True)
    print(mf)

if __name__ == '__main__':
    _args = getargs()
    main(_args)
