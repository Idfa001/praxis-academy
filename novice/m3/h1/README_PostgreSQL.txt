========================================>>  PSQL  <<========================================


Open PSQL	 > sudo -u postgres psql
\c <db_name>	 > Masuk ke Database
Membuat Database > CREATE DATABASE <name>;
Hapus Database	 > DROP DATABASE <name>;
Hapus Tabel	 > DROP TABLE <name>;
Menampiplkan	 > SELECT * FROM <name>;


YOUR F PROJEK

CREATE DATABASE music; #membuat database
\c music	       #masuk ke database

create table musicfyi (id int,judul char(30),genre char(20),penyanyi char(20),tahun char(20),album char(20),lirik varchar(10000));


INSERT INTO musicfyi VALUES ('1','Slow Dance In The Dark','POP','Joji','2018','','');

INSERT INTO musicfyi VALUES ('2','Ode an die freude','','ludwig van beethoven','1786','Symphony No. 9','');

INSERT INTO musicfyi VALUES ('3','Lo Que Siento','POP','Cuco','2017','single','~');




===========================================>> Output <<=========================================
(base) idfa001@Idfa:~$ sudo -u postgres psql
psql (9.3.17)
Type "help" for help.

postgres=# \c music
You are now connected to database "music" as user "postgres".
music=# \l
                                  List of databases
   Name    |  Owner   | Encoding |   Collate   |    Ctype    |   Access privileges   
-----------+----------+----------+-------------+-------------+-----------------------
 music     | postgres | UTF8     | en_US.UTF-8 | en_US.UTF-8 | 
 postgres  | postgres | UTF8     | en_US.UTF-8 | en_US.UTF-8 | 
 template0 | postgres | UTF8     | en_US.UTF-8 | en_US.UTF-8 | =c/postgres          +
           |          |          |             |             | postgres=CTc/postgres
 template1 | postgres | UTF8     | en_US.UTF-8 | en_US.UTF-8 | =c/postgres          +
           |          |          |             |             | postgres=CTc/postgres
(4 rows)

music=# SELECT * FROM musicfyi;
 id |             judul              |        genre         |       penyanyi       |        tahun         |        album         | lirik 
----+--------------------------------+----------------------+----------------------+----------------------+----------------------+-------
  1 | Slow Dance In The Dark         | POP                  | Joji                 | 2018                 |                      | 
  2 | Ode an die freude              |                      | ludwig van beethoven | 1786                 | Symphony No. 9       | 
  3 | Lo Que Siento                  | POP                  | Cuco                 | 2017                 | single               | ~
(3 rows)

music=# 
