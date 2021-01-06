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
apt install -y wget git unzip libtool python m4 automake build-essential clang
git clone https://github.com/github/codeql.git codeql-repo && cd codeql-repo && \
        wget https://github.com/github/codeql-cli-binaries/releases/download/v2.2.5/codeql-linux64.zip && \
        unzip codeql-linux64.zip && \
        mv codeql codeql-cli
cd ..
cd zlib
make clean
./configure
make -j$(nproc) clean
../codeql-repo/codeql-cli/codeql database create zlib-db --language=cpp --command="make -j$(nproc) all"
cat >> qlpack.yml << EOF
name: zlib
version: 0.0.0
libraryPathDependencies: codeql-cpp
EOF
echo 'its ok'
../codeql-repo/codeql-cli/codeql database upgrade zlib-db
../codeql-repo/codeql-cli/codeql query run litool.ql -d zlib-db > litout.log
../codeql-repo/codeql-cli/codeql query run strtool.ql -d zlib-db > outstr.log

# Do not make check as there are tests that fail when compiled with MSAN.
# make -j$(nproc) check


