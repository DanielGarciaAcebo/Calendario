CREATE DATABASE CALENDARIODB;
USE CALENDARIODB;

-- Creation tables for calendar
CREATE TABLE COMPANY(
    COMPANY_ID BIGINT UNSIGNED AUTO_INCREMENT PRIMARY KEY,
    NAME VARCHAR(50),
    DIRECTION VARCHAR(200),
    COMPANYTYPE INTEGER UNIQUE
);

CREATE TABLE USER(
    USER_ID BIGINT UNSIGNED AUTO_INCREMENT PRIMARY KEY NOT NULL,
    NAME VARCHAR(20),
    SURNAME VARCHAR(50),
    EMAIL VARCHAR(100) UNIQUE,
    NUMBERTF INTEGER UNIQUE,
    COMP INTEGER UNIQUE,
    PROPERTY BOOLEAN,
    CREATED_AT TIMESTAMP NULL
);

CREATE TABLE TYPE_COMPANY(
    COMPANY_TYPE INTEGER UNIQUE,
    NAME VARCHAR(20),
    DESCRIPTION VARCHAR(20)
);

CREATE TABLE TASK(
    NOTES_ID BIGINT UNSIGNED AUTO_INCREMENT PRIMARY KEY,
    COMMENT VARCHAR(20),
    DATE DATETIME,
    SEED INTEGER,
    USER INTEGER
);

CREATE TABLE DATE_HAS_NOTES(
    TNOTES_ID INTEGER,
    DATE_SEED_ID INTEGER
);

CREATE TABLE DATE_SEED(
    DATE_ID BIGINT UNSIGNED AUTO_INCREMENT PRIMARY KEY,
    SEED_ID INTEGER UNIQUE,
    DAY_TIME VARCHAR(20),
    DAY_COLLECTION DATE,
    FINAL_DAY DATE,
    START_DAY DATE
);

CREATE TABLE SEED(
    SEED_ID BIGINT UNSIGNED AUTO_INCREMENT PRIMARY KEY,
    NAME VARCHAR(50),
    DESCRIPTION VARCHAR(150),
    SHOW BOOLEAN
);


-- Creation of admin user for control
INSERT INTO USUARIO VALUES("admin","admin","admin@admin.com",000000000,0);
INSERT INTO COMPANY VALUES("company's admin","admin direction",0);

-- Creation type companies standar and admin. The admin isn't the real company
INSERT INTO TYPE_COMPANY VALUES(0,"admin company","description of companies admin");
INSERT INTO TYPE_COMPANY VALUES(1,"Ganadero","Empresa dedicada a la explotacion ganadera");
INSERT INTO TYPE_COMPANY VALUES(2,"Agricultor","Empresa la cual se dedica a la pantacion y recoleccion de grano y plano");
INSERT INTO TYPE_COMPANY VALUES(3,"Com Maquinaria","Empresa la cual se dedica a la contratacion de maquinaria para construccion y ayuda agroganadera");
INSERT INTO TYPE_COMPANY VALUES(4,"Veterinario","Empresa la cual se dedica a la salud animal");

-- Creation seeds use
INSERT INTO SEED VALUES(1,"Paja","Hierba alta la cual se seca en la pradera y se empaca");
INSERT INTO SEED VALUES(2,"Trigo","Cereal para poder hacer pan u otras cosas para consumo humano, el tayo seco se hace forraje");
INSERT INTO SEED VALUES(3,"Pradera","Hierba la cual se fermenta y es la base de fibra y proteina por defecto");
INSERT INTO SEED VALUES(4,"Maiz","Cereal el cual es uso exclusivo animal, es la base vitaminica mas importante");
