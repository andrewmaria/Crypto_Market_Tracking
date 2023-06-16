import time
import ccxt

woo = ccxt.woo({
    'apiKey': 'IjKas5kA45ys6BPcS0sPLQ==',
    'secret': '3GR3LUUB54F2JQC34NYE2YDYLZCP',
    'apiId':  '7a8f0b6f-51ea-4f9a-b312-706b27703589',
})

symbol = 'PERP_SUSHI_USDT'
params = {}
since=None
while(True):
    try:
        book = woo.fetch_order_book (symbol)
        trade = woo.fetch_trades(symbol, since, 1, params)
        current = trade[0]['info']['executed_price']
        b1 = book['bids'][0]
        b1p = b1[0]
        a1 = book['asks'][0]
        a1p = a1[0]
        if time.time()%60 >= 58.2:
            order = woo.create_market_sell_order (symbol, 1, params)
            print('bid', b1, '  ', current, '  ', a1, 'ask')
            print('------------------------------------')
            cancel = woo.cancel_all_orders (symbol,params)
            hold = woo.fetch_position(symbol)['info']['holding']
            neutral = woo.create_limit_buy_order (symbol, abs(float(hold)), b1p-0.001, params)#抵銷API費用
        time.sleep(0.5)
    except Exception as e:
        print(str(e))
        continue

#標記價格 = P1, P2, P3 之中位數
#P1 = 指數價格 * (1+最新資金費率 * (Time Until Funding /60))
#P2 = 指數價格 + 滾動平均值 (每30分鐘)
#P3 = 最新成交價，最優買價，最優賣價，三個價格中的中位數
#Funding rate=clamp[ 60_min_TWAP_(P3-index_price)/index_price)，0.003，-0.003] /24