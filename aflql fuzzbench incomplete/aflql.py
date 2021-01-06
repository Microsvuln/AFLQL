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
        #cleanDir = uninstrumented_build_directory+"_db"
        #subprocess.call(cleancom + [str(cleanDir)],shell=True)
        #subprocess.call(["rm qlpack.yml"],shell=True)
        #subprocess.call(["rm outstr.log"],shell=True)
        #subprocess.call(["rm outlit.log"],shell=True)
        #subprocess.call(["rm -rf dict"],shell=True)
        #subprocess.call(["make clean"],shell=True)
        #exit()
        '''
        command = [
            'codeql',
            'database',
            'create',
            uninstrumented_build_directory + "_db",
            '--language=cpp',  # FIXME: Find the max value allowed here.
            '--command=make'
        ]

        p = subprocess.Popen(command)
        print p.communicate()
        f = open("qlpack.yml", "a")
        f.write("name: " + uninstrumented_build_directory+"\n")
        f.write("version: 0.0.0"+"\n");
        f.write("libraryPathDependencies: codeql-cpp"+"\n")
        f.close()
        print "success"
        command = [
           'codeql',
           'database',
           'upgrade',
           uninstrumented_build_directory + "_db"
        ]
        w = subprocess.Popen(command)
        print w.communicate()
        print "Db upgrade"
        db1 = uninstrumented_build_directory + "_db"
        print "Ok"
        with open("outlit.log", "w") as f:
                stream = os.popen("codeql query run litool.ql -d " + db1 )
                output = stream.read()
                f.write(output)
                f.close()
        print 'scriptlog has been writen ..!'
        #os.makedirs("dict")
        print 'everything is ok ...'
        '''
        command = [
           'python3',
           '/out/new/libpng-1.2.56/litan.py',
           '/out/new/libpng-1.2.56/dict',
           '/out/new/libpng-1.2.56/litout.log'
        ]      
        worker1 = subprocess.Popen(command)
        print(worker1.communicate())
        command1 = [
           'python3',
           '/out/new/libpng-1.2.56/stan.py',
           '/out/new/libpng-1.2.56/dict1',
           '/out/new/libpng-1.2.56/outstr.log'
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
        subprocess.call(["cp /out/new/libpng-1.2.56/dict1/* /out/new/libpng-1.2.56/dict/."],shell=True)
        print('done!')
        subprocess.call(["cp -r /out/new/libpng-1.2.56/dict/ /out/new/dict/"],shell=True)
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
