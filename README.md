# Projet School_python_BD

Ce projet est une mise en pratique de l'utilisation d'une base de donnée
par python avec le patron de conception DAO.

## Objectif du projet Ecole persistante

Compléter l’application Ecole comportant un embryon de l’implémentation du design pattern DAO pour permettre une persistance complète de l’application. Modifier celle-ci pour qu’elle charge au lancement toutes les entités de la BD ecole.

**Optionnel** : compléter l’application pour qu’elle réponde à ses spécifications complètes

## Spécifications fonctionnelles gestion d’une école, v1.0

### I.      Diagramme de cas d’utilisation

<img width="766" height="557" alt="school-use_case" src="https://github.com/user-attachments/assets/4cc856a6-c821-484e-8db5-2f2a17469aff" />

### II. Spécifications fonctionnelles

En réponse aux besoins exprimés par le client, la couche métier a été élaboré et testé sur la base des fonctionnalités suivantes, accessibles par les acteurs concernés :

#### UC1 – Afficher la liste des cours et leur enseignant

Permet à un élève, enseignant ou directeur d’afficher la liste des cours suivants, en précisant pour chacun d’eux ses dates de début et de fin et l’enseignant en charge du cours:
•         élève : ceux qu’il suit ;
•         enseignant : ceux qu’il enseigne ;
•         directeur : tous.

#### UC2 – Afficher les élèves d'un cours

Permet à un élève, enseignant ou directeur, depuis UC1, après sélection d’un des cours de la
liste affichée, d’en afficher les élèves inscrits.UC3 – Gérer les élèves
Affiche au directeur la liste des élèves de l’école (en permettant de filtrer cette liste par une
partie du nom ou du prénom), lui permet d’en sélectionner un, de créer, modifier ou supprimer
un élève (sélectionné), en renseignant son prénom, son nom, son âge et son numéro d’étudiant
(ce dernier étant éventuellement automatiquement attribué par l’application, à partir par ex. de
l’année en cours et d’un n° d’ordre incrémenté à chaque création).

#### UC4 – Gérer les enseignants

Affiche au directeur la liste des enseignants de l’école (en permettant de filtrer cette liste par une partie du nom ou du prénom), lui permet d’en sélectionner un, de créer, modifier ou supprimer un enseignant (sélectionné), en renseignant son prénom, son nom, son âge et sa date d’arrivée dans l’école.

#### UC5 – Gérer et rattacher leurs adresses

Permet au directeur, pour un élève ou enseignant en cours de création ou modification (depuis UC3 ou UC4), de spécifier son adresse en renseignant sa rue, sa ville et son code postal.

#### UC6 – Gérer la liste des cours d'un enseignant

Permet au directeur, pour un enseignant en cours de création ou modification (depuis UC4), d’afficher la liste des cours qu’il enseigne et d’en supprimer un ou d’en ajouter un nouveau depuis la liste des cours qu’il n’enseigne pas.

#### UC7 – Gérer les cours

Affiche au directeur la liste des cours enseignés à l’école (en permettant de filtrer cette liste par une partie du nom du cours), lui permet d’en sélectionner un, de créer, modifier ou supprimer un cours (sélectionné), en renseignant son nom, sa date de début et sa date de fin.

#### UC8 – Gérer la liste des élèves suivant un cours

Permet au directeur, pour un cours en cours de création ou modification (depuis UC7), d’afficher la liste des élèves qui le suivent et d’en supprimer un ou d’en ajouter un nouveau
depuis la liste des élèves qui ne le suivent pas.

### III.   Diagramme de classes

<img width="506" height="482" alt="school-class" src="https://github.com/user-attachments/assets/6ad978e6-a58b-4f25-9432-fe67addbea89" />

### IV.    Diagrammes de séquence

#### Arrivée d’un élève à l’école

Elle correspond au scénario suivant : l’arrivée dans l’école de l’élève Paul qui va suivre les cours suivants : géographie, physique, anglais.

<img width="585" height="430" alt="student_arrival-sequence" src="https://github.com/user-attachments/assets/b6a36eab-3c9c-43ed-9dd8-9a5420a50a71" />

#### Assignation d’un enseignant à un cours

<img width="892" height="511" alt="set_course_teacher-sequence" src="https://github.com/user-attachments/assets/c052aee8-89e7-4201-9f2e-db4e619cf4ba" />

### V. Annexe

Limite du périmètre fonctionnelle de l’application : couche métier uniquement.

**APPLICATION MULTI COUCHE**

<img width="1705" height="862" alt="ApplicationMultiCouche" src="https://github.com/user-attachments/assets/aa631331-121c-4fbd-9a6b-f000bea6fec5" />

#### Modèle Conceptuel des Données (MCD) de la base de données ecole

<img width="1571" height="1823" alt="school-mcd" src="https://github.com/user-attachments/assets/135aba41-ad5c-4c4f-bcc4-2958c2444368" />

## Cloner le projet

```
git clone https://github.com/albanmartel/School_python_BD.git
```
