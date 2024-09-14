環境の構築手順
リポジトリをクローン

```bash
git clone <リポジトリURL>
cd <リポジトリディレクトリ>
```
Dockerイメージのビルド 以下のコマンドを使用して、Dockerイメージをビルドし、サービスを起動します。
```bash
docker-compose up --build
```
データベース接続確認 PostgreSQLコンテナが正しく動作しているかを確認するには、次のコマンドでコンテナに接続できます。

```bash
docker exec -it db psql -U postgres

```
Pythonコンテナの操作 Python環境を操作するには、次のコマンドを使用します。
```bash
docker exec -it py bash

```
