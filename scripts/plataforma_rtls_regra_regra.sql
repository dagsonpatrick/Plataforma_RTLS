-- MySQL dump 10.13  Distrib 8.0.22, for Win64 (x86_64)
--
-- Host: localhost    Database: plataforma_rtls
-- ------------------------------------------------------
-- Server version	8.0.22

/*!40101 SET @OLD_CHARACTER_SET_CLIENT=@@CHARACTER_SET_CLIENT */;
/*!40101 SET @OLD_CHARACTER_SET_RESULTS=@@CHARACTER_SET_RESULTS */;
/*!40101 SET @OLD_COLLATION_CONNECTION=@@COLLATION_CONNECTION */;
/*!50503 SET NAMES utf8 */;
/*!40103 SET @OLD_TIME_ZONE=@@TIME_ZONE */;
/*!40103 SET TIME_ZONE='+00:00' */;
/*!40014 SET @OLD_UNIQUE_CHECKS=@@UNIQUE_CHECKS, UNIQUE_CHECKS=0 */;
/*!40014 SET @OLD_FOREIGN_KEY_CHECKS=@@FOREIGN_KEY_CHECKS, FOREIGN_KEY_CHECKS=0 */;
/*!40101 SET @OLD_SQL_MODE=@@SQL_MODE, SQL_MODE='NO_AUTO_VALUE_ON_ZERO' */;
/*!40111 SET @OLD_SQL_NOTES=@@SQL_NOTES, SQL_NOTES=0 */;

--
-- Table structure for table `regra_regra`
--

DROP TABLE IF EXISTS `regra_regra`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!50503 SET character_set_client = utf8mb4 */;
CREATE TABLE `regra_regra` (
  `id` int NOT NULL AUTO_INCREMENT,
  `name` varchar(50) NOT NULL,
  `description` varchar(50) NOT NULL,
  `tempPermanencia` time(6) DEFAULT NULL,
  `event` varchar(15) NOT NULL,
  `action` varchar(15) NOT NULL,
  `portout` int NOT NULL,
  `portin` int DEFAULT NULL,
  `state` varchar(15) DEFAULT NULL,
  `mio_id` int NOT NULL,
  `plan_id` bigint NOT NULL,
  PRIMARY KEY (`id`),
  KEY `regra_regra_mio_id_c8075835_fk_mio_mio_id` (`mio_id`),
  KEY `regra_regra_plan_id_1c97628f_fk_planos_plano_id` (`plan_id`),
  CONSTRAINT `regra_regra_mio_id_c8075835_fk_mio_mio_id` FOREIGN KEY (`mio_id`) REFERENCES `mio_mio` (`id`),
  CONSTRAINT `regra_regra_plan_id_1c97628f_fk_planos_plano_id` FOREIGN KEY (`plan_id`) REFERENCES `planos_plano` (`id`)
) ENGINE=InnoDB DEFAULT CHARSET=utf8;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `regra_regra`
--

LOCK TABLES `regra_regra` WRITE;
/*!40000 ALTER TABLE `regra_regra` DISABLE KEYS */;
/*!40000 ALTER TABLE `regra_regra` ENABLE KEYS */;
UNLOCK TABLES;
/*!40103 SET TIME_ZONE=@OLD_TIME_ZONE */;

/*!40101 SET SQL_MODE=@OLD_SQL_MODE */;
/*!40014 SET FOREIGN_KEY_CHECKS=@OLD_FOREIGN_KEY_CHECKS */;
/*!40014 SET UNIQUE_CHECKS=@OLD_UNIQUE_CHECKS */;
/*!40101 SET CHARACTER_SET_CLIENT=@OLD_CHARACTER_SET_CLIENT */;
/*!40101 SET CHARACTER_SET_RESULTS=@OLD_CHARACTER_SET_RESULTS */;
/*!40101 SET COLLATION_CONNECTION=@OLD_COLLATION_CONNECTION */;
/*!40111 SET SQL_NOTES=@OLD_SQL_NOTES */;

-- Dump completed on 2022-02-17 14:30:10
