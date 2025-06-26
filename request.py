import requests
import time
import os
from dotenv import load_dotenv

load_dotenv()
# リクエストを投げるURL
URL = os.getenv("REQUEST_URL", "http://localhost/")
# 1秒間に2回リクエストを投げるため、リクエスト間の待機時間は0.5秒
# (1秒 / 2回 = 0.5秒)
# INTERVAL = 0.5
INTERVAL = 1

def make_request():
    """
    指定されたURLにGETリクエストを送信し、結果を表示する関数
    """
    try:
        # GETリクエストを送信
        response = requests.get(URL)

        # ステータスコードとレスポンスサイズを表示
        print(f"[{time.strftime('%Y-%m-%d %H:%M:%S')}] Request to {URL}: "
              f"Status Code = {response.status_code}, "
              f"Content Length = {len(response.content)} bytes")

        # 成功した場合は追加情報も表示（例: レスポンス時間）
        # print(f"  Response Time: {response.elapsed.total_seconds():.4f} seconds")

    except requests.exceptions.ConnectionError as e:
        print(f"[{time.strftime('%Y-%m-%d %H:%M:%S')}] Connection Error: {e}")
    except requests.exceptions.Timeout:
        print(f"[{time.strftime('%Y-%m-%d %H:%M:%S')}] Timeout Error: Request timed out")
    except requests.exceptions.RequestException as e:
        print(f"[{time.strftime('%Y-%m-%d %H:%M:%S')}] An error occurred: {e}")

def main():
    """
    メイン関数：定期的にリクエストを送信するループ
    """
    print(f"Starting to send requests to {URL} every {INTERVAL} seconds...")
    try:
        while True:
            make_request()
            time.sleep(INTERVAL) # 指定された時間だけ待機
    except KeyboardInterrupt:
        print("\nProgram terminated by user.")
    except Exception as e:
        print(f"An unexpected error occurred: {e}")

if __name__ == "__main__":
    main()