#!/usr/bin/env python3
import shutil
import subprocess
import os
import threading
import time
import sys
from sys import exit

def cuDir() :
        dirpath = os.getcwd()
        #print("current directory is : " + dirpath)
        foldername = os.path.basename(dirpath)
        #print("Directory name is : " + foldername)
        return foldername

def build():
        #cleancom = 'rm -rf'.split()
        #uninstrumented_build_directory=cuDir()
        
    
        command = [
           'python3',
           '/out/new/zlib/litan.py',
           '/out/new/zlib/dict',
           '/out/new/zlib/litout.log'
        ]      
        worker1 = subprocess.Popen(command)
        print(worker1.communicate())
        command1 = [
           'python3',
           '/out/new/zlib/stan.py',
           '/out/new/zlib/dict1',
           '/out/new/zlib/outstr.log'
        ]
        worker2 = subprocess.Popen(command1)
        print(worker2.communicate())
        
        subprocess.call(["cp /out/new/zlib/dict1/* /out/new/zlib/dict/."],shell=True)
        print('done!')
        subprocess.call(["cp -r /out/new/zlib/dict/ /out/new/dict/"],shell=True)
        print('done!!')        
        #subprocess.call(["cp /out/fuzz-target.dict /out/new/dict/."],shell=True)
        #print('done!!!')
        
def main():
    original_stdout = sys.stdout
    build()
    print('Results written, everthing is done!')

if __name__ == '__main__':
    main()
