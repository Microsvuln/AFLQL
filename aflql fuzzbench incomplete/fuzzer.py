# Copyright 2020 Google LLC
#
# Licensed under the Apache License, Version 2.0 (the "License");
# you may not use this file except in compliance with the License.
# You may obtain a copy of the License at
#
# http://www.apache.org/licenses/LICENSE-2.0
#
# Unless required by applicable law or agreed to in writing, software
# distributed under the License is distributed on an "AS IS" BASIS,
# WITHOUT WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied.
# See the License for the specific language governing permissions and
# limitations under the License.
"""Integration code for AFL fuzzer."""

import shutil,os
import subprocess
import sys

from fuzzers import utils

def cp_files_dic():
    src = '/out/new/testcases/'
    dest = '/out/new/dict/'
    src_files = os.listdir(src)
    for file_name in src_files:
        full_file_name = os.path.join(src, file_name)
        if os.path.isfile(full_file_name):
            shutil.copy(full_file_name, dest)


def is_benchmark(name):
    """Check if the benchmark contains the string |name|"""
    benchmark = os.getenv('BENCHMARK', None)
    return benchmark is not None and name in benchmark

def prepare_build_environment():
    """Set environment variables used to build targets for AFL-based
    fuzzers."""
    cflags = ['-fsanitize-coverage=trace-pc-guard']
    utils.append_flags('CFLAGS', cflags)
    utils.append_flags('CXXFLAGS', cflags)

    os.environ['CC'] = 'clang'
    os.environ['CXX'] = 'clang++'
    os.environ['FUZZER_LIB'] = '/libAFL.a'
    

