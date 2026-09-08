-- ------------------------------------------------
-- Table address
-- ------------------------------------------------

-- CREATE
INSERT INTO address (street, city, postal_code)
VALUES (?, ?, ?);

-- READ (unique)
SELECT id_address, street, city, postal_code
FROM address
WHERE id_address = ?;

-- READ (tous)
SELECT id_address, street, city, postal_code
FROM address;

-- UPDATE
UPDATE address
SET street = ?, city = ?, postal_code = ?
WHERE id_address = ?;

-- DELETE
DELETE FROM address
WHERE id_address = ?;


-- -----------------------------------------------------
-- Table person
-- -----------------------------------------------------

-- CREATE
INSERT INTO person (first_name, last_name, age, id_address)
VALUES (?, ?, ?, ?);

-- READ (unique avec son adresse liée)
SELECT p.id_person, p.first_name, p.last_name, p.age, p.id_address,
       a.street, a.city, a.postal_code
FROM person p
LEFT JOIN address a ON p.id_address = a.id_address
WHERE p.id_person = ?;

-- READ (tous)
SELECT id_person, first_name, last_name, age, id_address
FROM person;

-- UPDATE
UPDATE person
SET first_name = ?, last_name = ?, age = ?, id_address = ?
WHERE id_person = ?;

-- DELETE
DELETE FROM person
WHERE id_person = ?;

-- ----------------------------------------------------------
-- Table teacher
-- ----------------------------------------------------------

-- CREATE
INSERT INTO teacher (hiring_date, id_person)
VALUES (?, ?);

-- READ (unique avec informations personnelles)
SELECT t.id_teacher, t.hiring_date, p.id_person, p.first_name, p.last_name, p.age
FROM teacher t
JOIN person p ON t.id_person = p.id_person
WHERE t.id_teacher = ?;

-- READ (tous)
SELECT t.id_teacher, t.hiring_date, p.first_name, p.last_name
FROM teacher t
JOIN person p ON t.id_person = p.id_person;

-- UPDATE
UPDATE teacher
SET hiring_date = ?, id_person = ?
WHERE id_teacher = ?;

-- DELETE
DELETE FROM teacher
WHERE id_teacher = ?;

-- ----------------------------------------------------------
-- Table student
-- ----------------------------------------------------------

-- CREATE
INSERT INTO student (student_nbr, id_person)
VALUES (?, ?);

-- READ (unique avec informations personnelles)
SELECT s.student_nbr, p.id_person, p.first_name, p.last_name, p.age
FROM student s
JOIN person p ON s.id_person = p.id_person
WHERE s.student_nbr = ?;

-- READ (tous)
SELECT s.student_nbr, p.first_name, p.last_name
FROM student s
JOIN person p ON s.id_person = p.id_person;

-- UPDATE
UPDATE student
SET id_person = ?
WHERE student_nbr = ?;

-- DELETE
DELETE FROM student
WHERE student_nbr = ?;


-- ----------------------------------------------------------
-- Table course
-- ----------------------------------------------------------

-- CREATE
INSERT INTO course (name, start_date, end_date, id_teacher)
VALUES (?, ?, ?, ?);

-- READ (unique avec le professeur associé)
SELECT c.id_course, c.name, c.start_date, c.end_date, 
       p.first_name AS teacher_first_name, p.last_name AS teacher_last_name
FROM course c
JOIN teacher t ON c.id_teacher = t.id_teacher
JOIN person p ON t.id_person = p.id_person
WHERE c.id_course = ?;

-- READ (tous)
SELECT id_course, name, start_date, end_date, id_teacher
FROM course;

-- UPDATE
UPDATE course
SET name = ?, start_date = ?, end_date = ?, id_teacher = ?
WHERE id_course = ?;

-- DELETE
DELETE FROM course
WHERE id_course = ?;


-- ----------------------------------------------------------
-- Table takes
-- ----------------------------------------------------------

-- CREATE (Inscrire un étudiant à un cours)
INSERT INTO takes (student_nbr, id_course)
VALUES (?, ?);

-- READ (Tous les cours suivis par un étudiant)
SELECT c.id_course, c.name, c.start_date, c.end_date
FROM takes t
JOIN course c ON t.id_course = c.id_course
WHERE t.student_nbr = ?;

-- READ (Tous les étudiants inscrits à un cours)
SELECT s.student_nbr, p.first_name, p.last_name
FROM takes t
JOIN student s ON t.student_nbr = s.student_nbr
JOIN person p ON s.id_person = p.id_person
WHERE t.id_course = ?;

-- DELETE (Désinscrire un étudiant d'un cours)
DELETE FROM takes
WHERE student_nbr = ? AND id_course = ?;
