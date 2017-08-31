![zenbot logo](https://rawgit.com/carlos8f/zenbot/master/assets/logo.png)

> “To follow the path, look to the master, follow the master, walk with the master, see through the master, become the master.”
> – Zen Proverb

## New! Chat with other Zenbot users

[![zenbot logo](https://rawgit.com/carlos8f/zenbot/master/assets/discord.png)](https://discord.gg/ZdAd2gP)

## Disclaimer

- Zenbot is NOT a sure-fire profit machine. Use it AT YOUR OWN RISK.
- Crypto-currency is still an experiment, and therefore so is Zenbot. Meaning, both may fail at any time.
- Running a bot, and trading in general requires careful study of the risks and parameters involved. A wrong setting can cause you a major loss.
- Never leave the bot un-monitored for long periods of time. Zenbot doesn't know when to stop, so be prepared to stop it if too much loss occurs.
- Often times the default trade parameters will underperform vs. a buy-hold strategy, so run some simulations and find the optimal parameters for your chosen exchange/pair before going "all-in".

## Quick-start

### 1. Requirements: Windows, Linux or OSX or Docker, [Node.js](https://nodejs.org/) and [MongoDB](https://www.mongodb.com/) and Python3.

### 2. Install zenbot 4:

Run in your console,

```
git clone https://github.com/TheRoboKitten/zenaii.git
```

Then run:
```
sudo sh setup.sh
```
Then, Git clone this:
```
git clone https://github.com/s4w3d0ff/python-poloniex.git
```
Copy everything inside python-poloniex into the /Zenaii Directory, you can rename setup.py if you wish.
```
cp python-poloniex/* ZenAii/* -R
```
Install python-poloniex:
```
sudo python3 setup.py install
```


### Setup Command List:

Originally for zenaii:
```

sudo apt update
sudo apt install python3-setuptools python3 python3-pip mongodb libcurl4-openssl-dev libssl-dev dialog jq curl build-essential
sudo curl -sL https://deb.nodesource.com/setup_8.x | sudo -E bash -
sudo apt-get install -y nodejs
sudo dpkg --configure -a
sudo apt install -f
sudo pip3 install pycurl
sudo pip3 install pyyaml
sudo pip3 install pyparse
sudo pip3 install parse
sudo pip3 install pyaes
sudo pip3 install pandas
sudo pip3 install pymongo
sudo python3 setup.py gen_tl
sudo python3 setup.py install
sudo npm install
sudo npm link

echo "First, Create a telegram account... For more info read the README.md and README2.md"
echo "...And Then... Go here and get an API key and hash under Dev Tools: https://my.telegram.org/auth"
echo "...And Then... Input your hash, key, and phone into trader.py..."
echo "then input your poloniex (preferred) Key and hash into conf-example.js"
echo "...Then git clone this: https://github.com/TheRoboKitten/python-poloniex.git"
echo "...move everything inside that folder into the zenaii directory"
echo "Then run sudo python3 setup.py install"


```



Make sure to input your poloniex API KEY and HASH into conf-example.js

Then git clone this: 
```
https://github.com/TheRoboKitten/python-poloniex.git /python-poloniex
```
In zenaii directory, mv setup.py setup1.py out of the way.

```
mv setup.py setup1.py
```

Then cd into /python-poloniex
Then do:
```
cd /python-poloniex
sudo cp * /zenaii/ -rf
```

Then do:

```
sudo python3 setup.py install
```

THEN DO THE INSTRUCTIONS BELOW, THEY MIGHT BE OUT OF ORDER!

Read below for setting up telethon.



Follow the on-screen instructions, make sure to read README.md and README2.md


Readme2.md:


CryptoAlert ZenAii Instructions
![happy](happy.png)



Obtaining your Telegram ``API ID`` and ``Hash``
===============================================
In order to use Telethon, you first need to obtain your very own API ID and Hash:

1. Follow `this link <https://my.telegram.org>`_ and login with your phone number.
2. Click under *API Development tools*.
3. A *Create new application* window will appear. Fill in your application details.
   There is no need to enter any *URL*, and only the first two fields (*App title* and *Short name*)
   can be changed later as long as I'm aware.
4. Click on *Create application* at the end.

Now that you know your ``API ID`` and ``Hash``, you can continue installing Telethon.

Installing Telethon
===================


Installing Telethon manually
----------------------------

1. Install the required ``pyaes`` module: ``sudo -H pip install pyaes`` and ``sudo apt install python3 python3-pip``
2. Run the code generator: ``python3 setup.py gen_tl``
3. Run the code install: ``python3 setup.py install``

Running CryptoAlert ZenAII
================
If you've installed Telethon:
To run the explorer after inputting your phone and API ID/Key:
   ``sudo python3 trader.py``
  



### carlos8f's BTC, Zenbot License

`187rmNSkSvehgcKpBunre6a5wA5hQQop6W`

![zenbot logo](https://rawgit.com/carlos8f/zenbot/master/assets/zenbot_square.png)

Thanks!

### Zenaii Development BTC:

`1Ppitsjie6EcRTpfJEXmEYzUaoJgBdvhAg`

THANK YOU!!!

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
