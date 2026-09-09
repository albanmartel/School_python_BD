-- Modification du type de la données de code postal de int à varchar(6) permet de gérer plus situation
ALTER TABLE ecole.address MODIFY COLUMN postal_code VARCHAR(6) NOT NULL;
