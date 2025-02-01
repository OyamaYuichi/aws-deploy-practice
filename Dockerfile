FROM python:3.8
# 作業ディレクトリを指定
WORKDIR /src
# 現在のディレクトリのファイルを /srcディレクトリ(コンテナ上)に追加
ADD app.py .
# flaskのインストール
RUN pip install flask
#　実行
CMD ["python", "app.py"]