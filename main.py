import glob
import os
import re
import pikepdf
import tika
import openpyxl

tika.initVM()
from tika import parser
from nltk.stem import WordNetLemmatizer

wb = openpyxl.load_workbook("all.xlsx")
ws = wb["総合政策"]

"""
for row in ws.rows:
	addrs = []
	for cell in row:
		addrs.append(cell.value)
	print(",".join(addrs))
"""

values = []
for cell in ws['B']:
    values.append(cell.value.lower())
#print(values)
#print(len(values))


# 単語カウント-------------------------
# 単語を数える辞書を作成
words = {}
# split()でスペースと改行で分割したリストから単語を取り出す
for word in values:


    #存在しない単語や固有名詞を除外



    #動詞と名詞を原型にする
    lemmatizer = WordNetLemmatizer()
    word = lemmatizer.lemmatize(word, pos="v")  # 動詞原型にしてくれる
    word = lemmatizer.lemmatize(word, pos="n")  # 名詞原型にしてくれる
    word = lemmatizer.lemmatize(word, pos="a")  # 形容詞原型にしてくれる

    # 単語をキーとして値に1を足していく。
    # 辞書に単語がない、すなわち初めて辞書に登録するときは0+1になる。
    words[word] = words.get(word, 0) + 1  #

# リストに取り出して単語の出現回数でソート
d = [(v, k) for k, v in words.items()]
d.sort()
d.reverse()

#標準出力-------------------------


for count, word in d:
    print(count, word)