"""
    pip install openai
    pip install --upgrade deepl
    pip install requests
"""
from openai import OpenAI
import os
import time
import base64
import getpass
import main as mainfile
import sys
import shutil
import requests
DEEP_API_KEY ='55b8d148-cc17-4279-a736-2eb0c362e6ca:fx'
api_key='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'

text = mainfile.description
source_lang='JA'
target_lang='EN'

# パラメータの指定
params = {
            'auth_key' : DEEP_API_KEY,
            'text' : text,
            'source_lang' : source_lang, # 翻訳対象の言語
            "target_lang": target_lang  # 翻訳後の言語
        }

# リクエストを投げる
request = requests.post("https://api-free.deepl.com/v2/translate", data=params) # URIは有償版, 無償版で異なるため要注意
result = request.json()
translatedDiscription=result["translations"][0]["text"]


client = OpenAI(api_key=api_key)
"""client.api_key = os.getenv("OPENAI_API_KEY")  # API keyのセット"""



"""<<<<<<<<<<クレジット消費があるため、機能確認時以外はコメントアウト
response = client.images.generate(
  model="dall-e-3",  # モデル
  prompt=translatedDiscription+"photolike",  # プロンプト
  n=1,  # 生成数
  size="1024x1024",  # 解像度 dall-e-3では1024x1024、1792x1024、1024x1792
  response_format="b64_json",  # レスポンスフォーマット url or b64_json
  quality="hd",  # 品質 standard or hd
  style="vivid"  # スタイル vivid or natural
)



# 画像保存
for i, d in enumerate(response.data):
    with open(f"{mainfile.description}_imagename.png", "wb") as f:
        f.write(base64.b64decode(d.b64_json))
#画像移動
source_path = f"{mainfile.description}_imagename.png"
destination_path = "./images/"
shutil.move(source_path, destination_path)

コメントアウト>>>>>>>>>>"""
