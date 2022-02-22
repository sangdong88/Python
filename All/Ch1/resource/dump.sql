BEGIN TRANSACTION;
CREATE TABLE users(id INTIGER PRIMARY KEY, username text, email text,     phone text, website text, regidate text);
INSERT INTO "users" VALUES(1,'KIM','dk@naver.com','010-4564-2524','KIMKIM.com','2021-04-01 16:37:53');
INSERT INTO "users" VALUES(2,'park','park@daum.net','010-5478-5554','we3.com','2021-04-01 16:37:53');
INSERT INTO "users" VALUES(3,'Lee','Lee@naver.com','010-4545-5442','LEE.com','2021-04-01 16:37:53');
INSERT INTO "users" VALUES(4,'Cho','Cho@naver.com','010-4821-8763','Cho.com','2021-04-01 16:37:53');
INSERT INTO "users" VALUES(5,'Yoo','Yoo@naver.com','010-5432-8777','Yoo.com','2021-04-01 16:37:53');
COMMIT;
