-- MySQL dump 10.13  Distrib 8.0.30, for Win64 (x86_64)
--
-- Host: localhost    Database: g05
-- ------------------------------------------------------
-- Server version	8.0.30

/*!40101 SET @OLD_CHARACTER_SET_CLIENT=@@CHARACTER_SET_CLIENT */;
/*!40101 SET @OLD_CHARACTER_SET_RESULTS=@@CHARACTER_SET_RESULTS */;
/*!40101 SET @OLD_COLLATION_CONNECTION=@@COLLATION_CONNECTION */;
/*!50503 SET NAMES utf8mb4 */;
/*!40103 SET @OLD_TIME_ZONE=@@TIME_ZONE */;
/*!40103 SET TIME_ZONE='+00:00' */;
/*!40014 SET @OLD_UNIQUE_CHECKS=@@UNIQUE_CHECKS, UNIQUE_CHECKS=0 */;
/*!40014 SET @OLD_FOREIGN_KEY_CHECKS=@@FOREIGN_KEY_CHECKS, FOREIGN_KEY_CHECKS=0 */;
/*!40101 SET @OLD_SQL_MODE=@@SQL_MODE, SQL_MODE='NO_AUTO_VALUE_ON_ZERO' */;
/*!40111 SET @OLD_SQL_NOTES=@@SQL_NOTES, SQL_NOTES=0 */;

--
-- Table structure for table `favorites`
--

