DROP DATABASE CALENDARIODB;
CREATE DATABASE CALENDARIODB;
USE CALENDARIODB;

-- Creation tables for calendar
CREATE TABLE IF NOT EXISTS SEED(
    SEED_ID INTEGER UNIQUE,
    NAME VARCHAR(50),
    DESCRIPTION VARCHAR(150),
    DAYTIME VARCHAR(30),
    DAYCOLLECTION integer,
    FINALDAY DATE,
    STARTDAY DATE
);

CREATE TABLE IF NOT EXISTS TYPE_COMPANY(
    COMPANY_TYPE_ID INTEGER UNIQUE PRIMARY KEY,
    NAME VARCHAR(20),
    DESCRIPTION VARCHAR(200)
);

CREATE TABLE IF NOT EXISTS USER(
    USER_ID BIGINT UNSIGNED AUTO_INCREMENT PRIMARY KEY NOT NULL,
    NAME_USER VARCHAR(20),
    PASS VARCHAR(30),
    SURNAME VARCHAR(50),
    EMAIL VARCHAR(100) UNIQUE,
    NUMBERTF INTEGER UNIQUE,
    COMPANY_ID BIGINT UNIQUE,
    TASK_ID BIGINT UNIQUE,
    CREATED_AT TIMESTAMP NULL
);

CREATE TABLE IF NOT EXISTS COMPANY(
    ID_COMPANY BIGINT PRIMARY KEY,
    NAME_COMPANY VARCHAR(50) UNIQUE,
    CITYHALL VARCHAR(200),
    COMPANY_TYPE INTEGER,
    FOREIGN KEY (COMPANY_TYPE) REFERENCES TYPE_COMPANY(COMPANY_TYPE_ID) ON DELETE CASCADE ON UPDATE CASCADE,
    FOREIGN KEY (ID_COMPANY) REFERENCES USER(COMPANY_ID) ON DELETE CASCADE ON UPDATE CASCADE
);


CREATE TABLE IF NOT EXISTS TASK(
    NOTES_ID BIGINT NOT NULL UNIQUE,
    NAME VARCHAR(30),
    COMMENT VARCHAR(200),
    DATE DATETIME,
    USER BIGINT ,
    FOREIGN KEY (USER) REFERENCES USER(TASK_ID) ON DELETE CASCADE ON UPDATE CASCADE
);

-- Creation type companies standar and admin. The admin isn't the real company
INSERT INTO TYPE_COMPANY  (COMPANY_TYPE_ID, NAME, DESCRIPTION) VALUES (0,"admin company","description of companies admin");
INSERT INTO TYPE_COMPANY  (COMPANY_TYPE_ID, NAME, DESCRIPTION) VALUES (1,"Ganaderia","Empresa dedicada a la explotacion ganadera");
INSERT INTO TYPE_COMPANY  (COMPANY_TYPE_ID, NAME, DESCRIPTION) VALUES (2,"Agricultura","Empresa la cual se dedica a la pantacion y recoleccion de grano y plano");
INSERT INTO TYPE_COMPANY  (COMPANY_TYPE_ID, NAME, DESCRIPTION) VALUES (3,"Maquinaria","Empresa la cual se dedica a la contratacion de maquinaria para construccion y ayuda agroganadera");
INSERT INTO TYPE_COMPANY  (COMPANY_TYPE_ID, NAME, DESCRIPTION) VALUES (4,"Veterinaria","Empresa la cual se dedica a la salud animal");

-- Creation seeds use
INSERT INTO SEED (SEED_ID, NAME, DESCRIPTION, DAYTIME, DAYCOLLECTION, FINALDAY, STARTDAY) VALUES (1, "Paja", "Hierba alta la cual se seca en la pradera y se empaca", "semana Soleada", "60", "0000-09-25", "0000-06-25");
INSERT INTO SEED (SEED_ID, NAME, DESCRIPTION, DAYTIME, DAYCOLLECTION, FINALDAY, STARTDAY) VALUES (2, "Trigo", "Cereal para poder hacer pan u otras cosas para consumo humano, el tayo seco se hace forraje", "Semana Soleada", "60", "0000-09-25", "0000-06-25");
INSERT INTO SEED (SEED_ID, NAME, DESCRIPTION, DAYTIME, DAYCOLLECTION, FINALDAY, STARTDAY) VALUES (3, "Pradera", "Hierba la cual se fermenta y es la base de fibra y proteina por defecto", "Semana humeda sin llover", "40", "0000-09-25", "0000-06-25");
INSERT INTO SEED (SEED_ID, NAME, DESCRIPTION, DAYTIME, DAYCOLLECTION, FINALDAY, STARTDAY) VALUES (4, "Maiz", "Cereal el cual es uso exclusivo animal, es la base vitaminica mas importante", "Semana humeda sin llover", "80", "0000-06-25", "0000-03-25");

-- Creation of admin user for control
INSERT INTO USER (NAME_USER, PASS ,SURNAME, EMAIL, NUMBERTF, COMPANY_ID, TASK_ID) VALUES("admin", "admin", "adminSurname" , "admin@admin.com", 000000000, 1, 1);
INSERT INTO COMPANY ( ID_COMPANY, NAME_COMPANY, CITYHALL, COMPANY_TYPE) VALUES( 1, "company's admin", "admin direction", 0);


