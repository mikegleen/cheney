"""
Compare predicted with actual results. Two analyses are done:

1.
For each of the AP, 3LOP and FFTD grades, the absolute value of the difference
between that grade and the result is computed and the mean of those values is
displayed. This shows how accurate the predictions were. In this case, smaller
is better.

2.
The same computation is done, except that the actual value rather than the
absolute value is used. This shows how much better the result was than the
predicted result. In this case, larger positive numbers are better.

"""

from __future__ import print_function
import argparse
import pandas as pd
__author__ = 'mlg'

GRADE = pd.Series({'G': 1, 'F': 2, 'E': 3, 'D': 4, 'C': 5, 'B': 6, 'A': 7,
                   'A*': 8})
COLS1YR = ['name', 'tchgroup', 'most_recent_ap', '3lop', 'fftd']
COLS2YR = ['name', 'tchgroup', 'y11_ap5', '3lop_3', 'fftd_2']
RENAME1YR = {'most_recent_ap': 'ap', '3lop': 'lop', 'result_2': 'result'}
RENAME2YR = {'y11_ap5': 'ap', '3lop_3': 'lop', 'fftd_2': 'fftd',
             'result_2': 'result'}


def getparser():
    parser = argparse.ArgumentParser()
    parser.add_argument('-t', '--tchgroup')
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


def grade(g):
    return GRADE[g] if g == 'A*' else GRADE[g[0]]


def main(args):
    if args.tchgroup:
        print('tchgroup:   ' + args.tchgroup)
    print('targetfile: ' + args.targetfile)
    print('btecfile:   ' + args.btecfile)

    df = pd.read_csv(args.targetfile)
    if 'y11_ap5' in df:
        cols = COLS2YR
        renameyr = RENAME2YR
    else:
        cols = COLS1YR
        renameyr = RENAME1YR
    # print(df)
    df = df[cols]
    df.tchgroup = df.tchgroup.map(lambda x: x.lower())
    # print(df.info())
    if args.tchgroup:
        df = df[df.tchgroup == args.tchgroup.lower()]
    dfb = pd.read_csv(args.btecfile, usecols=['candidate', 'option',
                                              'result_2'])
    dfb = dfb[dfb['option'] == 'GEOGRAPHY (SPE CASH IN (LINEAR)']
    # print(dfb.info())
    del dfb['option']
    dfb.rename(columns={'candidate': 'name'}, inplace=True)
    # print(dfb)
    mf = pd.merge(df, dfb, on='name')
    mf.rename(columns=renameyr, inplace=True)
    # print(mf)
    mf.dropna(inplace=True)
    mf.ap = mf.ap.map(grade)
    mf.lop = mf.lop.map(grade)
    mf.fftd = mf.fftd.map(grade)
    mf.result = mf.result.map(grade)
    # Compute Value Added and Difference from Actual
    mf.va = mf.result - mf.ap
    mf.v3 = mf.result - mf.lop
    mf.vf = mf.result - mf.fftd
    mf.da = mf.va.abs()
    mf.d3 = mf.v3.abs()
    mf.df = mf.vf.abs()
    # print(mf)
    print('Number of students: {}'.format(len(mf)))
    print('Mean of ap, 3lop, and fftp differences from actual:')
    print('{:5.3f} {:5.3f} {:5.3f}'.format(mf.da.mean(), mf.d3.mean(),
                                           mf.df.mean()))
    print('\nMean of ap, 3lop, and fftp value added:')
    print('{:5.3f} {:5.3f} {:5.3f}'.format(mf.va.mean(), mf.v3.mean(),
                                           mf.vf.mean()))

if __name__ == '__main__':
    print('\n-----------------')
    _args = getargs()
    main(_args)
