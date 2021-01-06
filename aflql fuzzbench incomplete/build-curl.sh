#!/bin/bash
apt install -y wget git unzip python libtool m4 automake build-essential clang
git clone https://github.com/github/codeql.git codeql-repo && cd codeql-repo && \
	wget https://github.com/github/codeql-cli-binaries/releases/download/v2.2.5/codeql-linux64.zip && \
	unzip codeql-linux64.zip && \
    	mv codeql codeql-cli

#cd ..
#export "PATH=/out/new/codeql-repo/codeql-cli/:$PATH"

cd ../curl
make clean
./buildconf
./configure
../codeql-repo/codeql-cli/codeql database create curl-db --language=cpp --command="make -j$(nproc)" 
cat >> qlpack.yml << EOF
name: curl
version: 0.0.0
libraryPathDependencies: codeql-cpp
EOF
#../codeql-repo/codeql-cli/codeql database create curl-db --language=cpp --command=make
../codeql-repo/codeql-cli/codeql database upgrade curl-db
../codeql-repo/codeql-cli/codeql query run litool.ql -d curl-db > litout.log
../codeql-repo/codeql-cli/codeql query run strtool.ql -d curl-db > outstr.log
