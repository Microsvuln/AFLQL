#!/bin/bash -ex
# Copyright 2020 Google LLC
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
apt install -y   make autoconf libtool git python 
cd harfbuzz
make clean
git checkout f73a87d9a8c76a181794b74b527ea268048f78e3
./autogen.sh
(cd ./src/hb-ucdn && make clean && CCLD="$CXX $CXXFLAGS" ../../../codeql-repo/codeql-cli/codeql database create harfbuzz-db --language=cpp --command=make)
cat >> qlpack.yml << EOF
name: harbuzz
version: 0.0.0
libraryPathDependencies: codeql-cpp
EOF
echo 'its ok'
CCLD="$CXX $CXXFLAGS" ./configure --enable-static --disable-shared \
    --with-glib=no --with-cairo=no
../codeql-repo/codeql-cli/codeql database create harfbuzz-db --language=cpp --command="make -j$(nproc) -C src"
../codeql-repo/codeql-cli/codeql database upgrade harfbuzz-db
../codeql-repo/codeql-cli/codeql query run litool.ql -d harfbuzz-db > litout.log
../codeql-repo/codeql-cli/codeql query run strtool.ql -d harfbuzz-db > outstr.log
echo 'Done!'
