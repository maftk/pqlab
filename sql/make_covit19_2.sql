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

