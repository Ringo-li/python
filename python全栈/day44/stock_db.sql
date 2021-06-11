DROP TABLE IF EXISTS `focus`;
CREATE TABLE `focus` (
    `id` int(10) unsigned NOT NULL AUTO_INCREMENT,
    `note_info` varchar(200) DEFAULT '',
    `info_id` int(10) unsigned DEFAULT NULL,
    PRIMARY KEY (`id`),
    KEY `info_id` (`info_id`)
    CONSTRAINT `focus_ibfk_1` FOREIGN KEY (`info_id`) REFERENCES `info` (`id`)
) ENGINE=InnoDB AUTO_INCREMENT=14 DEFAULT CHARSET=utf8;

LOCK TABLE `focus` WRITE;
INSERT INTO `focus` VALUE (2, '你确定买这个？', '36'), (3, '利好',37), (9, '', 88), (10, '', 89), (13, '', 1);
UNLOCK TABLES;

DROP TABLE IF EXISTS `info`;
CREATE TABLE `info` (
    `id` int(10) unsigned NOT NULL AUTO_INCREMENT,
    `code` varchar(6) NOT NULL COMMENT '股票代码',
    `short` varchar(10) NOT NULL COMMENT '股票简称',
    `chg` varchar(6) NOT NULL COMMENT '涨跌幅',
    `turnover` varchar(255) NOT NULL COMMENT '换手率',
    `price` decimal(10, 2) NOT NULL COMMENT '最新价',
    `highs` decimal(10, 2) NOT NULL COMMENT '前期高点',
    `time` date DEFAULT NULL,
    PRIMARY KEY (`id`)
) ENGINE=InnoDB AUTO_INCREMENT=95 DEFAULT CHARSET=utf8;

LOCK TABLE `info` WRITE;
INSERT INTO `info` VALUE (1, '000007', '全新好', '10.01%', '4.01%', 16.05, 14.60, '2017-07-18'),
(2, '000007', '全新好', '10.01%', '4.01%', 16.05, 14.60, '2017-07-18'), 
(3, '000023', '我的娃', '13.01%', '4.01%', 16.05, 14.60, '2017-07-18'), 
(4, '000012', '范德萨', '32.01%', '4.01%', 16.05, 14.60, '2017-07-18'), 
(5, '000065', '第三次', '11.01%', '4.01%', 16.05, 14.60, '2017-07-18'), 
(6, '000002', '非会员', '03.01%', '4.01%', 16.05, 14.60, '2017-07-18'), 
(7, '000028', '一套房', '20.01%', '4.01%', 16.05, 14.60, '2017-07-18'), 
(8, '000703', '我都会', '30.01%', '4.01%', 16.05, 14.60, '2017-07-18');
UNLOCK TABLES;