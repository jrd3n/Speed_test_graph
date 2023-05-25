# Speed_test_graph

## install

```bash

wget https://github.com/jrd3n/Speed_test_graph/archive/refs/heads/master.zip
unzip master
cd Speed_test_graph-master
sudo apt-get install python3-venv
```

```bash
python3 -m venv venv
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