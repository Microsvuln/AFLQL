#!/bin/bash 
cd openssl
apt-get update && apt install -y  make python
#git clone https://github.com/github/codeql.git codeql-repo && cd codeql-repo && \
#        wget https://github.com/github/codeql-cli-binaries/releases/download/v2.2.5/codeql-linux64.zip && \
#        unzip codeql-linux64.zip && \
#        mv codeql codeql-cli

make clean
./config --debug -DPEDANTIC no-shared enable-tls1_3 enable-rc5 enable-md2 enable-ec_nistp_64_gcc_128 enable-ssl3 enable-ssl3-method enable-nextprotoneg enable-weak-ssl-ciphers $CFLAGS $CONFIGURE_FLAGS
codeql-repo/codeql-cli/codeql database create x509-db --language=cpp --command="make -j$(nproc)"
cat >> qlpack.yml << EOF
name: openssl
version: 0.0.0
libraryPathDependencies: codeql-cpp
EOF
#codeql-repo/codeql-cli/codeql database create x509-db --language=cpp --command="make -j$(nproc)"
codeql-repo/codeql-cli/codeql database upgrade x509-db
codeql-repo/codeql-cli/codeql query run litool.ql -d x509-db > litout.log
codeql-repo/codeql-cli/codeql query run strtool.ql -d x509-db > outstr.log

