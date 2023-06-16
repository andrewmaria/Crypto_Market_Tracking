import ccxt
import time
import numpy as np

woo = ccxt.woo({
    'apiKey': 'IjKas5kA45ys6BPcS0sPLQ==',
    'secret': '3GR3LUUB54F2JQC34NYE2YDYLZCP',
    'apiId':  '7a8f0b6f-51ea-4f9a-b312-706b27703589',
})

symbol = 'PERP_LDO_USDT'
params = {}
since=None
c = 250
while(c):
    try:
        if time.time()%120 <= 1.5:
            book = woo.fetch_order_book (symbol)
            a1 = book['asks'][0][0]
            print(a1)
            order = woo.create_limit_buy_order (symbol, 50, a1, params)
            c -= 1
            time.sleep(58)
    except Exception as e:
        print(str(e))
        continue

