import requests
from bs4 import BeautifulSoup
import pandas as pd

url = 'https://iftp.chinamoney.com.cn/english/bdInfo/'
response = requests.get(url)
soup = BeautifulSoup(response.text, 'html.parser')

# 找到表格并提取所需数据
table = soup.find("tabel")
data = []
headers = ['ISIN', 'Bond Code', 'Issuer', 'Bond Type', 'Issue Date', 'Latest Rating']

for row in table.find_all('tr'):
    cells = row.find_all('td')
    if len(cells) == len(headers):
        data.append([cell.text.strip() for cell in cells])


df = pd.DataFrame(data, columns=headers)

# 根据条件过滤数据
filtered_df = df[(df['Bond Type'] == 'Treasury Bond') & (df['Issue Date'].str.contains('2023'))]

# 保存为CSV文件
filtered_df.to_csv('bond_data.csv', index=False)