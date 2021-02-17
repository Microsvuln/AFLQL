#!/usr/bin/env python3
import os
import string
import binascii 
import codecs
import errno
import struct
import argparse
from binascii import unhexlify

def ensure_dir(dir):
    try:
        os.makedirs(dir)
    except OSError as e:
        if e.errno != errno.EEXIST:
            raise

def parse_args():
    parser = argparse.ArgumentParser(description=(
        "Helper - Specify input file analysis and output folder to save corpus for strings in the overall project ---------------------------------------------------------------------------  Example usage : python2 thisfile.py outdir str.txt"    ))
    parser.add_argument("corpdir",
        help="The path to the corpus directory to generate strings.")
    parser.add_argument("infile",
        help="Specify file output of codeql analysis - ex. ooo-atr.txt, analysis take place on this file, example : python2 thisfile.py outdir strings.txt")

    return parser.parse_args()


def do_string_analysis(corpdir, infile1):
    with open(infile1, "r") as f1:        
        lines = f1.readlines()[1:]       
        f1.close()       
        new_lst1 = []
        n = 1
        for i, num1 in enumerate(lines):
            if i != 0:
                new_lst1.append(num1)
                str11 = str(num1)
                str11 = str11.rstrip('\r\n')
                str11 = str11.replace(" ","")
                str11 = str11.replace("|","")
                # do some fix here ...
                #print str1
                with open(corpdir+'/seed-str{0}'.format(n), 'w') as file:                    
                        file.write(str11)
                        #print(str1)
                n=n+1

def main():
    args = parse_args()    
    ensure_dir(args.corpdir)
    do_string_analysis(args.corpdir, args.infile)
if __name__ == '__main__':
    main()
