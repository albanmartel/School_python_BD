-- 1. Créer l'utilisateur 'ecole' s'il n'existe pas
CREATE USER IF NOT EXISTS 'ecole'@'localhost' IDENTIFIED BY 'FqDEuKWd9TxLERZg6ooh';

-- 2. Accorder tous les privilèges sur ta base de données (remplace ma_base par le nom réel)
GRANT ALL PRIVILEGES ON *.* TO `ecole`@`localhost` ;

-- 3. Mettre à jour les droits
FLUSH PRIVILEGES;