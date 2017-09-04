
from __future__ import print_function
from telethon import TelegramClient
from telethon.tl.types import UpdateNewMessage
from telethon.tl.types import InputPeerChat
from telethon.tl.types import Message
from telethon.tl.types.input_peer_self import InputPeerSelf
from telethon.tl.types.input_peer_chat import InputPeerChat
from telethon.tl.types.input_peer_channel import InputPeerChannel
from telethon.tl.functions.messages.forward_message import ForwardMessageRequest
import sys, json, requests, re, unicodedata, subprocess, os, sqlite3, threading
from subprocess import PIPE,Popen,STDOUT
from decimal import *
from time import time
from time import sleep
import logging
from operator import itemgetter
from pymongo import MongoClient
import pandas as pd
import numpy as np
import multiprocessing







global sell
global flag
global variable
global var1
global sellstr
global buystr
global coincoin
global coin
print('Cryptoping Auto-Trader, with live updates...')
print('Cryptoping Auto-Trader, with live updates...')
print('Cryptoping Auto-Trader, with live updates...')
print('CTRL-C To exit')
print('CTRL-C To exit')
print('CTRL-C To exit')
print('To test me, type a coin into the cryptoping telegram bot window on telegram such as #LTC and #DASH')
print('When testing, look for a small-digit number in the 1-10000 range appearing in the console or a buy/sell order')
pid = 'coin.run'
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
    global coincoin
    global buystr
    global sellstr
    global sell
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
        word_list = ["#DCR", "#LTC", "#NAUT", "#NXT", "#XCP", "#GRC", "#REP", "#PPC", "#RIC", "#STRAT", "#GAME", "#BTM", "#CLAM", "#ARDR", "#BLK", "#OMNI", "#SJCX", "#FLDC", "#BCH", "#DOGE", "#POT", "#VRC", "#ETH", "#PINK", "#NOTE", "#BTS", "#AMP", "#NAV", "#BELA", "#BCN", "#ETC", "#FLO", "#VIA", "#XBC", "#XPM", "#DASH", "#XVC", "#GNO", "#NMC", "#RADS", "#VTC", "#XEM", "#FCT", "#XRP", "#NXC", "#STEEM", "#SBD", "#BURST", "#XMR", "#DGB", "#LBC", "#BCY", "#PASC", "#SC", "#LSK", "#EXP", "#MAID", "#BTCD", "#SYS", "#GNT", "#HUC", "#EMC2", "#NEOS", "#ZEC", "#STR", "#ZRX", "#EMC2"]
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
                    buy =  'buyit'
                    coincoin = var.replace('#', '')
                    if (os.path.isfile(pid)):
                        print('Waiting on current process to finish... If you experience errors, delete process.run')
                    else:
                        sell = 'notready'
                        m = multiprocessing.Process(target = runrun , args = ())
                        m.start()
                        client(ForwardMessageRequest(peer=peer1, id=(idd), random_id=(generate_random_long())))
                except Exception as e:
                    print(e)



logger = logging.getLogger(__name__)

def rsi(df, window, targetcol='weightedAverage', colname='rsi'):
    """ Calculates the Relative Strength Index (RSI) from a pandas dataframe
    http://stackoverflow.com/a/32346692/3389859
    """
    series = df[targetcol]
    delta = series.diff().dropna()
    u = delta * 0
    d = u.copy()
    u[delta > 0] = delta[delta > 0]
    d[delta < 0] = -delta[delta < 0]
    # first value is sum of avg gains
    u[u.index[window - 1]] = np.mean(u[:window])
    u = u.drop(u.index[:(window - 1)])
    # first value is sum of avg losses
    d[d.index[window - 1]] = np.mean(d[:window])
    d = d.drop(d.index[:(window - 1)])
    rs = u.ewm(com=window - 1,
               ignore_na=False,
               min_periods=0,
               adjust=False).mean() / d.ewm(com=window - 1,
                                            ignore_na=False,
                                            min_periods=0,
                                            adjust=False).mean()
    df[colname] = 100 - 100 / (1 + rs)
    return df


