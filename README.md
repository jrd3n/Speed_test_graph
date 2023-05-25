# Speed_test_graph

## install

```bash

wget https://github.com/jrd3n/Speed_test_graph/archive/refs/heads/master.zip
unzip master
cd Speed_test_graph-master
sudo apt-get install python3-venv
```

```bash
sudo apt-get update
sudo apt-get install -y build-essential zlib1g-dev libncurses5-dev libgdbm-dev libnss3-dev libssl-dev libsqlite3-dev libreadline-dev libffi-dev curl libbz2-dev
curl -O https://www.python.org/ftp/python/3.11.2/Python-3.11.2.tar.xz
tar -xf Python-3.11.2.tar.xz
cd Python-3.11.2
./configure --enable-optimizations
sudo make altinstall
```

```bash
python3.11.2 -m venv venv
source ./venv/bin/activate
pip install -r requirements.txt
python3 app.py

```

```bash
crontab -e

```

```
*/10 * * * * ~/Speed_test_graph/venv/bin/python ~/Speed_test_graph/speed_test.py
@reboot sleep 30 && ~/Speed_test_graph/venv/bin/python ~/Speed_test_graph/app.py &

```