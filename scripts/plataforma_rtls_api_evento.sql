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
-- Table structure for table `api_evento`
--

DROP TABLE IF EXISTS `api_evento`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!50503 SET character_set_client = utf8mb4 */;
CREATE TABLE `api_evento` (
  `id` int NOT NULL AUTO_INCREMENT,
  `dtInicio` datetime(6) NOT NULL,
  `dtFim` datetime(6) DEFAULT NULL,
  `permanencia` time(6) DEFAULT NULL,
  `status` int NOT NULL,
  `idanchor_id` bigint NOT NULL,
  `idcolaborador_id` bigint DEFAULT NULL,
  `idtag_id` bigint NOT NULL,
  PRIMARY KEY (`id`),
  KEY `api_evento_idanchor_id_961d82c6_fk_anchor_anchor_id` (`idanchor_id`),
  KEY `api_evento_idcolaborador_id_0423c7e4_fk_collabora` (`idcolaborador_id`),
  KEY `api_evento_idtag_id_85462a90_fk_tag_tag_id` (`idtag_id`),
  CONSTRAINT `api_evento_idanchor_id_961d82c6_fk_anchor_anchor_id` FOREIGN KEY (`idanchor_id`) REFERENCES `anchor_anchor` (`id`),
  CONSTRAINT `api_evento_idcolaborador_id_0423c7e4_fk_collabora` FOREIGN KEY (`idcolaborador_id`) REFERENCES `collaborator_collaborator` (`id`),
  CONSTRAINT `api_evento_idtag_id_85462a90_fk_tag_tag_id` FOREIGN KEY (`idtag_id`) REFERENCES `tag_tag` (`id`)
) ENGINE=InnoDB DEFAULT CHARSET=utf8;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `api_evento`
--

LOCK TABLES `api_evento` WRITE;
/*!40000 ALTER TABLE `api_evento` DISABLE KEYS */;
/*!40000 ALTER TABLE `api_evento` ENABLE KEYS */;
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
