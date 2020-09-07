cd ~
if [ -d "codeql-repo" ]; then
    echo "Exist !"
    exit 1
fi
sudo apt install build-essential libtool-bin python3-dev automake git vim 
git clone https://github.com/github/codeql.git codeql-repo
cd codeql-repo
wget https://github.com/github/codeql-cli-binaries/releases/download/v2.2.5/codeql-linux64.zip
unzip codeql-linux64.zip 
mv codeql codeql-cli
export "PATH=~/codeql-repo/codeql-cli/:$PATH"
codeql resolve languages
codeql resolve qlpacks
echo "export PATH=~/codeql-repo/codeql-cli/:$PATH" >> ~/.bashrc