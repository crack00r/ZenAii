![zenbot logo](https://rawgit.com/carlos8f/zenbot/master/assets/logo.png)

> “To follow the path, look to the master, follow the master, walk with the master, see through the master, become the master.”
> – Zen Proverb

## New! Chat with other Zenbot users

[![zenbot logo](https://rawgit.com/carlos8f/zenbot/master/assets/discord.png)](https://discord.gg/ZdAd2gP)

Zenbot has a Discord chat again! You can get in [through this invite link](https://discord.gg/ZdAd2gP).




### 1. Requirements: Prefer: Ubuntu Xenial on Google Cloud Compute n1-standard-1 or higher.

### 2. Git clone zenbot to /zenbot (yes, in root directory please):
```
cd /
sudo apt install git
sudo git clone https://github.com/TheRoboKitten/zenbot.git /zenbot
```

### 3. Change directory to zenbot:

```
cd /zenbot/
```

### 4. Install dependencies:
```
sudo apt update
sudo apt install python-setuptools python-dev build-essential python mongodb libcurl4-openssl-dev libssl-dev dialog jq curl
sudo curl -sL https://deb.nodesource.com/setup_7.x | sudo -E bash -
sudo apt-get install -y nodejs
sudo pip install pycurl
sudo pip install pyyaml
sudo pip install pyparse
sudo pip install parse
```

### 5. Install cron job on system start and save:
```
sudo crontab -u root -e
```
Select the editor of your choice and input:
```
@reboot cd /zenbot/ && sudo ./start.sh
```

### 6. Edit conf-sample.js
The main line you want to input is here is your poloniex API key and Secret.
Lines 29 and 30:
```
c.poloniex.key = 'YOUR-API-KEY'
c.poloniex.secret = 'YOUR-SECRET'
```
### 7. Install node dependencies
Run these commands in the /zenbot/ directory.
```
sudo npm install
sudo npm link
```
### 8. Install Proxy: Warning: it sometimes crashes, needs debugging but auto-restarts on fail.
1. git clone polproxy:
```
cd /zenbot/
sudo git clone https://github.com/TheRoboKitten/polproxy.git
cd /polproxy
```
2. Input a second API key and secret into settings.yml
```
sudo nano settings.yml
```
```
# Your poloniex.com api key and secret.
api_key: API KEY HERE 
api_secret: API SECRET HERE
```
3. edit /etc/hosts
```
sudo nano /etc/hosts
```
and add the line:
```
127.0.0.1 poloniex.com
```
4. Add polproxy service:
``` 
sudo nano /etc/systemd/system/polproxy.service
```
5. Input into polproxy.service:
```
[Unit]
Description=PolProxy

[Service]
ExecStart=/usr/bin/python /zenbot/polproxy/polproxy.py
Restart=always

[Install]
WantedBy=multi-user.target
```
6. Save and set permissions on polproxy.service:
```
sudo chmod 644 /etc/systemd/system/polproxy.service
```
7. Reload the systemctl daemon.
```
sudo systemctl daemon-reload
```
8. Run polproxy
```
sudo service polproxy start
sudo service polproxy status
```


### 9. Final touches:

#### 1. Edit /zenbot/node_modules/poloniex.js/lib/poloniex.js and change the line:
THIS STEP IS MANDATORY FOR THE PROXY TO WORK
```
Poloniex.STRICT_SSL = true;
```
to
```
Poloniex.STRICT_SSL = false;
```

#### 2. Run zenbot once against a single coin to check for errors as follows in the zenbot directory:

```
sudo ./zenbot.sh trade --strategy=speed --period=1m poloniex.ETH-BTC
```

#### 3. Run the start.sh script as follows, this will take approx 60s * coins on poloniex. It will download trade data, and can overlap as all output is on one window at the moment. 60s is given for time to download the trade data. It will reinstall mongodb to assure the program starts.

```
sudo chmod +x /zenbot/start.sh
cd /zenbot/ && sudo ./start.sh
```

#### 4. If all is well, reboot and check that node and ./zenbot.sh is starting. (this can take awhile) and check polproxy service for incoming requests.

(if something is missing when running zenbot, such as a component, just do npm install (component) in the /zenbot/ directory.
(if a python module is missing, run pip install (module))

Thanks!!!!!
### Please report any issues as a issue on github for me to take a look at.

## Donate to carlos!!!!! He's a great guy. It's his software, this is just a fork.

P.S., some have asked for how to donate to Zenbot development. I accept donations at **my Bitcoin address** Here:

### carlos8f's BTC

`187rmNSkSvehgcKpBunre6a5wA5hQQop6W`

![zenbot logo](https://rawgit.com/carlos8f/zenbot/master/assets/zenbot_square.png)

Thanks!

- - -

### License: MIT

- Copyright (C) 2017 Carlos Rodriguez
- Copyright (C) 2017 Terra Eclipse, Inc. (http://www.terraeclipse.com/)

Permission is hereby granted, free of charge, to any person obtaining a copy
of this software and associated documentation files (the &quot;Software&quot;), to deal
in the Software without restriction, including without limitation the rights
to use, copy, modify, merge, publish, distribute, sublicense, and/or sell
copies of the Software, and to permit persons to whom the Software is furnished
to do so, subject to the following conditions:

The above copyright notice and this permission notice shall be included in
all copies or substantial portions of the Software.

THE SOFTWARE IS PROVIDED &quot;AS IS&quot;, WITHOUT WARRANTY OF ANY KIND, EXPRESS OR
IMPLIED, INCLUDING BUT NOT LIMITED TO THE WARRANTIES OF MERCHANTABILITY,
FITNESS FOR A PARTICULAR PURPOSE AND NONINFRINGEMENT. IN NO EVENT SHALL THE
AUTHORS OR COPYRIGHT HOLDERS BE LIABLE FOR ANY CLAIM, DAMAGES OR OTHER
LIABILITY, WHETHER IN AN ACTION OF CONTRACT, TORT OR OTHERWISE, ARISING FROM,
OUT OF OR IN CONNECTION WITH THE SOFTWARE OR THE USE OR OTHER DEALINGS IN THE
SOFTWARE.
