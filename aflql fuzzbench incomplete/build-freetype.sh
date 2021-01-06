#!/bin/bash
apt install -y   make autoconf libtool python 
cd freetype2
./autogen.sh
./configure --with-harfbuzz=no --with-bzip2=no --with-png=no --without-zlib
make clean
../codeql-repo/codeql-cli/codeql database create freetype-db --language=cpp --command="make all -j $(nproc)"
../codeql-repo/codeql-cli/codeql database upgrade freetype-db
cat >> qlpack.yml << EOF
name: freetype2
version: 0.0.0
libraryPathDependencies: codeql-cpp
EOF
echo 'its ok'
../codeql-repo/codeql-cli/codeql query run litool.ql -d freetype-db > litout.log
../codeql-repo/codeql-cli/codeql query run strtool.ql -d freetype-db > outstr.log