-- Creation 8 users and 8 companies for tests
INSERT INTO USER (NAME_USER, PASS ,SURNAME, EMAIL, NUMBERTF, COMPANY_ID, TASK_ID) VALUES("user1", "user1", "user1Surname" , "user1@user1.com", 111111111, 2, 2);
INSERT INTO COMPANY ( ID_COMPANY, NAME_COMPANY, CITYHALL, COMPANY_TYPE) VALUES( 2, "company's user1", "user1 direction", 1);

INSERT INTO USER (NAME_USER, PASS ,SURNAME, EMAIL, NUMBERTF, COMPANY_ID, TASK_ID) VALUES("user2", "user2", "user2Surname" , "user2@user2.com", 222222222, 3, 3);
INSERT INTO COMPANY ( ID_COMPANY, NAME_COMPANY, CITYHALL, COMPANY_TYPE) VALUES( 3, "company's user2", "admin direction", 1);

INSERT INTO USER (NAME_USER, PASS ,SURNAME, EMAIL, NUMBERTF, COMPANY_ID, TASK_ID) VALUES("user3", "user3", "user3Surname" , "user3@user3.com", 333333333, 4, 4);
INSERT INTO COMPANY ( ID_COMPANY, NAME_COMPANY, CITYHALL, COMPANY_TYPE) VALUES( 4, "company's user3", "user3 direction", 2);

INSERT INTO USER (NAME_USER, PASS ,SURNAME, EMAIL, NUMBERTF, COMPANY_ID, TASK_ID) VALUES("user4", "user4", "user4Surname" , "user4@user4.com", 444444444, 5, 5);
INSERT INTO COMPANY ( ID_COMPANY, NAME_COMPANY, CITYHALL, COMPANY_TYPE) VALUES( 5, "company's user4", "user4 direction", 2);

INSERT INTO USER (NAME_USER, PASS ,SURNAME, EMAIL, NUMBERTF, COMPANY_ID, TASK_ID) VALUES("user5", "user5", "user5Surname" , "user5@user5.com", 555555555, 6, 6);
INSERT INTO COMPANY ( ID_COMPANY, NAME_COMPANY, CITYHALL, COMPANY_TYPE) VALUES( 6, "company's user5", "user5 direction", 3);

INSERT INTO USER (NAME_USER, PASS ,SURNAME, EMAIL, NUMBERTF, COMPANY_ID, TASK_ID) VALUES("user6", "user6", "user6Surname" , "user6@user6.com", 666666666, 7, 7);
INSERT INTO COMPANY ( ID_COMPANY, NAME_COMPANY, CITYHALL, COMPANY_TYPE) VALUES( 7, "company's user6", "user6 direction", 3);

INSERT INTO USER (NAME_USER, PASS ,SURNAME, EMAIL, NUMBERTF, COMPANY_ID, TASK_ID) VALUES("user7", "user7", "user7Surname" , "user7@user7.com", 777777777, 8, 8);
INSERT INTO COMPANY ( ID_COMPANY, NAME_COMPANY, CITYHALL, COMPANY_TYPE) VALUES( 8, "company's user7", "user7 direction", 4);

INSERT INTO USER (NAME_USER, PASS ,SURNAME, EMAIL, NUMBERTF, COMPANY_ID, TASK_ID) VALUES("user8", "user8", "user8Surname" , "user8@user8.com", 888888888, 9, 9);
INSERT INTO COMPANY ( ID_COMPANY, NAME_COMPANY, CITYHALL, COMPANY_TYPE) VALUES( 9, "company's user8", "user8 direction", 4);

INSERT INTO TASK (NOTES_ID, NAME, COMMENT, DATE, USER ) VALUES (1,"notes test1", "this is a coment test","2021-12-10",1);
INSERT INTO TASK (NOTES_ID, NAME, COMMENT, DATE, USER ) VALUES (2,"notes test2", "this is a coment test","2021-12-10",1);
INSERT INTO TASK (NOTES_ID, NAME, COMMENT, DATE, USER ) VALUES (3,"notes test3", "this is a coment test","2021-12-10",1);
INSERT INTO TASK (NOTES_ID, NAME, COMMENT, DATE, USER ) VALUES (4,"notes test3", "this is a coment test","2021-12-10",1);
INSERT INTO TASK (NOTES_ID, NAME, COMMENT, DATE, USER ) VALUES (5,"notes test3", "this is a coment test","2021-12-10",1);
INSERT INTO TASK (NOTES_ID, NAME, COMMENT, DATE, USER ) VALUES (6,"notes test3", "this is a coment test","2021-12-10",1);
INSERT INTO TASK (NOTES_ID, NAME, COMMENT, DATE, USER ) VALUES (7,"notes test3", "this is a coment test","2021-12-10",1);
INSERT INTO TASK (NOTES_ID, NAME, COMMENT, DATE, USER ) VALUES (8,"notes test3", "this is a coment test","2021-12-10",1);
INSERT INTO TASK (NOTES_ID, NAME, COMMENT, DATE, USER ) VALUES (9,"notes test3", "this is a coment test","2021-12-10",1);
INSERT INTO TASK (NOTES_ID, NAME, COMMENT, DATE, USER ) VALUES (10,"notes test3", "this is a coment test","2021-12-10",1);
INSERT INTO TASK (NOTES_ID, NAME, COMMENT, DATE, USER ) VALUES (11,"notes test3", "this is a coment test","2021-12-10",1);

