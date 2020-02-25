# 最もシンプルなJSONをPOSTするプログラム
# PythonのHelloWorldを終わらして間もない人でも理解できるように、コメントは多めにしています。

# flaskのFlaskとrequestをインポート
from flask import Flask, request
# JSONを扱うために、jsonをインポート
import json
# POSTするプログラムを書けるようにするために、requestsをインポートする
import requests

if __name__ == "__main__":
	# POSTを送るURLを定義
	url = "http://localhost:5000/"
	# POSTするJSONを定義
	jsonData = json.dumps({"name": "Yoshioka",
							"favorite": "fishing"})
	# POSTリクエストを送る (headersはおまじない)
	requests.post(url, jsonData, headers={"Content-Type": "application/json"})