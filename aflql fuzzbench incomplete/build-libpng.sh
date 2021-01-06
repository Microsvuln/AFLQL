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

#tar xf libpng-1.2.56.tar.gz
apt install -y python
cd libpng-1.2.56
make clean
./configure
../codeql-repo/codeql-cli/codeql database create libpng-db --language=cpp --command=make
../codeql-repo/codeql-cli/codeql database upgrade libpng-db
../codeql-repo/codeql-cli/codeql query run litool.ql -d libpng-db > litout.log
../codeql-repo/codeql-cli/codeql query run strtool.ql -d libpng-db > outstr.log
