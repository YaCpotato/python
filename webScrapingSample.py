#サイトのHTML要素によっては正常に動きません
# coding: UTF-8
import requests
from bs4 import BeautifulSoup
from urllib.parse import urljoin

# ユーザー名とパスワードの指定
USER = ""
PASS = ""

# セッションを開始
session = requests.session()

# ログイン：：：よくわかっていない
login_info = {
    "login":USER,
    "passwd":PASS,
}

# action
url_login = ""#ログインリクエストを含めたURLを記述
res = session.post(url_login, data=login_info)
res.raise_for_status() # エラーならここで例外を発生させる

print(res.text)


#参考URL:https://qiita.com/shunyooo/items/36af8bcb501baf8c7014
