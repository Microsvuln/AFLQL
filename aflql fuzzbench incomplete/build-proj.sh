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
apt-get update && apt install -y  make unzip wget git python

git clone https://github.com/github/codeql.git codeql-repo && cd codeql-repo && \
        wget https://github.com/github/codeql-cli-binaries/releases/download/v2.2.5/codeql-linux64.zip && \
        unzip codeql-linux64.zip && \
        mv codeql codeql-cli
cd PROJ
make clean
git checkout d00501750b210a73f9fb107ac97a683d4e3d8e7a
./autogen.sh
./configure
../codeql-repo/codeql-cli/codeql database create proj-db --language=cpp --command="make -j$(nproc)"
cat >> qlpack.yml << EOF
name: PROJ
version: 0.0.0
libraryPathDependencies: codeql-cpp
EOF
echo 'its ok'
../codeql-repo/codeql-cli/codeql database upgrade proj-db
../codeql-repo/codeql-cli/codeql query run litool.ql -d proj-db > litout.log
../codeql-repo/codeql-cli/codeql query run strtool.ql -d proj-db > outstr.log


