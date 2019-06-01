import pandas as pd
import jieba
import numpy
from wordcloud import WordCloud
import matplotlib.pyplot as plt
import matplotlib
def drop_stopwords(content,stopwords):
    content_clean=[]
    all_words=[]
    for line in content:
        line_clean=[]
        for word in line:
            if word in stopwords:
                continue
            line_clean.append(word)
            all_words.append(str(word))
        content_clean.append(line_clean)
    return content_clean,all_words
pd.set_option('display.width',None)
df_news=pd.read_csv('./data/Preliminary-finals.csv',names=['category','theme','URL','content'],encoding='utf-8',sep='\t')
df_news=df_news.dropna()
# print(df_news.head())
content=df_news.content.values.tolist()
# print(content[1000])
content_S=[]
for line in content:
    current_segment=jieba.lcut(line)
    if len(current_segment)>1 and current_segment!='\r\n':
        content_S.append(current_segment)
# print(content_S[1000])
df_content=pd.DataFrame({'content_S':content_S})
stopwords=pd.read_csv('./data/stopwords.txt',index_col=False,sep='\t',quoting=3,names=['stopword'],encoding='utf-8')
contents=df_content.content_S.values.tolist()
stopwords=stopwords.stopword.values.tolist()
content_clean,all_words=drop_stopwords(contents,stopwords)
df_content=pd.DataFrame({'contentes_clean':content_clean})
df_all_words=pd.DataFrame({'all_words':all_words})
print(df_all_words.head())
#构建词云
words_count=df_all_words.groupby('all_words')
words_count.head()
# print(df_content.head())
matplotlib.rcParams['figure.figsize']=(10.0,5.0)
wordcloud=WordCloud(font_path="./data/simhei.ttf",background_color="white",max_font_size=80)
word_frequence={x[0]:x[1] for x in words_count.head(100).values}
wordcloud=wordcloud.fit_words(word_frequence)
plt.imshow(wordcloud)

#提取关键词
import jieba.analyse
index=1000
print(df_news['content'][index])
content_S_str="".join(content_S[index])
print(" ".join(jieba.analyse.extract_tags(content_S_str,topK=5,withWeight=False)))