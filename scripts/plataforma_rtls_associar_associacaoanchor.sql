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
-- Table structure for table `associar_associacaoanchor`
--

DROP TABLE IF EXISTS `associar_associacaoanchor`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!50503 SET character_set_client = utf8mb4 */;
CREATE TABLE `associar_associacaoanchor` (
  `id` bigint NOT NULL AUTO_INCREMENT,
  `anchor_id` bigint NOT NULL,
  `plano_id` bigint NOT NULL,
  PRIMARY KEY (`id`),
  KEY `associar_associacaoanchor_anchor_id_841ccdbe_fk_anchor_anchor_id` (`anchor_id`),
  KEY `associar_associacaoanchor_plano_id_94cb666c_fk_planos_plano_id` (`plano_id`),
  CONSTRAINT `associar_associacaoanchor_anchor_id_841ccdbe_fk_anchor_anchor_id` FOREIGN KEY (`anchor_id`) REFERENCES `anchor_anchor` (`id`),
  CONSTRAINT `associar_associacaoanchor_plano_id_94cb666c_fk_planos_plano_id` FOREIGN KEY (`plano_id`) REFERENCES `planos_plano` (`id`)
) ENGINE=InnoDB DEFAULT CHARSET=utf8;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `associar_associacaoanchor`
--

LOCK TABLES `associar_associacaoanchor` WRITE;
/*!40000 ALTER TABLE `associar_associacaoanchor` DISABLE KEYS */;
/*!40000 ALTER TABLE `associar_associacaoanchor` ENABLE KEYS */;
UNLOCK TABLES;
/*!40103 SET TIME_ZONE=@OLD_TIME_ZONE */;

/*!40101 SET SQL_MODE=@OLD_SQL_MODE */;
/*!40014 SET FOREIGN_KEY_CHECKS=@OLD_FOREIGN_KEY_CHECKS */;
/*!40014 SET UNIQUE_CHECKS=@OLD_UNIQUE_CHECKS */;
/*!40101 SET CHARACTER_SET_CLIENT=@OLD_CHARACTER_SET_CLIENT */;
/*!40101 SET CHARACTER_SET_RESULTS=@OLD_CHARACTER_SET_RESULTS */;
/*!40101 SET COLLATION_CONNECTION=@OLD_COLLATION_CONNECTION */;
/*!40111 SET SQL_NOTES=@OLD_SQL_NOTES */;

-- Dump completed on 2022-02-17 14:30:16
