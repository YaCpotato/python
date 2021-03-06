#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Sun Jun  2 00:06:11 2019

@author: shoichi
"""

import requests
from bs4 import BeautifulSoup
from requests.compat import urljoin
from time import sleep

url = 'https://pokemon.gamepedia.jp/rgbp/monsters/page/4'
# スクレイピングするユーザーエージェントを指定
headers = {'User-Agent':'Mozilla/5.0'}
soup = BeautifulSoup(requests.get(url,headers=headers).content,'html')
images = [] # 画像リストの空配列
print('check')
for img in soup.find_all('img', class_="media-object"):
    # コンソールへスクレイピング対象の画像URLを表示。特段必須ではない
    print(img.get("src"))
    ab_path = urljoin(url,img.get("src"))
    # imagesの空配列へsrcを登録
    images.append(ab_path)

# imagesからtargetに入れる
for target in images:
    target = target.split('?')[0]
    re = requests.get(target)
    with open('./pokemon/' + target.split('/')[-1], 'wb') as f: # imgフォルダに格納
      # .contentで画像データとして書き込む
      f.write(re.content)
      print(target)
      #サイトに負荷をかけないように適度なスリープを！
      sleep(10)

# スクレイピング終了確認
print("画像保存が完了しました。")
