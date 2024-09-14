環境の構築手順
リポジトリをクローン

```bash
git clone https://github.com/maftk/pqlab.git
cd pqlab
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

読み込んでいて気付いたこと
`covit19_sum.sql`,`pref_code.sql`,`make_covit19_2.sql`から`init.sql`
を作った。
```sql
--covit19_sum.sql
CREATE TABLE covid19_sum (--covit19_sum > covid19_sum

--pref_code.sql
--pref_name列に入る漢字の文字化けを修正
--修正前
INSERT INTO pref_code VALUES('01','kC¹','Hokkaido');
--修正後
INSERT INTO pref_code VALUES('01','北海道','Hokkaido');


--make_covit19_2.sql
--covit19.sum.sqlにより作られたテーブル名が間違ってた
covid19_sum AS c --最初に見つけたエラー部分
```
