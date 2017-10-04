import csv
import sys

def fix_file(fin, fout, field, numfields):
    reader = csv.reader(fin)
    writer = csv.writer(fout)
    
    for row in reader:
        if not numfields:
            numfields = len(row)
        
        if len(row) > numfields:
            rowstart = row[:field-1]
            rowend = row[-(numfields-field):]
            badfield = row[field-1:-(numfields-field)]
            badfield = ','.join(badfield)
            row = rowstart + [badfield] + rowend
            
        writer.writerow(row)

if __name__ == '__main__':
    import argparse

    parser = argparse.ArgumentParser(
        description='A tool to fix CSV files corrupted by unquoted commas in one field.'
    )
    parser.add_argument('-f', '--field', required=True, type=int, help='the bad field containing commas (only one allowed, starts from 1)')
    parser.add_argument('-n', '--numfields', default=None, type=int, help='the number of fields [defaults to trusting first line]')
    parser.add_argument('file', nargs='?', default=None, help='input files [defaults to stdin]')

    args = parser.parse_args()

    if args.file:
        with open(args.file, "ra") as fin:
            fix_file(fin, sys.stdout, args.field, args.numfields)
    else:
        fix_file(sys.stdin, sys.stdout, args.field, args.numfields)
