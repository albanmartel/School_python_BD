CREATE DATABASE 
IF NOT EXISTS ecole
CHARACTER SET utf8mb4 
COLLATE utf8mb4_unicode_ci;
USE ecole;

-- Déactiver la vérification des clefs étrangères

SET FOREIGN_KEY_CHECKS = 0;

DROP TABLE IF EXISTS address;
DROP TABLE IF EXISTS course;
DROP TABLE IF EXISTS person;
DROP TABLE IF EXISTS student;
DROP TABLE IF EXISTS takes;
DROP TABLE IF EXISTS teacher;

-- Réactiver la vérification des clefs étrangères

SET FOREIGN_KEY_CHECKS = 1;

CREATE TABLE address (
  id_address int NOT NULL AUTO_INCREMENT,
  street varchar(80) NOT NULL,
  city varchar(50) NOT NULL,
  postal_code smallint NOT NULL,
  PRIMARY KEY (id_address)
);

CREATE TABLE course (
  id_course int NOT NULL AUTO_INCREMENT,
  name varchar(50) NOT NULL,
  start_date date NOT NULL,
  end_date date NOT NULL,
  id_teacher int NOT NULL,
  PRIMARY KEY (id_course),
  KEY id_teacher (id_teacher)
);


CREATE TABLE person (
  id_person int NOT NULL AUTO_INCREMENT,
  first_name varchar(50) NOT NULL,
  last_name varchar(50) NOT NULL,
  age tinyint NOT NULL,
  id_address int DEFAULT NULL,
  PRIMARY KEY (id_person),
  UNIQUE KEY id_address (id_address)
);


CREATE TABLE student (
  student_nbr int NOT NULL,
  id_person int NOT NULL,
  PRIMARY KEY (student_nbr),
  UNIQUE KEY id_person (id_person)
);


CREATE TABLE takes (
  student_nbr int NOT NULL,
  id_course int NOT NULL,
  PRIMARY KEY (student_nbr,id_course),
  KEY id_course (id_course)
);

CREATE TABLE teacher (
  id_teacher int NOT NULL AUTO_INCREMENT,
  hiring_date date NOT NULL,
  id_person int NOT NULL,
  PRIMARY KEY (id_teacher),
  UNIQUE KEY id_person (id_person)
);

--
-- Contraintes pour la table course
--
ALTER TABLE course
  ADD CONSTRAINT course_ibfk_1 FOREIGN KEY (id_teacher) REFERENCES teacher (id_teacher);

--
-- Contraintes pour la table person
--
ALTER TABLE person
  ADD CONSTRAINT person_ibfk_1 FOREIGN KEY (id_address) REFERENCES address (id_address);

--
-- Contraintes pour la table student
--
ALTER TABLE student
  ADD CONSTRAINT student_ibfk_1 FOREIGN KEY (id_person) REFERENCES person (id_person);

--
-- Contraintes pour la table takes
--
ALTER TABLE takes
  ADD CONSTRAINT takes_ibfk_1 FOREIGN KEY (student_nbr) REFERENCES student (student_nbr),
  ADD CONSTRAINT takes_ibfk_2 FOREIGN KEY (id_course) REFERENCES course (id_course);

--
-- Contraintes pour la table teacher
--
ALTER TABLE teacher
  ADD CONSTRAINT teacher_ibfk_1 FOREIGN KEY (id_person) REFERENCES person (id_person);