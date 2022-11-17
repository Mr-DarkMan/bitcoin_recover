set -e

# Download and install Armory v0.93.3 plus prerequisites
# (v0.94+ is unsupported on Ubuntu 12.04 w/o recompiling libstdc++6)

curl -LfsS --retry 10 -o 'armory.deb' "$LATEST"

sudo apt-get -q update
sudo apt-get -yq install gdebi-core
sudo gdebi -nq armory.deb

curl -fsS --retry 10 https://bootstrap.pypa.io/get-pip.py | sudo python
sudo /usr/local/bin/pip install -q protobuf scrypt pylibscrypt coincurve pysha3 green