DROP TABLE IF EXISTS `favorites`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!50503 SET character_set_client = utf8mb4 */;
CREATE TABLE `favorites` (
  `user_id` int NOT NULL,
  `thesis_id` int NOT NULL,
  PRIMARY KEY (`user_id`,`thesis_id`),
  KEY `thesis_id` (`thesis_id`),
  CONSTRAINT `favorites_ibfk_1` FOREIGN KEY (`user_id`) REFERENCES `user` (`user_id`),
  CONSTRAINT `favorites_ibfk_2` FOREIGN KEY (`thesis_id`) REFERENCES `thesis` (`thesis_id`)
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_0900_ai_ci;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `favorites`
--

LOCK TABLES `favorites` WRITE;
/*!40000 ALTER TABLE `favorites` DISABLE KEYS */;
/*!40000 ALTER TABLE `favorites` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `keyword`
--

DROP TABLE IF EXISTS `keyword`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!50503 SET character_set_client = utf8mb4 */;
CREATE TABLE `keyword` (
  `data` varchar(50) NOT NULL,
  PRIMARY KEY (`data`)
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_0900_ai_ci;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `keyword`
--

LOCK TABLES `keyword` WRITE;
/*!40000 ALTER TABLE `keyword` DISABLE KEYS */;
INSERT INTO `keyword` VALUES ('action recognition'),('active learning'),('adaptive learning'),('adversarial attacks'),('adversarial learning'),('adversarial networks'),('adversarial training'),('anomaly detection'),('artificial neural networks'),('attention based'),('attention model'),('attention networks'),('bayesian'),('bayesian deep learning'),('bayesian inference'),('bayesian learning'),('bayesian model'),('bayesian network'),('bayesian neural networks'),('bayesian optimization'),('belief network'),('capsule networks'),('classification based'),('classification learning'),('classification models'),('classification networks'),('clustering'),('collaborative learning'),('community detection'),('component analysis'),('continual learning'),('convolutional networks'),('convolutional neural networks'),('data augmentation'),('data learning'),('deep complex networks'),('deep feature'),('deep generative'),('deep graph'),('deep learning'),('deep learning networks'),('deep networks'),('deep neural networks'),('deep reinforcement learning'),('deep semantic'),('deep video'),('detection algorithm'),('detection models'),('dictionary learning'),('discriminative learning'),('distributed learning'),('distribution learning'),('domain adaptation'),('embedding'),('embedding learning'),('ensemble learning'),('event detection'),('face detection'),('face recognition'),('feature extraction'),('feature learning'),('feature selection'),('federated learning'),('few-shot learning'),('generative adversarial network'),('generative learning'),('generative models'),('gradient descent'),('graph based'),('graph convolutional networks'),('graph learning'),('graph network'),('graph neural networks'),('graphical models'),('hierarchical neural'),('image analysis'),('image captioning'),('image classification'),('image compression'),('image features extraction'),('image generation'),('image models'),('image processing'),('image recognition'),('image reconstruction'),('image retrieval'),('image segmentation'),('image synthesis'),('images learning'),('imitation learning'),('incremental learning'),('inference'),('inference networks'),('joint learning'),('kernel learning'),('language detection'),('language generation'),('language learning'),('language modeling'),('language models'),('language understanding'),('learning algorithms'),('learning approach'),('learning based'),('learning classifier'),('learning framework'),('learning model'),('learning rate'),('learning real-time'),('learning vector'),('lifelong learning'),('linear models'),('machine learning'),('manifold learning'),('markov model'),('memory network'),('metric learning'),('model adaptation'),('model compression'),('model selection'),('models learning'),('multi-task learning'),('multi-view learning'),('named entity recognition'),('natural language inference'),('natural language processing'),('network algorithm'),('network compression'),('network embedding'),('network flow'),('network modeling'),('network models'),('network predictions'),('network representation learning'),('networks estimation'),('networks graph'),('neural architecture search'),('neural image'),('neural language models'),('neural machine'),('neural machine translation'),('neural model'),('neural network architectures'),('neural network training'),('neural networks'),('object recognition'),('object segmentation'),('online learning'),('policy learning'),('pose estimation'),('prediction'),('prediction model'),('probabilistic models'),('question answering'),('reasoning learning'),('recognition learning'),('recognition network'),('recurrent neural networks'),('regression'),('regression model'),('regression network'),('reinforcement learning'),('representation learning'),('residual learning'),('residual networks'),('segmentation networks'),('semantic'),('semantic models'),('semantic segmentation'),('semantics learning'),('semi-supervised learning'),('sentiment analysis'),('sentiment classification'),('sequence learning'),('similarity learning'),('speech recognition'),('spiking neural networks'),('state networks'),('stochastic gradient'),('stochastic optimization'),('structure learning'),('temporal difference learning'),('tensor networks'),('text classification'),('text detection'),('time series'),('transfer learning'),('translation learning'),('unsupervised domain'),('unsupervised learning'),('variational inference'),('word embeddings'),('word representations'),('zero-shot learning');
/*!40000 ALTER TABLE `keyword` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `thesis`
--

DROP TABLE IF EXISTS `thesis`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!50503 SET character_set_client = utf8mb4 */;
CREATE TABLE `thesis` (
  `thesis_id` int NOT NULL AUTO_INCREMENT,
  `title` varchar(100) NOT NULL,
  `author` varchar(100) NOT NULL,
  `publication_date` date DEFAULT NULL,
  `image_link` varchar(150) DEFAULT NULL,
  `abstract` varchar(1500) NOT NULL,
  `link` varchar(150) DEFAULT NULL,
  `citation_num` int DEFAULT NULL,
  `rating` double DEFAULT NULL,
  PRIMARY KEY (`thesis_id`)
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_0900_ai_ci;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `thesis`
--

LOCK TABLES `thesis` WRITE;
/*!40000 ALTER TABLE `thesis` DISABLE KEYS */;
/*!40000 ALTER TABLE `thesis` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `user`
--

DROP TABLE IF EXISTS `user`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!50503 SET character_set_client = utf8mb4 */;
CREATE TABLE `user` (
  `user_id` int NOT NULL AUTO_INCREMENT,
  `user_name` varchar(20) NOT NULL,
  `password` varchar(20) NOT NULL,
  `email` varchar(40) NOT NULL,
  `city` varchar(30) DEFAULT NULL,
  `motto` varchar(150) DEFAULT NULL,
  PRIMARY KEY (`user_id`)
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_0900_ai_ci;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `user`
--

LOCK TABLES `user` WRITE;
/*!40000 ALTER TABLE `user` DISABLE KEYS */;
/*!40000 ALTER TABLE `user` ENABLE KEYS */;
UNLOCK TABLES;
/*!40103 SET TIME_ZONE=@OLD_TIME_ZONE */;

/*!40101 SET SQL_MODE=@OLD_SQL_MODE */;
/*!40014 SET FOREIGN_KEY_CHECKS=@OLD_FOREIGN_KEY_CHECKS */;
/*!40014 SET UNIQUE_CHECKS=@OLD_UNIQUE_CHECKS */;
/*!40101 SET CHARACTER_SET_CLIENT=@OLD_CHARACTER_SET_CLIENT */;
/*!40101 SET CHARACTER_SET_RESULTS=@OLD_CHARACTER_SET_RESULTS */;
/*!40101 SET COLLATION_CONNECTION=@OLD_COLLATION_CONNECTION */;
/*!40111 SET SQL_NOTES=@OLD_SQL_NOTES */;

-- Dump completed on 2022-12-18 15:36:03
