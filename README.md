# LogRelay
LogRelayは、ログメッセージをLINE, Slack, Discord, メールに転送するためのライブラリです。
※ 現在はLINEのみで順次追加予定です。

## プロジェクト情報

- **名前**: logrelay
- **バージョン**: 0.1.0
- **説明**: エラーログをLINEやメールなどの方法でリレーするライブラリ
- **依存関係**:
  - requests>=2.32.3
- **README**: [README.md](README.md)
- **Pythonバージョン**: >= 3.8

## インストール
```sh
pip install logrelay
```

## 使用方法 (LINE)
### 環境変数

1. [LINE Developers](https://developers.line.biz/ja/) でチャネルを作成
1. プロバイダー（または新規作成）を選択
1. Messaging API チャネルを作成
1. ｢チャネルアクセストークン（長期）｣ を取得
    - トップ > ユーザー名 > サービス名 > Messaging API設定 > チャネルアクセストークン > チャネルアクセストークン（長期）
1. QRコードをスマートフォンで読み込み友だち追加する
    - トップ > ユーザー名 > サービス名 > Messaging API設定 > ボット情報 > QRコード
1. ｢あなたのユーザーID｣を取得
    - トップ > ユーザー名 > サービス名 > チャネル基本設定 > 基本情報 > あなたのユーザーID
1. 環境変数に値を割り当てる
    - line_access_token: チャネルアクセストークン（長期）
    - user_id: あなたのユーザーID

### 使用例
```python
import requests
from logrelay import LogRelay

line_access_token = "YOUR_LINE_ACCESS_TOKEN"
user_id = "TARGET_USER_ID"

log_relay = LogRelay(line_access_token, user_id)

try:
    response = requests.get("https://example.com/api")
    response.raise_for_status()
except requests.exceptions.RequestException as e:
    error_message = f"<Example_Service>Error: {str(e)}"
    log_relay.send_line_message(error_message)
    print(error_message)
```

