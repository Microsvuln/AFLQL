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
apt-get update && apt install -y  make unzip wget git python

git clone https://github.com/github/codeql.git codeql-repo && cd codeql-repo && \
        wget https://github.com/github/codeql-cli-binaries/releases/download/v2.2.5/codeql-linux64.zip && \
        unzip codeql-linux64.zip && \
        mv codeql codeql-cli
cd openthread
make clean
git checkout 5b0af03afb8e70e8216f69623bd18bcd3d4b8b43
./bootstrap
export CPPFLAGS="                                     \
    -DOPENTHREAD_CONFIG_BORDER_AGENT_ENABLE=1         \
    -DOPENTHREAD_CONFIG_BORDER_ROUTER_ENABLE=1        \
    -DOPENTHREAD_CONFIG_CHANNEL_MANAGER_ENABLE=1      \
    -DOPENTHREAD_CONFIG_CHANNEL_MONITOR_ENABLE=1      \
    -DOPENTHREAD_CONFIG_CHILD_SUPERVISION_ENABLE=1    \
    -DOPENTHREAD_CONFIG_COAP_API_ENABLE=1             \
    -DOPENTHREAD_CONFIG_COAP_SECURE_API_ENABLE=1      \
    -DOPENTHREAD_CONFIG_COMMISSIONER_ENABLE=1         \
    -DOPENTHREAD_CONFIG_DHCP6_CLIENT_ENABLE=1         \
    -DOPENTHREAD_CONFIG_DHCP6_SERVER_ENABLE=1         \
    -DOPENTHREAD_CONFIG_DIAG_ENABLE=1                 \
    -DOPENTHREAD_CONFIG_DNS_CLIENT_ENABLE=1           \
    -DOPENTHREAD_CONFIG_ECDSA_ENABLE=1                \
    -DOPENTHREAD_CONFIG_LEGACY_ENABLE=1               \
    -DOPENTHREAD_CONFIG_JAM_DETECTION_ENABLE=1        \
    -DOPENTHREAD_CONFIG_JOINER_ENABLE=1               \
    -DOPENTHREAD_CONFIG_LINK_RAW_ENABLE=1             \
    -DOPENTHREAD_CONFIG_MAC_FILTER_ENABLE=1           \
    -DOPENTHREAD_CONFIG_NCP_UART_ENABLE=1             \
    -DOPENTHREAD_CONFIG_REFERENCE_DEVICE_ENABLE=1     \
    -DOPENTHREAD_CONFIG_SNTP_CLIENT_ENABLE=1          \
    -DOPENTHREAD_CONFIG_TMF_NETDATA_SERVICE_ENABLE=1  \
    -DOPENTHREAD_CONFIG_TMF_NETWORK_DIAG_MTD_ENABLE=1 \
    -DOPENTHREAD_CONFIG_UDP_FORWARD_ENABLE=1"
sed -i 's/ -Werror//g' config*  # Disable compiler warnings.
./configure --enable-cli --enable-ftd --enable-joiner \
    --enable-ncp --disable-docs
../codeql-repo/codeql-cli/codeql database create othread-db --language=cpp --command="make V=1 -j $(nproc)"
cat >> qlpack.yml << EOF
name: openthread
version: 0.0.0
libraryPathDependencies: codeql-cpp
EOF
echo 'its ok'
../codeql-repo/codeql-cli/codeql database upgrade othread-db
../codeql-repo/codeql-cli/codeql query run litool.ql -d othread-db > litout.log
../codeql-repo/codeql-cli/codeql query run strtool.ql -d othread-db > outstr.log
#cp tests/fuzz/ip6-send-fuzzer $OUT/fuzz-target
