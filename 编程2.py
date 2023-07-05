import pandas as pd

url = 'https://edidata.oss-cn-beijing.aliyuncs.com/fyx_chinamoney.csv'
data = pd.read_csv(url)
# 将列表拆分为多个批次并打印输出
batch = 80
for i in range(0, len(data), batch):
    bat = data[i:i+batch]
    print(bat)