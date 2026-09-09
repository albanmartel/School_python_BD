USE ecole;

INSERT INTO address (id_address, street, city, postal_code) VALUES
(1, '12 rue des Pinsons', 'Castanet', '31320'),
(2, '43 avenue Jean Zay', 'Toulouse', '31200'),
(3, '7 impasse des Coteaux', 'Cornebarrieu', '31150');

INSERT INTO person (id_person, first_name, last_name, age, id_address) VALUES
(1, 'Paul', 'Dubois', 12, 1),
(2, 'Valérie', 'Dumont', 13, 2),
(3, 'Louis', 'Berthot', 11, 3),
(4, 'Victor', 'Hugo', 23, NULL),
(5, 'Jules', 'Michelet', 32, NULL),
(6, 'Sophie', 'Germain', 25, NULL),
(7, 'Marie', 'Curie', 31, NULL),
(8, 'William', 'Shakespeare', 34, NULL),
(9, 'Michel', 'Platini', 42, NULL);

INSERT INTO teacher (id_teacher, hiring_date, id_person) VALUES
(1, '2023-09-04', 4),
(2, '2023-09-04', 5),
(3, '2023-09-04', 6),
(4, '2023-09-04', 7),
(5, '2023-09-04', 8),
(6, '2023-09-04', 9);

INSERT INTO course (id_course, name, start_date, end_date, id_teacher) VALUES
(1, 'Français', '2024-01-29', '2024-02-16', 1),
(2, 'Histoire', '2024-02-05', '2024-02-16', 2),
(3, 'Géographie', '2024-02-05', '2024-02-16', 2),
(4, 'Mathématiques', '2024-02-12', '2024-03-08', 3),
(5, 'Physique', '2024-02-19', '2024-03-08', 4),
(6, 'Chimie', '2024-02-26', '2024-03-15', 4),
(7, 'Anglais', '2024-02-12', '2024-02-24', 5),
(8, 'Sport', '2024-03-04', '2024-03-15', 6);

INSERT INTO student (student_nbr, id_person) VALUES
(1, 1),
(2, 2),
(3, 3);

INSERT INTO takes (student_nbr, id_course) VALUES
(2, 1),
(2, 2),
(1, 3),
(3, 3),
(3, 4),
(1, 5),
(3, 5),
(2, 6),
(1, 7),
(3, 8);


