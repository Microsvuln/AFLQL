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
cd mbedtls

# build project
perl scripts/config.pl set MBEDTLS_PLATFORM_TIME_ALT
git -C crypto checkout -f 819799cfc68e4c4381673a8a27af19802c8263f2
rm -rf build
mkdir build
cd build
cmake ..
# build including fuzzers
../codeql-repo/codeql-cli/codeql database create ../mbedtls-db --language=cpp --command="make -j$(nproc) all"
cat >> qlpack.yml << EOF
name: mbedtls
version: 0.0.0
libraryPathDependencies: codeql-cpp
EOF
cp qlpack.yml ../qlpack.yml
#codeql-repo/codeql-cli/codeql database create x509-db --language=cpp --command="make -j$(nproc)"
../codeql-repo/codeql-cli/codeql database upgrade ../mbedtls-db
../codeql-repo/codeql-cli/codeql query run ../litool.ql -d ../mbedtls-db > litout.log
../codeql-repo/codeql-cli/codeql query run ../strtool.ql -d ../mbedtls-db > outstr.log
cp litout.log ../litout.log
cp outstr.log ../outstr.log

