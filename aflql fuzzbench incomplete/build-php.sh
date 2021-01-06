#!/bin/bash
# Copyright 2019 Google Inc.
#
# Licensed under the Apache License, Version 2.0 (the "License");
# you may not use this file except in compliance with the License.
# You may obtain a copy of the License at
#
#      http://www.apache.org/licenses/LICENSE-2.0
#
# Unless required by applicable law or agreed to in writing, software
# distributed under the License is distributed on an "AS IS" BASIS,
# WITHOUT WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied.
# See the License for the specific language governing permissions and
# limitations under the License.
#
################################################################################

# build oniguruma and link statically
apt install -y autoconf automake libtool bison re2c pkg-config unzip wget git

#rm -rf codeql-repo
apt install -y wget git unzip libtool m4 automake build-essential clang
git clone https://github.com/github/codeql.git codeql-repo && cd codeql-repo && \
        wget https://github.com/github/codeql-cli-binaries/releases/download/v2.2.5/codeql-linux64.zip && \
        unzip codeql-linux64.zip && \
        mv codeql codeql-cli
#pushd oniguruma
#make clean
#autoreconf -vfi
#./configure
#make -j$(nproc)
#popd
export ONIG_CFLAGS="-I$PWD/oniguruma/src"
export ONIG_LIBS="-L$PWD/oniguruma/src/.libs -l:libonig.a"

# PHP's zend_function union is incompatible with the object-size sanitizer
export CFLAGS="$CFLAGS -fno-sanitize=object-size"
export CXXFLAGS="$CXXFLAGS -fno-sanitize=object-size"
cd /out/new/php-src
make clean
# build project
./buildconf
./configure \
    --disable-all \
    --enable-option-checking=fatal \      
    --enable-mbstring \
    --without-pcre-jit \
    --disable-phpdbg \
    --disable-cgi \
    --with-pic
../codeql-repo/codeql-cli/codeql database create php-db --language=cpp --command="make -j$(nproc)"
#codeql-cli/codeql
cat >> qlpack.yml << EOF
name: php-src
version: 0.0.0
libraryPathDependencies: codeql-cpp
EOF
echo 'its ok'
../codeql-repo/codeql-cli/codeql database upgrade php-db
../codeql-repo/codeql-cli/codeql query run litool.ql -d php-db > litout.log
../codeql-repo/codeql-cli/codeql query run strtool.ql -d php-db > outstr.log
# Generate initial corpus for parser fuzzer
#sapi/cli/php sapi/fuzzer/generate_parser_corpus.php
#cp sapi/fuzzer/dict/parser $OUT/php-fuzz-parser.dict

