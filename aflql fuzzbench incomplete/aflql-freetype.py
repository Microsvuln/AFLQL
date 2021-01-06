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
           '/out/new/freetype2/litan.py',
           '/out/new/freetype2/dict',
           '/out/new/freetype2/litout.log'
        ]      
        worker1 = subprocess.Popen(command)
        print(worker1.communicate())
        command1 = [
           'python3',
           '/out/new/freetype2/stan.py',
           '/out/new/freetype2/dict1',
           '/out/new/freetype2/outstr.log'
        ]
        worker2 = subprocess.Popen(command1)
        print(worker2.communicate())
        #print('Lits has been written')
        #with open("outstr.log", "w") as f:
        #        stream = os.popen("codeql query run strtool.ql -d " + db1 )
         #       output = stream.read()
          #      f.write(output)
           #     f.close()
        #command = [
        #   'python2',
        #   'stan.py',
        #   'dict1',
        #   'outstr.log'
        #]
        #q = subprocess.Popen(command)
        #print 'strs has been writen'
        #print q.communicate()
        #print 'its okay'
        #command2 = [
        #        'cp',
        #        '/out/new/libpng-1.2.56/dict1/*',
        #        '/out/new/libpng-1.2.56/dict/.'
        #]
        #worker3 = subprocess.Popen(command2)
        #print(worker3.communicate())
        subprocess.call(["cp /out/new/freetype2/dict1/* /out/new/freetype2/dict/."],shell=True)
        print('done!')
        subprocess.call(["cp -r /out/new/freetype2/dict/ /out/new/dict/"],shell=True)
        print('done!!')        
        #subprocess.call(["cp /out/fuzz-target.dict /out/new/dict/."],shell=True)
        print('done!!!')
        #print 'Copy done!'
        #subprocess.call(["rm -rf /out/new/libpng-1.2.56/dict1"], shell=True)
        #subprocess.call(["cp -r /out/new/libpng-1.2.56/dict /out/new/."],shell=True)
        #print 'Done!'
def main():
    original_stdout = sys.stdout
    build()
    print('Results written, everthing is done!')

if __name__ == '__main__':
    main()
