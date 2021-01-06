#!/usr/bin/env python3
import string
import binascii
import os
import codecs
import struct
import argparse
import errno
from binascii import unhexlify

def do_string_analysis(infile):
    with open(infile, "r") as f:        
        lines = f.readlines()[1:]       
        f.close()       
        new_lst = []
        n = 1
        for i, num2 in enumerate(lines):
            if i != 0:
                new_lst.append(num2)
                str2 = str(num2)                
                print(str2)
                with open('dict/dict-str{0}.dict'.format(n), 'w') as file:                    
                        file.write(str2)
                        #print(str1)
                n=n+1
def main():
    #args = parse_args()    
    #ensure_dir(args.corpdir)
    do_string_analysis('dict-proj.dict')
if __name__ == '__main__':
    main()
