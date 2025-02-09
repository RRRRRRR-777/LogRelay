import requests


class LogRelay:
    """
    LogRelay: 指定されたメッセージをLINEに送信するライブラリ
    """
    def __init__(self, line_access_token: str, user_id: str):
        """
        :param line_access_token: LINEのチャネルアクセストークン
        :param user_id: 送信対象のユーザーID
        """
        # 引数をインスタンス変数に格納
        self.line_access_token = line_access_token
        self.user_id = user_id
        # LINE API エンドポイント
        self.LINE_API_URL = "https://api.line.me/v2/bot/message/push"
        if not self.line_access_token or not self.user_id:
            raise ValueError("LINE_ACCESS_TOKEN または USER_ID が設定されていません。")

    def send_line_message(self, message: str):
        """
        指定されたメッセージをLINEに送信する
        :param message: 送信するメッセージ（String型）
        :return: APIレスポンス（JSON形式）
        """
        headers = {
            "Content-Type": "application/json",
            "Authorization": f"Bearer {self.line_access_token}",
        }
        data = {
            "to": self.user_id,
            "messages": [{"type": "text", "text": message}],
        }

        try:
            response = requests.post(self.LINE_API_URL, headers=headers, json=data)
            response.raise_for_status()  # HTTPエラーがある場合は例外を発生
            return response.json()
        except requests.exceptions.RequestException as e:
            return {"error": str(e)}
