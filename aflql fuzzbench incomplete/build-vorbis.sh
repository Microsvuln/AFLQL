#!/bin/bash
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
readonly INSTALL_DIR="$PWD/INSTALL"

cd ogg
git checkout c8391c2b267a7faf9a09df66b1f7d324e9eb7766
./autogen.sh
./configure \
    --prefix="$INSTALL_DIR" \
    --enable-static \
    --disable-shared \
    --disable-crc
make -j $(nproc)
make install
cd ..

cd vorbis
make clean
git checkout c1c2831fc7306d5fbd7bc800324efd12b28d327f
./autogen.sh
./configure \
    --prefix="$INSTALL_DIR" \
    --enable-static \
    --disable-shared
#make -j $(nproc)
../codeql-repo/codeql-cli/codeql database create vorbis-db --language=cpp --command="make -j $(nproc)"
cat >> qlpack.yml << EOF
name: vorbis
version: 0.0.0
libraryPathDependencies: codeql-cpp
EOF
echo 'its ok'
../codeql-repo/codeql-cli/codeql database upgrade vorbis-db
../codeql-repo/codeql-cli/codeql query run litool.ql -d vorbis-db > litout.log
../codeql-repo/codeql-cli/codeql query run strtool.ql -d vorbis-db > outstr.log
make install
cd ..

