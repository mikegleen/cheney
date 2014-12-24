"""
   Read a CSV file and write it with duplicate column names fixed. A suffix of
    _1, _2, ... will be appended to the duplicate names.
"""
from __future__ import print_function
import argparse
from collections import Counter
import csv

__author__ = 'mlg'


def getparser():
    parser = argparse.ArgumentParser()
    parser.add_argument('-k', '--skip', type=int, default=0, help="""
    Number of rows to skip.""")
    parser.add_argument('infile')
    parser.add_argument('outfile')
    return parser


def getargs():
    parser = getparser()
    args = parser.parse_args()
    return args


def main(args):
    infile = open(args.infile, 'rb')
    outfile = open(args.outfile, 'wb')
    reader = csv.reader(infile)
    writer = csv.writer(outfile)
    for n in range(args.skip):
        reader.next()
    header = reader.next()
    newheader = []
    cntr = Counter()
    for name in header:
        if not name:
            continue
        cntr[name] += 1
        print(name, cntr[name])
        if cntr[name] > 1:
            name += '_' + str(cntr[name] - 1)
        newheader.append(name)
    writer.writerow(newheader)
    for row in reader:
        if row[0].isdigit():
            writer.writerow(row)


if __name__ == '__main__':
    _args = getargs()
    main(_args)