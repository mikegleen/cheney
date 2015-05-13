"""
   Read a CSV file and write it with column names fixed:

   * A suffix of _1, _2, ... will be appended to duplicate names.
   * Unnamed columns will be given arbitrary names.
   * Names are converted to lower case.
   * Trailing spaces are stripped.
   * Embedded spaces are converted to '_' characters.

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
        name = name.strip()
        cntr[name] += 1
        # print(name, cntr[name])
        # if duplicate names or the name is blank
        if cntr[name] > 1 or not name:
            name += '_' + str(cntr[name])
        newheader.append(name.lower().replace(' ', '_'))
    writer.writerow(newheader)
    for row in reader:
        if row[0].strip():
            writer.writerow(row)


if __name__ == '__main__':
    _args = getargs()
    main(_args)
