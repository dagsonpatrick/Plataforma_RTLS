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
-- Table structure for table `auth_permission`
--

DROP TABLE IF EXISTS `auth_permission`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!50503 SET character_set_client = utf8mb4 */;
CREATE TABLE `auth_permission` (
  `id` int NOT NULL AUTO_INCREMENT,
  `name` varchar(255) NOT NULL,
  `content_type_id` int NOT NULL,
  `codename` varchar(100) NOT NULL,
  PRIMARY KEY (`id`),
  UNIQUE KEY `auth_permission_content_type_id_codename_01ab375a_uniq` (`content_type_id`,`codename`),
  CONSTRAINT `auth_permission_content_type_id_2f476e4b_fk_django_co` FOREIGN KEY (`content_type_id`) REFERENCES `django_content_type` (`id`)
) ENGINE=InnoDB AUTO_INCREMENT=101 DEFAULT CHARSET=utf8;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `auth_permission`
--

LOCK TABLES `auth_permission` WRITE;
/*!40000 ALTER TABLE `auth_permission` DISABLE KEYS */;
INSERT INTO `auth_permission` VALUES (1,'Can add log entry',1,'add_logentry'),(2,'Can change log entry',1,'change_logentry'),(3,'Can delete log entry',1,'delete_logentry'),(4,'Can view log entry',1,'view_logentry'),(5,'Can add permission',2,'add_permission'),(6,'Can change permission',2,'change_permission'),(7,'Can delete permission',2,'delete_permission'),(8,'Can view permission',2,'view_permission'),(9,'Can add group',3,'add_group'),(10,'Can change group',3,'change_group'),(11,'Can delete group',3,'delete_group'),(12,'Can view group',3,'view_group'),(13,'Can add user',4,'add_user'),(14,'Can change user',4,'change_user'),(15,'Can delete user',4,'delete_user'),(16,'Can view user',4,'view_user'),(17,'Can add content type',5,'add_contenttype'),(18,'Can change content type',5,'change_contenttype'),(19,'Can delete content type',5,'delete_contenttype'),(20,'Can view content type',5,'view_contenttype'),(21,'Can add session',6,'add_session'),(22,'Can change session',6,'change_session'),(23,'Can delete session',6,'delete_session'),(24,'Can view session',6,'view_session'),(25,'Can add tarefa',7,'add_tarefa'),(26,'Can change tarefa',7,'change_tarefa'),(27,'Can delete tarefa',7,'delete_tarefa'),(28,'Can view tarefa',7,'view_tarefa'),(29,'Can add foto user',8,'add_fotouser'),(30,'Can change foto user',8,'change_fotouser'),(31,'Can delete foto user',8,'delete_fotouser'),(32,'Can view foto user',8,'view_fotouser'),(33,'Can add plano',9,'add_plano'),(34,'Can change plano',9,'change_plano'),(35,'Can delete plano',9,'delete_plano'),(36,'Can view plano',9,'view_plano'),(37,'Can add tag',10,'add_tag'),(38,'Can change tag',10,'change_tag'),(39,'Can delete tag',10,'delete_tag'),(40,'Can view tag',10,'view_tag'),(41,'Can add anchor',11,'add_anchor'),(42,'Can change anchor',11,'change_anchor'),(43,'Can delete anchor',11,'delete_anchor'),(44,'Can view anchor',11,'view_anchor'),(45,'Can add collaborator',12,'add_collaborator'),(46,'Can change collaborator',12,'change_collaborator'),(47,'Can delete collaborator',12,'delete_collaborator'),(48,'Can view collaborator',12,'view_collaborator'),(49,'Can add associacao collaborator',13,'add_associacaocollaborator'),(50,'Can change associacao collaborator',13,'change_associacaocollaborator'),(51,'Can delete associacao collaborator',13,'delete_associacaocollaborator'),(52,'Can view associacao collaborator',13,'view_associacaocollaborator'),(53,'Can add associacao ativo',14,'add_associacaoativo'),(54,'Can change associacao ativo',14,'change_associacaoativo'),(55,'Can delete associacao ativo',14,'delete_associacaoativo'),(56,'Can view associacao ativo',14,'view_associacaoativo'),(57,'Can add associacao anchor',15,'add_associacaoanchor'),(58,'Can change associacao anchor',15,'change_associacaoanchor'),(59,'Can delete associacao anchor',15,'delete_associacaoanchor'),(60,'Can view associacao anchor',15,'view_associacaoanchor'),(61,'Can add coletor',16,'add_coletor'),(62,'Can change coletor',16,'change_coletor'),(63,'Can delete coletor',16,'delete_coletor'),(64,'Can view coletor',16,'view_coletor'),(65,'Can add dev',17,'add_dev'),(66,'Can change dev',17,'change_dev'),(67,'Can delete dev',17,'delete_dev'),(68,'Can view dev',17,'view_dev'),(69,'Can add evento dev aws',18,'add_eventodevaws'),(70,'Can change evento dev aws',18,'change_eventodevaws'),(71,'Can delete evento dev aws',18,'delete_eventodevaws'),(72,'Can view evento dev aws',18,'view_eventodevaws'),(73,'Can add info evento',19,'add_infoevento'),(74,'Can change info evento',19,'change_infoevento'),(75,'Can delete info evento',19,'delete_infoevento'),(76,'Can view info evento',19,'view_infoevento'),(77,'Can add info planta',20,'add_infoplanta'),(78,'Can change info planta',20,'change_infoplanta'),(79,'Can delete info planta',20,'delete_infoplanta'),(80,'Can view info planta',20,'view_infoplanta'),(81,'Can add evento',21,'add_evento'),(82,'Can change evento',21,'change_evento'),(83,'Can delete evento',21,'delete_evento'),(84,'Can view evento',21,'view_evento'),(85,'Can add ativo',22,'add_ativo'),(86,'Can change ativo',22,'change_ativo'),(87,'Can delete ativo',22,'delete_ativo'),(88,'Can view ativo',22,'view_ativo'),(89,'Can add alarme',23,'add_alarme'),(90,'Can change alarme',23,'change_alarme'),(91,'Can delete alarme',23,'delete_alarme'),(92,'Can view alarme',23,'view_alarme'),(93,'Can add mio',24,'add_mio'),(94,'Can change mio',24,'change_mio'),(95,'Can delete mio',24,'delete_mio'),(96,'Can view mio',24,'view_mio'),(97,'Can add regra',25,'add_regra'),(98,'Can change regra',25,'change_regra'),(99,'Can delete regra',25,'delete_regra'),(100,'Can view regra',25,'view_regra');
/*!40000 ALTER TABLE `auth_permission` ENABLE KEYS */;
UNLOCK TABLES;
/*!40103 SET TIME_ZONE=@OLD_TIME_ZONE */;

/*!40101 SET SQL_MODE=@OLD_SQL_MODE */;
/*!40014 SET FOREIGN_KEY_CHECKS=@OLD_FOREIGN_KEY_CHECKS */;
/*!40014 SET UNIQUE_CHECKS=@OLD_UNIQUE_CHECKS */;
/*!40101 SET CHARACTER_SET_CLIENT=@OLD_CHARACTER_SET_CLIENT */;
/*!40101 SET CHARACTER_SET_RESULTS=@OLD_CHARACTER_SET_RESULTS */;
/*!40101 SET COLLATION_CONNECTION=@OLD_COLLATION_CONNECTION */;
/*!40111 SET SQL_NOTES=@OLD_SQL_NOTES */;

-- Dump completed on 2022-02-17 14:30:07
