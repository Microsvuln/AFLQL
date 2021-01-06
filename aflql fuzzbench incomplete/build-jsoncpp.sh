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
cd jsoncpp
rm -rf build
mkdir -p build
cd build
cmake -DCMAKE_CXX_COMPILER=$CXX -DCMAKE_CXX_FLAGS="$CXXFLAGS" \
      -DJSONCPP_WITH_POST_BUILD_UNITTEST=OFF -DJSONCPP_WITH_TESTS=OFF \
      -DBUILD_SHARED_LIBS=OFF -G "Unix Makefiles" ..
../codeql-repo/codeql-cli/codeql database create ../jsoncpp-db --language=cpp --command="make -j$(nproc)"
cat >> ../qlpack.yml << EOF
name: jsoncpp
version: 0.0.0
libraryPathDependencies: codeql-cpp
EOF
echo 'its ok'
../codeql-repo/codeql-cli/codeql database upgrade ../jsoncpp-db
../codeql-repo/codeql-cli/codeql query run ../litool.ql -d ../jsoncpp-db > litout.log
../codeql-repo/codeql-cli/codeql query run ../strtool.ql -d ../jsoncpp-db > outstr.log
cp litout.log ../litout.log
cp outstr.log ../outstr.log

