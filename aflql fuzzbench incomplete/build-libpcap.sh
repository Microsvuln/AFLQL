#!/bin/bash -eu
# Copyright 2018 Google Inc.
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
apt install -y python
cd libpcap
# build project
git apply ../patch.diff
rm -rf build
mkdir build
cd build
cmake ..
../../codeql-repo/codeql-cli/codeql database create ../libpcap-db --language=cpp --command="make -j$(nproc)"
cat >> ../qlpack.yml << EOF
name: libpcap
version: 0.0.0
libraryPathDependencies: codeql-cpp
EOF
echo 'its ok'
../../codeql-repo/codeql-cli/codeql database upgrade ../libpcap-db
../../codeql-repo/codeql-cli/codeql query run ../litool.ql -d ../libpcap-db > litout.log
../../codeql-repo/codeql-cli/codeql query run ../strtool.ql -d ../libpcap-db > outstr.log
cp litout.log ../litout.log
cp outstr.log ../outstr.log



