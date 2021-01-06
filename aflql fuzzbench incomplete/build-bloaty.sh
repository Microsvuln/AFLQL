#!/bin/bash -eu
# Copyright 2017 Google Inc.
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

#cd $WORK
#rm -rf bloaty
apt-get update && apt-get install -y cmake ninja-build g++ git protobuf-compiler wget python
#git clone --depth 1 https://github.com/google/bloaty.git bloaty
git clone https://github.com/google/bloaty.git bloaty
cd bloaty
#mkdir build
#cd build
#cmake -G Ninja -DBUILD_TESTING=false ..
#make -j6
make clean
cmake .
#cmake -G Ninja -DBUILD_TESTING=false /out/new/bloaty/
#ninja -j$(nproc)
../codeql-repo/codeql-cli/codeql database create ../bloaty-db --language=cpp --command="make -j16"
echo "Good job!"
cat >> ../qlpack.yml << EOF
name: bloaty
version: 0.0.0
libraryPathDependencies: codeql-cpp
EOF
echo 'its ok'
../codeql-repo/codeql-cli/codeql database upgrade ../bloaty-db
../codeql-repo/codeql-cli/codeql query run ../litool.ql -d ../bloaty-db > litout.log
../codeql-repo/codeql-cli/codeql query run ../strtool.ql -d ../bloaty-db > outstr.log
echo 'good'
cp litout.log ../.
cp outstr.log ../.
#bloaty/codeql-repo/codeql-cli/codeql
#cp fuzz_target $OUT
#zip -j $OUT/fuzz_target_seed_corpus.zip $SRC/bloaty/tests/testdata/fuzz_corpus/*

