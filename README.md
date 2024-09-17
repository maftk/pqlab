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

sqlにデータを入れる
```bash
python set_data.py
```
確認プログラムの起動
```bash
streamlit run lit.py
```
ブラウザでアクセス\
`localhost:8501`\
公開してみた\
`https://pqlab.onrender.com`\
読み込んでいて気付いたこと
`covit19_sum.sql`,`pref_code.sql`,`make_covit19_2.sql`から`init.sql`
を作った。
```sql
--covit19_sum.sql
--修正前
CREATE TABLE covit19_sum (
--修正後
CREATE TABLE covid19_sum (

--pref_code.sql
--修正前
INSERT INTO pref_code VALUES('01','�k�C�¹','Hokkaido');
--修正後
INSERT INTO pref_code VALUES('01','北海道','Hokkaido');

--make_covit19_2.sql
--追加
SELECT c.reporting_date,p.pref_code,c.Hokkaido FROM covid19_sum AS c CROSS JOIN pref_code AS p WHERE p.pref_code='01' UNION
```
終わり
