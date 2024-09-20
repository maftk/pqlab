from sqlalchemy import text

init_sql = text('''
CREATE TABLE covid19_sum (--covit19_sum > covid19_sum
  reporting_date DATE
  , nationwide INTEGER
  , hokkaido INTEGER
  , aomori INTEGER
  , iwate INTEGER
  , miyagi INTEGER
  , akita INTEGER
  , yamagata INTEGER
  , fukushima INTEGER
  , ibaraki INTEGER
  , tochigi INTEGER
  , gunma INTEGER
  , saitama INTEGER
  , chiba INTEGER
  , tokyo INTEGER
  , kanagawa INTEGER
  , niigata INTEGER
  , toyama INTEGER
  , ishikawa INTEGER
  , fukui INTEGER
  , yamanashi INTEGER
  , nagano INTEGER
  , gifu INTEGER
  , shizuoka INTEGER
  , aichi INTEGER
  , mie INTEGER
  , shiga INTEGER
  , kyoto INTEGER
  , osaka INTEGER
  , hyogo INTEGER
  , nara INTEGER
  , wakayama INTEGER
  , tottori INTEGER
  , shimane INTEGER
  , okayama INTEGER
  , hiroshima INTEGER
  , yamaguchi INTEGER
  , tokushima INTEGER
  , kagawa INTEGER
  , ehime INTEGER
  , kochi INTEGER
  , fukuoka INTEGER
  , saga INTEGER
  , nagasaki INTEGER
  , kumamoto INTEGER
  , oita INTEGER
  , miyazaki INTEGER
  , kagoshima INTEGER
  , okinawa INTEGER
);

copy covid19_sum from '/data/covid19_sum.csv' with csv;

--pref_code.sql
CREATE TABLE pref_code
(
  pref_code	CHAR(2),
  pref_name	VARCHAR(16),
  eng_pref_name	VARCHAR(16)
)
;
--pref_name列に入る漢字の文字化けを修正
INSERT INTO pref_code VALUES('01','北海道','Hokkaido');
INSERT INTO pref_code VALUES('02','青森県','Aomori');
INSERT INTO pref_code VALUES('03','岩手県','Iwate');
INSERT INTO pref_code VALUES('04','宮城県','Miyagi');
INSERT INTO pref_code VALUES('05','秋田県','Akita');
INSERT INTO pref_code VALUES('06','山形県','Yamagata');
INSERT INTO pref_code VALUES('07','福島県','Fukushima');
INSERT INTO pref_code VALUES('08','茨城県','Ibaraki');
INSERT INTO pref_code VALUES('09','栃木県','Tochigi');
INSERT INTO pref_code VALUES('10','群馬県','Gunma');
INSERT INTO pref_code VALUES('11','埼玉県','Saitama');
INSERT INTO pref_code VALUES('12','千葉県','Chiba');
INSERT INTO pref_code VALUES('13','東京都','Tokyo');
INSERT INTO pref_code VALUES('14','神奈川県','Kanagawa');
INSERT INTO pref_code VALUES('15','新潟県','Niigata');
INSERT INTO pref_code VALUES('16','富山県','Toyama');
INSERT INTO pref_code VALUES('17','石川県','Ishikawa');
INSERT INTO pref_code VALUES('18','福井県','Fukui');
INSERT INTO pref_code VALUES('19','山梨県','Yamanashi');
INSERT INTO pref_code VALUES('20','長野県','Nagano');
INSERT INTO pref_code VALUES('21','岐阜県','Gifu');
INSERT INTO pref_code VALUES('22','静岡県','Shizuoka');
INSERT INTO pref_code VALUES('23','愛知県','Aichi');
INSERT INTO pref_code VALUES('24','三重県','Mie');
INSERT INTO pref_code VALUES('25','滋賀県','Shiga');
INSERT INTO pref_code VALUES('26','京都府','Kyoto');
INSERT INTO pref_code VALUES('27','大阪府','Osaka');
INSERT INTO pref_code VALUES('28','兵庫県','Hyogo');
INSERT INTO pref_code VALUES('29','奈良県','Nara');
INSERT INTO pref_code VALUES('30','和歌山県','Wakayama');
INSERT INTO pref_code VALUES('31','鳥取県','Tottori');
INSERT INTO pref_code VALUES('32','島根県','Shimane');
INSERT INTO pref_code VALUES('33','岡山県','Okayama');
INSERT INTO pref_code VALUES('34','広島県','Hiroshima');
INSERT INTO pref_code VALUES('35','山口県','Yamaguchi');
INSERT INTO pref_code VALUES('36','徳島県','Tokushima');
INSERT INTO pref_code VALUES('37','香川県','Kagawa');
INSERT INTO pref_code VALUES('38','愛媛県','Ehime');
INSERT INTO pref_code VALUES('39','高知県','Kochi');
INSERT INTO pref_code VALUES('40','福岡県','Fukuoka');
INSERT INTO pref_code VALUES('41','佐賀県','Saga');
INSERT INTO pref_code VALUES('42','長崎県','Nagasaki');
INSERT INTO pref_code VALUES('43','熊本県','Kumamoto');
INSERT INTO pref_code VALUES('44','大分県','Oita');
INSERT INTO pref_code VALUES('45','宮崎県','Miyazaki');
INSERT INTO pref_code VALUES('46','鹿児島県','Kagoshima');
INSERT INTO pref_code VALUES('47','沖縄県','Okinawa');

--make_covit19_2.sql
CREATE TABLE covid_19
AS 
SELECT c.reporting_date AS reporting_date,
       p.pref_code AS pref_code,
       c.Hokkaido AS infected
FROM
	covid19_sum AS c 
  CROSS JOIN
	pref_code AS p
WHERE
	p.pref_code='01'
;


INSERT INTO covid_19
SELECT c.reporting_date,p.pref_code,c.Aomori FROM covid19_sum AS c CROSS JOIN pref_code AS p WHERE p.pref_code='02' UNION
SELECT c.reporting_date,p.pref_code,c.Iwate FROM covid19_sum AS c CROSS JOIN pref_code AS p WHERE p.pref_code='03' UNION
SELECT c.reporting_date,p.pref_code,c.Miyagi FROM covid19_sum AS c CROSS JOIN pref_code AS p WHERE p.pref_code='04' UNION
SELECT c.reporting_date,p.pref_code,c.Akita FROM covid19_sum AS c CROSS JOIN pref_code AS p WHERE p.pref_code='05' UNION
SELECT c.reporting_date,p.pref_code,c.Yamagata FROM covid19_sum AS c CROSS JOIN pref_code AS p WHERE p.pref_code='06' UNION
SELECT c.reporting_date,p.pref_code,c.Fukushima FROM covid19_sum AS c CROSS JOIN pref_code AS p WHERE p.pref_code='07' UNION
SELECT c.reporting_date,p.pref_code,c.Ibaraki FROM covid19_sum AS c CROSS JOIN pref_code AS p WHERE p.pref_code='08' UNION
SELECT c.reporting_date,p.pref_code,c.Tochigi FROM covid19_sum AS c CROSS JOIN pref_code AS p WHERE p.pref_code='09' UNION
SELECT c.reporting_date,p.pref_code,c.Gunma FROM covid19_sum AS c CROSS JOIN pref_code AS p WHERE p.pref_code='10' UNION
SELECT c.reporting_date,p.pref_code,c.Saitama FROM covid19_sum AS c CROSS JOIN pref_code AS p WHERE p.pref_code='11' UNION
SELECT c.reporting_date,p.pref_code,c.Chiba FROM covid19_sum AS c CROSS JOIN pref_code AS p WHERE p.pref_code='12' UNION
SELECT c.reporting_date,p.pref_code,c.Tokyo FROM covid19_sum AS c CROSS JOIN pref_code AS p WHERE p.pref_code='13' UNION
SELECT c.reporting_date,p.pref_code,c.Kanagawa FROM covid19_sum AS c CROSS JOIN pref_code AS p WHERE p.pref_code='14' UNION
SELECT c.reporting_date,p.pref_code,c.Niigata FROM covid19_sum AS c CROSS JOIN pref_code AS p WHERE p.pref_code='15' UNION
SELECT c.reporting_date,p.pref_code,c.Toyama FROM covid19_sum AS c CROSS JOIN pref_code AS p WHERE p.pref_code='16' UNION
SELECT c.reporting_date,p.pref_code,c.Ishikawa FROM covid19_sum AS c CROSS JOIN pref_code AS p WHERE p.pref_code='17' UNION
SELECT c.reporting_date,p.pref_code,c.Fukui FROM covid19_sum AS c CROSS JOIN pref_code AS p WHERE p.pref_code='18' UNION
SELECT c.reporting_date,p.pref_code,c.Yamanashi FROM covid19_sum AS c CROSS JOIN pref_code AS p WHERE p.pref_code='19' UNION
SELECT c.reporting_date,p.pref_code,c.Nagano FROM covid19_sum AS c CROSS JOIN pref_code AS p WHERE p.pref_code='20' UNION
SELECT c.reporting_date,p.pref_code,c.Gifu FROM covid19_sum AS c CROSS JOIN pref_code AS p WHERE p.pref_code='21' UNION
SELECT c.reporting_date,p.pref_code,c.Shizuoka FROM covid19_sum AS c CROSS JOIN pref_code AS p WHERE p.pref_code='22' UNION
SELECT c.reporting_date,p.pref_code,c.Aichi FROM covid19_sum AS c CROSS JOIN pref_code AS p WHERE p.pref_code='23' UNION
SELECT c.reporting_date,p.pref_code,c.Mie FROM covid19_sum AS c CROSS JOIN pref_code AS p WHERE p.pref_code='24' UNION
SELECT c.reporting_date,p.pref_code,c.Shiga FROM covid19_sum AS c CROSS JOIN pref_code AS p WHERE p.pref_code='25' UNION
SELECT c.reporting_date,p.pref_code,c.Kyoto FROM covid19_sum AS c CROSS JOIN pref_code AS p WHERE p.pref_code='26' UNION
SELECT c.reporting_date,p.pref_code,c.Osaka FROM covid19_sum AS c CROSS JOIN pref_code AS p WHERE p.pref_code='27' UNION
SELECT c.reporting_date,p.pref_code,c.Hyogo FROM covid19_sum AS c CROSS JOIN pref_code AS p WHERE p.pref_code='28' UNION
SELECT c.reporting_date,p.pref_code,c.Nara FROM covid19_sum AS c CROSS JOIN pref_code AS p WHERE p.pref_code='29' UNION
SELECT c.reporting_date,p.pref_code,c.Wakayama FROM covid19_sum AS c CROSS JOIN pref_code AS p WHERE p.pref_code='30' UNION
SELECT c.reporting_date,p.pref_code,c.Tottori FROM covid19_sum AS c CROSS JOIN pref_code AS p WHERE p.pref_code='31' UNION
SELECT c.reporting_date,p.pref_code,c.Shimane FROM covid19_sum AS c CROSS JOIN pref_code AS p WHERE p.pref_code='32' UNION
SELECT c.reporting_date,p.pref_code,c.Okayama FROM covid19_sum AS c CROSS JOIN pref_code AS p WHERE p.pref_code='33' UNION
SELECT c.reporting_date,p.pref_code,c.Hiroshima FROM covid19_sum AS c CROSS JOIN pref_code AS p WHERE p.pref_code='34' UNION
SELECT c.reporting_date,p.pref_code,c.Yamaguchi FROM covid19_sum AS c CROSS JOIN pref_code AS p WHERE p.pref_code='35' UNION
SELECT c.reporting_date,p.pref_code,c.Tokushima FROM covid19_sum AS c CROSS JOIN pref_code AS p WHERE p.pref_code='36' UNION
SELECT c.reporting_date,p.pref_code,c.Kagawa FROM covid19_sum AS c CROSS JOIN pref_code AS p WHERE p.pref_code='37' UNION
SELECT c.reporting_date,p.pref_code,c.Ehime FROM covid19_sum AS c CROSS JOIN pref_code AS p WHERE p.pref_code='38' UNION
SELECT c.reporting_date,p.pref_code,c.Kochi FROM covid19_sum AS c CROSS JOIN pref_code AS p WHERE p.pref_code='39' UNION
SELECT c.reporting_date,p.pref_code,c.Fukuoka FROM covid19_sum AS c CROSS JOIN pref_code AS p WHERE p.pref_code='40' UNION
SELECT c.reporting_date,p.pref_code,c.Saga FROM covid19_sum AS c CROSS JOIN pref_code AS p WHERE p.pref_code='41' UNION
SELECT c.reporting_date,p.pref_code,c.Nagasaki FROM covid19_sum AS c CROSS JOIN pref_code AS p WHERE p.pref_code='42' UNION
SELECT c.reporting_date,p.pref_code,c.Kumamoto FROM covid19_sum AS c CROSS JOIN pref_code AS p WHERE p.pref_code='43' UNION
SELECT c.reporting_date,p.pref_code,c.Oita FROM covid19_sum AS c CROSS JOIN pref_code AS p WHERE p.pref_code='44' UNION
SELECT c.reporting_date,p.pref_code,c.Miyazaki FROM covid19_sum AS c CROSS JOIN pref_code AS p WHERE p.pref_code='45' UNION
SELECT c.reporting_date,p.pref_code,c.Kagoshima FROM covid19_sum AS c CROSS JOIN pref_code AS p WHERE p.pref_code='46' UNION
SELECT c.reporting_date,p.pref_code,c.Okinawa FROM covid19_sum AS c CROSS JOIN pref_code AS p WHERE p.pref_code='47'
;
CREATE UNIQUE INDEX ui_covid_19 ON covid_19(reporting_date,pref_code);
''')
