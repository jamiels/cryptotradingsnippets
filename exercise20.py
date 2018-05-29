import requests, io, json, time
import matplotlib.pyplot as plt
import pandas as pd
import datetime as dt


def main(): 
    ETH_USD = 0
    BTC_USD = 1
    pairs = ['eth-usd','btc-usd']
    blotter, col_names = initialize_blotter()
    pl, pl_col_names = initialize_pl(pairs)
    
    blotter, pl = trade(blotter, pl, 1,pairs[ETH_USD])
    blotter, pl = trade(blotter,pl, 2,pairs[ETH_USD])
    blotter, pl = trade(blotter,pl, -1,pairs[ETH_USD])
    blotter, pl = trade(blotter,pl, 3.3,pairs[BTC_USD])
    
    print(blotter)

def trade(blotter, pl, qty, pair):
    bid, ask = get_price(pair)
    if qty > 0:
        price = ask
    else:
        price = bid
    data = pd.DataFrame([[dt.datetime.now(),pair,qty,price]],columns=['Timestamp','Pair','Quantity','Executed Price'])
    blotter = blotter.append(data, ignore_index=True)
    pl = update_pl (pl,pair,qty,price)
    return blotter, pl


def update_pl(pl,pair,qty,price):
    if qty > 0: # buy
        current_qty = pl.at[pair,'Position']
        current_vwap = pl.at[pair,'VWAP']
        new_vwap = calc_vwap(current_qty, current_vwap, qty, price)
        pl.at[pair,'Position'] = current_qty + qty
        pl.at[pair,'VWAP'] = new_vwap
        # TODO: Recalc UPL, etc.
    else: #handle sell
        pass
    
    return pl

def calc_vwap(current_qty, current_vwap, qty, price):
    current_dollar = current_qty * current_vwap
    new_dollar = current_dollar + (qty * price)
    new_qty = current_qty + qty
    new_vwap = new_dollar / new_qty
    return new_vwap
    
def initialize_pl(pairs):
    col_names = ['Pairs','Position','VWAP','UPL','RPL']
    pl = pd.DataFrame(columns=col_names)
    for p in pairs:
        data = pd.DataFrame([[p,0,0,0,0]],columns=col_names)
        pl = pl.append(data,ignore_index=True)
    return pl, col_names

def initialize_blotter():
    col_names = ['Timestamp','Pair','Quantity','Executed Price']
    df = pd.DataFrame(columns=col_names)
    return df, col_names

def get_price(pair):
    df = load('https://api.gdax.com/products/'+pair+'/book')
    ask = df.iloc[0]['asks'][0]
    bid = df.iloc[0]['bids'][0]
    return float(bid),float(ask)

def get_trades_for_product(product_id):
    return load('https://api.gdax.com/products/' + product_id + '/trades',printout=False)


def load(url,printout=False,delay=0,remove_bottom_rows=0,remove_columns=[]):
    time.sleep(delay)
    headers = {'User-Agent': 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_10_1) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/39.0.2171.95 Safari/537.36'}
    response = requests.get(url,headers=headers)
    df = pd.read_json(response.text)

    if remove_bottom_rows > 0:
        df.drop(df.tail(remove_bottom_rows).index,inplace=True)
    df.drop(columns=remove_columns,axis=1,inplace=True)
    df = df.dropna(axis=1)
    if printout:
        print(df.head())
        print(df.tail())
    return df





if __name__ == "__main__":
    main()


