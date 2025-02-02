import os

import requests
from dotenv import load_dotenv

load_dotenv('.env')

# LINE API エンドポイント
LINE_API_URL = "https://api.line.me/v2/bot/message/push"
# 取得したチャネルアクセストークン
LINE_ACCESS_TOKEN = os.environ["LINE_ACCESS_TOKEN"]

# 送信対象のユーザーID
USER_ID = os.environ["USER_ID"]

def send_line_message(message):
    headers = {
        "Content-Type": "application/json",
        "Authorization": f"Bearer {LINE_ACCESS_TOKEN}",
    }
    data = {
        "to": USER_ID,
        "messages": [{"type": "text", "text": message}],
    }

    response = requests.post(LINE_API_URL, headers=headers, json=data)
    return response.json()

# 送信テスト
message = "こんにちは！これはテストメッセージです。"
try:
    send_line_message(f"エラーが発生しました。\nエラー内容{message}")
except Exception as e:
    send_line_message(f"LogRelay APIにて問題が発生しました。\nエラー内容: {e}")
