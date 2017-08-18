
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
global var1
print('Cryptoping Auto-Trader, with live updates...')
print('Cryptoping Auto-Trader, with live updates...')
print('Cryptoping Auto-Trader, with live updates...')
print('CTRL-C To exit')
print('CTRL-C To exit')
print('CTRL-C To exit')
print('To test me, type a coin into the cryptoping telegram bot window on telegram such as #LTC and #DASH')
print('When testing, look for a small-digit number in the 1-10000 range appearing in the console or a buy/sell order')

threads = []
flag = "test"
variable = "test"
var1 = "test"
api_id = 189914
api_hash = '75b1fbdede4c49f7b7ca4a8681d5dfdf'
# 'session_id' can be 'your_name'. It'll be saved as your_name.session
client = TelegramClient('session_id', api_id, api_hash)
client.connect()


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
    global var1
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
        word_list = ["#DCR", "#LTC", "#NAUT", "#NXT", "#XCP", "#GRC", "#REP", "#PPC", "#RIC", "#STRAT", "#GAME", "#BTM", "#CLAM", "#ARDR", "#BLK", "#OMNI", "#SJCX", "#FLDC", "#BCH", "#DOGE", "#POT", "#VRC", "#ETH", "#PINK", "#NOTE", "#BTS", "#AMP", "#NAV", "#BELA", "#BCN", "#ETC", "#FLO", "#VIA", "#XBC", "#XPM", "#DASH", "#XVC", "#GNO", "#NMC", "#RADS", "#VTC", "#XEM", "#FCT", "#XRP", "#NXC", "#STEEM", "#SBD", "#BURST", "#XMR", "#DGB", "#LBC", "#BCY", "#PASC", "#SC", "#LSK", "#EXP", "#MAID", "#BTCD", "#SYS", "#GNT", "#HUC", "#EMC2", "#NEOS", "#ZEC", "#STR"]
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
                    m = create_process()
                    m.start()
                    client(ForwardMessageRequest(peer=peer1, id=(idd), random_id=(generate_random_long())))
                except Exception as e:
                    print(e)

def create_process():
    return multiprocessing.Process(target = runitt , args = ())
 
def runitt():
    global variable
    global var1
    variable=str(variable)
    variablestr=str(variable)
    print('Starting Buy Of: ' + variablestr + ' --  And will wait until bought')
    process0='./zenbot.sh buy --order_adjust_time=10000 --debug  poloniex.' + variablestr	
    proc0 = subprocess.Popen(process0,shell=True)
    proc0.communicate()
    if var1:
       while True:
            print('Taking first price measurement')
            wjdata1 = requests.get('https://poloniex.com/public?command=returnTicker&period=60').json()
            for key in wjdata1:
                if re.match(r'BTC_' + var1 + '+', key):
                    print(key)       
                    pct2=(wjdata1[key]['last'])
                    pct3=Decimal(pct2)
                    pr1=format(pct3, 'f')
                    print(pr1)
            time.sleep(180)
            wjdata2 = requests.get('https://poloniex.com/public?command=returnTicker&period=60').json()
            print('Taking second price measurement')
            for key in wjdata2:
                if re.match(r'BTC_' + var1 + '+', key):
                    print(key)       
                    pct2=(wjdata2[key]['last'])
                    pct3=Decimal(pct2)
                    pr2=format(pct3, 'f')
                    print(pr2)
            if pr1 > pr2:
                print('Starting Sell Of: ' + variablestr + ' --  Sell 100 pct at 0pct markup or manually sell using poloniex web interface... Be careful not to encounter a bug')
                process1='./zenbot.sh sell --order_adjust_time=10000 --markup_pct=0 --debug  poloniex.' + variablestr	
                proc1 = subprocess.Popen(process1,shell=True)
                break
            else:
                print('Waiting for profit...')



# From now on, any update received will be passed to 'update_handler'
client.add_update_handler(update_handler)

input('Press <ENTER> to exit...')
client.disconnect()


