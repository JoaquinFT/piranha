from django.shortcuts import render
from django.http import HttpResponse
from collect.models import Trades, Config, Spreads
import requests

# Create your views here.
def index(request):
    try:
        print(Config.objects.values())
    except:
        print('problemos')
    return HttpResponse(Trades.objects.values())

def trades(request, pair = 'XBTEUR'):
    try:
        #check if is the first time or not
        try:
            since = Config.objects.filter(pair = pair, series = 'trades')[0].last
        except:
            since = None
        params = {'pair': pair}
        if since:
            params['since'] = since
        trades = requests.get('https://api.kraken.com/0/public/Trades', params = params).json()
        result = trades.get('result', {})
        assert(len(result.keys()) == 2), "More than two keys on trades[result]"
        assert('last' in result), "There is no [last] key in trades[result]"
        for k in result.keys():
            if k == 'last':
                last = str(result.get('last'))
            else:
                data = result[k]
        bulk = []
        for x in data:
            price = float(x[0])
            volume = float(x[1])
            time = float(x[2])
            bulk.append(Trades(price = price, time = time, volume = volume, pair = pair))
        Trades.objects.bulk_create(bulk)
        print('ADDED NEW ' + str(len(data)) + ' OBJECTS')
        if last and since:
            Config.objects.filter(pair = pair, series = 'trades').update(last = last)
        else:
            Config.objects.create(pair = pair, series = 'trades', last = last)
        return HttpResponse('DONE')
    except Exception as e:
        print(e)
        return HttpResponse('DONE')

def spreads(request, pair = 'XBTEUR'):
    try:
        #check if is the first time or not
        try:
            since = Config.objects.filter(pair = pair, series = 'spreads')[0].last
        except:
            since = None
        params = {'pair': pair}
        if since:
            params['since'] = since
        spreads = requests.get('https://api.kraken.com/0/public/Spread', params = params).json()
        result = spreads.get('result', {})
        assert(len(result.keys()) == 2), "More than two keys on trades[result]"
        assert('last' in result), "There is no [last] key in trades[result]"
        for k in result.keys():
            if k == 'last':
                last = str(result.get('last'))
            else:
                data = result[k]
        bulk = []
        for x in data:
            time = float(x[0])
            bid = float(x[1])
            ask = float(x[2])
            bulk.append(Spreads(time = time, bid = bid, ask = ask, pair = pair))
        Spreads.objects.bulk_create(bulk)
        print('ADDED NEW ' + str(len(data)) + ' OBJECTS')
        if last and since:
            Config.objects.filter(pair = pair, series = 'spreads').update(last = last)
        else:
            Config.objects.create(pair = pair, series = 'spreads', last = last)
        return HttpResponse('DONE')
    except Exception as e:
        print(e)
        return HttpResponse('DONE')