def sma(df, window, targetcol='weightedAverage', colname='sma'):
    """ Calculates Simple Moving Average on a 'targetcol' in a pandas dataframe
    """
    df[colname] = df[targetcol].rolling(window=window, center=False).mean()
    return df


def ema(df, window, targetcol='weightedAverage', colname='ema', **kwargs):
    """ Calculates Expodential Moving Average on a 'targetcol' in a pandas
    dataframe """
    df[colname] = df[targetcol].ewm(
        span=window,
        min_periods=kwargs.get('min_periods', 1),
        adjust=kwargs.get('adjust', True),
        ignore_na=kwargs.get('ignore_na', False)
    ).mean()
    return df
def emamacd(df, window, targetcol='macd', colname='ema', **kwargs):
    """ Calculates Expodential Moving Average on a 'targetcol' in a pandas
    dataframe """
    df[colname] = df[targetcol].ewm(
        span=window,
        min_periods=kwargs.get('min_periods', 1),
        adjust=kwargs.get('adjust', True),
        ignore_na=kwargs.get('ignore_na', False)
    ).mean()
    return df

def macd(df, fastcol='emafast', slowcol='emaslow', colname='macd'):
    """ Calculates the differance between 'fastcol' and 'slowcol' in a pandas
    dataframe """
    df[colname] = df[fastcol] - df[slowcol]
    return df


def bbands(df, window, targetcol='weightedAverage', stddev=2.0):
    """ Calculates Bollinger Bands for 'targetcol' of a pandas dataframe """
    if not 'sma' in df:
        df = sma(df, window, targetcol)
    df['bbtop'] = df['sma'] + stddev * df[targetcol].rolling(
        min_periods=window,
        window=window,
        center=False).std()
    df['bbbottom'] = df['sma'] - stddev * df[targetcol].rolling(
        min_periods=window,
        window=window,
        center=False).std()
    df['bbrange'] = df['bbtop'] - df['bbbottom']
    df['bbpercent'] = ((df[targetcol] - df['bbbottom']) / df['bbrange']) - 0.5
    return df


