import time
import ccxt

woo = ccxt.woo({
    'apiKey': 'IjKas5kA45ys6BPcS0sPLQ==',
    'secret': '3GR3LUUB54F2JQC34NYE2YDYLZCP',
    'apiId':  '7a8f0b6f-51ea-4f9a-b312-706b27703589',
})

symbol = 'PERP_CRV_USDT'
params = {}
since=None
while(True):
    try:
        if time.time()%60 >= 58.5:
            order = woo.create_market_sell_order (symbol, 1, params)
            time.sleep(1.5)
        if time.time()%60 <= 1.5:
            book = woo.fetch_order_book (symbol)
            crv = woo.fetch_my_trades('PERP_CRV_USDT')
            last = round(float(crv[len(crv)-1]['info']['executed_timestamp'])%60,2)
            b1 = book['bids'][0]
            b1p = b1[0]
            a1 = book['asks'][0]
            a1p = a1[0]
            print('bid', b1, crv[len(crv)-1]['price'], a1, 'ask', last)
            print('------------------------------------')
            cancel = woo.cancel_all_orders (symbol,params)
            hold = woo.fetch_position(symbol)['info']['holding']
            neutral = woo.create_limit_buy_order (symbol, abs(float(hold)), b1p-0.0004, params)#抵銷API費用
            time.sleep(50)
    except Exception as e:
        print(str(e))
        continue