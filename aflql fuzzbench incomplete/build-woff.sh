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

# Get seeds.
apt-get update && \
    apt-get install -y \
    make \
    automake \
    autoconf \
    libtool \
    python

cd oss-fuzz
git checkout e8ffee4077b59e35824a2e97aa214ee95d39ed13
mkdir -p $OUT/seeds
cp projects/woff2/corpus/* $OUT/seeds
cd ..

cd brotli
git checkout 3a9032ba8733532a6cd6727970bade7f7c0e2f52
cd ..

cd woff2
git checkout 9476664fd6931ea6ec532c94b816d8fbbe3aed90

for f in font.cc normalize.cc transform.cc woff2_common.cc woff2_dec.cc \
         woff2_enc.cc glyph.cc table_tags.cc variable_length.cc woff2_out.cc; do
  ../codeql-repo/codeql-cli/codeql database create woff-db --language=cpp --command="$CXX $CXXFLAGS -std=c++11 -I ../b#rotli/dec -I ../brotli/enc -c src/$f" &
done
for f in ../brotli/dec/*.c ../brotli/enc/*.cc; do
  $CXX $CXXFLAGS -c $f &
done
wait

cat >> qlpack.yml << EOF
name: woff2
version: 0.0.0
libraryPathDependencies: codeql-cpp
EOF
echo 'its ok'
../codeql-repo/codeql-cli/codeql database upgrade woff-db
../codeql-repo/codeql-cli/codeql query run litool.ql -d woff-db > litout.log
../codeql-repo/codeql-cli/codeql query run strtool.ql -d woff-db > outstr.log
