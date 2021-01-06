#!/bin/bash -eu
#
# Copyright 2019 Google Inc.
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
cd libxslt
# This would require an instrumented libgcrypt build.
CRYPTO_CONF=--with-crypto
CRYPTO_LIBS=-lgcrypt

cd ../libxml2
./autogen.sh \
    --disable-shared \
    --without-c14n \
    --without-legacy \
    --without-push \
    --without-python \
    --without-reader \
    --without-regexps \
    --without-sax1 \
    --without-schemas \
    --without-schematron \
    --without-valid \
    --without-writer \
    --without-zlib \
    --without-lzma
make -j$(nproc) V=1

cd ../libxslt
./autogen.sh \
    --with-libxml-src=../libxml2 \
    --disable-shared \
    --without-python \
    $CRYPTO_CONF \
    --without-debug \
    --without-debugger \
    --without-profiler
codeql-repo/codeql-cli/codeql database create libxslt-db --language=cpp --command="make -j$(nproc) V=1"
cat >> qlpack.yml << EOF
name: libxslt
version: 0.0.0
libraryPathDependencies: codeql-cpp
EOF
echo 'its ok'
codeql-repo/codeql-cli/codeql database upgrade libxslt-db
codeql-repo/codeql-cli/codeql query run litool.ql -d libxslt-db > litout.log
codeql-repo/codeql-cli/codeql query run strtool.ql -d libxslt-db > outstr.log
