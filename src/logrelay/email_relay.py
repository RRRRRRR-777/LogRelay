import smtplib
from email.mime.multipart import MIMEMultipart
from email.mime.text import MIMEText


class EmailRelay:
    """
    EmailRelay: エラーメッセージをメールで送信するクラス
    """

    def __init__(self, smtp_server: str, smtp_port: int, smtp_user: str, smtp_password: str):
        """
        :param smtp_server: SMTPサーバーのアドレス
        :param smtp_port: SMTPサーバーのポート
        :param smtp_user: SMTPサーバーのユーザー名
        :param smtp_password: SMTPサーバーのパスワード
        """
        self.smtp_server = smtp_server
        self.smtp_port = smtp_port
        self.smtp_user = smtp_user
        self.smtp_password = smtp_password

    def send_message(self, error_message: str):
        """
        エラーメッセージをメールで送信する
        :param error_message: 送信するエラーメッセージ（String型）
        """
        msg = MIMEMultipart()
        msg['From'] = self.smtp_user
        msg['To'] = self.smtp_user
        msg['Subject'] = "LogRelay Error Notification"

        body = f"An error occurred: {error_message}"
        msg.attach(MIMEText(body, 'plain'))

        try:
            server = smtplib.SMTP(self.smtp_server, self.smtp_port)
            server.starttls()
            server.login(self.smtp_user, self.smtp_password)
            text = msg.as_string()
            server.sendmail(self.smtp_user, self.smtp_user, text)
            server.quit()
        except Exception as e:
            print(f"Failed to send email: {str(e)}")
