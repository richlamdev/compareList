#!/bin/usr/python
#
# Richard Lam, March 2019
#
# Script to compare a list of strings from two separate files.  
# Delimited (separated) by newline (\n)
# 
# Written for Python 3

import sys
import argparse

def compare_files(args):

    file1 = args.first_list.name
    file2 = args.second_list.name

    with args.first_list as firstfile:
        lista = [line.rstrip() for line in firstfile]

    with args.second_list as secondfile:
        listb = [line.rstrip() for line in secondfile]

    # determine common strings between files
    comm = sorted(set(lista) & set(listb))

    # determine strings only in first file
    diffa = sorted(set(lista) - set(listb))

    # determine strings only in second file
    diffb = sorted(set(listb) - set(lista))

    print ()
    print ("Strings common to " + file1 + " and " + file2)
    print(*comm, sep = "\n")
    print ()
    print ("Strings only in: " + file1 )
    print(*diffa, sep = "\n")
    print ()
    print ("Strings only in: " + file2 )
    print(*diffb, sep = "\n")

    with open(file1 + "_" + file2 + "_strings_common.txt","w") as common_file:
        for string in comm:
            print(string, sep='', file=common_file)

    with open(file1 + "_" + file2 + "_strings_only_in_" + file1,"w") as diff_filea:
        for string in diffa:
            print(string, sep='', file=diff_filea)

    with open(file1 + "_" + file2 + "_strings_only_in_" + file2,"w") as diff_fileb:
        for string in diffb:
            print(string, sep='', file=diff_fileb)

    print ()
    print ("Files created:")
    print (file1 + "_" + file2 + "_strings_common.txt")
    print (file1 + "_" + file2 + "_strings_only_in_" + file1)
    print (file1 + "_" + file2 + "_strings_only_in_" + file2)

def main():
    parser = argparse.ArgumentParser (add_help=True,
             description="Compares two lists.\n\n\
Output: Common strings to both files.\n\
        Strings exclusive to the first file.\n\
        Strings exclusive to the second file.", 
    formatter_class=argparse.RawTextHelpFormatter)

    parser.add_argument('first_list', type=argparse.FileType('r'),
                        metavar="<first file>", help="list of strings, Format: one string per line.")

    parser.add_argument('second_list', type=argparse.FileType('r'),
                        metavar="<second file>", help="list of strings, Format: one string per line.")

    args = parser.parse_args()

    compare_files (args)

if __name__ == "__main__":
    main()