def build():
    """Build benchmark."""
    prepare_build_environment()
    utils.build_benchmark()

    print('[post_build] Copying afl-fuzz to $OUT directory')
    # Copy out the afl-fuzz binary as a build artifact.
    shutil.copy('/afl/afl-fuzz', os.environ['OUT'])
    #shutil.copy('fuzzers/aflql/aflql.py', os.environ['OUT'])
    src = os.getenv('SRC')
    print(src)
    work = os.getenv('WORK')
    #benchmark_name = os.environ['BENCHMARK']
    #shutil.copytree(src,os.environ['OUT']+'/new')
    #if is_benchmark('matio_matio_fuzzer'):
        #os.chdir(os.environ['OUT'])
        #os.chdir(os.environ['SRC'])
        #shutil.copytree(src,os.environ['OUT']+'/new')
        #os.mkdir('/out/new/')
        #shutil.copytree('/src',os.environ['OUT']+'/new')
        #print('Hello matio!')
        #matio_fuzzer
        #shutil.copytree(src,os.environ['OUT']+'/new')
        #shutil.copy('../fuzzers/aflql/build-matio.sh',os.environ['OUT']+'/new/build-matio.sh')
    if is_benchmark('lcms-2017-03-21') :
        shutil.copytree(src,os.environ['OUT']+'/new')
        shutil.copy('fuzzers/aflql/build-lcms.sh',os.environ['OUT']+'/new/build-lcms.sh')
        shutil.copy('fuzzers/aflql/aflql-lcms.py',os.environ['OUT']+'/new/Little-CMS/aflql.py')
        shutil.copy('fuzzers/aflql/dictan-lcms.py',os.environ['OUT']+'/new/dictan.py')
        shutil.copy('fuzzers/aflql/lcms-dict.dict',os.environ['OUT']+'/new/lcms-dict.dict')
        shutil.copy('fuzzers/aflql/stan.py',os.environ['OUT']+'/new/Little-CMS/stan.py')
        shutil.copy('fuzzers/aflql/litan.py',os.environ['OUT']+'/new/Little-CMS/litan.py')
        shutil.copy('fuzzers/aflql/litool.ql',os.environ['OUT']+'/new/Little-CMS/litool.ql')
        shutil.copy('fuzzers/aflql/strtool.ql',os.environ['OUT']+'/new/Little-CMS/strtool.ql')
        shutil.copy('fuzzers/aflql/gentoken.sh',os.environ['OUT']+'/new/gentoken.sh')
        build_script = 'build-lcms.sh'
        os.chdir(os.environ['OUT']+'/new/')
        os.system('chmod +x build-lcms.sh')
        subprocess.check_call(['/bin/bash', build_script])
        print('All ok ...')
        with open('/out/new/target.txt','w') as out:
            line1 = "line 1: "
        print('its okay')
        subprocess.check_call(['python3','/out/new/Little-CMS/aflql.py'])
        subprocess.check_call(['python3','/out/new/dictan.py'])
        build_script2 = 'gentoken.sh'
        os.chdir(os.environ['OUT']+'/new')
        os.mkdir('/out/new/testcases')
        os.system('chmod +x gentoken.sh')
        print('set x flag ok')
        subprocess.check_call(['/bin/bash',build_script2,'/out/cms_transform_fuzzer'])
        print('Token completed')
        os.system('ulimit -S -s unlimited')
        cp_files_dic()
        os.chdir(os.environ['OUT']+'/new/dict')
        os.system('find . -type f -name "*" -size +128c -delete')
        os.system('rm -rf /out/new/testcases')
    if is_benchmark('libjpeg-turbo-07-2017'):
        shutil.copytree(src,os.environ['OUT']+'/new')
        shutil.copy('fuzzers/aflql/build-libjpeg.sh',os.environ['OUT']+'/new/build-libjpeg.sh')
        shutil.copy('fuzzers/aflql/jpeg-dict.dict',os.environ['OUT']+'/new/jpeg-dict.dict')
        shutil.copy('fuzzers/aflql/aflql-libjpeg.py',os.environ['OUT']+'/new/libjpeg-turbo/aflql.py')
        shutil.copy('fuzzers/aflql/dictan-jpeg.py',os.environ['OUT']+'/new/dictan.py')
        shutil.copy('fuzzers/aflql/stan.py',os.environ['OUT']+'/new/libjpeg-turbo/stan.py')
        shutil.copy('fuzzers/aflql/litan.py',os.environ['OUT']+'/new/libjpeg-turbo/litan.py')
        shutil.copy('fuzzers/aflql/litool.ql',os.environ['OUT']+'/new/libjpeg-turbo/litool.ql')
        shutil.copy('fuzzers/aflql/strtool.ql',os.environ['OUT']+'/new/libjpeg-turbo/strtool.ql')
        shutil.copy('fuzzers/aflql/gentoken.sh',os.environ['OUT']+'/new/gentoken.sh')
        build_script = 'build-libjpeg.sh'
        #libjpeg_turbo_fuzzer
        os.chdir(os.environ['OUT']+'/new/')
        os.system('chmod +x build-libjpeg.sh')
        subprocess.check_call(['/bin/bash', build_script])
        print('All ok ...')
        with open('/out/new/target.txt','w') as out:
            line1 = "line 1: "
        print('its okay')
        subprocess.check_call(['python3','/out/new/libjpeg-turbo/aflql.py'])
        subprocess.check_call(['python3','/out/new/dictan.py'])
        build_script2 = 'gentoken.sh'
        os.chdir(os.environ['OUT']+'/new')
        os.mkdir('/out/new/testcases')
        os.system('chmod +x gentoken.sh')
        print('set x flag ok')
        subprocess.check_call(['/bin/bash',build_script2,'/out/libjpeg_turbo_fuzzer'])
        print('Token completed')
        os.system('ulimit -S -s unlimited')
        cp_files_dic()
        os.chdir(os.environ['OUT']+'/new/dict')
        os.system('find . -type f -name "*" -size +128c -delete')
        os.system('rm -rf /out/new/testcases')
    if is_benchmark('libpcap_fuzz_both'):
        shutil.copytree(src,os.environ['OUT']+'/new')
        shutil.copy('fuzzers/aflql/build-libpcap.sh',os.environ['OUT']+'/new/build-libpcap.sh')
        shutil.copy('fuzzers/aflql/aflql-libpcap.py',os.environ['OUT']+'/new/libpcap/aflql.py')
        shutil.copy('fuzzers/aflql/stan.py',os.environ['OUT']+'/new/libpcap/stan.py')
        shutil.copy('fuzzers/aflql/litan.py',os.environ['OUT']+'/new/libpcap/litan.py')
        shutil.copy('fuzzers/aflql/litool.ql',os.environ['OUT']+'/new/libpcap/litool.ql')
        shutil.copy('fuzzers/aflql/strtool.ql',os.environ['OUT']+'/new/libpcap/strtool.ql')
        shutil.copy('fuzzers/aflql/gentoken.sh',os.environ['OUT']+'/new/gentoken.sh')
        build_script = 'build-libpcap.sh'
        os.chdir(os.environ['OUT']+'/new/')
        os.system('chmod +x build-libpcap.sh')
        subprocess.check_call(['/bin/bash', build_script])
        print('All ok ...')
        with open('/out/new/target.txt','w') as out:
            line1 = "line 1: "
        print('All ok ...')
        subprocess.check_call(['python3','/out/new/libpcap/aflql.py'])
        build_script2 = 'gentoken.sh'
        os.chdir(os.environ['OUT']+'/new')
        os.mkdir('/out/new/testcases')
        os.system('chmod +x gentoken.sh')
        print('set x flag ok')
        subprocess.check_call(['/bin/bash',build_script2,'/out/fuzz_both'])
        print('Token completed')
        os.system('ulimit -S -s unlimited')
        cp_files_dic()
        os.chdir(os.environ['OUT']+'/new/dict')
        os.system('find . -type f -name "*" -size +128c -delete')
        os.system('rm -rf /out/new/testcases')
    if is_benchmark('jsoncpp_jsoncpp_fuzzer'):
        shutil.copytree(src,os.environ['OUT']+'/new')
        shutil.copy('../fuzzers/aflql/build-jsoncpp.sh',os.environ['OUT']+'/new/build-jsoncpp.sh')
        shutil.copy('../fuzzers/aflql/stan.py',os.environ['OUT']+'/new/jsoncpp/stan.py')
        shutil.copy('../fuzzers/aflql/litan.py',os.environ['OUT']+'/new/jsoncpp/litan.py')
        shutil.copy('../fuzzers/aflql/litool.ql',os.environ['OUT']+'/new/jsoncpp/litool.ql')
        shutil.copy('../fuzzers/aflql/strtool.ql',os.environ['OUT']+'/new/jsoncpp/strtool.ql')
        shutil.copy('../fuzzers/aflql/aflql-jsoncpp.py',os.environ['OUT']+'/new/jsoncpp/aflql.py')
        shutil.copy('../fuzzers/aflql/jsoncpp-dict.dict',os.environ['OUT']+'/new/jsoncpp-dict.dict')
        shutil.copy('../fuzzers/aflql/dictan-jsoncpp.py',os.environ['OUT']+'/new/dictan.py')
        shutil.copy('../fuzzers/aflql/gentoken.sh',os.environ['OUT']+'/new/gentoken.sh')
        build_script = 'build-jsoncpp.sh'
        os.chdir(os.environ['OUT']+'/new/')
        os.system('chmod +x build-jsoncpp.sh')
        subprocess.check_call(['/bin/bash', build_script])
        print('All ok ...')
        with open('/out/new/target.txt','w') as out:
            line1 = "line 1: "
        print('All ok ...')
        subprocess.check_call(['python3','/out/new/jsoncpp/aflql.py'])
        subprocess.check_call(['python3','/out/new/dictan.py'])
        build_script2 = 'gentoken.sh'
        os.chdir(os.environ['OUT']+'/new')
        os.mkdir('/out/new/testcases')
        os.system('chmod +x gentoken.sh')
        print('set x flag ok')
        subprocess.check_call(['/bin/bash',build_script2,'/out/jsoncpp_fuzzer'])
        print('Token completed')
        os.system('ulimit -S -s unlimited')
        cp_files_dic()
        os.chdir(os.environ['OUT']+'/new/dict')
        os.system('find . -type f -name "*" -size +128c -delete')
        os.system('rm -rf /out/new/testcases')
        #fuzzers/aflql/build-jsoncpp.sh
    if is_benchmark('libxml2-v2.9.2'):
        shutil.copytree(src,os.environ['OUT']+'/new')
        shutil.copy('fuzzers/aflql/build-libxml2.sh',os.environ['OUT']+'/new/build-libxml2.sh')
        shutil.copy('fuzzers/aflql/aflql-libxml.py',os.environ['OUT']+'/new/libxml2/aflql.py')
        shutil.copy('fuzzers/aflql/stan.py',os.environ['OUT']+'/new/libxml2/stan.py')
        shutil.copy('fuzzers/aflql/stan.py',os.environ['OUT']+'/new/libxml2/litan.py')
        shutil.copy('fuzzers/aflql/litool.ql',os.environ['OUT']+'/new/libxml2/litool.ql')
        shutil.copy('fuzzers/aflql/strtool.ql',os.environ['OUT']+'/new/libxml2/strtool.ql')
        shutil.copy('fuzzers/aflql/dictan-libxml.py',os.environ['OUT']+'/new/dictan.py')
        shutil.copy('fuzzers/aflql/libxml-dict.dict',os.environ['OUT']+'/new/libxml-dict.dict')
        shutil.copy('fuzzers/aflql/gentoken.sh',os.environ['OUT']+'/new/gentoken.sh')
        build_script = 'build-libxml2.sh'
        os.chdir(os.environ['OUT']+'/new/')
        os.system('chmod +x build-libxml2.sh')
        subprocess.check_call(['/bin/bash', build_script])
        print('All ok ...')
        with open('/out/new/target.txt','w') as out:
            line1 = "line 1: "
        print('All ok ...')
        subprocess.check_call(['python3','/out/new/libxml2/aflql.py'])
        subprocess.check_call(['python3','/out/new/dictan.py'])
        build_script2 = 'gentoken.sh'
        os.chdir(os.environ['OUT']+'/new')
        os.mkdir('/out/new/testcases')
        os.system('chmod +x gentoken.sh')
        print('set x flag ok')
        subprocess.check_call(['/bin/bash',build_script2,'/out/xml'])
        print('Token completed')
        os.system('ulimit -S -s unlimited')
        cp_files_dic()
        os.chdir(os.environ['OUT']+'/new/dict')
        os.system('find . -type f -name "*" -size +128c -delete')
        os.system('rm -rf /out/new/testcases')
    if is_benchmark('libxslt_xpath'):
        shutil.copytree(src,os.environ['OUT']+'/new')
        shutil.copy('../fuzzers/aflql/build-libxslt.sh',os.environ['OUT']+'/new/build-libxslt.sh')
        shutil.copy('../fuzzers/aflql/litan.py',os.environ['OUT']+'/new/libxslt/litan.py')
        shutil.copy('../fuzzers/aflql/aflql-libexslt.py',os.environ['OUT']+'/new/libxslt/aflql.py')
        shutil.copy('../fuzzers/aflql/stan.py',os.environ['OUT']+'/new/libxslt/stan.py')
        shutil.copy('../fuzzers/aflql/litool.ql',os.environ['OUT']+'/new/libxslt/litool.ql')
        shutil.copy('../fuzzers/aflql/strtool.ql',os.environ['OUT']+'/new/libxslt/strtool.ql')
        shutil.copy('../fuzzers/aflql/dictan-libxslt.py',os.environ['OUT']+'/new/dictan.py')
        shutil.copy('../fuzzers/aflql/libxslt-dict.dict',os.environ['OUT']+'/new/libxslt-dict.dict')
        shutil.copy('../fuzzers/aflql/gentoken.sh',os.environ['OUT']+'/new/gentoken.sh')
        build_script = 'build-libxslt.sh'
        os.chdir(os.environ['OUT']+'/new/')
        os.system('chmod +x build-libxslt.sh')
        subprocess.check_call(['/bin/bash', build_script])
        print('All ok ...')
        with open('/out/new/target.txt','w') as out:
            line1 = "line 1: "
        print('All ok ...')
        subprocess.check_call(['python3','/out/new/libxslt/aflql.py'])
        subprocess.check_call(['python3','/out/new/dictan.py'])
        build_script2 = 'gentoken.sh'
        os.chdir(os.environ['OUT']+'/new')
        os.system('chmod +x gentoken.sh')
        os.mkdir('/out/new/testcases')
        print('set x flag ok')
        subprocess.check_call(['/bin/bash',build_script2,'/out/xpath'])
        print('Token completed')
        os.system('ulimit -S -s unlimited')
        cp_files_dic()
        os.chdir(os.environ['OUT']+'/new/dict')
        os.system('find . -type f -name "*" -size +128c -delete')
        os.system('rm -rf /out/new/testcases')
    if is_benchmark('mbedtls_fuzz_dtlsclient'):
        shutil.copytree(src,os.environ['OUT']+'/new')
        shutil.copy('../fuzzers/aflql/build-mbedtls.sh',os.environ['OUT']+'/new/build-mbedtls.sh')
        shutil.copy('../fuzzers/aflql/litan.py',os.environ['OUT']+'/new/mbedtls/litan.py')
        shutil.copy('../fuzzers/aflql/aflql-mbedtls.py',os.environ['OUT']+'/new/mbedtls/aflql.py')
        shutil.copy('../fuzzers/aflql/stan.py',os.environ['OUT']+'/new/mbedtls/stan.py')
        shutil.copy('../fuzzers/aflql/litool.ql',os.environ['OUT']+'/new/mbedtls/litool.ql')
        shutil.copy('../fuzzers/aflql/strtool.ql',os.environ['OUT']+'/new/mbedtls/strtool.ql')
        shutil.copy('../fuzzers/aflql/gentoken.sh',os.environ['OUT']+'/new/gentoken.sh')
        build_script = 'build-mbedtls.sh'
        os.chdir(os.environ['OUT']+'/new/')
        os.system('chmod +x build-mbedtls.sh')
        subprocess.check_call(['/bin/bash', build_script])
        print('All ok ...')
        with open('/out/new/target.txt','w') as out:
            line1 = "line 1: "
        print('All ok ...')
        subprocess.check_call(['python3','/out/new/mbedtls/aflql.py'])
        build_script2 = 'gentoken.sh'
        os.chdir(os.environ['OUT']+'/new')
        os.mkdir('/out/new/testcases')
        os.system('chmod +x gentoken.sh')
        print('set x flag ok')
        subprocess.check_call(['/bin/bash',build_script2,'/out/fuzz_dtlsclient'])
        print('Token completed')
        os.system('ulimit -S -s unlimited')
        cp_files_dic()
        os.chdir(os.environ['OUT']+'/new/dict')
        os.system('find . -type f -name "*" -size +128c -delete')
        os.system('rm -rf /out/new/testcases')
    if is_benchmark('sqlite3_ossfuzz'):
        shutil.copytree(src,os.environ['OUT']+'/new')
        shutil.copy('../fuzzers/aflql/build-sqlite.sh',os.environ['OUT']+'/new/build-sqlite.sh')
        shutil.copy('../fuzzers/aflql/litan.py',os.environ['OUT']+'/new/sqlite3/litan.py')
        shutil.copy('../fuzzers/aflql/aflql-sqlite.py',os.environ['OUT']+'/new/sqlite3/aflql.py')
        shutil.copy('../fuzzers/aflql/stan.py',os.environ['OUT']+'/new/sqlite3/stan.py')
        shutil.copy('../fuzzers/aflql/litool.ql',os.environ['OUT']+'/new/sqlite3/litool.ql')
        shutil.copy('../fuzzers/aflql/strtool.ql',os.environ['OUT']+'/new/sqlite3/strtool.ql')
        shutil.copy('../fuzzers/aflql/sqlite-dict.dict',os.environ['OUT']+'/new/sqlite-dict.dict')
        shutil.copy('../fuzzers/aflql/dictan-sqlite.py',os.environ['OUT']+'/new/dictan.py')
        shutil.copy('../fuzzers/aflql/gentoken.sh',os.environ['OUT']+'/new/gentoken.sh')
        build_script = 'build-sqlite.sh'
        os.chdir(os.environ['OUT']+'/new/')
        os.system('chmod +x build-sqlite.sh')
        subprocess.check_call(['/bin/bash', build_script])
        print('All ok ...')
        with open('/out/new/target.txt','w') as out:
            line1 = "line 1: "
        print('All ok ...')        
        subprocess.check_call(['python3','/out/new/sqlite3/aflql.py'])
        subprocess.check_call(['python3','/out/new/dictan.py'])
        build_script2 = 'gentoken.sh'
        os.chdir(os.environ['OUT']+'/new')
        os.mkdir('/out/new/testcases')
        os.system('chmod +x gentoken.sh')
        print('set x flag ok')
        subprocess.check_call(['/bin/bash',build_script2,'/out/ossfuzz'])        
        print('Token completed')
        os.system('ulimit -S -s unlimited')
        cp_files_dic()
        os.chdir(os.environ['OUT']+'/new/dict')
        os.system('find . -type f -name "*" -size +128c -delete')
        os.system('rm -rf /out/new/testcases')
        #shutil.copy('../fuzzers/aflql/litan.py',os.environ['OUT']+'/new/vorbis/litan.py')
    if is_benchmark('vorbis-2017-12-11') :
        print('vorbis bench')
        shutil.copytree(src,os.environ['OUT']+'/new')
        shutil.copy('fuzzers/aflql/build-vorbis.sh',os.environ['OUT']+'/new/build-vorbis.sh')
        shutil.copy('fuzzers/aflql/litan.py',os.environ['OUT']+'/new/vorbis/litan.py')
        shutil.copy('fuzzers/aflql/aflql-vorbis.py',os.environ['OUT']+'/new/vorbis/aflql.py')
        shutil.copy('fuzzers/aflql/stan.py',os.environ['OUT']+'/new/vorbis/stan.py')
        shutil.copy('fuzzers/aflql/litool.ql',os.environ['OUT']+'/new/vorbis/litool.ql')
        shutil.copy('fuzzers/aflql/strtool.ql',os.environ['OUT']+'/new/vorbis/strtool.ql')
        shutil.copy('fuzzers/aflql/gentoken.sh',os.environ['OUT']+'/new/gentoken.sh')
        build_script = 'build-vorbis.sh'
        os.chdir(os.environ['OUT']+'/new/')
        os.system('chmod +x build-vorbis.sh')
        subprocess.check_call(['/bin/bash', build_script])
        print('All ok ...')
        with open('/out/new/target.txt','w') as out:
            line1 = "line 1: "
        print('All ok ...')
        subprocess.check_call(['python3','/out/new/vorbis/aflql.py'])
        build_script2 = 'gentoken.sh'
        os.chdir(os.environ['OUT']+'/new')
        os.mkdir('/out/new/testcases')
        os.system('chmod +x gentoken.sh')
        print('set x flag ok')
        subprocess.check_call(['/bin/bash',build_script2,'/out/decode_fuzzer'])
        print('Token completed')
        os.system('ulimit -S -s unlimited')
        cp_files_dic()
        os.chdir(os.environ['OUT']+'/new/dict')
        os.system('find . -type f -name "*" -size +128c -delete')
        os.system('rm -rf /out/new/testcases')
        # decode_fuzzer
    #fuzzers/aflql/build-vorbis.sh
    if is_benchmark('systemd_fuzz-link-parser'):
        shutil.copytree(src,os.environ['OUT']+'/new')
        shutil.copy('../fuzzers/aflql/build-systemd.sh',os.environ['OUT']+'/new/build-systemd.sh')
        shutil.copy('../fuzzers/aflql/gentoken.sh',os.environ['OUT']+'/new/gentoken.sh')
        build_script = 'build-systemd.sh'
        os.chdir(os.environ['OUT']+'/new/')
        os.system('chmod +x build-systemd.sh')
        subprocess.check_call(['/bin/bash', build_script])
        build_script2 = 'gentoken.sh'
        os.chdir(os.environ['OUT']+'/new')
        os.mkdir('/out/new/testcases')
        os.mkdir('/out/new/dict')
        os.system('chmod +x gentoken.sh')
        print('set x flag ok')
        subprocess.check_call(['/bin/bash',build_script2,'/out/fuzz-link-parser'])
        print('Token completed')
        os.system('ulimit -S -s unlimited')
        cp_files_dic()
        os.chdir(os.environ['OUT']+'/new/dict')
        os.system('find . -type f -name "*" -size +128c -delete')
        os.system('rm -rf /out/new/testcases')
        #fuzz-link-parser
        #subprocess.check_call(['/bin/bash', build_script])
        #shutil.copy('fuzzers/aflql/litan.py',os.environ['OUT']+'/new/woff2/litan.py')


    if is_benchmark('woff2-2016-05-06'):
        shutil.copytree(src,os.environ['OUT']+'/new')
        shutil.copy('fuzzers/aflql/build-woff.sh',os.environ['OUT']+'/new/build-woff.sh')
        shutil.copy('fuzzers/aflql/litan.py',os.environ['OUT']+'/new/woff2/litan.py')
        shutil.copy('fuzzers/aflql/aflql-woff2.py',os.environ['OUT']+'/new/woff2/aflql.py')
        shutil.copy('fuzzers/aflql/stan.py',os.environ['OUT']+'/new/woff2/stan.py')
        shutil.copy('fuzzers/aflql/litool.ql',os.environ['OUT']+'/new/woff2/litool.ql')
        shutil.copy('fuzzers/aflql/strtool.ql',os.environ['OUT']+'/new/woff2/strtool.ql')
        shutil.copy('fuzzers/aflql/gentoken.sh',os.environ['OUT']+'/new/gentoken.sh')
        build_script = 'build-woff.sh'
        os.chdir(os.environ['OUT']+'/new/')
        os.system('chmod +x build-woff.sh')
        subprocess.check_call(['/bin/bash', build_script])        
        print('All ok ...')
        subprocess.check_call(['python3','/out/new/woff2/aflql.py'])
        build_script2 = 'gentoken.sh'
        os.chdir(os.environ['OUT']+'/new')
        os.mkdir('/out/new/testcases')
        os.system('chmod +x gentoken.sh')
        print('set x flag ok')
        subprocess.check_call(['/bin/bash',build_script2,'/out/convert_woff2ttf_fuzzer'])
        print('Token completed')
        os.system('ulimit -S -s unlimited')
        cp_files_dic()
        os.chdir(os.environ['OUT']+'/new/dict')
        os.system('find . -type f -name "*" -size +128c -delete')
        os.system('rm -rf /out/new/testcases')

    if is_benchmark('zlib_zlib_uncompress_fuzzer'):
        shutil.copytree(src,os.environ['OUT']+'/new')            
        shutil.copy('../fuzzers/aflql/build-zlib.sh',os.environ['OUT']+'/new/build-zlib.sh')
        shutil.copy('../fuzzers/aflql/litan.py',os.environ['OUT']+'/new/zlib/litan.py')
        shutil.copy('../fuzzers/aflql/aflql-zlib.py',os.environ['OUT']+'/new/zlib/aflql.py')
        shutil.copy('../fuzzers/aflql/stan.py',os.environ['OUT']+'/new/zlib/stan.py')
        shutil.copy('../fuzzers/aflql/litool.ql',os.environ['OUT']+'/new/zlib/litool.ql')
        shutil.copy('../fuzzers/aflql/strtool.ql',os.environ['OUT']+'/new/zlib/strtool.ql')
        shutil.copy('../fuzzers/aflql/gentoken.sh',os.environ['OUT']+'/new/gentoken.sh')
        build_script = 'build-zlib.sh'
        os.chdir(os.environ['OUT']+'/new/')
        os.system('chmod +x build-zlib.sh')
        subprocess.check_call(['/bin/bash', build_script])
        with open('/out/new/target.txt','w') as out:
            line1 = "line 1: "
        print('All ok ...')
        subprocess.check_call(['python3','/out/new/zlib/aflql.py'])
        #zlib_uncompress_fuzzer
        build_script2 = 'gentoken.sh'
        os.chdir(os.environ['OUT']+'/new')
        os.mkdir('/out/new/testcases')
        os.system('chmod +x gentoken.sh')
        print('set x flag ok')
        subprocess.check_call(['/bin/bash',build_script2,'/out/zlib_uncompress_fuzzer'])
        print('Token completed')
        os.system('ulimit -S -s unlimited')
        cp_files_dic()
        os.chdir(os.environ['OUT']+'/new/dict')
        os.system('find . -type f -name "*" -size +128c -delete')
        os.system('rm -rf /out/new/testcases')

        

    if is_benchmark('re2-2014-12-09'):
        shutil.copytree(src,os.environ['OUT']+'/new')
        shutil.copy('fuzzers/aflql/build-re2.sh',os.environ['OUT']+'/new/build-re2.sh')
        shutil.copy('fuzzers/aflql/litan.py',os.environ['OUT']+'/new/re2/litan.py')
        shutil.copy('fuzzers/aflql/stan.py',os.environ['OUT']+'/new/re2/stan.py')
        shutil.copy('fuzzers/aflql/litool.ql',os.environ['OUT']+'/new/re2/litool.ql')
        shutil.copy('fuzzers/aflql/strtool.ql',os.environ['OUT']+'/new/re2/strtool.ql')
        shutil.copy('fuzzers/aflql/aflql-re2.py',os.environ['OUT']+'/new/re2/aflql.py')
        shutil.copy('fuzzers/aflql/re2-dict.dict',os.environ['OUT']+'/new/re2-dict.dict')
        shutil.copy('fuzzers/aflql/dictan-re2.py',os.environ['OUT']+'/new/dictan.py')
        shutil.copy('fuzzers/aflql/gentoken.sh',os.environ['OUT']+'/new/gentoken.sh')
        print('Ok!')
        build_script = 'build-re2.sh'
        os.chdir(os.environ['OUT']+'/new/')
        os.system('chmod +x build-re2.sh')
        subprocess.check_call(['/bin/bash', build_script])
        print('Ok!')
        subprocess.check_call(['python3','/out/new/re2/aflql.py'])
        subprocess.check_call(['python3','/out/new/dictan.py'])
        build_script2 = 'gentoken.sh'
        os.chdir(os.environ['OUT']+'/new')
        os.mkdir('/out/new/testcases')
        os.system('chmod +x gentoken.sh')
        print('set x flag ok')
        subprocess.check_call(['/bin/bash',build_script2,'/out/fuzzer'])
        print('Token completed')
        os.system('ulimit -S -s unlimited')
        cp_files_dic()
        os.chdir(os.environ['OUT']+'/new/dict')
        os.system('find . -type f -name "*" -size +128c -delete')
        os.system('rm -rf /out/new/testcases')
        #fuzzer

    if is_benchmark('proj4-2017-08-14'):
        shutil.copytree(src,os.environ['OUT']+'/new')
        shutil.copy('fuzzers/aflql/build-proj.sh',os.environ['OUT']+'/new/build-proj.sh')
        shutil.copy('fuzzers/aflql/litan.py',os.environ['OUT']+'/new/PROJ/litan.py')
        shutil.copy('fuzzers/aflql/stan.py',os.environ['OUT']+'/new/PROJ/stan.py')
        shutil.copy('fuzzers/aflql/litool.ql',os.environ['OUT']+'/new/PROJ/litool.ql')
        shutil.copy('fuzzers/aflql/strtool.ql',os.environ['OUT']+'/new/PROJ/strtool.ql')
        shutil.copy('fuzzers/aflql/aflql-proj.py',os.environ['OUT']+'/new/PROJ/aflql.py')
        shutil.copy('fuzzers/aflql/dict-proj.dict',os.environ['OUT']+'/new/dict-proj.dict')
        shutil.copy('fuzzers/aflql/dictan-proj.py',os.environ['OUT']+'/new/dictan.py')
        shutil.copy('fuzzers/aflql/gentoken.sh',os.environ['OUT']+'/new/gentoken.sh')
        os.chdir(os.environ['OUT']+'/new/')        
        os.system('chmod +x build-proj.sh')
        build_script = 'build-proj.sh'
        subprocess.check_call(['/bin/bash', build_script])
        with open('/out/new/target.txt','w') as out:
            line1 = "line 1: "
        print('All ok ...')
        #subprocess.check_call(['python3','/out/new/dictan.py'])
        subprocess.check_call(['python3','/out/new/PROJ/aflql.py'])
        print('DONE')
        subprocess.check_call(['python3','/out/new/dictan.py'])
        #standard_fuzzer
        build_script2 = 'gentoken.sh'
        os.chdir(os.environ['OUT']+'/new')
        os.mkdir('/out/new/testcases')
        os.system('chmod +x gentoken.sh')
        print('set x flag ok')
        subprocess.check_call(['/bin/bash',build_script2,'/out/standard_fuzzer'])
        print('Token completed')
        os.system('ulimit -S -s unlimited')
        cp_files_dic()
        os.chdir(os.environ['OUT']+'/new/dict')
        os.system('find . -type f -name "*" -size +128c -delete')
        os.system('rm -rf /out/new/testcases')

    if is_benchmark('openthread-2019-12-23'):
        print('Hello OpenThread')
        shutil.copytree(src,os.environ['OUT']+'/new')
        shutil.copy('fuzzers/aflql/build-openthread.sh',os.environ['OUT']+'/new/build-openthread.sh')
        #shutil.copy('fuzzers/aflql/dictan-php.py',os.environ['OUT']+'/new/dictan.py')
        shutil.copy('fuzzers/aflql/litan.py',os.environ['OUT']+'/new/openthread/litan.py')
        shutil.copy('fuzzers/aflql/stan.py',os.environ['OUT']+'/new/openthread/stan.py')
        shutil.copy('fuzzers/aflql/litool.ql',os.environ['OUT']+'/new/openthread/litool.ql')        
        shutil.copy('fuzzers/aflql/strtool.ql',os.environ['OUT']+'/new/openthread/strtool.ql')
        shutil.copy('fuzzers/aflql/aflql-openthread.py',os.environ['OUT']+'/new/openthread/aflql.py')
        shutil.copy('fuzzers/aflql/gentoken.sh',os.environ['OUT']+'/new/gentoken.sh')
        #shutil.copy('../fuzzers/aflql/dictan-proj.py',os.environ['OUT']+'/new/dictan.py')
        os.chdir(os.environ['OUT']+'/new/')
        os.system('chmod +x build-openthread.sh')
        build_script = 'build-openthread.sh'
        subprocess.check_call(['/bin/bash', build_script])
        with open('/out/new/target.txt','w') as out:
            line1 = "line 1: "
        print('All ok ...')
        subprocess.check_call(['python3','/out/new/openthread/aflql.py'])
        # ip6-send-fuzzer
        build_script2 = 'gentoken.sh'
        os.chdir(os.environ['OUT']+'/new')
        os.mkdir('/out/new/testcases')
        os.system('chmod +x gentoken.sh')
        print('set x flag ok')
        subprocess.check_call(['/bin/bash',build_script2,'/out/ip6-send-fuzzer'])
        print('Token completed')
        os.system('ulimit -S -s unlimited')
        cp_files_dic()
        os.chdir(os.environ['OUT']+'/new/dict')
        os.system('find . -type f -name "*" -size +128c -delete')
        os.system('rm -rf /out/new/testcases')
    if is_benchmark('php_php-fuzz-parser'):
        print('Hello PHP')
        shutil.copytree(src,os.environ['OUT']+'/new')
        shutil.copy('../fuzzers/aflql/build-php.sh',os.environ['OUT']+'/new/build-php.sh')
        shutil.copy('../fuzzers/aflql/dictan-php.py',os.environ['OUT']+'/new/dictan.py')
        shutil.copy('../fuzzers/aflql/litan.py',os.environ['OUT']+'/new/php-src/litan.py')
        shutil.copy('../fuzzers/aflql/stan.py',os.environ['OUT']+'/new/php-src/stan.py')
        shutil.copy('../fuzzers/aflql/litool.ql',os.environ['OUT']+'/new/php-src/litool.ql')
        shutil.copy('../fuzzers/aflql/php-dict.dict',os.environ['OUT']+'/new/php.dict')
        shutil.copy('../fuzzers/aflql/strtool.ql',os.environ['OUT']+'/new/php-src/strtool.ql')
        shutil.copy('../fuzzers/aflql/aflql-php.py',os.environ['OUT']+'/new/php-src/aflql.py')
        os.chdir(os.environ['OUT']+'/new/')
        os.system('chmod +x build-php.sh')
        build_script = 'build-php.sh'
        subprocess.check_call(['/bin/bash', build_script])
        with open('/out/new/target.txt','w') as out:
            line1 = "line 1: "
        print('All ok ...')
        subprocess.check_call(['python3','/out/new/php-src/aflql.py'])
        subprocess.check_call(['python3','/out/new/dictan.py'])
        os.chdir(os.environ['OUT']+'/new/dict')
        os.system('find . -type f -name "*" -size +128c -delete')
        os.system('rm -rf /out/new/testcases')
    #utils.build_benchmark()
    if is_benchmark('openssl_x509'):
        print('Hello x509')
        shutil.copytree(src,os.environ['OUT']+'/new')
        shutil.copy('../fuzzers/aflql/build-x509.sh',os.environ['OUT']+'/new/build-x509.sh')
        shutil.copy('../fuzzers/aflql/dictan-x509.py',os.environ['OUT']+'/new/dictan.py')
        shutil.copy('../fuzzers/aflql/x509.dict',os.environ['OUT']+'/new/x509.dict')
        shutil.copy('../fuzzers/aflql/litan.py',os.environ['OUT']+'/new/openssl/litan.py')
        shutil.copy('../fuzzers/aflql/stan.py',os.environ['OUT']+'/new/openssl/stan.py')
        shutil.copy('../fuzzers/aflql/litool.ql',os.environ['OUT']+'/new/openssl/litool.ql')
        shutil.copy('../fuzzers/aflql/strtool.ql',os.environ['OUT']+'/new/openssl/strtool.ql')
        shutil.copy('../fuzzers/aflql/aflql-x509.py',os.environ['OUT']+'/new/openssl/aflql.py')
        shutil.copy('../fuzzers/aflql/gentoken.sh',os.environ['OUT']+'/new/gentoken.sh')
        os.chdir(os.environ['OUT']+'/new/')
        os.system('chmod +x build-x509.sh')
        build_script = 'build-x509.sh'
        subprocess.check_call(['/bin/bash', build_script])
        with open('/out/new/target.txt','w') as out:
            line1 = "line 1: "
        print('All ok ...')
        subprocess.check_call(['python3','/out/new/openssl/aflql.py'])
        subprocess.check_call(['python3','/out/new/dictan.py'])
        build_script2 = 'gentoken.sh'
        os.chdir(os.environ['OUT']+'/new')
        os.mkdir('/out/new/testcases')
        os.system('chmod +x gentoken.sh')
        print('set x flag ok')
        subprocess.check_call(['/bin/bash',build_script2,'/out/x509'])
        print('Token completed')
        os.system('ulimit -S -s unlimited')
        cp_files_dic()
        os.chdir(os.environ['OUT']+'/new/dict')
        os.system('find . -type f -name "*" -size +128c -delete')
        os.system('rm -rf /out/new/testcases')
    if is_benchmark('harfbuzz-1.3.2'):
        print('Hello harfbuzz')
        shutil.copytree(src,os.environ['OUT']+'/new')
        shutil.copy('fuzzers/aflql/build-harfbuzz.sh',os.environ['OUT']+'/new/build-harfbuzz.sh')
        shutil.copy('fuzzers/aflql/litan.py',os.environ['OUT']+'/new/harfbuzz/litan.py')
        shutil.copy('fuzzers/aflql/stan.py',os.environ['OUT']+'/new/harfbuzz/stan.py')
        shutil.copy('fuzzers/aflql/litool.ql',os.environ['OUT']+'/new/harfbuzz/litool.ql')
        shutil.copy('fuzzers/aflql/strtool.ql',os.environ['OUT']+'/new/harfbuzz/strtool.ql')
        shutil.copy('fuzzers/aflql/aflql-harf.py',os.environ['OUT']+'/new/harfbuzz/aflql.py')
        shutil.copy('fuzzers/aflql/gentoken.sh',os.environ['OUT']+'/new/gentoken.sh')
        #hb-shape-fuzzer
        with open('/out/new/target.txt','w') as out:
            line1 = "line 1: "
        os.chdir(os.environ['OUT']+'/new/')
        os.system('chmod +x build-harfbuzz.sh')
        build_script = 'build-harfbuzz.sh'
        subprocess.check_call(['/bin/bash', '-ex', build_script])        
        subprocess.check_call(['python3','/out/new/harfbuzz/aflql.py'])
        build_script2 = 'gentoken.sh'
        os.chdir(os.environ['OUT']+'/new')
        os.mkdir('/out/new/testcases')
        os.system('chmod +x gentoken.sh')
        print('set x flag ok')
        subprocess.check_call(['/bin/bash',build_script2,'/out/hb-shape-fuzzer'])
        print('Token completed')
        os.system('ulimit -S -s unlimited')
        cp_files_dic()
        os.chdir(os.environ['OUT']+'/new/dict')
        os.system('find . -type f -name "*" -size +127c -delete')
        os.system('rm -rf /out/new/testcases')
    if is_benchmark('freetype2-2017'):
        print('Hello freetype !')
        shutil.copytree(src,os.environ['OUT']+'/new')
        shutil.copy('fuzzers/aflql/build-freetype.sh',os.environ['OUT']+'/new/build-freetype.sh')
        shutil.copy('fuzzers/aflql/litan.py',os.environ['OUT']+'/new/freetype2/litan.py')
        shutil.copy('fuzzers/aflql/stan.py',os.environ['OUT']+'/new/freetype2/stan.py')
        shutil.copy('fuzzers/aflql/litool.ql',os.environ['OUT']+'/new/freetype2/litool.ql')
        shutil.copy('fuzzers/aflql/strtool.ql',os.environ['OUT']+'/new/freetype2/strtool.ql')
        shutil.copy('fuzzers/aflql/aflql-freetype.py',os.environ['OUT']+'/new/freetype2/aflql.py')
        shutil.copy('fuzzers/aflql/gentoken.sh',os.environ['OUT']+'/new/gentoken.sh')
        with open('/out/new/target.txt','w') as out:
            line1 = "line 1: "
        os.chdir(os.environ['OUT']+'/new/')
        os.system('chmod +x build-freetype.sh')
        build_script = 'build-freetype.sh'
        subprocess.check_call(['/bin/bash',build_script])
        subprocess.check_call(['python3','/out/new/freetype2/aflql.py'])
        # ftfuzzer
        build_script2 = 'gentoken.sh'
        os.chdir(os.environ['OUT']+'/new')
        os.mkdir('/out/new/testcases')
        os.system('chmod +x gentoken.sh')
        print('set x flag ok')
        subprocess.check_call(['/bin/bash',build_script2,'/out/ftfuzzer'])
        print('Token completed')
        os.system('ulimit -S -s unlimited')
        cp_files_dic()
        os.chdir(os.environ['OUT']+'/new/dict')
        os.system('find . -type f -name "*" -size +127c -delete')
        os.system('rm -rf /out/new/testcases')


        #build-freetype.sh
    if is_benchmark('curl_curl_fuzzer_http'):
        print('Hello curl!')
        shutil.copytree(src,os.environ['OUT']+'/new')
        # fuzzers/aflql/build-curl.sh
        shutil.copy('../fuzzers/aflql/build-curl.sh',os.environ['OUT']+'/new/build-curl.sh')
        shutil.copy('../fuzzers/aflql/litan.py',os.environ['OUT']+'/new/curl/litan.py')
        shutil.copy('../fuzzers/aflql/stan.py',os.environ['OUT']+'/new/curl/stan.py')
        shutil.copy('../fuzzers/aflql/litool.ql',os.environ['OUT']+'/new/curl/litool.ql')
        shutil.copy('../fuzzers/aflql/strtool.ql',os.environ['OUT']+'/new/curl/strtool.ql')
        shutil.copy('../fuzzers/aflql/aflql-curl.py',os.environ['OUT']+'/new/curl/aflql.py')
        shutil.copy('../fuzzers/aflql/curl-http.dict', os.environ['OUT']+'/new/curl-http.dict')
        shutil.copy('../fuzzers/aflql/dictan-curl.py',os.environ['OUT']+'/new/dictan.py')
        shutil.copy('../fuzzers/aflql/gentoken.sh',os.environ['OUT']+'/new/gentoken.sh')
        #curl-http.dict
        with open('/out/new/target.txt','w') as out:
            line1 = "line 1: "
            line2 = "line 2: "
            line3 = "line 3: "
            print("I'm going to write these to the file.")
            out.write('{}\n{}\n{}\n'.format(line1,line2,line3))
        print('Done!')
        os.chdir(os.environ['OUT']+'/new/')
        os.system('chmod +x build-curl.sh')
        build_script = 'build-curl.sh'
        subprocess.check_call(['/bin/bash',build_script])
        print('All ok')
        subprocess.check_call(['python3','/out/new/curl/aflql.py'])
        subprocess.check_call(['python3','/out/new/dictan.py'])
        build_script2 = 'gentoken.sh'
        os.chdir(os.environ['OUT']+'/new')
        os.mkdir('/out/new/testcases')
        os.system('chmod +x gentoken.sh')
        print('set x flag ok')
        subprocess.check_call(['/bin/bash',build_script2,'/out/curl_fuzzer_http'])
        #subprocess.check_call(['/bin/bash', build_script2,'/out/fuzz_target'])
        print('Token completed')
        os.system('ulimit -S -s unlimited')
        cp_files_dic()
        #subprocess.call(["cp testcases/* dict/."],shell=True)
        #shutil.copy('/out/new/testcases/*',os.environ['OUT']+'/new/dict/.')
        #curl_fuzzer_http
        os.chdir(os.environ['OUT']+'/new/dict')
        os.system('find . -type f -name "*" -size +127c -delete')
        os.system('rm -rf /out/new/testcases')
    if is_benchmark('bloaty_fuzz_target'):                
        shutil.copytree(src,os.environ['OUT']+'/new')
        #src = os.getenv('SRC')
        #work = os.getenv('WORK')
        #out = os.getenv('OUT')
        #shutil.copy('../fuzzers/aflql/dictan.py', os.environ['OUT']+'/new/bloaty/dictan.py')
        shutil.copy('../fuzzers/aflql/build-bloaty.sh',os.environ['OUT']+'/new/bloaty/build-bloaty.sh')
        shutil.copy('../fuzzers/aflql/gentoken.sh',os.environ['OUT']+'/new/gentoken.sh')
        #os.mkdir('/out/new/bloaty/bloaty')
        shutil.copy('../fuzzers/aflql/litool.ql',os.environ['OUT']+'/new/bloaty/litool.ql')
        shutil.copy('../fuzzers/aflql/strtool.ql',os.environ['OUT']+'/new/bloaty/strtool.ql')
        shutil.copy('../fuzzers/aflql/stan.py',os.environ['OUT']+'/new/bloaty/stan.py')
        shutil.copy('../fuzzers/aflql/litan.py',os.environ['OUT']+'/new/bloaty/litan.py')
        shutil.copy('../fuzzers/aflql/aflql-bloaty.py',os.environ['OUT']+'/new/bloaty/aflql.py')    
        os.chdir(os.environ['OUT']+'/new/bloaty')
        os.system('chmod +x build-bloaty.sh')
        build_script = 'build-bloaty.sh'        
        subprocess.check_call(['/bin/bash', build_script])
        with open('/out/new/target.txt','w') as out:
            line1 = "line 1: "
        print('All ok ...')
        subprocess.check_call(['python3','/out/new/bloaty/aflql.py'])
        build_script2 = 'gentoken.sh'
        os.chdir(os.environ['OUT']+'/new')
        os.mkdir('/out/new/testcases')
        os.system('chmod +x gentoken.sh')
        print('set x flag ok')
        #subprocess.check_call(['/bin/bash',build_script2,'/out/fuzz_target'])
        subprocess.check_call(['/bin/bash', build_script2,'/out/fuzz_target'])
        print('Token completed')
        os.system('ulimit -S -s unlimited')
        cp_files_dic()
        #subprocess.call(["cp /out/new/testcases/* /out/new/dict/."],shell=True)
        os.chdir(os.environ['OUT']+'/new/dict')
        os.system('find . -type f -name "*" -size +127c -delete')
        #except:
        #    raise
        #print('ok')
        os.system('rm -rf /out/new/testcases')
    if is_benchmark('libpng-1.2.56'):
        print('Libpng target entered')
        shutil.copytree(src,os.environ['OUT']+'/new')
        shutil.copy('fuzzers/aflql/build-libpng.sh',os.environ['OUT']+'/new/buildql.sh')
        shutil.copy('fuzzers/aflql/qlpack.yml', os.environ['OUT']+'/new/libpng-1.2.56/qlpack.yml')
        shutil.copy('fuzzers/aflql/litool.ql',os.environ['OUT']+'/new/libpng-1.2.56/litool.ql')
        shutil.copy('fuzzers/aflql/strtool.ql',os.environ['OUT']+'/new/libpng-1.2.56/strtool.ql')
        shutil.copy('fuzzers/aflql/stan.py',os.environ['OUT']+'/new/libpng-1.2.56/stan.py')
        shutil.copy('fuzzers/aflql/litan.py',os.environ['OUT']+'/new/libpng-1.2.56/litan.py')
        shutil.copy('fuzzers/aflql/aflql.py', os.environ['OUT']+'/new/libpng-1.2.56/aflql.py')
        shutil.copy('fuzzers/aflql/target-dict.dict', os.environ['OUT']+'/new/target-dict.dict')
        shutil.copy('fuzzers/aflql/dictan.py', os.environ['OUT']+'/new/dictan.py')
        shutil.copy('fuzzers/aflql/gentoken.sh',os.environ['OUT']+'/new/gentoken.sh')
        curdir = os.getcwd()
        print(curdir)
    #build_script = os.path.join(os.environ['OUT']+'/new/', 'build.sh')
        build_script = 'buildql.sh'
        os.chdir(os.environ['OUT']+'/new/')
        print("new path is :")
        cur = os.getcwd()
        print(cur)
        subprocess.check_call(['/bin/bash', '-ex', build_script])
        subprocess.check_call(['python3','/out/new/libpng-1.2.56/aflql.py'])
        subprocess.check_call(['python3','/out/new/dictan.py'])
        # libpng_read_fuzzer
        build_script2 = 'gentoken.sh'
        os.chdir(os.environ['OUT']+'/new')
        os.mkdir('/out/new/testcases')
        os.system('chmod +x gentoken.sh')
        print('set x flag ok')
        subprocess.check_call(['/bin/bash',build_script2,'/out/libpng_read_fuzzer'])
        print('Token completed')
        os.system('ulimit -S -s unlimited')
        cp_files_dic()
        os.chdir(os.environ['OUT']+'/new/dict')
        os.system('find . -type f -name "*" -size +127c -delete')
        os.system('rm -rf /out/new/testcases')
    #utils.build_benchmark()
    print('Done!')

