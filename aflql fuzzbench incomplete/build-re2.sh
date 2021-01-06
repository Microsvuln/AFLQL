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
apt install -y wget git unzip libtool m4 automake build-essential clang python
cd re2
make clean
git checkout 499ef7eff7455ce9c9fae86111d4a77b6ac335de
../codeql-repo/codeql-cli/codeql database create re-db --language=cpp --command="make -j$(nproc)"
cat >> qlpack.yml << EOF
name: re2
version: 0.0.0
libraryPathDependencies: codeql-cpp
EOF
echo 'its ok'
../codeql-repo/codeql-cli/codeql database upgrade re-db
../codeql-repo/codeql-cli/codeql query run litool.ql -d re-db > litout.log
../codeql-repo/codeql-cli/codeql query run strtool.ql -d re-db > outstr.log

