create database test-db;
use test-db;
CREATE TABLE `login` (
  `id` int NOT NULL AUTO_INCREMENT,
  `login_cd` varchar(32) DEFAULT NULL,
  `hashed_password` varchar(255) DEFAULT NULL,
  PRIMARY KEY (`id`)
) ENGINE=InnoDB AUTO_INCREMENT=17 DEFAULT CHARSET=utf8mb3;