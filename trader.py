
from telethon import TelegramClient
from telethon.tl.types import UpdateNewMessage
from telethon.tl.types import InputPeerChat
from telethon.tl.types import Message
from telethon.tl.types.input_peer_self import InputPeerSelf
from telethon.tl.types.input_peer_chat import InputPeerChat
from telethon.tl.types.input_peer_channel import InputPeerChannel
from telethon.tl.functions.messages.forward_message import ForwardMessageRequest
import multiprocessing, sys, time, json, requests, re, unicodedata, subprocess, os, sqlite3, threading
from subprocess import PIPE,Popen,STDOUT
from decimal import *

global flag
global variable
pid = 'coin.run'
print('CryptoAlert Auto-Trader, with live updates...')
print('CryptoAlert Auto-Trader, with live updates...')
print('CryptoAlert Auto-Trader, with live updates...')
print('CTRL-C To exit')
print('CTRL-C To exit')
print('CTRL-C To exit')
print('To test me, type a coin into the cryptoping telegram bot window on telegram such as #LTC and #DASH')
print('The Telegram updates in a while loop, and creates a pid equialent... delete coin.run if exiting in the middle of a sell signal')
threads = []
flag = "test"
variable = "test"
api_id = 189914
api_hash = '75b1fbdede4c49f7b7ca4a8681d5dfdf'
# 'session_id' can be 'your_name'. It'll be saved as your_name.session
client = TelegramClient('session_id', api_id, api_hash)
client.connect()

# PUT YOUR PHONE NUMBER ASSICOATED WITH TELEGRAM BELOW google voice works...
if not client.is_user_authorized():
  client.send_code_request('+14698447320')
  client.sign_in('+14698447320', input('Enter code: '))
# Now you can use the connected client as you wish

def generate_random_long():
    import random
    return random.choice(range(0,10000000))




def update_handler(d):
    global flag
    global variable
    # On this example, we just show the update object itself
    d = str(d)
    #testChannel
    re1 = '( id: )(?:[0-9][0-9]+)(,)' 

    rg = re.compile(re1,re.IGNORECASE|re.DOTALL)
    m = rg.search(d)
    if m:
        word1=m.group(0)
        word2=word1.replace(' id: ', '')
        word3=word2.replace(',', '')
        word4=word3
        idd = int(word4)
        peer1 = InputPeerSelf()
        #INPUT YOUR KEYWORDS BELOW
        word_list = ["#DCR", "#LTC", "#NAUT", "#NXT", "#XCP", "#GRC", "#REP", "#PPC", "#RIC", "#STRAT", "#GAME", "#BTM", "#CLAM", "#ARDR", "#BLK", "#OMNI", "#SJCX", "#FLDC", "#BCH", "#POT", "#VRC", "#ETH", "#PINK", "#NOTE", "#BTS", "#AMP", "#NAV", "#BELA", "#ETC", "#FLO", "#VIA", "#XBC", "#XPM", "#DASH", "#XVC", "#GNO", "#NMC", "#RADS", "#VTC", "#XEM", "#FCT", "#XRP", "#NXC", "#STEEM", "#SBD", "#BURST", "#XMR", "#DGB", "#LBC", "#BCY", "#PASC", "#LSK", "#EXP", "#MAID", "#BTCD", "#SYS", "#GNT", "#HUC", "#EMC2", "#NEOS", "#ZEC", "#STR"]
        regex_string = "(?<=\W)(%s)(?=\W)" % "|".join(word_list)
        finder = re.compile(regex_string)
        string_to_be_searched = d
        results = finder.findall(" %s " % string_to_be_searched)
        result_set = set(results)
        print(idd)
        for word in word_list:
            if word in result_set:
                try:
                    var = word
                    var1 = var.replace('#', '')
                    btc = '-BTC'
                    variable = var1 + btc
                    if (os.path.isfile(pid)):
                        print('Waiting on current process to finish... If you experience errors, delete process.run')
                    else:
                        sell = 'notready'
                        m = multiprocessing.Process(target = runitt , args = ())
                        m.start()
                        client(ForwardMessageRequest(peer=peer1, id=(idd), random_id=(generate_random_long())))
                except Exception as e:
                    print(e)

def create_process():
    return multiprocessing.Process(target = runitt , args = ())
 
def runitt():
    open(pid, 'w').close()
    global variable
    variable=str(variable)
    variablestr=str(variable)
    print('Starting Buy Of:' + variablestr + 'And will wait until 50pct balance bought.')
    process0='./zenbot.sh buy --order_adjust_time=1000000000 --buy_pct=50 --markup_pct=0  poloniex.' + variablestr
    proc0 = subprocess.Popen(process0,shell=True)
    proc0.communicate()
    print('Starting Profit Sell Of:' + variablestr + ' Sell 100 pct at 2pct markup or manually sell using poloniex web interface... You must do this manually')
    process1='./zenbot.sh sell --order_adjust_time=1000000000 --sell_pct=100 --markup_pct=2  poloniex.' + variablestr
    proc1 = subprocess.Popen(process1,shell=True)
    proc1.communicate()
    print('Starting 2pct markup error sell Of:' + variablestr + ' In Case of Error')
    process2='./zenbot.sh sell --order_adjust_time=1000000000 --sell_pct=100 --markup_pct=0  poloniex.' + variablestr
    proc2 = subprocess.Popen(process2,shell=True)
    proc2.communicate()
    print('Starting Error Sell Of:' + variablestr + ' In Case of Error')
    process3='./zenbot.sh sell --order_adjust_time=1000000000 --sell_pct=100 --markup_pct=0  poloniex.' + variablestr
    proc3 = subprocess.Popen(process3,shell=True)
    proc3.communicate()
    os.remove(pid)
    print('Done running loop, process file deleted. Waiting for another coin...')
# From now on, any update received will be passed to 'update_handler' NOTE... Later, Zenbot will be modified to cancel on order adjust.
while True:
    client.add_update_handler(update_handler)
    input('Press <ENTER> to exit...')
    client.disconnect()