class Chart(object):
    """ Saves and retrieves chart data to/from mongodb. It saves the chart
    based on candle size, and when called, it will automaticly update chart
    data if needed using the timestamp of the newest candle to determine how
    much data needs to be updated """

    def __init__(self, api, pair, **kwargs):
        """
        api = poloniex api object
        pair = market pair
        period = time period of candles (default: 5 Min)
        """
        self.pair = pair
        self.api = api
        self.period = kwargs.get('period', self.api.MINUTE * 5)
        self.db = MongoClient()['poloniex']['%s_%s_chart' %
                                            (self.pair, str(self.period))]

    def __call__(self, size=0):
        """ Returns raw data from the db, updates the db if needed """
        # get old data from db
        old = sorted(list(self.db.find()), key=itemgetter('_id'))
        try:
            # get last candle
            last = old[-1]
        except:
            # no candle found, db collection is empty
            last = False
        # no entrys found, get last year of data to fill the db
        if not last:
            logger.warning('%s collection is empty!',
                           '%s_%s_chart' % (self.pair, str(self.period)))
            new = self.api.returnChartData(self.pair,
                                           period=self.period,
                                           start=time() - self.api.YEAR)
        # we have data in db already
        else:
            new = self.api.returnChartData(self.pair,
                                           period=self.period,
                                           start=int(last['_id']))
        # add new candles
        updateSize = len(new)
        logger.info('Updating %s with %s new entrys!',
                    self.pair + '-' + str(self.period), str(updateSize))
        # show progress
        for i in range(updateSize):
            print("\r%s/%s" % (str(i + 1), str(updateSize)), end=" complete ")
            date = new[i]['date']
            del new[i]['date']
            self.db.update_one({'_id': date}, {"$set": new[i]}, upsert=True)
        print('')
        logger.debug('Getting chart data from db')
        # return data from db
        return sorted(list(self.db.find()), key=itemgetter('_id'))[-size:]

    def dataFrame(self, size=0, window=120):
        # get data from db
        data = self.__call__(size)
        # make dataframe
        df = pd.DataFrame(data)
        # format dates
        df['date'] = [pd.to_datetime(c['_id'], unit='s') for c in data]
        # del '_id'
        del df['_id']
        # set 'date' col as index
        df.set_index('date', inplace=True)
        # calculate/add sma and bbands
        df = bbands(df, window)
        df = ema(df, window // 26, colname='emaslow')
        # add fast ema
        df = ema(df, window // 12, colname='emafast')
        # add macd
        df = macd(df)
        df = emamacd(df, window // 9, colname='emasig')
        df = macd(df)
        # add rsi
        df = rsi(df, window // 5)
        # add candle body and shadow size
        df['bodysize'] = df['open'] - df['close']
        df['shadowsize'] = df['high'] - df['low']
        # add percent change
        df['percentChange'] = df['close'].pct_change()
        return df



def runrun():
    open(pid, 'w').close()
    waitwait = 'notready'
    readyup = 'notready'
    print('Running Process Created, if you get errors delete process.run')
    while True:
        global sellstr
        global buystr
        global coincoin
        global coin
        global flag
        btcc='BTC_'
        coin= btcc + coincoin
        word=coin
        from poloniex import Poloniex
        api = Poloniex(jsonNums=float)
        df = Chart(api, word).dataFrame()
        df.dropna(inplace=True)
        data = (df.tail(2)[['macd']])
        data1 = (df.tail(2)[['emasig']])
        #Turn Data into a string
        txt=str(data)
        txt1=str(data1)
        # search for floats in the returned data
        re1='.*?'	# Non-greedy match on filler
        re2='([+-]?\\d*\\.\\d+)(?![-+0-9\\.])'	# Float 1
        re3='.*?'	# Non-greedy match on filler
        re4='([+-]?\\d*\\.\\d+)(?![-+0-9\\.])'	# Float 2
        rg = re.compile(re1+re2+re3+re4,re.IGNORECASE|re.DOTALL)
        m = rg.search(txt)
        re1='.*?'	# Non-greedy match on filler
        re2='([+-]?\\d*\\.\\d+)(?![-+0-9\\.])'	# Float 1
        re3='.*?'	# Non-greedy match on filler
        re4='([+-]?\\d*\\.\\d+)(?![-+0-9\\.])'	# Float 2
        rg = re.compile(re1+re2+re3+re4,re.IGNORECASE|re.DOTALL)
        m1 = rg.search(txt1)
        # Search for floats that are too small to trade decision on
        re1='.*?'	# Non-greedy match on filler
        re2='([+-]?\\d*\\.\\d+)(?![-+0-9\\.])'	# Float 1
        re3='((?:[a-z][a-z0-9_]*))'	# Variable Name 1
        re4='([-+]\\d+)'	# Integer Number 1
        re5='.*?'	# Non-greedy match on filler
        re6='([+-]?\\d*\\.\\d+)(?![-+0-9\\.])'	# Float 2
        re7='((?:[a-z][a-z0-9_]*))'	# Variable Name 2
        re8='([-+]\\d+)'	# Integer Number 2
        rg = re.compile(re1+re2+re3+re4+re5+re6+re7+re8,re.IGNORECASE|re.DOTALL)
        deny = rg.search(txt)
        re1='.*?'	# Non-greedy match on filler
        re2='([+-]?\\d*\\.\\d+)(?![-+0-9\\.])'	# Float 1
        re3='((?:[a-z][a-z0-9_]*))'	# Variable Name 1
        re4='([-+]\\d+)'	# Integer Number 1
        re5='.*?'	# Non-greedy match on filler
        re6='([+-]?\\d*\\.\\d+)(?![-+0-9\\.])'	# Float 2
        re7='((?:[a-z][a-z0-9_]*))'	# Variable Name 2
        re8='([-+]\\d+)'	# Integer Number 2
        rg = re.compile(re1+re2+re3+re4+re5+re6+re7+re8,re.IGNORECASE|re.DOTALL)
        deny1 = rg.search(txt1)
        # 4 if statements to decide what will happen...
        print(data)
        print(data1)
        print(waitwait)
        if deny and deny1:
            float1=deny.group(1) + deny.group(2) + deny.group(3)
            float2=deny.group(4) + deny.group(5) + deny.group(6)
            float3 = float(float1)
            float4 = float(float2)
            float5=deny1.group(1) + deny1.group(2) + deny1.group(3)
            float6=deny1.group(4) + deny1.group(5) + deny1.group(6)
            float7 = float(float5)
            float8 = float(float6)
            print(float3, float4, float7, float8)
            # Calculate the difference in the two numbers
            diff = Decimal(float(float7 - float3))
            diff1 = Decimal(float(float8 - float4))
            diffstr = str(diff)
            diffstr1 = str(diff1)
            diff4 = (diff1 - diff)
            diff4str=str(diff4)
            print(diffstr1)
            print('Buying ' + word + ' on error correction loop.')
            ke1=coincoin.replace('BTC_', '')
            ke3='-BTC'
            ke8=ke1+ke3
            buystr=ke8
            # HERE DIFF 4 IS HISTOGRAM SIGNAL ON UPTREND. DIFF 1 IS ACTUAL MACD SIGNAL
            if (Decimal(diff4) > 0):
                print('Buying on HIST UP: ' + word + ' Current macd hist diff is: ' + diff4str)
                buybuy()
                readyup = 'ready'
            if (Decimal(diff4) > 0) and (readyup == 'ready'):
                print('Setting MACD UP ready signal to sell: ' + word + ' Current macd hist diff is: ' + diff4str)
                waitwait = 'ready'
            elif (Decimal(diff4) < 0) and (waitwait == 'ready'):
                print('Selling on ready and macd down signal: ' + word + ' Current macd hist diff is: ' + diff4str)
                sellstr=ke8
                sellsell()
                break
            else:
                print('Waiting for MACD HIST up signal and macd UP signal for ready' + word + ' Current macd hist diff is: ' + diff4str)
        elif deny:
            float1=deny.group(1) + deny.group(2) + deny.group(3)
            float2=deny.group(4) + deny.group(5) + deny.group(6)
            float3 = float(float1)
            float4 = float(float2)
            float5=m1.group(1)
            float6=m1.group(2)
            float7 = float(float5)
            float8 = float(float6)
            print(float3, float4, float7, float8)
            # Calculate the difference in the two numbers
            diff = Decimal(float(float7 - float3))
            diff1 = Decimal(float(float8 - float4))
            diffstr = str(diff)
            diffstr1 = str(diff1)
            diff4 = (diff1 - diff)
            diff4str=str(diff4)
            print(diffstr1)
            print('Buying ' + word + ' on error correction loop.')
            ke1=word.replace('BTC_', '')
            ke3='-BTC'
            ke8=ke1+ke3
            buystr=ke8
            # HERE DIFF 4 IS HISTOGRAM SIGNAL ON UPTREND. DIFF 1 IS ACTUAL MACD SIGNAL
            if (Decimal(diff4) > 0):
                print('Buying on HIST UP: ' + word + ' Current macd hist diff is: ' + diff4str)
                buybuy()
                readyup = 'ready'
            if (Decimal(diff4) > 0) and (readyup == 'ready'):
                print('Setting MACD UP ready signal to sell: ' + word + ' Current macd hist diff is: ' + diff4str)
                waitwait = 'ready'
            elif (Decimal(diff4) < 0) and (waitwait == 'ready'):
                print('Selling on ready and macd down signal: ' + word + ' Current macd hist diff is: ' + diff4str)
                sellstr=ke8
                sellsell()
                break
            else:
                print('Waiting for MACD HIST up signal and macd UP signal for ready' + word + ' Current macd hist diff is: ' + diff4str)
        elif deny1:
            float1=m.group(1)
            float2=m.group(2)
            float3 = float(float1)
            float4 = float(float2)
            float5=deny1.group(1) + deny1.group(2) + deny1.group(3)
            float6=deny1.group(4) + deny1.group(5) + deny1.group(6)
            float7 = float(float5)
            float8 = float(float6)
            print(float3, float4, float7, float8)
            # Calculate the difference in the two numbers
            diff = Decimal(float(float7 - float3))
            diff1 = Decimal(float(float8 - float4))
            diffstr = str(diff)
            diffstr1 = str(diff1)
            diff4 = (diff1 - diff)
            diff4str=str(diff4)
            print(diffstr1)
            print('Buying ' + word + ' on error correction loop.')
            ke1=word.replace('BTC_', '')
            ke3='-BTC'
            ke8=ke1+ke3
            buystr=ke8
            # HERE DIFF 4 IS HISTOGRAM SIGNAL ON UPTREND. DIFF 1 IS ACTUAL MACD SIGNAL
            if (Decimal(diff4) > 0):
                print('Buying on HIST UP: ' + word + ' Current macd hist diff is: ' + diff4str)
                buybuy()
                readyup = 'ready'
            if (Decimal(diff4) > 0) and (readyup == 'ready'):
                print('Setting MACD UP ready signal to sell: ' + word + ' Current macd hist diff is: ' + diff4str)
                waitwait = 'ready'
            elif (Decimal(diff4) < 0) and (waitwait == 'ready'):
                print('Selling on ready and macd down signal: ' + word + ' Current macd hist diff is: ' + diff4str)
                sellstr=ke8
                sellsell()
                break
            else:
                print('Waiting for MACD HIST up signal and macd UP signal for ready' + word + ' Current macd hist diff is: ' + diff4str)
        elif m and m1:
            float1=m.group(1)
            float2=m.group(2)
            float3 = float(float1)
            float4 = float(float2)
            float5=m1.group(1)
            float6=m1.group(2)
            float7 = float(float5)
            float8 = float(float6)
            print(float3, float4, float7, float8)
            # Calculate the difference in the two numbers
            diff = Decimal(float(float7 - float3))
            diff1 = Decimal(float(float8 - float4))
            diffstr = str(diff)
            diffstr1 = str(diff1)
            diff4 = (diff1 - diff)
            diff4str=str(diff4)
            print(diffstr1)
            print('Buying ' + word + ' on error correction loop.')
            ke1=word.replace('BTC_', '')
            ke3='-BTC'
            ke8=ke1+ke3
            buystr=ke8
            # HERE DIFF 4 IS HISTOGRAM SIGNAL ON UPTREND. DIFF 1 IS ACTUAL MACD SIGNAL
            if (Decimal(diff4) > 0):
                print('Buying on HIST UP: ' + word + ' Current macd hist diff is: ' + diff4str)
                buybuy()
                readyup = 'ready'
            if (Decimal(diff4) > 0) and (readyup == 'ready'):
                print('Setting MACD UP ready signal to sell: ' + word + ' Current macd hist diff is: ' + diff4str)
                waitwait = 'ready'
            elif (Decimal(diff4) < 0) and (waitwait == 'ready'):
                print('Selling on ready and macd down signal: ' + word + ' Current macd hist diff is: ' + diff4str)
                sellstr=ke8
                sellsell()
                break
            else:
                print('Waiting for MACD HIST up signal and macd UP signal for ready' + word + ' Current macd hist diff is: ' + diff4str)
        else:
            print('Regex did not match any matches for m, m1 or deny and deny1')
    os.remove(pid)
    print('Done running loop, process file deted. Waiting for another coin...')

def buy():
    return multiprocessing.Process(target = buybuy , args = ())
 
def buybuy():
    global buystr
    variable=str(buystr)
    variablestr=str(variable)
    print('Starting BUY Of: ' + variablestr + ' Buying and waiting for macd HIST UP buy signal to allow macd sell.')
    process1='./zenbot.sh buy --order_adjust_time=20000 --markup_pct=-0.1  poloniex.' + variablestr	
    subprocess.call(process1,shell=True)

def sell():
    return multiprocessing.Process(target = sellsell , args = ())
 
def sellsell():
    global sellstr
    variable=str(sellstr)
    variablestr=str(variable)
    print('Starting SELL Of: ' + variablestr + 'Selling on macd sell signal. Lines have crossed!!!')
    process1='./zenbot.sh sell --order_adjust_time=20000 --markup_pct=-0.1 --debug  poloniex.' + variablestr	
    subprocess.call(process1,shell=True)

# From now on, any update received will be passed to 'update_handler'
while True:
    client.add_update_handler(update_handler)
    input('Press <ENTER> to exit...')
    client.disconnect()

