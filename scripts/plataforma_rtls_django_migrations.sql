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
-- Table structure for table `django_migrations`
--

DROP TABLE IF EXISTS `django_migrations`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!50503 SET character_set_client = utf8mb4 */;
CREATE TABLE `django_migrations` (
  `id` int NOT NULL AUTO_INCREMENT,
  `app` varchar(255) NOT NULL,
  `name` varchar(255) NOT NULL,
  `applied` datetime(6) NOT NULL,
  PRIMARY KEY (`id`)
) ENGINE=InnoDB AUTO_INCREMENT=31 DEFAULT CHARSET=utf8;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `django_migrations`
--

LOCK TABLES `django_migrations` WRITE;
/*!40000 ALTER TABLE `django_migrations` DISABLE KEYS */;
INSERT INTO `django_migrations` VALUES (1,'contenttypes','0001_initial','2021-01-09 13:20:42.075232'),(2,'auth','0001_initial','2021-01-09 13:20:42.313454'),(3,'accounts','0001_initial','2021-01-09 13:20:42.814654'),(4,'admin','0001_initial','2021-01-09 13:20:42.914887'),(5,'admin','0002_logentry_remove_auto_add','2021-01-09 13:20:43.077610'),(6,'admin','0003_logentry_add_action_flag_choices','2021-01-09 13:20:43.093228'),(7,'alarme','0001_initial','2021-01-09 13:20:43.115358'),(8,'anchor','0001_initial','2021-01-09 13:20:43.146603'),(9,'tag','0001_initial','2021-01-09 13:20:43.177844'),(10,'collaborator','0001_initial','2021-01-09 13:20:43.249253'),(11,'api','0001_initial','2021-01-09 13:20:43.415996'),(12,'app','0001_initial','2021-01-09 13:20:43.632097'),(13,'planos','0001_initial','2021-01-09 13:20:43.763583'),(14,'ativo','0001_initial','2021-01-09 13:20:43.801328'),(15,'associar','0001_initial','2021-01-09 13:20:43.895061'),(16,'contenttypes','0002_remove_content_type_name','2021-01-09 13:20:44.681365'),(17,'auth','0002_alter_permission_name_max_length','2021-01-09 13:20:44.797222'),(18,'auth','0003_alter_user_email_max_length','2021-01-09 13:20:44.850600'),(19,'auth','0004_alter_user_username_opts','2021-01-09 13:20:44.866220'),(20,'auth','0005_alter_user_last_login_null','2021-01-09 13:20:44.950840'),(21,'auth','0006_require_contenttypes_0002','2021-01-09 13:20:44.950840'),(22,'auth','0007_alter_validators_add_error_messages','2021-01-09 13:20:44.966461'),(23,'auth','0008_alter_user_username_max_length','2021-01-09 13:20:45.035453'),(24,'auth','0009_alter_user_last_name_max_length','2021-01-09 13:20:45.120068'),(25,'auth','0010_alter_group_name_max_length','2021-01-09 13:20:45.204685'),(26,'auth','0011_update_proxy_permissions','2021-01-09 13:20:45.221757'),(27,'coletor','0001_initial','2021-01-09 13:20:45.253000'),(28,'mio','0001_initial','2021-01-09 13:20:45.284242'),(29,'regra','0001_initial','2021-01-09 13:20:45.320497'),(30,'sessions','0001_initial','2021-01-09 13:20:45.583454');
/*!40000 ALTER TABLE `django_migrations` ENABLE KEYS */;
UNLOCK TABLES;
/*!40103 SET TIME_ZONE=@OLD_TIME_ZONE */;

/*!40101 SET SQL_MODE=@OLD_SQL_MODE */;
/*!40014 SET FOREIGN_KEY_CHECKS=@OLD_FOREIGN_KEY_CHECKS */;
/*!40014 SET UNIQUE_CHECKS=@OLD_UNIQUE_CHECKS */;
/*!40101 SET CHARACTER_SET_CLIENT=@OLD_CHARACTER_SET_CLIENT */;
/*!40101 SET CHARACTER_SET_RESULTS=@OLD_CHARACTER_SET_RESULTS */;
/*!40101 SET COLLATION_CONNECTION=@OLD_COLLATION_CONNECTION */;
/*!40111 SET SQL_NOTES=@OLD_SQL_NOTES */;

-- Dump completed on 2022-02-17 14:30:12
