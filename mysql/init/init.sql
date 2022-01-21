create database test;
use test;
CREATE TABLE `login` (
  `id` int NOT NULL AUTO_INCREMENT,
  `login_cd` varchar(32) DEFAULT NULL,
  `hashed_password` varchar(255) DEFAULT NULL,
  PRIMARY KEY (`id`)
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb3;