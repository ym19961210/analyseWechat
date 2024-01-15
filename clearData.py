import pandas as pd

# 读取Excel文件
df = pd.read_csv('D:\\deskpet\\chatlog.csv')

# 删除包含'<msg>'的行
df_filtered = df[~df['StrContent'].str.contains('<msg>', na=False)]

# 保存到新的Excel文件
df_filtered.to_csv('D:\\deskpet\\chatlogbak.csv', index=False)
