USE ssafezone;

CREATE TABLE user(
    idUser INT AUTO_INCREMENT,
    nombre VARCHAR(75) NOT NULL,
    password VARCHAR(255) NOT NULL,
    photo LONGBLOB,
    
    CONSTRAINT pk_user_idUser PRIMARY KEY(idUser)
);

SELECT * FROM `user`;