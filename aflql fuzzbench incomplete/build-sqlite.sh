#!/bin/bash -eu
# Copyright 2016 Google Inc.
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
apt-get update && apt-get install -y make autoconf python automake libtool curl tcl zlib1g-dev unzip git wget
git clone https://github.com/github/codeql.git codeql-repo && cd codeql-repo && \
        wget https://github.com/github/codeql-cli-binaries/releases/download/v2.2.5/codeql-linux64.zip && \
        unzip codeql-linux64.zip && \
        mv codeql codeql-cli
cd ..
cd sqlite3
mkdir bld
cd bld
make clean
export ASAN_OPTIONS=detect_leaks=0

# Limit max length of data blobs and sql queries to prevent irrelevant OOMs.
# Also limit max memory page count to avoid creating large databases.
export CFLAGS="$CFLAGS -DSQLITE_MAX_LENGTH=128000000 \
               -DSQLITE_MAX_SQL_LENGTH=128000000 \
               -DSQLITE_MAX_MEMORY=25000000 \
               -DSQLITE_PRINTF_PRECISION_LIMIT=1048576 \
               -DSQLITE_DEBUG=1 \
               -DSQLITE_MAX_PAGE_COUNT=16384"             
               
../configure
../codeql-repo/codeql-cli/codeql database create ../sqlite-db --language=cpp --command="make -j$(nproc)"
make sqlite3.c
cat >> qlpack.yml << EOF
name: sqlite3
version: 0.0.0
libraryPathDependencies: codeql-cpp
EOF
cp qlpack.yml ../qlpack.yml
echo 'its ok'
../codeql-repo/codeql-cli/codeql database upgrade ../sqlite-db
../codeql-repo/codeql-cli/codeql query run ../litool.ql -d ../sqlite-db > litout.log
../codeql-repo/codeql-cli/codeql query run ../strtool.ql -d ../sqlite-db > outstr.log
cp litout.log ../litout.log
cp outstr.log ../outstr.log
