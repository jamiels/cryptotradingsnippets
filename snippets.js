        conbaseProRequest = `
    {
        "type": "subscribe",
        "product_ids": [
            "ETH-USD"
        ],
        "channels": [
            "level2",
            "ticker",
            {
                "name": "ticker",
                "product_ids": [
                    "ETH-USD"
                ]
            }
        ]
    }`
    
    
    
    bitfinexRequest = `
    {
        "event":"subscribe",
        "channel":"book",
        "symbol":"ETHUSD"
     }

    pizzaBlockHash = "00000000152340ca42227603908689183edc47355204e7aca59383b0aaac1fd8";
    pizzaTxHash = "a1075db55d416d3ca199f55b6084e2115b9345e16c5cf302fc80e9d5fbf5d48d";
    
    laszloAddress = "1XPTgDRhN8RFnzniWCddobD9iKZatrvH4";
    
    function getHeaders() {
    return {'User-Agent': 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_11_6) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/61.0.3163.100 Safari/537.36'};
    }

function requestBuilder() {
    request = `
    {
        "type": "subscribe",
        "product_ids": [
            "ETH-USD"
        ],
        "channels": [
            "level2",
            "ticker",
            {
                "name": "ticker",
                "product_ids": [
                    "ETH-USD"
                ]
            }
        ]
    }`

    return request;
}
    
    
