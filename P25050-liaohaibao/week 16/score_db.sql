# Host: localhost  (Version: 5.5.53)
# Date: 2020-02-12 16:46:02
# Generator: MySQL-Front 5.3  (Build 4.234)

/*!40101 SET NAMES utf8 */;

#
# Structure for table "group"
#

DROP TABLE IF EXISTS `group`;
CREATE TABLE `group` (
  `Id` int(11) NOT NULL AUTO_INCREMENT,
  `description` varchar(255) NOT NULL DEFAULT '' COMMENT '描述',
  PRIMARY KEY (`Id`)
) ENGINE=MyISAM DEFAULT CHARSET=utf8 COMMENT='角色表';

#
# Data for table "group"
#

/*!40000 ALTER TABLE `group` DISABLE KEYS */;
INSERT INTO `group` VALUES (1,'teacher'),(2,'student');
/*!40000 ALTER TABLE `group` ENABLE KEYS */;

#
# Structure for table "score"
#

DROP TABLE IF EXISTS `score`;
CREATE TABLE `score` (
  `Id` int(11) NOT NULL AUTO_INCREMENT,
  `userId` int(11) NOT NULL DEFAULT '0' COMMENT '用户Id',
  `score` varchar(255) NOT NULL DEFAULT '' COMMENT '成绩',
  PRIMARY KEY (`Id`)
) ENGINE=MyISAM DEFAULT CHARSET=utf8 COMMENT='成绩表';

#
# Data for table "score"
#

/*!40000 ALTER TABLE `score` DISABLE KEYS */;
INSERT INTO `score` VALUES (1,103,'语文90、数学78、英语92'),(2,104,'语文95、数学98、英语90'),(3,102,'语文98、数学85、英语100');
/*!40000 ALTER TABLE `score` ENABLE KEYS */;

#
# Structure for table "user"
#

DROP TABLE IF EXISTS `user`;
CREATE TABLE `user` (
  `Id` int(10) NOT NULL AUTO_INCREMENT COMMENT '用户Id',
  `name` varchar(60) NOT NULL DEFAULT '' COMMENT '姓名',
  `groupId` int(11) NOT NULL DEFAULT '2' COMMENT '角色Id',
  `password` varchar(100) NOT NULL DEFAULT '' COMMENT '密码',
  PRIMARY KEY (`Id`),
  UNIQUE KEY `nameIdx` (`name`)
) ENGINE=MyISAM AUTO_INCREMENT=105 DEFAULT CHARSET=utf8 COMMENT='用户表';

#
# Data for table "user"
#

/*!40000 ALTER TABLE `user` DISABLE KEYS */;
INSERT INTO `user` VALUES (100,'leo',1,'123456'),(101,'jim',1,'123456'),(102,'tony',2,'123456'),(103,'cindy',2,'123456'),(104,'tom',2,'123456'),(105,'lucy',2,'123456'),(106,'a',2,'123456'),(107,'b',2,'123456'),(108,'c',2,'123456');
/*!40000 ALTER TABLE `user` ENABLE KEYS */;
