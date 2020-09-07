#!/usr/bin/env python2
import string
import binascii 
import codecs
import struct
import os
import argparse
import errno
from binascii import unhexlify

def parse_args():
    parser = argparse.ArgumentParser(description=(
        "Helper - Specify input file to analysis and output folder to save corpdirus for constants in the overall project ---------------------------------------------------------------------------  Example usage : python2 thisfile.py outdir ooo.txt"    ))
    parser.add_argument("corpdir",
        help="The path to the corpus directory to generate files.")
    parser.add_argument("infile",
        help="Specify file output of codeql analysis - ex. ooo-hex.txt, analysis take place on this file, example : python2 thisfile.py outdir ooo.txt")

    return parser.parse_args()
    
def ensure_dir(dir):
    try:
        os.makedirs(dir)
    except OSError as e:
        if e.errno == errno.EEXIST:
            print "[-] Directory exists, specify another directory"
            exit(1)

def do_analysis(corpdir, infile):
    with open(infile, "rb") as f:        
        lines = f.readlines()[2:]       
        f.close()       
        new_lst = []
        n = 1
        for i, num in enumerate(lines):
            if i != 0:
                new_lst.append(num)
                str1 = str(num)
                str1 = str1.rstrip('\n\n')
                str1 = str1.replace("0x","");
                str1 = str1.replace("|","")
                str1 = str1.rstrip('\r\n')
                str1 = str1.replace(" ","")
                str1 = str1.translate(None, string.punctuation)
                try:
                        str1 = str1.decode("hex")
                        with open(corpdir+'/seed{0}'.format(n), 'w') as file:                    
                                print str1
                                file.write(str1)
                        #print(str1)
                    
                except:
                        str1 = str1+"0"
                        with open(corpdir+'/seed{0}'.format(n), 'w') as file:
                                print str1
                                file.write(str1)
                n = n+1



def main():
    args = parse_args()    
    ensure_dir(args.corpdir)
    do_analysis(args.corpdir, args.infile)
if __name__ == '__main__':
    main()