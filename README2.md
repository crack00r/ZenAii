CryptoPing ZenAii Instructions
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

Running Cryptoping ZenAII
================
If you've installed Telethon:
To run the explorer after inputting your phone and API ID/Key:
   ``sudo python3 trader.py``
  
