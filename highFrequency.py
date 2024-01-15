import pandas as pd
from collections import Counter
import jieba
import matplotlib.pyplot as plt

# 读取CSV文件，并将所有的值转换为字符串
df = pd.read_csv('D:\\deskpet\\chatlogbak.csv').astype(str)

# 对方发送的消息
other_messages = df[df['IsSender'] == '0']['StrContent']
# 我方发送的消息
my_messages = df[df['IsSender'] == '1']['StrContent']

stopwords = ['我', '你', '了', '的', '呀', '啦', '吗', '吧', '[', ']', '，', '是', '也', '有', '哦', '  ', '他','？','～','~','。',]

# 对消息进行分词，并过滤停用词
other_words = [word for message in other_messages for word in jieba.cut(message) if word not in stopwords]
my_words = [word for message in my_messages for word in jieba.cut(message) if word not in stopwords]

# 统计词频
other_word_counts = Counter(other_words)
my_word_counts = Counter(my_words)

# 打印词频前50的词语和出现的次数
print('对方发送的消息的词频前50的词语和出现的次数:')
for word, count in other_word_counts.most_common(50):
    print(word, count)

print('我方发送的消息的词频前50的词语和出现的次数:')
for word, count in my_word_counts.most_common(50):
    print(word, count)


other_top50 = other_word_counts.most_common(50)
my_top50 = my_word_counts.most_common(50)

plt.rcParams['font.sans-serif'] = ['SimHei']  # Windows系统
plt.rcParams['axes.unicode_minus'] = False  # 用来正常显示负号

# 绘制对方发送的消息的词频图
plt.figure(figsize=(10, 5))
plt.bar(*zip(*other_top50))
plt.title('Top 50 words in messages sent by the other party')
plt.xlabel('Words')
plt.ylabel('Frequency')
plt.xticks(rotation=90)
plt.show()

# 绘制我方发送的消息的词频图
plt.figure(figsize=(10, 5))
plt.bar(*zip(*my_top50))
plt.title('Top 50 words in messages sent by me')
plt.xlabel('Words')
plt.ylabel('Frequency')
plt.xticks(rotation=90)
plt.show()