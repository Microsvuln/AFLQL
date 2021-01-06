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
apt install -y python
cd libxml2
make clean
# Git is converting CRLF to LF automatically and causing issues when checking
# out the branch. So use -f to ignore the complaint about lost changes that we
# don't even want.
git checkout -f v2.9.2
./autogen.sh
CCLD="$CXX $CXXFLAGS" ./configure --without-python --with-threads=no \
    --with-zlib=no --with-lzma=no
../codeql-repo/codeql-cli/codeql database create libxml-db --language=cpp --command="make -j $(nproc)"
cat >> qlpack.yml << EOF
name: libxml2
version: 0.0.0
libraryPathDependencies: codeql-cpp
EOF
echo 'its ok'
../codeql-repo/codeql-cli/codeql database upgrade libxml-db
../codeql-repo/codeql-cli/codeql query run litool.ql -d libxml-db > litout.log
../codeql-repo/codeql-cli/codeql query run strtool.ql -d libxml-db > outstr.log

