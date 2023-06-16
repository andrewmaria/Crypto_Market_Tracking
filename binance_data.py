from binance.client import Client
import pandas as pd
import time
api_key = 'bn3I2XFfzoAz9RkXPoFpsTrUBQE8wHNeQcpusr1f4qGRKQg57HstVmZDH858UOYx'
api_secret = '0L3jcElJE7XMSu0D2dl4Eu6aLoqDm9VaENA25rM3iNdbgDXBZvD837nqbQ6NDugh'
client = Client(api_key, api_secret)

# 定义变量
symbol = "MATICUSDT"
interval = Client.KLINE_INTERVAL_1HOUR
start_date = "1 Jan 2020"
end_date = "28 Feb 2023"
start_timestamp = pd.Timestamp(start_date).timestamp() * 1000
# 创建空数据帧
df = pd.DataFrame()

# 循环获取数据
for i in range(0, 1000000):
    # 获取数据
    klines = client.get_historical_klines(symbol, interval, str(int(start_timestamp)), end_date)
    if len(klines) == 0:
        break
    # 将数据转换为Pandas数据帧
    new_df = pd.DataFrame(klines, columns=['timestamp', 'open', 'high', 'low', 'close', 'volume', 'close_time', 'quote_asset_volume', 'number_of_trades', 'taker_buy_base_asset_volume', 'taker_buy_quote_asset_volume', 'ignore'])
    # 将时间戳转换为日期时间
    new_df['timestamp'] = pd.to_datetime(new_df['timestamp'], unit='ms')
    # 将时间戳转换为毫秒时间戳
    new_df['timestamp'] = new_df['timestamp'].apply(lambda x: x.timestamp() * 1000)
    # 选择需要保存的列
    new_df = new_df[['timestamp', 'open', 'high', 'low', 'close']]
    # 将新的数据添加到数据帧中
    df = pd.concat([df, new_df], ignore_index=True)
    # 更新起始时间
    last_timestamp = klines[-1][0]
    start_timestamp = last_timestamp + 60 * 60 * 1000  # 将时间戳增加1小时
    
df['timestamp'] = pd.to_datetime(df['timestamp'], unit='ms')
# 将数据保存为CSV文件
df.to_csv('matic.csv', index=False)