def prepare_fuzz_environment(input_corpus):
    """Prepare to fuzz with AFL or another AFL-based fuzzer."""
    # Tell AFL to not use its terminal UI so we get usable logs.
    os.environ['AFL_NO_UI'] = '1'
    # Skip AFL's CPU frequency check (fails on Docker).
    os.environ['AFL_SKIP_CPUFREQ'] = '1'
    # No need to bind affinity to one core, Docker enforces 1 core usage.
    os.environ['AFL_NO_AFFINITY'] = '1'
    # AFL will abort on startup if the core pattern sends notifications to
    # external programs. We don't care about this.
    os.environ['AFL_I_DONT_CARE_ABOUT_MISSING_CRASHES'] = '1'

    # AFL needs at least one non-empty seed to start.
    utils.create_seed_file_for_empty_corpus(input_corpus)


def run_afl_fuzz(input_corpus,
                 output_corpus,
                 target_binary,
                 additional_flags=None,
                 hide_output=False):
    """Run afl-fuzz."""
    # Spawn the afl fuzzing process.
    # FIXME: Currently AFL will exit if it encounters a crashing input in seed
    # corpus (usually timeouts). Add a way to skip/delete such inputs and
    # re-run AFL.
    print('[run_afl_fuzz] Running target with afl-fuzz')
    command = [
        './afl-fuzz',
        '-i',
        input_corpus,
        '-o',
        output_corpus,
        # Use deterministic mode as it does best when we don't have
        # seeds which is often the case.
        '-d',
        # Use no memory limit as ASAN doesn't play nicely with one.
        '-m',
        'none',
        '-t',
        '1000+',  # Use same default 1 sec timeout, but add '+' to skip hangs.
        '-x',
        '/out/new/dict'
    ]
    if additional_flags:
        command.extend(additional_flags)
    dictionary_path = utils.get_dictionary_path(target_binary)
    #if dictionary_path:
    #    command.extend(['-x', '/out/new/dict/'])
    command += [
        '--',
        target_binary,
        # Pass INT_MAX to afl the maximize the number of persistent loops it
        # performs.
        '2147483647'
    ]
    print('[run_afl_fuzz] Running command: ' + ' '.join(command))
    output_stream = subprocess.DEVNULL if hide_output else None
    subprocess.check_call(command, stdout=output_stream, stderr=output_stream)


def fuzz(input_corpus, output_corpus, target_binary):
    """Run afl-fuzz on target."""
    prepare_fuzz_environment(input_corpus)

    run_afl_fuzz(input_corpus, output_corpus, target_binary)

