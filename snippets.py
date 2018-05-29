# Used in exercise 1
pizza_tx_hash = "a1075db55d416d3ca199f55b6084e2115b9345e16c5cf302fc80e9d5fbf5d48d"

pizza_block_hash = "00000000152340ca42227603908689183edc47355204e7aca59383b0aaac1fd8"


laszlo_addr = "1XPTgDRhN8RFnzniWCddobD9iKZatrvH4"

# Used in later exercises
headers = {'User-Agent': 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_10_1) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/39.0.2171.95 Safari/537.36'}

if __name__ == "__main__":
    main()
    
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

def build_request():
    return "{ \"type\": \"subscribe\",    \"channels\": [{ \"name\": \"heartbeat\", \"product_ids\": [\"ETH-USD\"] }]}"
