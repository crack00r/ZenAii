
from __future__ import print_function
from telethon import TelegramClient
from telethon.tl.types import UpdateNewMessage
from telethon.tl.types import InputPeerChat
from telethon.tl.types import Message
from telethon.tl.types.input_peer_self import InputPeerSelf
from telethon.tl.types.input_peer_chat import InputPeerChat
from telethon.tl.types.input_peer_channel import InputPeerChannel
from telethon.tl.functions.messages.forward_message import ForwardMessageRequest
import multiprocessing, sys, json, requests, re, unicodedata, subprocess, os, sqlite3, threading
from subprocess import PIPE,Popen,STDOUT
from decimal import *
from time import time
from time import sleep
import logging
from operator import itemgetter
from pymongo import MongoClient
import pandas as pd
import numpy as np










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
                    coincoin = var.replace('#', '')
                    btc = '-BTC'
                    buystr = coincoin + btc
                    m = buy()
                    m.start()
                    m = run()
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
        # add slow ema
        df = ema(df, window // 2, colname='emaslow')
        # add fast ema
        df = ema(df, window // 4, colname='emafast')
        # add macd
        df = macd(df)
        # add rsi
        df = rsi(df, window // 5)
        # add candle body and shadow size
        df['bodysize'] = df['open'] - df['close']
        df['shadowsize'] = df['high'] - df['low']
        # add percent change
        df['percentChange'] = df['close'].pct_change()
        return df


def run():
    while True:
        global sellstr
        global buystr
        global coincoin
        global coin
        btcc='BTC_'
        coin= btcc + coincoin
        from poloniex import Poloniex
        api = Poloniex(jsonNums=float)
        # Below is the coin list, please follow its format... I choose coins with volume above 1000 daily.
        # initiate the data calculations
        df = Chart(api, coin).dataFrame()
        df.dropna(inplace=False)
        data = (df.tail(2)[['macd']])
        #Turn Data into a string
        txt=str(data)
        print(data)
        # search for floats in the returned data
        re1='.*?'	# Non-greedy match on filler
        re2='([+-]?\\d*\\.\\d+)(?![-+0-9\\.])'	# Float 1
        re3='.*?'	# Non-greedy match on filler
        re4='([+-]?\\d*\\.\\d+)(?![-+0-9\\.])'	# Float 2
        rg = re.compile(re1+re2+re3+re4,re.IGNORECASE|re.DOTALL)
        m = rg.search(txt)
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
        # Two if statements to decide what will happen... buy/sell/deny trade on limited data
        if deny:
            # Set the floats from the data that are real numbers

            float1=deny.group(1)
            var1=deny.group(2)
            signed_int1=deny.group(3)
            float2=deny.group(4)
            var2=deny.group(5)
            signed_int2=deny.group(6)
            float1= float1 + var1 + signed_int1
            float2= float2 + var2 + signed_int2
            float3 = float(float1)
            float4 = float(float2)
            # Calculate the difference in the two numbers
            diff = Decimal(float(float4 - float3))
            diffstr = str(diff)
            if (Decimal(float3) == 0):
                print(coincoin + ' -- Not Enough Data On This Measurement')
            elif (Decimal(float4) == 0):
                print(coincoin + ' -- Not Enough Data On This Measurement')
            # If Macd is not positive, then sell
            elif ( 0 > diff):
                print(coincoin, Decimal(float3), Decimal(float4))
                print('Current diff is: ' + diffstr)
                ke1=coin.replace('BTC_', '')
                ke3='-BTC'
                ke8=ke1+ke3
                sellstr=ke8
                start(sell())
                break
            
            else:
                print(coincoin, Decimal(float3), Decimal(float4))
                print('Current diff is: ' + diffstr)
                print('Waiting...')
        elif m:
            # Set the floats from the data that are real numbers
            float1=m.group(1)
            float2=m.group(2)
            float3 = float(float1)
            float4 = float(float2)
            # Calculate the difference in the two numbers
            diff = Decimal(float(float4 - float3))
            diffstr = str(diff)
            if (Decimal(float3) == 0):
                print(coincoin + ' -- Not Enough Data On This Measurement')
            elif (Decimal(float4) == 0):
                print(coincoin + ' -- Not Enough Data On This Measurement')
            # If Macd is not positive, then sell
            elif ( 0 > diff):
                print(coincoin, Decimal(float3), Decimal(float4))
                print('Current diff is: ' + diffstr)
                ke1=coin.replace('BTC_', '')
                ke3='-BTC'
                ke8=ke1+ke3
                sellstr=ke8
                start(sell())
                break
             
            else:
                print(coincoin, Decimal(float3), Decimal(float4))
                print('Current diff is: ' + diffstr)
                print('Waiting...')

def buy():
    return multiprocessing.Process(target = buybuy , args = ())
 
def buybuy():
    global buystr
    variable=str(buystr)
    variablestr=str(variable)
    print('Starting BUY Of: ' + variablestr + ' -- MACD Is Increasing')
    process1='./zenbot.sh buy --order_adjust_time=10000 --debug  poloniex.' + variablestr	
    subprocess.Popen(process1,shell=True)

def sell():
    return multiprocessing.Process(target = sellsell , args = ())
 
def sellsell():
    global sellstr
    variable=str(sellstr)
    variablestr=str(variable)
    print('Starting SELL Of: ' + variablestr + ' -- Macd Is Decreasing')
    process1='./zenbot.sh sell --order_adjust_time=10000 --markup_pct=0 --debug  poloniex.' + variablestr	
    subprocess.Popen(process1,shell=True)

# From now on, any update received will be passed to 'update_handler'
client.add_update_handler(update_handler)
input('Press <ENTER> to exit...')
client.disconnect()

