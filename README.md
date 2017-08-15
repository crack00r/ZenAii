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
sudo git clone https://github.com/TheRoboKitten/ZenAii.git /zenaii
```

### 3. Change directory to zenbot:

```
cd zenaii/
```

### 4. Install dependencies:
```
sudo apt update
sudo apt install python-setuptools python3 python3-pip mongodb libcurl4-openssl-dev libssl-dev dialog jq curl
sudo curl -sL https://deb.nodesource.com/setup_7.x | sudo -E bash -
sudo apt-get install -y nodejs nodejs-legacy
sudo pip3 install pycurl
sudo pip3 install pyyaml
sudo pip3 install pyparse
sudo pip3 install parse
```

### 5. Edit conf-sample.js
The main line you want to input is here is your poloniex API key and Secret.
Lines 29 and 30:
```
c.poloniex.key = 'YOUR-API-KEY'
c.poloniex.secret = 'YOUR-SECRET'
```
### 6. Install node dependencies
Run these commands in the /zenbot/ directory.
```
sudo npm install
sudo npm link
```
### 7. Install Telethon
```
sudo ./setup.sh
```
or
```
sudo python3 setup.py gen_tl
sudo python3 setup.py install
```

Open setup.sh for more instructions please!!! This will guide you the way.



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
