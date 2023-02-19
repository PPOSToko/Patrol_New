/*
 Navicat Premium Data Transfer

 Source Server         : 21
 Source Server Type    : MySQL
 Source Server Version : 100148
 Source Host           : 192.168.30.21:3306
 Source Schema         : patrol

 Target Server Type    : MySQL
 Target Server Version : 100148
 File Encoding         : 65001

 Date: 30/01/2023 15:31:04
*/

SET NAMES utf8mb4;
SET FOREIGN_KEY_CHECKS = 0;

-- ----------------------------
-- Table structure for _aksesmenu
-- ----------------------------
DROP TABLE IF EXISTS `_aksesmenu`;
CREATE TABLE `_aksesmenu`  (
  `level` varchar(1) CHARACTER SET utf8mb4 COLLATE utf8mb4_general_ci NOT NULL,
  `idmenu` varchar(5) CHARACTER SET utf8mb4 COLLATE utf8mb4_general_ci NOT NULL,
  `mn01` varchar(1) CHARACTER SET utf8mb4 COLLATE utf8mb4_general_ci NULL DEFAULT 'X',
  `mn02` varchar(1) CHARACTER SET utf8mb4 COLLATE utf8mb4_general_ci NULL DEFAULT NULL,
  `mn03` varchar(1) CHARACTER SET utf8mb4 COLLATE utf8mb4_general_ci NULL DEFAULT NULL,
  `mn04` varchar(1) CHARACTER SET utf8mb4 COLLATE utf8mb4_general_ci NULL DEFAULT NULL,
  `mn05` varchar(1) CHARACTER SET utf8mb4 COLLATE utf8mb4_general_ci NULL DEFAULT NULL,
  `mn06` varchar(1) CHARACTER SET utf8mb4 COLLATE utf8mb4_general_ci NULL DEFAULT NULL,
  `mn07` varchar(1) CHARACTER SET utf8mb4 COLLATE utf8mb4_general_ci NULL DEFAULT NULL,
  `mn08` varchar(1) CHARACTER SET utf8mb4 COLLATE utf8mb4_general_ci NULL DEFAULT NULL,
  `mn09` varchar(1) CHARACTER SET utf8mb4 COLLATE utf8mb4_general_ci NULL DEFAULT NULL,
  `mn10` varchar(1) CHARACTER SET utf8mb4 COLLATE utf8mb4_general_ci NULL DEFAULT NULL,
  `mn11` varchar(1) CHARACTER SET utf8mb4 COLLATE utf8mb4_general_ci NULL DEFAULT NULL,
  `mn12` varchar(1) CHARACTER SET utf8mb4 COLLATE utf8mb4_general_ci NULL DEFAULT NULL,
  `mn13` varchar(1) CHARACTER SET utf8mb4 COLLATE utf8mb4_general_ci NULL DEFAULT 'X',
  `mn14` varchar(1) CHARACTER SET utf8mb4 COLLATE utf8mb4_general_ci NULL DEFAULT 'X',
  PRIMARY KEY (`level`, `idmenu`) USING BTREE
) ENGINE = InnoDB CHARACTER SET = utf8mb4 COLLATE = utf8mb4_general_ci ROW_FORMAT = Compact;

-- ----------------------------
-- Records of _aksesmenu
-- ----------------------------
INSERT INTO `_aksesmenu` VALUES ('1', '', 'X', 'X', 'X', 'V', 'V', 'V', 'X', 'X', 'V', 'X', 'X', 'X', 'X', 'X');
INSERT INTO `_aksesmenu` VALUES ('2', '', 'V', 'V', 'V', 'V', 'V', 'V', 'V', 'V', 'V', 'X', 'X', 'X', 'X', 'X');
INSERT INTO `_aksesmenu` VALUES ('3', '', 'V', 'V', 'V', 'V', 'V', 'V', 'V', 'V', 'V', 'X', 'X', 'X', 'X', 'X');

-- ----------------------------
-- Table structure for _mainmenu
-- ----------------------------
DROP TABLE IF EXISTS `_mainmenu`;
CREATE TABLE `_mainmenu`  (
  `id_mm` varchar(3) CHARACTER SET latin1 COLLATE latin1_swedish_ci NOT NULL,
  `des_mm` varchar(100) CHARACTER SET latin1 COLLATE latin1_swedish_ci NULL DEFAULT NULL,
  `icon` varchar(50) CHARACTER SET latin1 COLLATE latin1_swedish_ci NULL DEFAULT NULL,
  `lnk` varchar(50) CHARACTER SET latin1 COLLATE latin1_swedish_ci NULL DEFAULT NULL,
  `aktif` varchar(1) CHARACTER SET latin1 COLLATE latin1_swedish_ci NULL DEFAULT NULL,
  PRIMARY KEY (`id_mm`) USING BTREE
) ENGINE = MyISAM CHARACTER SET = latin1 COLLATE = latin1_swedish_ci ROW_FORMAT = Dynamic;

-- ----------------------------
-- Records of _mainmenu
-- ----------------------------
INSERT INTO `_mainmenu` VALUES ('001', 'Dashborad', 'fa-gears', 'gridmenu.html', '1');
INSERT INTO `_mainmenu` VALUES ('002', 'Adminstrator', 'fa-list-alt', 'gridmenu.html', '1');
INSERT INTO `_mainmenu` VALUES ('003', 'Patrol', 'fa-medkit', 'gridmenu.html', '1');

-- ----------------------------
-- Table structure for _menu
-- ----------------------------
DROP TABLE IF EXISTS `_menu`;
CREATE TABLE `_menu`  (
  `id_mn` varchar(3) CHARACTER SET latin1 COLLATE latin1_swedish_ci NOT NULL,
  `id_mm` varchar(3) CHARACTER SET latin1 COLLATE latin1_swedish_ci NOT NULL,
  `des_mn` varchar(100) CHARACTER SET latin1 COLLATE latin1_swedish_ci NULL DEFAULT NULL,
  `icon` varchar(50) CHARACTER SET latin1 COLLATE latin1_swedish_ci NULL DEFAULT NULL,
  `lnk` varchar(50) CHARACTER SET latin1 COLLATE latin1_swedish_ci NULL DEFAULT NULL,
  `aktif` varchar(1) CHARACTER SET latin1 COLLATE latin1_swedish_ci NULL DEFAULT NULL,
  `info` varchar(255) CHARACTER SET latin1 COLLATE latin1_swedish_ci NULL DEFAULT NULL,
  PRIMARY KEY (`id_mn`, `id_mm`) USING BTREE
) ENGINE = MyISAM CHARACTER SET = latin1 COLLATE = latin1_swedish_ci ROW_FORMAT = Dynamic;

-- ----------------------------
-- Records of _menu
-- ----------------------------
INSERT INTO `_menu` VALUES ('001', '001', 'Dashboard', NULL, NULL, '1', NULL);

-- ----------------------------
-- Table structure for _menuotr
-- ----------------------------
DROP TABLE IF EXISTS `_menuotr`;
CREATE TABLE `_menuotr`  (
  `username` varchar(30) CHARACTER SET latin1 COLLATE latin1_swedish_ci NULL DEFAULT NULL,
  `id_mm` varchar(3) CHARACTER SET latin1 COLLATE latin1_swedish_ci NULL DEFAULT NULL,
  `id_mn` varchar(3) CHARACTER SET latin1 COLLATE latin1_swedish_ci NULL DEFAULT NULL
) ENGINE = MyISAM CHARACTER SET = latin1 COLLATE = latin1_swedish_ci ROW_FORMAT = Dynamic;

-- ----------------------------
-- Records of _menuotr
-- ----------------------------
INSERT INTO `_menuotr` VALUES ('admin', '001', '001');
INSERT INTO `_menuotr` VALUES ('admin', '001', '002');
INSERT INTO `_menuotr` VALUES ('admin', '001', '003');
INSERT INTO `_menuotr` VALUES ('admin', '001', '004');
INSERT INTO `_menuotr` VALUES ('admin', '002', '005');
INSERT INTO `_menuotr` VALUES ('admin', '002', '006');
INSERT INTO `_menuotr` VALUES ('admin', '002', '007');
INSERT INTO `_menuotr` VALUES ('admin', '002', '008');
INSERT INTO `_menuotr` VALUES ('admin', '002', '012');
INSERT INTO `_menuotr` VALUES ('admin', '002', '013');
INSERT INTO `_menuotr` VALUES ('admin', '002', '014');
INSERT INTO `_menuotr` VALUES ('admin', '003', '015');
INSERT INTO `_menuotr` VALUES ('admin', '003', '016');
INSERT INTO `_menuotr` VALUES ('admin', '004', '017');
INSERT INTO `_menuotr` VALUES ('admin', '004', '018');
INSERT INTO `_menuotr` VALUES ('admin', '004', '019');
INSERT INTO `_menuotr` VALUES ('admin', '004', '020');
INSERT INTO `_menuotr` VALUES ('admin', '004', '021');
INSERT INTO `_menuotr` VALUES ('admin', '004', '022');
INSERT INTO `_menuotr` VALUES ('admin', '004', '023');
INSERT INTO `_menuotr` VALUES ('admin', '004', '024');
INSERT INTO `_menuotr` VALUES ('admin', '004', '025');
INSERT INTO `_menuotr` VALUES ('admin', '004', '026');
INSERT INTO `_menuotr` VALUES ('admin', '004', '027');
INSERT INTO `_menuotr` VALUES ('admin', '005', '028');
INSERT INTO `_menuotr` VALUES ('admin', '005', '029');
INSERT INTO `_menuotr` VALUES ('zaenuddin', '004', '019');
INSERT INTO `_menuotr` VALUES ('admin', '002', '009');
INSERT INTO `_menuotr` VALUES ('admin', '002', '010');
INSERT INTO `_menuotr` VALUES ('admin', '002', '011');

-- ----------------------------
-- Table structure for _settupdata
-- ----------------------------
DROP TABLE IF EXISTS `_settupdata`;
CREATE TABLE `_settupdata`  (
  `idpatrol` int NULL DEFAULT 0
) ENGINE = InnoDB CHARACTER SET = utf8mb4 COLLATE = utf8mb4_general_ci ROW_FORMAT = Compact;

-- ----------------------------
-- Records of _settupdata
-- ----------------------------
INSERT INTO `_settupdata` VALUES (166);

-- ----------------------------
-- Table structure for _users
-- ----------------------------
DROP TABLE IF EXISTS `_users`;
CREATE TABLE `_users`  (
  `username` varchar(30) CHARACTER SET latin1 COLLATE latin1_swedish_ci NOT NULL DEFAULT '',
  `password` varchar(100) CHARACTER SET latin1 COLLATE latin1_swedish_ci NULL DEFAULT NULL,
  `nama` varchar(50) CHARACTER SET latin1 COLLATE latin1_swedish_ci NULL DEFAULT NULL,
  `level` varchar(1) CHARACTER SET latin1 COLLATE latin1_swedish_ci NULL DEFAULT NULL,
  `aktif` varchar(1) CHARACTER SET latin1 COLLATE latin1_swedish_ci NULL DEFAULT NULL,
  PRIMARY KEY (`username`) USING BTREE
) ENGINE = InnoDB CHARACTER SET = latin1 COLLATE = latin1_swedish_ci ROW_FORMAT = Compact;

-- ----------------------------
-- Records of _users
-- ----------------------------
INSERT INTO `_users` VALUES ('AgungJ', 'e807f1fcf82d132f9bb018ca6738a19f', 'Agung Jiwiandono', '1', NULL);
INSERT INTO `_users` VALUES ('ali', '24c718831b46f19e2230cca070990102', 'Muhammad Ali', '3', '1');
INSERT INTO `_users` VALUES ('Amai', 'e807f1fcf82d132f9bb018ca6738a19f', 'Astri Amai', '1', NULL);
INSERT INTO `_users` VALUES ('AndiA', 'e807f1fcf82d132f9bb018ca6738a19f', 'Andi Akbar', '1', NULL);
INSERT INTO `_users` VALUES ('Andy', 'e807f1fcf82d132f9bb018ca6738a19f', 'Andy WIlliam', '1', '');
INSERT INTO `_users` VALUES ('Angel', 'e807f1fcf82d132f9bb018ca6738a19f', 'Angel Jan Sarwono', '1', '1');
INSERT INTO `_users` VALUES ('Anugrah', 'e807f1fcf82d132f9bb018ca6738a19f', 'Anugrah P', '1', NULL);
INSERT INTO `_users` VALUES ('Anwar', 'e807f1fcf82d132f9bb018ca6738a19f', 'Anwar Faturachman', '1', NULL);
INSERT INTO `_users` VALUES ('Arief', 'e807f1fcf82d132f9bb018ca6738a19f', 'Arief Hanifan', '1', NULL);
INSERT INTO `_users` VALUES ('Asalim', 'e807f1fcf82d132f9bb018ca6738a19f', 'Agus Salim', '1', NULL);
INSERT INTO `_users` VALUES ('Daisy', 'e807f1fcf82d132f9bb018ca6738a19f', 'Daisy', '1', NULL);
INSERT INTO `_users` VALUES ('Danny', 'e807f1fcf82d132f9bb018ca6738a19f', 'Danny Lim', '1', NULL);
INSERT INTO `_users` VALUES ('Eny', 'e807f1fcf82d132f9bb018ca6738a19f', 'Eny Budhi Astuti', '1', NULL);
INSERT INTO `_users` VALUES ('Erwin', 'e807f1fcf82d132f9bb018ca6738a19f', 'Muhammad Erwin Priyanto', '1', NULL);
INSERT INTO `_users` VALUES ('Ewi', 'e807f1fcf82d132f9bb018ca6738a19f', 'Ewifiewanty Thjin', '1', NULL);
INSERT INTO `_users` VALUES ('Ewy', 'e807f1fcf82d132f9bb018ca6738a19f', 'Ewy Fieyanti Thjin', '1', NULL);
INSERT INTO `_users` VALUES ('Fuji', 'e807f1fcf82d132f9bb018ca6738a19f', 'Fujianto Tan', '1', NULL);
INSERT INTO `_users` VALUES ('Hendra', 'e807f1fcf82d132f9bb018ca6738a19f', 'Hendra Saputra', '1', NULL);
INSERT INTO `_users` VALUES ('heru', '8365616df7abfa0541b1ebbec310acae', 'heru Wahyu', '2', '1');
INSERT INTO `_users` VALUES ('inspec', 'f8d6966f5d5046a86aa2a5ddf6b1ce2c', 'testinspect', '1', '1');
INSERT INTO `_users` VALUES ('inspect', 'e807f1fcf82d132f9bb018ca6738a19f', 'testinspect', '1', NULL);
INSERT INTO `_users` VALUES ('Isa', 'e807f1fcf82d132f9bb018ca6738a19f', 'Isa Al-Anshari', '1', NULL);
INSERT INTO `_users` VALUES ('Kusro', 'e807f1fcf82d132f9bb018ca6738a19f', 'Kusro', '1', NULL);
INSERT INTO `_users` VALUES ('Meidyanto', 'e807f1fcf82d132f9bb018ca6738a19f', 'Meidyanto Thjin', '1', NULL);
INSERT INTO `_users` VALUES ('Nadya', 'e807f1fcf82d132f9bb018ca6738a19f', 'Nadya Desiana', '1', NULL);
INSERT INTO `_users` VALUES ('Permana', 'e807f1fcf82d132f9bb018ca6738a19f', 'Linda Permana', '1', NULL);
INSERT INTO `_users` VALUES ('Rani', 'e807f1fcf82d132f9bb018ca6738a19f', 'Rani', '1', NULL);
INSERT INTO `_users` VALUES ('Rifqi', 'e807f1fcf82d132f9bb018ca6738a19f', 'Rifqi Hammami', '1', NULL);
INSERT INTO `_users` VALUES ('Sandrio', 'e807f1fcf82d132f9bb018ca6738a19f', 'Sandrio Martin', '1', NULL);
INSERT INTO `_users` VALUES ('Steve', 'e807f1fcf82d132f9bb018ca6738a19f', 'Steve Bongso', '1', NULL);
INSERT INTO `_users` VALUES ('Tendry', 'e807f1fcf82d132f9bb018ca6738a19f', 'Tendry Andromeda Edwinardie', '1', NULL);
INSERT INTO `_users` VALUES ('test', 'f8d6966f5d5046a86aa2a5ddf6b1ce2c', 'test123', '2', NULL);
INSERT INTO `_users` VALUES ('widy', 'f5b6346ecd70e05865f15dc9e73e8dd9', 'widy fernando', '3', NULL);

-- ----------------------------
-- Table structure for induk
-- ----------------------------
DROP TABLE IF EXISTS `induk`;
CREATE TABLE `induk`  (
  `id_induk` int NOT NULL AUTO_INCREMENT,
  `description` varchar(255) CHARACTER SET latin1 COLLATE latin1_swedish_ci NULL DEFAULT NULL,
  `status` varchar(1) CHARACTER SET latin1 COLLATE latin1_swedish_ci NULL DEFAULT NULL,
  PRIMARY KEY (`id_induk`) USING BTREE
) ENGINE = InnoDB AUTO_INCREMENT = 6 CHARACTER SET = latin1 COLLATE = latin1_swedish_ci ROW_FORMAT = Compact;

-- ----------------------------
-- Records of induk
-- ----------------------------
INSERT INTO `induk` VALUES (1, 'FIELD HEAD FINISHING', '0');
INSERT INTO `induk` VALUES (2, 'FIELD HEAD PRINTING', '1');
INSERT INTO `induk` VALUES (3, 'INK', '1');
INSERT INTO `induk` VALUES (4, 'TOOLING', '1');
INSERT INTO `induk` VALUES (5, 'PRINTING', '1');

-- ----------------------------
-- Table structure for patrol_header
-- ----------------------------
DROP TABLE IF EXISTS `patrol_header`;
CREATE TABLE `patrol_header`  (
  `id_patrol` int NULL DEFAULT NULL,
  `id_petugas` varchar(30) CHARACTER SET latin1 COLLATE latin1_swedish_ci NULL DEFAULT NULL,
  `id_induk` int NULL DEFAULT NULL,
  `id_korlap` varchar(30) CHARACTER SET latin1 COLLATE latin1_swedish_ci NULL DEFAULT NULL,
  `id_karyawan` varchar(30) CHARACTER SET latin1 COLLATE latin1_swedish_ci NULL DEFAULT NULL,
  `star_date` datetime NULL DEFAULT NULL,
  `stop_date` datetime NULL DEFAULT NULL,
  `finishdate` datetime NULL DEFAULT NULL,
  `status` int NOT NULL DEFAULT 0 COMMENT '1. Finish 0. Unfinish',
  `total_score` float(3, 2) NULL DEFAULT NULL
) ENGINE = InnoDB CHARACTER SET = latin1 COLLATE = latin1_swedish_ci ROW_FORMAT = Compact;

-- ----------------------------
-- Records of patrol_header
-- ----------------------------
INSERT INTO `patrol_header` VALUES (155, 'ali', 2, '3', '', '2023-01-23 17:03:07', NULL, NULL, 1, NULL);
INSERT INTO `patrol_header` VALUES (163, 'ali', 3, '3', '4', '2023-01-27 14:07:36', '2023-01-27 14:09:33', '2023-01-27 14:09:33', 1, NULL);

-- ----------------------------
-- Table structure for patrol_line
-- ----------------------------
DROP TABLE IF EXISTS `patrol_line`;
CREATE TABLE `patrol_line`  (
  `id_line` int NOT NULL AUTO_INCREMENT,
  `id_patrol` int NULL DEFAULT NULL,
  `id_pertanyaan` int NULL DEFAULT NULL,
  `id_point` int NULL DEFAULT NULL,
  `status` int NULL DEFAULT NULL COMMENT '0.Not Answer 1. Answer',
  `score` int NULL DEFAULT NULL COMMENT '0. Tidak Sesuai 1. Sesuai',
  `answer_date` datetime NULL DEFAULT NULL,
  `flag_jawab` varchar(1) CHARACTER SET latin1 COLLATE latin1_swedish_ci NULL DEFAULT 'X',
  `remark` varchar(255) CHARACTER SET latin1 COLLATE latin1_swedish_ci NULL DEFAULT NULL,
  PRIMARY KEY (`id_line`) USING BTREE
) ENGINE = InnoDB AUTO_INCREMENT = 33 CHARACTER SET = latin1 COLLATE = latin1_swedish_ci ROW_FORMAT = Compact;

-- ----------------------------
-- Records of patrol_line
-- ----------------------------
INSERT INTO `patrol_line` VALUES (1, 155, 3, 1, NULL, NULL, NULL, 'X', NULL);
INSERT INTO `patrol_line` VALUES (2, 155, 1, 1, NULL, NULL, NULL, 'X', NULL);
INSERT INTO `patrol_line` VALUES (3, 155, 4, 2, NULL, NULL, NULL, 'X', NULL);
INSERT INTO `patrol_line` VALUES (4, 155, 7, 2, NULL, NULL, NULL, 'X', NULL);
INSERT INTO `patrol_line` VALUES (5, 155, 14, 3, NULL, NULL, NULL, 'X', NULL);
INSERT INTO `patrol_line` VALUES (6, 155, 12, 3, NULL, NULL, NULL, 'X', NULL);
INSERT INTO `patrol_line` VALUES (7, 155, 16, 4, NULL, NULL, NULL, 'X', NULL);
INSERT INTO `patrol_line` VALUES (8, 155, 15, 4, NULL, NULL, NULL, 'X', NULL);
INSERT INTO `patrol_line` VALUES (9, 155, 17, 5, NULL, NULL, NULL, 'X', NULL);
INSERT INTO `patrol_line` VALUES (10, 155, 19, 5, NULL, NULL, NULL, 'X', NULL);
INSERT INTO `patrol_line` VALUES (11, 155, 2, 1, NULL, NULL, NULL, 'X', NULL);
INSERT INTO `patrol_line` VALUES (12, 155, 5, 2, NULL, NULL, NULL, 'X', NULL);
INSERT INTO `patrol_line` VALUES (13, 155, 9, 2, NULL, NULL, NULL, 'X', NULL);
INSERT INTO `patrol_line` VALUES (14, 155, 13, 3, NULL, NULL, NULL, 'X', NULL);
INSERT INTO `patrol_line` VALUES (15, 155, 11, 3, NULL, NULL, NULL, 'X', NULL);
INSERT INTO `patrol_line` VALUES (16, 155, 18, 5, NULL, NULL, NULL, 'X', NULL);
INSERT INTO `patrol_line` VALUES (17, 155, 8, 2, NULL, NULL, NULL, 'X', NULL);
INSERT INTO `patrol_line` VALUES (18, 155, 6, 2, NULL, NULL, NULL, 'X', NULL);
INSERT INTO `patrol_line` VALUES (19, 155, 10, 3, NULL, NULL, NULL, 'X', NULL);
INSERT INTO `patrol_line` VALUES (20, 163, 38, 8, 0, 0, '2023-01-27 14:08:19', 'V', 'Jaka sembung naik ojek');
INSERT INTO `patrol_line` VALUES (21, 163, 35, 8, 0, 0, '2023-01-27 14:08:59', 'V', 'Jaka sembung bawa gelas');
INSERT INTO `patrol_line` VALUES (22, 163, 46, 9, 0, 0, '2023-01-27 14:09:17', 'V', 'Jaka sembung bawa mobil');
INSERT INTO `patrol_line` VALUES (23, 163, 43, 9, NULL, NULL, NULL, 'X', NULL);
INSERT INTO `patrol_line` VALUES (24, 163, 36, 8, NULL, NULL, NULL, 'X', NULL);
INSERT INTO `patrol_line` VALUES (25, 163, 34, 8, NULL, NULL, NULL, 'X', NULL);
INSERT INTO `patrol_line` VALUES (26, 163, 42, 9, NULL, NULL, NULL, 'X', NULL);
INSERT INTO `patrol_line` VALUES (27, 163, 44, 9, NULL, NULL, NULL, 'X', NULL);
INSERT INTO `patrol_line` VALUES (28, 163, 37, 8, NULL, NULL, NULL, 'X', NULL);
INSERT INTO `patrol_line` VALUES (29, 163, 40, 9, NULL, NULL, NULL, 'X', NULL);
INSERT INTO `patrol_line` VALUES (30, 163, 45, 9, NULL, NULL, NULL, 'X', NULL);
INSERT INTO `patrol_line` VALUES (31, 163, 41, 9, NULL, NULL, NULL, 'X', NULL);
INSERT INTO `patrol_line` VALUES (32, 163, 39, 9, NULL, NULL, NULL, 'X', NULL);

-- ----------------------------
-- Table structure for pertanyaan
-- ----------------------------
DROP TABLE IF EXISTS `pertanyaan`;
CREATE TABLE `pertanyaan`  (
  `id_pertanyaan` int NOT NULL AUTO_INCREMENT,
  `id_point` int NULL DEFAULT NULL,
  `pertanyaan` text CHARACTER SET latin1 COLLATE latin1_swedish_ci NULL,
  `std_jawaban` text CHARACTER SET latin1 COLLATE latin1_swedish_ci NULL,
  `eff_from` date NULL DEFAULT NULL,
  `eff_to` date NULL DEFAULT NULL,
  `date_input` datetime NULL DEFAULT NULL ON UPDATE CURRENT_TIMESTAMP,
  `user_input` varchar(20) CHARACTER SET latin1 COLLATE latin1_swedish_ci NULL DEFAULT NULL,
  `id_induk` int NULL DEFAULT NULL,
  PRIMARY KEY (`id_pertanyaan`) USING BTREE
) ENGINE = InnoDB AUTO_INCREMENT = 101 CHARACTER SET = latin1 COLLATE = latin1_swedish_ci ROW_FORMAT = Compact;

-- ----------------------------
-- Records of pertanyaan
-- ----------------------------
INSERT INTO `pertanyaan` VALUES (1, 1, 'Apakah anda melakukan verifikasi terhadap penyimpanan tinta? Kapan dan apa dasar dari verifikasi tersebut?', 'Ya, dilakukan setiap hari / mingguan dengan melakukan verifikasi terhadap data inputan di CERM dengan lokasi penyimpanan secara random sampling. ', '0000-00-00', '0000-00-00', '2023-01-19 13:16:09', 'heru', 2);
INSERT INTO `pertanyaan` VALUES (2, 1, 'Apa yang anda lakukan jika terjadi ketidaksesuain warna khusus pada saat proses cetak (Pra Cetak)?', 'Leader akan meminta operator INK untuk melakukan Color Matching sampai didapatkan warna yang sesuai dengan artwork, setiap perubahan yang dilakukan akan diverifikasi oleh leader di Form Laporan INK Operator (FR-PRD-009)', '0000-00-00', '0000-00-00', '2023-01-19 13:16:52', 'heru', 2);
INSERT INTO `pertanyaan` VALUES (3, 1, 'Bagaimana standard suhu penyimpanan dan masa simpan tinta yang dilakukan?', 'Tinta harus disimpan dalam suhu 23 - 25oC dan masa penyimpanan Tinta Maksimal 1 Tahun, setelah itu harus didisposal.', '0000-00-00', '0000-00-00', '2023-01-19 13:17:44', 'heru', 2);
INSERT INTO `pertanyaan` VALUES (4, 2, 'Apa yang dilakukan, Jika Spesifikasi Bahan yang ada di Job Ticket di rubah secara manual?', 'Leader dapat menjelaskan secara flow proses seperti berikut:\na. Informasi diterima dari operator tooling ataupun saat pengecekan kesesuaian bahan\nb. Field Head / Leader akan melakukan konfirmasi perubahan bahan tersebut ke tim PPIC.\nc. Field Head / Leader', '0000-00-00', '0000-00-00', '2023-01-19 13:18:42', 'heru', 2);
INSERT INTO `pertanyaan` VALUES (5, 2, 'Pengecekan apa saja yang dilakukan pada dokumen Form Sejarah Proof?', 'Operator dapat menjelaskan Critical Point seperti berikut:\na. Spesifikasi Bahan dan CRB yang digunakan sesuai dengan Job Ticket\nb. No. Anliox yang digunakan\nc. Tinta yang digunakan pada anilox', '0000-00-00', '0000-00-00', '2023-01-19 13:19:02', 'heru', 2);
INSERT INTO `pertanyaan` VALUES (6, 2, 'Verifikasi apa yang anda lakukan terkait dengan hasil mounting plate ke cylinder?', 'Standard Pengecekan Mounting Plate:\n- Plate Menempel secara menyeluruh\n- Sambungan Plate dan Tape tidak sejajar\n- Plate rata atau tidak bergelembung\n- Cross Bar plate sejajar pada bagaian kiri dan kanan', '0000-00-00', '0000-00-00', '2023-01-19 13:19:32', 'heru', 2);
INSERT INTO `pertanyaan` VALUES (7, 2, 'Apakah anda mengetahui defect apa yang akan terjadi jika mounting plate tidak sesuai?', 'a. Miss Register\nb. Warna Cetakan tidak sesuai\nc. Plate terlepas dari Cylinder', '0000-00-00', '0000-00-00', '2023-01-19 13:19:51', 'heru', 2);
INSERT INTO `pertanyaan` VALUES (8, 2, 'Verifikasi apa yang anda lakukan terkait dengan hasil pemasangan Screen ke cylinder?', 'Standard Pengecekan Handling Screen:\n- Screen Tidak Mampet (Terlihat ketika diterawang)\n- Screen Tidak Terlipat\n- Screen Tidak Berkerut\n- Pemasangan Plate Lurus', '0000-00-00', '0000-00-00', '2023-01-19 13:20:09', 'heru', 2);
INSERT INTO `pertanyaan` VALUES (9, 2, 'Apakah anda mengetahui defect apa yang akan terjadi jika Handling Screen tidak sesuai?', 'a. Miss Register\nb. Garis Pada Cetakan\nc. Warna Cetakan Kotor / Cetakan ada yang hilang', '0000-00-00', '0000-00-00', '2023-01-19 13:21:10', 'heru', 2);
INSERT INTO `pertanyaan` VALUES (10, 3, 'Apa fungsi Line Clearance dilakukan pada saat awal proses produksi?', 'Untuk memastikan bahwa kondisi mesin, peralatan dan area yang akan digunakan sudah terbebas dari sisa produksi sebelumnya dan siap untuk digunakan', '0000-00-00', '0000-00-00', '2023-01-19 13:21:38', 'heru', 2);
INSERT INTO `pertanyaan` VALUES (11, 3, 'Apakah anda mengetahui dampak apa saja yang terjadi jika tidak menjalankan Line Clearance?', 'Beberapa damapak yang terjadi jika tidak menjalankan Line Clearance:\n- Hasil Cetakan Tercampur\n- Kontaminasi terhadap hasil cetakan, baik dari kotoran (debu) ataupun tumpahan tinta\n- Kegagalan dari hasil cetak yang dapat menyebabkan kerugian secara finans', '0000-00-00', '0000-00-00', '2023-01-19 13:22:40', 'heru', 2);
INSERT INTO `pertanyaan` VALUES (12, 3, 'Apakah anda mengetahui alasan mengapa NIPP ROLL wajib untuk selalu dibersihkan?', 'NIPP ROLL dibersihkan untuk menghindari adanya kotoran yang terbawa pada saat proses cetak, hal ini akan berdamapak dengan adanya defect bintik/kotoran pada hasil cetak', '0000-00-00', '0000-00-00', '2023-01-19 13:23:00', 'heru', 2);
INSERT INTO `pertanyaan` VALUES (13, 3, 'Bagaimana standard pengecekan Doctor Blade dan defect apa yang terjadi jika kondisi doctor blade sudah tidak bagus?', 'Pengecekan dialkukan secara visual pada bagian pisau sapuan, jika sudah tidak rata maka doctor blade sudah dalam kondisi \"Aus\". Jika tetap digunakan maka akan menyebabkan defect label bergaris pada label.', '0000-00-00', '0000-00-00', '2023-01-19 13:23:21', 'heru', 2);
INSERT INTO `pertanyaan` VALUES (14, 3, 'Apa yang akan anda lakukan jika ditemukan hasil actual dari line clearance tidak sesuai dengan data yang tertera pada Laporan di Form Line Clearance?', 'Leader akan bertanggung jawab untuk meminta operator tooling untuk melakukan pengecekan line clearance ulang secara menyeluruh dan mendampingi proses line clearance yang dilakukan.', '0000-00-00', '0000-00-00', '2023-01-19 13:23:48', 'heru', 2);
INSERT INTO `pertanyaan` VALUES (15, 4, 'Apakah anda melakukan verifikasi terhadap hasil pemasangan / set-up yang dilakukan pada mesin? Apa saja yang anda verifikasi?', 'Ya, melakukan verifikasi seperti:\na. Pengecekan hasil pemasangan bahan\nb. Pengecekan hasil pemasangan Anilox\nc. Pengecekan hasil pemasangan Chamber & Doctor Blade\nd. Pengecekan bak Tinta\ne. Pengecekan hasil pemasangan Cylinder Plate\nf. Pengecekan hasil pe', '0000-00-00', '0000-00-00', '2023-01-19 13:24:15', 'heru', 2);
INSERT INTO `pertanyaan` VALUES (16, 4, 'Apa yang anda lakukan jika pada saat register plate tidak mendapatkan hasil yang diinginkan?', 'a. Stop mesin dan melakukan review kembali hasil pemasangan cylinder plate yang digunakan\nb. Jika ditemukan adanya kesalahan pada saat pemasangan, meminta operator untuk  bongkar dan pasang kembali cylinder plate yang digunakan dan mengawasi prosesnya\nc. ', '0000-00-00', '0000-00-00', '2023-01-19 13:24:54', 'heru', 2);
INSERT INTO `pertanyaan` VALUES (17, 5, 'Apa saja yang dijadikan patokan untuk setup Master Image?', 'Setup master image berdasarkan pada karakteristik produsk, contoh: Logo, Tulisan, Gambar pada label', '0000-00-00', '0000-00-00', '2023-01-19 13:25:30', 'heru', 2);
INSERT INTO `pertanyaan` VALUES (18, 5, 'Berapa standard Sensitivitas yang digunakan pada mesin AVT sebagai mesin inspeksi?', 'Standard set up sensivitas pada mesin AVT adalah 6 untuk semua kategori', '0000-00-00', '0000-00-00', '2023-01-19 13:25:46', 'heru', 2);
INSERT INTO `pertanyaan` VALUES (19, 5, 'Apa yang akan anda lakukan, Jika ditemukan hasil set-up UVT tidak sesuai dengan standard?', 'a. Stop mesin dan catat quantity yang sudah terbaca oleh AVT (yang salah set-up)\nb. Berikan penandaan pada roll sebagai info ke tim finishing untuk melakukan sortir\nc. Lakukan perbaikan Set-Up AVT sesuai standard\nd. Lanjutkan proses dan laporkan NC terseb', '0000-00-00', '0000-00-00', '2023-01-19 13:26:10', 'heru', 2);
INSERT INTO `pertanyaan` VALUES (20, 6, 'Apa fungsi dari Label Merah dan Kapan anda melakukan penempelan label tersebut?', 'a. Label Merah digunakan sebagai penanda adanya Defect Critical yang harus dibuang pada saat sortir.\nb. Contoh defectnya seperti: Defect ketika Setting, Sambungan, Mesin Mati, Mesin Bermasalah, Tinta Habis', '0000-00-00', '0000-00-00', '2023-01-19 13:26:32', 'heru', 2);
INSERT INTO `pertanyaan` VALUES (21, 6, 'Apa fungsi dari Label Biru dan Kapan anda melakukan penempelan label tersebut?', 'a. Label Biru digunakan sebagai penanda adanya Defect Major-Minor yang harus disortir pada saat slitting.\nb. Contoh defectnya seperti: adanya debu, bercak tinta, lem, miss register, garis, die cut tembus.', '0000-00-00', '0000-00-00', '2023-01-19 13:26:47', 'heru', 2);
INSERT INTO `pertanyaan` VALUES (22, 6, 'Apakah anda melakukan monitoring penandaan label terhadap roll yang sudah selesai? apa yang anda verifikasi?', 'Ya, Field Head akan melakukan pengecekan terhadap penanadaan defect pada label, seperti\na. Penandaan Awal Core Ada\nb. Penandaan Label Defect Terdapat 2 (Awal Defect dan Akhir Defect)\nc. Label Start AVT dan / atau Sync Defect AVT ada (Jika Menggunakan AVT)', '0000-00-00', '0000-00-00', '2023-01-19 13:27:23', 'heru', 2);
INSERT INTO `pertanyaan` VALUES (23, 6, 'Lakukan sampling Pengecekan penandaan defect Langsung terhadap Roll yang sudah selesai', 'a. Penandaan Awal Core Ada\nb. Penandaan Label Defect Terdapat Awal Defect dan Akhir Defect\nc. Label Start AVT dan / atau Sync Defect AVT ada (Jika Menggunakan AVT)\nd. Contoh defect ditempelkan pada sisi Roll\ne. Data Defect tertera pada CERM', '0000-00-00', '0000-00-00', '2023-01-19 13:29:00', 'heru', 2);
INSERT INTO `pertanyaan` VALUES (24, 6, 'Apakah anda mengetahui apa yang terjadi jika penandaan label yang dijalankan tidak sesuai?', 'a. Proses finishing akan mengalami kesulitan ketika proses slitting atau sortir, dikarenakan adanya defect diluar dari penandaan yang ada.\nb. Tingginya resiko akan terjadinya product reject yang lolos ke customer yang dapat mengakibatkan adanya komplain', '0000-00-00', '0000-00-00', '2023-01-19 13:29:20', 'heru', 2);
INSERT INTO `pertanyaan` VALUES (25, 7, 'Apa yang anda lakukan jika ditemukan ketidaksesuaian pada hasil Die-Cut?', 'a. Stop Mesin\nb. Cek Kondisi Diecut\nc. Cek Kebersihan Magnetic Die Cut dan Die Cutnya\nd. Cek Pressure Die Cut\ne. Cek Posisi Bearing Magnetic', '0000-00-00', '0000-00-00', '2023-01-19 13:46:28', 'heru', 2);
INSERT INTO `pertanyaan` VALUES (26, 7, 'Apa yang anda lakukan jika ditemukan ketidaksesuaian pada hasil Tapping Test?', 'a. Stop Mesin\nb. Cek Aktifasi Corona\nc. Cek Kondisi Lampu UV (Lifetime / tidak)\nd. Cek Varnis', '0000-00-00', '0000-00-00', '2023-01-19 13:48:07', 'heru', 2);
INSERT INTO `pertanyaan` VALUES (27, 7, 'Apa yang anda lakukan jika ditemukan ketidaksesuaian pada hasil Rub Test?', 'a. Stop Mesin\nb. Cek Aktifasi Corona\nc. Cek Kondisi Lampu UV (Lifetime / tidak)\nd. Cek Varnis', '0000-00-00', '0000-00-00', '2023-01-19 13:48:33', 'heru', 2);
INSERT INTO `pertanyaan` VALUES (28, 7, 'Apa yang anda lakukan jika ditemukan ketidaksesuaian pada hasil Dyne Test?', 'a. Stop Mesin\nb. Cek Aktifasi Corona\nc. Cek dyne level material awal sebelum corona\nd. Cek Tinta, Ini dilakukan jika area dyne level tidak langsung diatas material', '0000-00-00', '0000-00-00', '2023-01-19 13:50:19', 'heru', 2);
INSERT INTO `pertanyaan` VALUES (29, 7, 'Apa yang anda lakukan jika ditemukan ketidaksesuaian pada hasil Peeling Test?', 'a. Stop Mesin\nb. Cek Aktifasi Corona\nc. Cek Kondisi Lampu UV (Lifetime / tidak)', '0000-00-00', '0000-00-00', '2023-01-19 13:50:47', 'heru', 2);
INSERT INTO `pertanyaan` VALUES (30, 7, 'Apa yang anda lakukan jika ditemukan ketidaksesuaian pada hasil Visual Tension?', 'a. Stop Mesin\nb. Cek Pressure Tension Laminasi\nc. Cek Nip Roll Unit', '0000-00-00', '0000-00-00', '2023-01-19 13:51:42', 'heru', 2);
INSERT INTO `pertanyaan` VALUES (31, 7, 'Apa yang anda lakukan jika ditemukan defect warna pada hasil cetak?', 'a. Stop Mesin\nb. Verifikasi Ulang ke Awal Buku Standard\nc. Lakukan Adjustment / Colour Matching Ulang\nd. Lakukan Pengukuran Sesuai Nilai Standard\ne. Verifikasi bersama operator di Standard Box Lampu untuk Pengecekan Warna', '0000-00-00', '0000-00-00', '2023-01-19 13:54:11', 'heru', 2);
INSERT INTO `pertanyaan` VALUES (32, 7, 'Apa yang anda lakukan jika ditemukan sample pengujian untuk pemeriksaan kualitas tidak dilakukan secara benar?', 'a. Menegur operator terkait dengan proses pemeriksaan kualitas yang masih tidak sesuai\nb. Meminta operator untuk melakukan pengecekan sample sesuai dengan standard\nc. Memastikan kembali hasil pengecekan yang dilakukan oleh operator', '0000-00-00', '0000-00-00', '2023-01-19 13:54:48', 'heru', 2);
INSERT INTO `pertanyaan` VALUES (33, 7, 'Lakukan random sampling LPK yang sedang berjalan dan pastikan sample pengujian sesuai dengan standard', 'a. Setiap sample yang dilampirkan pada LPK sudah sesuai dengan jumlah sampling yang dilakukan.\nb. Sample sudah dilakukan pengujian terlihat dari bekas pengujian, seperti bekas spidol untuk pengecekan die cut, bekas spidol pada bagian batch untuk pengeceka', '0000-00-00', '0000-00-00', '2023-01-19 13:55:38', 'heru', 2);
INSERT INTO `pertanyaan` VALUES (34, 8, 'Apa saja verifikasi yang dilakukan pada saat penerimaan tinta?', 'a. Label SKU Pada Container Tinta\nb. CoA Tinta dari Supplier\nc. Pengecekan Kondisi Fisik Wadah Tinta\nd. Pemeriksaan Batas Kadaluarsa (Shelf Life/Best Before)', '0000-00-00', '0000-00-00', '2023-01-19 13:58:35', 'heru', 3);
INSERT INTO `pertanyaan` VALUES (35, 8, 'Bagaimana Proses Sampling pemeriksaan yang dilakukan?', 'Pemeriksaan dilakukan secara 100% Inspeksi', '0000-00-00', '0000-00-00', '2023-01-19 13:58:53', 'heru', 3);
INSERT INTO `pertanyaan` VALUES (36, 8, 'Bagaimana sistem penyimpanan tinta yang dilakukan?', 'Proses penyimpanan tinta berdasarkan dari FIFO (First in-First Out)', '0000-00-00', '0000-00-00', '2023-01-19 13:59:11', 'heru', 3);
INSERT INTO `pertanyaan` VALUES (37, 8, 'Bagaimana standard suhu penyimpanan dan masa simpan tinta yang dilakukan?', 'Tinta harus disimpan dalam suhu 23 - 25oC dan masa penyimpanan Tinta Maksimal 1 Tahun, setelah itu harus didisposal', '0000-00-00', '0000-00-00', '2023-01-19 13:59:26', 'heru', 3);
INSERT INTO `pertanyaan` VALUES (38, 8, 'Bagaimana proses yang dilakukan jika ditemukan ketidaksesuaian pada Material/Tinta yang datang?', 'a. Memisahkan Material tersebut ke area material tidak sesuai\nb. diberikan penandaan berupa Sticker Berwarna Merah pada Container\nc. Laporkan kejadian tersebut kepada Field Head Flexo / Section Head untuk diteruskan ke tim QA/QC untuk dibuatkan NC kepada ', '0000-00-00', '0000-00-00', '2023-01-19 14:01:37', 'heru', 3);
INSERT INTO `pertanyaan` VALUES (39, 9, 'Dokumen/data apa yang dijadikan patokan anda untuk persiapan Tinta?', 'Data yang digunakan adalah Jadwal Produksi pada system CERM tiap harinya', '0000-00-00', '0000-00-00', '2023-01-23 10:28:37', 'heru', 3);
INSERT INTO `pertanyaan` VALUES (40, 9, 'Bagaimana proses persiapan yang dilakukan untuk Tinta Warna Dasar?', 'a. Operator akan melakukan pengecekan ketersediaan tinta untuk disetiap mesinnya\nb. Operator akan mengisi wadah tinta jika ditemukan wadah yang kosong/habis\nc. Operator tinta akan mencatat pemakaian tinta pada sistem CERM jika tinta yang digunakan adalah ', '0000-00-00', '0000-00-00', '2023-01-23 10:28:52', 'heru', 3);
INSERT INTO `pertanyaan` VALUES (41, 9, 'Bagaimana proses persiapan yang dilakukan untuk Tinta Warna Khusus (Pantone)?', 'a. Operator akan menyiapkan pencampuran tinta sesuai dengan formula tinta kusus yang digunakan\nb. Hasil dari proses pencampuran akan dibandingkan dengan reference buku pantone\nc. Tinta yang sudah dibuat akan disimpan terlebih dahulu pada rak penyimpanan s', '0000-00-00', '0000-00-00', '2023-01-23 10:29:09', 'heru', 3);
INSERT INTO `pertanyaan` VALUES (42, 9, 'Apa alat ukur yang digunakan untuk memastikan tinta yang dibuat sesuai standard? dan berapa syarat nya?', 'Instrument/alat yang digunakan adalah SPECTRO DENSITOMETER dengan syarat Delta E<1', '0000-00-00', '0000-00-00', '2023-01-23 10:29:56', 'heru', 3);
INSERT INTO `pertanyaan` VALUES (43, 9, 'Apa yang anda lakukan jika ditemukan ketidaksesuaian tinta warna khusus pada saat proses persiapan?', 'Operator akan melakukan adjustment kembali tinta tersebut di Ink Lab sebelum tinta tersebut didistribusikan kesetiap mesin.', '0000-00-00', '0000-00-00', '2023-01-23 10:39:05', 'heru', 3);
INSERT INTO `pertanyaan` VALUES (44, 9, 'Apa yang anda lakukan jika ditemukan ketidaksesuaian tinta warna khusus pada saat proses cetak?', 'Operator akan melakukan color matching kembali di mesin produksi hingga didaptakan warna yang sesuai dengan artwork', '0000-00-00', '0000-00-00', '2023-01-23 10:40:09', 'heru', 3);
INSERT INTO `pertanyaan` VALUES (45, 9, 'Apa yang anda lakukan jika pada saat color matching membutuhkan campuran warna lain diluar standard formulasi?', 'Operator akan melakukan pencatatan perubahan data formulasi di Form Laporan Ink Operator (FR-PRD-009) kemudian akan menginfokan kepada Flexo Field Head/Section Head dan Operator dari Siegwerk terkait perubahan formulasi yang digunakan', '0000-00-00', '0000-00-00', '2023-01-23 10:43:50', 'heru', 3);
INSERT INTO `pertanyaan` VALUES (46, 9, 'Apakah anda mengetahui apa akar masalah dari ketidaksesuaian warna khusus pada saat proses cetak?', 'Ketidaksesuaian ini bisa disebabkan penggunaan volume anilox yang berbeda dengan standard pemakaian ', '0000-00-00', '0000-00-00', '2023-01-23 10:44:08', 'heru', 3);
INSERT INTO `pertanyaan` VALUES (47, 10, 'Apa saja verifikasi yang dilakukan pada saat preparation document Tooling?', '- Form Pre-Setup\n- Dokumen Job Folder', '0000-00-00', '0000-00-00', '2023-01-23 11:42:58', 'heru', 4);
INSERT INTO `pertanyaan` VALUES (48, 10, 'Dokumen apa saja yang ada pada Job Folder?', '- Job Ticket\n- Buku Standard (Color Range Book)\n- Final Spec\n- Form Sejarah Proof', '0000-00-00', '0000-00-00', '2023-01-23 11:43:43', 'heru', 4);
INSERT INTO `pertanyaan` VALUES (49, 10, 'Apa yang dilakukan, Jika Spesifikasi Bahan yang ada di Job Ticket di rubah secara manual?', 'Operator dapat menjelaskan secara flow proses seperti berikut:\na. Operator tooling akan menginformasikan hal tersebut ke Leader dan PPIC untuk konfirmasi kesesuaian dan alsaan perubahan.\nb. Operator menginfokan kepada tim QC terkait perubahan tersebut unt', '0000-00-00', '0000-00-00', '2023-01-23 11:44:02', 'heru', 4);
INSERT INTO `pertanyaan` VALUES (50, 10, 'Pengecekan apa saja yang dilakukan pada dokumen Form Sejarah Proof? Berikan Contoh 1 Produk yang sudah jalan/in-process.', 'Operator dapat menjelaskan Critical Point seperti berikut:\na. Spesifikasi Bahan dan CRB yang digunakan sesuai dengan Job Ticket\nb. No. Anliox yang digunakan\nc. Tinta yang digunakan pada anilox', '0000-00-00', '0000-00-00', '2023-01-23 11:45:37', 'heru', 4);
INSERT INTO `pertanyaan` VALUES (51, 11, 'Apa saja perlengkapan peralatan/tools yang harus disiapkan?', 'Plate, Diecut, Screen, Gear, Double Tape, Roll Tersedia dan Masa Lifetime sudah diverifikasi', '0000-00-00', '0000-00-00', '2023-01-23 11:50:14', 'heru', 4);
INSERT INTO `pertanyaan` VALUES (52, 11, 'Bagaimana Proses Mounting Plate ke Cylinder dan Standard Kualitas nya?', 'a. Operator menjelaskan Proses Mounting Plate sesuai dengan Standard Instruksi Kerja \"Mounting Plate\" / Visual Management\nb. Standard Pengecekan Mounting Plate:\n- Plate Menempel secara menyeluruh\n- Sambungan Plate dan Tape tidak sejajar\n- Plate rata atau ', '0000-00-00', '0000-00-00', '2023-01-23 11:50:27', 'heru', 4);
INSERT INTO `pertanyaan` VALUES (53, 11, 'Apakah anda mengetahui defect apa yang akan terjadi jika mounting plate tidak sesuai?', 'a. Miss Register\nb. Warna Cetakan tidak sesuai\nc. Plate terlepas dari Cylinder', '0000-00-00', '0000-00-00', '2023-01-23 11:50:41', 'heru', 4);
INSERT INTO `pertanyaan` VALUES (54, 11, 'Bagaimana Proses Handling Screen dan Standard Kualitas nya?', 'a. Operator menjelaskan Proses Handling Screen sesuai dengan Standard Instruksi Kerja \"Mounting Plate\" / Visual Management\nb. Standard Pengecekan Handling Screen:\n- Screen Tidak Mampet\n- Screen Tidak Terlipat\n- Screen Tidak Berkerut\n- Pemasangan Plate Lur', '0000-00-00', '0000-00-00', '2023-01-23 11:50:55', 'heru', 4);
INSERT INTO `pertanyaan` VALUES (55, 11, 'Apakah anda mengetahui defect apa yang akan terjadi jika Handling Screen tidak sesuai?', 'a. Miss Register\nb. Garis Pada Cetakan\nc. Warna Cetakan Kotor', '0000-00-00', '0000-00-00', '2023-01-23 11:51:08', 'heru', 4);
INSERT INTO `pertanyaan` VALUES (56, 12, 'Bagaimana standard pengecekan Anilox yang sudah dibersihkan?', 'Anliox dalam kondisi kering / tidak ada sisa cairan pencuci dan / atau sisa tinta yang masih menempel pada anilox.', '0000-00-00', '0000-00-00', '2023-01-23 11:51:32', 'heru', 4);
INSERT INTO `pertanyaan` VALUES (57, 12, 'Defect apa yang terjadi jika hasil pembersihan anilox tidak dilakukan pengecekan?', 'Penampung / hole pada anilox akan berkerak dan / atau diameter dalam penampung / hole anilox sudah tidak sesuai ukuran, yang dapat menyebabkan defect pada warna cetakan', '0000-00-00', '0000-00-00', '2023-01-23 11:51:46', 'heru', 4);
INSERT INTO `pertanyaan` VALUES (58, 12, 'Bagaimana standard pengecekan Plate yang sudah dibersihkan?', '- Plate dalam kondisi kering dan tidak ada sisa tinta yang menempel pada plate\n- tidak ada bagian plate yang rusak setelah pembersihan (kritikal untuk bagian-bagian yang memiliki ukuran kecil seperti teks)', '0000-00-00', '0000-00-00', '2023-01-23 11:52:15', 'heru', 4);
INSERT INTO `pertanyaan` VALUES (59, 12, 'Defect apa yang terjadi jika hasil pembersihan Plate tidak dilakukan pengecekan?', 'Ketika digunakan pada proses cetak, akan timbul defect seperti miss register dan desain cetakan yang tidak sesuai dengan standard dan mengakibatkan downtime yang tinggi.', '0000-00-00', '0000-00-00', '2023-01-23 11:52:28', 'heru', 4);
INSERT INTO `pertanyaan` VALUES (60, 12, 'Bagaimana standard pengecekan screen yang sudah dibersihkan?', '- Sisa lem pada screen sudah hilang dan tidak menempel pada bagian gambar\n- Pori-pori pada screen tidak rusak\n- Bagian gear bersih dari sisa lem', '0000-00-00', '0000-00-00', '2023-01-23 11:52:47', 'heru', 4);
INSERT INTO `pertanyaan` VALUES (61, 12, 'Defect apa yang terjadi jika hasil pembersihan screen tidak dilakukan pengecekan?', 'Ketika digunakan pada proses cetak, akan timbul defect seperti miss register dan desain cetakan yang tidak sesuai dengan standard dan mengakibatkan downtime yang tinggi.', '0000-00-00', '0000-00-00', '2023-01-23 11:53:02', 'heru', 4);
INSERT INTO `pertanyaan` VALUES (62, 14, 'Apakah Dokumen Kerja Proses Pra-Cetak tersedia dan dilakukan dengan benar?', '- Line clearance sudah di isi dan di validasi sebelum bekerja\n- Job Ticket tersedia\n- Buku standar tersedia & Valid\n- Artwork tersedia & Valid\n- Form Sejarah Proof tersedia & terupdate\n- *Final Spec tersedia & Valid (Untuk Yasulor)\n- Kesesuaian Bahan Baku', '0000-00-00', '0000-00-00', '2023-01-23 11:59:23', 'heru', 5);
INSERT INTO `pertanyaan` VALUES (63, 14, 'Apa yang dilakukan, Jika Spesifikasi Bahan atau perbedaan lainnya yang ada di Job Ticket di rubah secara manual/tidak sesuai dengan data system?', 'Operator dapat menjelaskan secara flow proses seperti berikut:\na. Operator Flexo/LP akan menginformasikan hal tersebut ke Leader dan PPIC untuk konfirmasi kesesuaian dan alsaan perubahan.\nb. Operator menginfokan kepada tim QC terkait perubahan tersebut un', '0000-00-00', '0000-00-00', '2023-01-23 12:01:51', 'heru', 5);
INSERT INTO `pertanyaan` VALUES (64, 14, 'Pengecekan apa saja yang dilakukan pada dokumen Form Sejarah Proof? Berikan contoh dari Produk yang sedang jalan atau sudah selesai.', 'Operator dapat menjelaskan Critical Point seperti berikut:\na. Spesifikasi Bahan dan CRB yang digunakan sesuai dengan Job Ticket\nb. No. Anliox yang digunakan\nc. Kesesuaian tinta yang digunakan pada tiap nomor anilox', '0000-00-00', '0000-00-00', '2023-01-23 12:00:22', 'heru', 5);
INSERT INTO `pertanyaan` VALUES (65, 15, 'SET UP Tension:\nBagaimana proses set up tension pada mesin? apakah perbedaan jenis bahan mempengaruhi setting tension? apa yang terjadi jika tension terlalu rendah/tinggi?', 'Operator menjelaskan proses set up standard tension pada mesin berdasarkan dari jenis bahan yang digunakan. (Default/Self Adhesive = In 200 Out 220 dan Monofoil/Shrink/InMould = In 80 Out 100).', '0000-00-00', '0000-00-00', '2023-01-23 13:07:10', 'heru', 5);
INSERT INTO `pertanyaan` VALUES (66, 15, 'SET UP Tension:\nApa yang terjadi jika tension terlalu rendah/tinggi?', 'Operator menjelaskan defect jika salah dalam set up tension, yaitu:\n- Bahan menjadi mudah putus\n- Gulungan bahan akan keriput/wrinkle\n- Warna menjadi rusak atau bergaris', '0000-00-00', '0000-00-00', '2023-01-23 13:07:43', 'heru', 5);
INSERT INTO `pertanyaan` VALUES (67, 15, 'Pemasangan Bahan:\nBagaimana Cara Pemasangan Bahan / Roll pada mesin? Bagaimana handling bahan tersebut kedalam mesin?', 'a. Operator menjelaskan cara pemasangan bahan sesui dengan Visual Management Pemasangan Bahan\nb. Operator menggunakan trolly untuk membawa barang keposisi pemasangan dan diangkat ketika pemasangan (Tidak digulingkan dilantai)', '0000-00-00', '0000-00-00', '2023-01-23 13:07:56', 'heru', 5);
INSERT INTO `pertanyaan` VALUES (68, 15, 'Pemasangan Bahan:\nBagaimana cara penyambungan bahan pada saat proses cetak? berapa banyak jumlah sambungan yang diperbolehkan?', 'a. Operator menjelaskan cara penyambungan bahan sesuai dengan Visual Management Penyambungan Bahan\nb. Jumlah sabungan yang diperbolehkan Maximal 3 Sambungan', '0000-00-00', '0000-00-00', '2023-01-23 13:08:11', 'heru', 5);
INSERT INTO `pertanyaan` VALUES (69, 15, 'Pemasangan Bahan:\nJika pemasangan bahan tidak sesuai, apakah anda tau defect yang terjadi apa saja?', 'Operator mengetahui defect yang akan terjadi, yaitu:\n- Sambungan akan mudah putus pada saat proses di finishing\n- Mesin akan mengalami downtime ketika sambungan putus pada saat proses cetak dan / atau finishing', '0000-00-00', '0000-00-00', '2023-01-23 13:08:27', 'heru', 5);
INSERT INTO `pertanyaan` VALUES (70, 15, 'Pemasangan Chamber dan Docter Blade:\nBagaimana standard pengecekan Doctor Blade dan defect apa yang terjadi jika kondisi doctor blade sudah tidak bagus?', 'Pengecekan dialkukan secara visual pada bagian pisau sapuan, jika sudah tidak rata maka doctor blade sudah dalam kondisi \"Aus\". Jika tetap digunakan maka akan menyebabkan defect label bergaris pada label.', '0000-00-00', '0000-00-00', '2023-01-23 13:08:46', 'heru', 5);
INSERT INTO `pertanyaan` VALUES (71, 15, 'Pemasangan Anilox:\nBagaimana cara pemasangan anilox pada mesin?', 'Operator menjelaskan cara pemasangan bahan sesuai dengan Visual Management Pemasangan Anilox dan handling yang dilakukan benar menggunakan 2 tangan', '0000-00-00', '0000-00-00', '2023-01-23 13:08:59', 'heru', 5);
INSERT INTO `pertanyaan` VALUES (72, 15, 'Pemasangan Cylinder Plate:\nPada saat pemasangan plate, apa yang perlu anda perhatikan? apakah anda mengetahui defect apa yang terjadi jika pemasangan plate tidak sesuai?', 'Pada saat pemasangan, Posisi Gear presisi dan bearing masuk kedalam pen cylinder. Jika pemasangan tidak sesuai maka hasil cetakan akan mengalami defect miss register.', '0000-00-00', '0000-00-00', '2023-01-23 13:09:11', 'heru', 5);
INSERT INTO `pertanyaan` VALUES (73, 15, 'Pemasangan Cylinder Die Cut :\nPada saat pemasangan Cylinder Die Cut, apa yang perlu anda perhatikan? apakah anda mengetahui defect apa yang terjadi jika pemasangan plate tidak sesuai?', 'Garis yang terdapat pada cross die cut sejajar dengan cylinder magnetic gear. Jika pemasangan tidak sesuai, makan akan terjadi defect lenght dan / atau width label tidak sesuai dengan artwork', '0000-00-00', '0000-00-00', '2023-01-23 13:09:23', 'heru', 5);
INSERT INTO `pertanyaan` VALUES (74, 15, 'Kalibrasi Unit:\nKapan kalibrasi unit dilakukan dan apa fungsinya kalibrasi unit dilakukan?', 'Kalibrasi dilakukan setiap unit akan digunakan, fungsi dari kalibrasi ini adalah untuk memastikan bahwa perputaran cylinder pada mesin sesuai dan dalam kondisi yang baik.', '0000-00-00', '0000-00-00', '2023-01-23 13:09:40', 'heru', 5);
INSERT INTO `pertanyaan` VALUES (75, 15, 'Penggunaan Lampu UV:\nLakukan pengecekan terhadap jumlah lampu yang digunakan pada saat proses cetak dan cek lifetime Lampu UV', 'Total lampu yang digunakan sesuai dengan jumlah warna yang digunakan dan Lampu UV masih dalam masa lifetime penggunaan', '0000-00-00', '0000-00-00', '2023-01-23 13:09:52', 'heru', 5);
INSERT INTO `pertanyaan` VALUES (76, 15, 'Register Plate:\nApa standard pengecekan register plate pada saat proses cetak?', 'Image yang didapatkan sesuai dengan artwork dan berpatokan pada cross di side bar unit sebelumnya yang menandakan semua plate sudah ter-register.', '0000-00-00', '0000-00-00', '2023-01-23 13:10:06', 'heru', 5);
INSERT INTO `pertanyaan` VALUES (77, 15, 'Colour Matching\nApa standard pengecekan Colour Matching pada saat proses cetak?', 'Warna yang didapatkan sesuai dengan artwork dan berpatokan pada cross di side bar unit sebelumnya.', '0000-00-00', '0000-00-00', '2023-01-23 13:10:21', 'heru', 5);
INSERT INTO `pertanyaan` VALUES (78, 16, 'Apa saja sensor yang disetting diluar dari setting pada monitor dan apa fungsinya?', 'a. Sensor Pembaca Hasil Cetak : Sebagai kamera untuk mendeteksi hasil cetakan yang didapatkan.\nb. Sensor Roller : Sebagai sensor untuk membaca jumlah / quantity label yang terbaca.', '0000-00-00', '0000-00-00', '2023-01-23 13:10:45', 'heru', 5);
INSERT INTO `pertanyaan` VALUES (79, 16, 'Apa saja yang dijadikan patokan untuk setup Master Image?', 'Setup master image berdasarkan pada karakteristik produk, contoh: Logo, Tulisan, Gambar pada label', '0000-00-00', '0000-00-00', '2023-01-23 13:10:57', 'heru', 5);
INSERT INTO `pertanyaan` VALUES (80, 16, 'Apa saja yang pengecekan yang dibaca dan di setting pada mesin AVT?', 'Jumlah penegcekan berdasarkan pada karakteristik dari label tersebut, pengecekannya seperti:\n- Register\n- Spot\n- Streak\n- Color\n- Matrix\n- Die Cut\n- Character\n- Other (Area lain yang ingin dideteksi pada label)\n- Edge', '0000-00-00', '0000-00-00', '2023-01-23 13:11:17', 'heru', 5);
INSERT INTO `pertanyaan` VALUES (81, 16, 'Berapa standard Sensitivitas yang digunakan pada mesin AVT sebagai mesin inspeksi?', 'Standard set up sensivitas pada mesin AVT adalah 6 untuk semua kategori', '0000-00-00', '0000-00-00', '2023-01-23 13:11:29', 'heru', 5);
INSERT INTO `pertanyaan` VALUES (82, 16, 'Apa yang anda lakukan jika defect terbaca pada saat pengecekan AVT?', 'Menempelkan label \"SYNC DEFECT AVT\" pada roll dan Melakukan pencatatan defect yang terbaca pada AVT didalam system CERM untuk informasi pada label SFG di tiap Roll yang mengalami Defect.', '0000-00-00', '0000-00-00', '2023-01-23 13:11:46', 'heru', 5);
INSERT INTO `pertanyaan` VALUES (83, 17, 'Apa fungsi Line Clearance dilakukan pada saat awal proses produksi?', 'Untuk memastikan bahwa kondisi mesin, peralatan dan area yang akan digunakan sudah terbebas dari sisa produksi sebelumnya dan siap untuk digunakan', '0000-00-00', '0000-00-00', '2023-01-23 13:12:26', 'heru', 5);
INSERT INTO `pertanyaan` VALUES (84, 17, 'Apakah anda mengaetahui dampak apa saja yang terjadi jika tidak menjalankan Line Clearance?', 'Beberapa damapak yang terjadi jika tidak menjalankan Line Clearance:\n- Hasil Cetakan Tercampur\n- Kontaminasi terhadap hasil cetakan, baik dari kotoran (debu) ataupun tumpahan tinta\n- Kegagalan dari hasil cetak yang dapat menyebabkan kerugian secara finans', '0000-00-00', '0000-00-00', '2023-01-23 13:12:38', 'heru', 5);
INSERT INTO `pertanyaan` VALUES (85, 17, 'Apakah anda mengetahui alasan mengapa NIPP ROLL wajib untuk selalu dibersihkan?', 'NIPP ROLL dibersihkan untuk menghindari adanya kotoran yang terbawa pada saat proses cetak, hal ini akan berdamapak dengan adanya defect bintik/kotoran pada hasil cetak', '0000-00-00', '0000-00-00', '2023-01-23 13:12:52', 'heru', 5);
INSERT INTO `pertanyaan` VALUES (86, 17, 'Bagaimana standard pengecekan Doctor Blade dan defect apa yang terjadi jika kondisi doctor blade sudah tidak bagus?', 'Pengecekan dialkukan secara visual pada bagian pisau sapuan, jika sudah tidak rata maka doctor blade sudah dalam kondisi \"Aus\". Jika tetap digunakan maka akan menyebabkan defect label bergaris pada label.', '0000-00-00', '0000-00-00', '2023-01-23 13:13:03', 'heru', 5);
INSERT INTO `pertanyaan` VALUES (87, 18, 'Apa saja label yang digunakan untuk penandaan defect?', 'a. Label Merah Awal Core\nb. Label Merah No. 1 \nc. Label Merah No. 2\nd. Label Biru No. 1\ne. Label Biru No. 2\nf. Label Biru Start AVT\ng. Label Biru Snyc Defect AVT', '0000-00-00', '0000-00-00', '2023-01-23 13:15:12', 'heru', 5);
INSERT INTO `pertanyaan` VALUES (88, 18, 'Apa fungsi dari Label Merah dan Kapan anda melakukan penempelan label tersebut?', 'a. Label Merah digunakan sebagai penanda adanya Defect Critical yang harus dibuang pada saat sortir.\nb. Contoh defectnya seperti: Defect ketika Setting, Sambungan, Mesin Mati, Mesin Bermasalah, Tinta Habis', '0000-00-00', '0000-00-00', '2023-01-23 13:15:24', 'heru', 5);
INSERT INTO `pertanyaan` VALUES (89, 18, 'Apa fungsi dari Label Biru dan Kapan anda melakukan penempelan label tersebut?', 'a. Label Biru digunakan sebagai penanda adanya Defect Major-Minor yang harus disortir pada saat slitting.\nb. Contoh defectnya seperti: adanya debu, bercak tinta, lem, miss register, garis, die cut tembus.', '0000-00-00', '0000-00-00', '2023-01-23 13:15:36', 'heru', 5);
INSERT INTO `pertanyaan` VALUES (90, 18, 'Bagaimana Flow yang anda lakukan jika terjadi defect ketika proses cetak sedang berjalan?', 'Operator menjelaskan secara Sistematik, seperti:\na. Operator Menghentikan mesin\nb. Melakukan Pengecekan terhadap sumber masalah\nc. Menginformasikan masalah tersebut ke Field Head / Section Head\nd. Memberikan penandaan sesuai dengan defect yang ditemukan\ne', '0000-00-00', '0000-00-00', '2023-01-23 13:16:10', 'heru', 5);
INSERT INTO `pertanyaan` VALUES (91, 18, 'Inspector melakukan Pengecekan penandaan defect Langsung terhadap Roll yang sudah selesai', 'a. Penandaan Awal Core Ada\nb. Penandaan Label Defect Terdapat 2 (Awal Defect dan Akhir Defect)\nc. Label Start AVT dan / atau Sync Defect AVT ada (Jika Menggunakan AVT)\nd. Contoh defect ditempelkan pada sisi Roll\ne. Data Defect tertera pada CERM', '0000-00-00', '0000-00-00', '2023-01-23 13:16:47', 'heru', 5);
INSERT INTO `pertanyaan` VALUES (92, 26, 'Pemeriksaan apa saja yang dilakukan pada saat awal proses dan dalam proses?', 'Operator dapat menjelaskan cara pengujian yang tertera pada Form LPK (FR-QC-009)\na. Hasil Cetak\nb. Dimensi\nc. Fungsi Barcode (Jika ada pada desain)\nd. Taping Test (Hanya bahan Film)\ne. Die Cut\nf. Hasil Laminating (Peeling Test & Visual Tension)\ng. Varnish', '0000-00-00', '0000-00-00', '2023-01-23 13:17:15', 'heru', 5);
INSERT INTO `pertanyaan` VALUES (93, 26, 'Berapa interval sampling yang digunakan pada saat pemeriksaan in proses?', 'Pemeriksaan berdasarkan dari kecepatan mesin dan dengan menggunakan AVT dan Non-AVT:\nA. Tanpa AVT :\n- Speed 20 - 70 m/min = 10 menit\n- Speed > 70 m/min = 15 menit\nB. Dengan AVT :\n- Sampling DIlakukan setiap 30 menit dan potong 2 UP pada tiap akhir gulunga', '0000-00-00', '0000-00-00', '2023-01-23 13:19:24', 'heru', 5);
INSERT INTO `pertanyaan` VALUES (94, 26, 'Bagaimana metode pemeriksaan untuk bahan Shrink dan In Mold?', 'a. Pemeriksaan Awal Proses : Ambil 2 UP dan bandingkan dengan Buku Standard\nb. Pada Saat Running Mesin : Pengecekan hanya secara visual tanpa pengambilan sampling pada saat mesin jalan\nc. Pada Saat Turun Roll & Akhir Proses : Potong 2 UP dan periksa hasil', '0000-00-00', '0000-00-00', '2023-01-23 13:19:53', 'heru', 5);
INSERT INTO `pertanyaan` VALUES (95, 26, 'Apa yang anda lakukan jika ditemukan ketidaksesuaian pada hasil Die-Cut?', 'a. Stop Mesin\nb. Cek Kondisi Diecut\nc. Cek Kebersihan Magnetic Die Cut dan Die Cutnya\nd. Cek Pressure Die Cut\ne. Cek Posisi Bearing Magnetic', '0000-00-00', '0000-00-00', '2023-01-23 13:20:22', 'heru', 5);
INSERT INTO `pertanyaan` VALUES (96, 26, 'Apa yang anda lakukan jika ditemukan ketidaksesuaian pada hasil Tapping/Rub Test?', 'a. Stop Mesin\nb. Cek Aktifasi Corona\nc. Cek Kondisi Lampu UV (Lifetime / tidak)\nd. Cek Varnis', '0000-00-00', '0000-00-00', '2023-01-23 13:25:37', 'heru', 5);
INSERT INTO `pertanyaan` VALUES (97, 26, 'Apa yang anda lakukan jika ditemukan ketidaksesuaian pada hasil Dyne Test?', 'a. Stop Mesin\nb. Cek Aktifasi Corona\nc. Cek dyne level material awal sebelum corona\nd. Cek Tinta, Ini dilakukan jika area dyne level tidak langsung diatas material', '0000-00-00', '0000-00-00', '2023-01-23 13:26:19', 'heru', 5);
INSERT INTO `pertanyaan` VALUES (98, 26, 'Apa yang anda lakukan jika ditemukan ketidaksesuaian pada hasil Peeling Test?', 'a. Stop Mesin\nb. Cek Aktifasi Corona\nc. Cek Kondisi Lampu UV (Lifetime / tidak)', '0000-00-00', '0000-00-00', '2023-01-23 13:26:32', 'heru', 5);
INSERT INTO `pertanyaan` VALUES (99, 26, 'Apa yang anda lakukan jika ditemukan ketidaksesuaian pada hasil Visual Tension?', 'a. Stop Mesin\nb. Cek Pressure Tension Laminasi\nc. Cek Nip Roll Unit', '0000-00-00', '0000-00-00', '2023-01-23 13:26:44', 'heru', 5);
INSERT INTO `pertanyaan` VALUES (100, 26, 'Apa yang anda lakukan jika ditemukan defect warna pada hasil cetak?', 'a. Stop Mesin\nb. Verifikasi Ulang ke Awal Buku Standard\nc. Lakukan Adjustment / Colour Matching Ulang\nd. Lakukan Pengukuran Sesuai Nilai Standard\ne. Verifikasi bersama operator di Standard Box Lampu untuk Pengecekan Warna', '0000-00-00', '0000-00-00', '2023-01-23 13:26:56', 'heru', 5);

-- ----------------------------
-- Table structure for petugas
-- ----------------------------
DROP TABLE IF EXISTS `petugas`;
CREATE TABLE `petugas`  (
  `id_karyawan` int(6) UNSIGNED ZEROFILL NOT NULL AUTO_INCREMENT,
  `nama` varchar(50) CHARACTER SET latin1 COLLATE latin1_swedish_ci NULL DEFAULT NULL,
  `jabatan` varchar(1) CHARACTER SET latin1 COLLATE latin1_swedish_ci NULL DEFAULT NULL COMMENT '1. Leader 2. OPerator',
  `status` varchar(1) CHARACTER SET latin1 COLLATE latin1_swedish_ci NULL DEFAULT NULL COMMENT '1. Active 2. Not Active',
  PRIMARY KEY (`id_karyawan`) USING BTREE
) ENGINE = InnoDB AUTO_INCREMENT = 48 CHARACTER SET = latin1 COLLATE = latin1_swedish_ci ROW_FORMAT = Compact;

-- ----------------------------
-- Records of petugas
-- ----------------------------
INSERT INTO `petugas` VALUES (000001, 'Warkum', '1', '1');
INSERT INTO `petugas` VALUES (000002, 'Rahmad Dani', '1', '1');
INSERT INTO `petugas` VALUES (000003, 'Aris Trianto', '1', '1');
INSERT INTO `petugas` VALUES (000004, 'Didi Maksudi', '0', '1');
INSERT INTO `petugas` VALUES (000005, 'Rano Marno', '0', '1');
INSERT INTO `petugas` VALUES (000006, 'Ary Setyo Adhy', '0', '1');
INSERT INTO `petugas` VALUES (000007, 'Rusdi Zakaria', '0', '1');
INSERT INTO `petugas` VALUES (000008, 'Iman Firmansyah', '0', '1');
INSERT INTO `petugas` VALUES (000009, 'Pendi', '0', '1');
INSERT INTO `petugas` VALUES (000010, 'Feri M Saifurrochman', '0', '1');
INSERT INTO `petugas` VALUES (000011, 'Wiwit Setiyono', '0', '1');
INSERT INTO `petugas` VALUES (000012, 'Atang Miswandi', '0', '1');
INSERT INTO `petugas` VALUES (000013, 'Asep Saepudin', '0', '1');
INSERT INTO `petugas` VALUES (000014, 'Makhrufin', '0', '1');
INSERT INTO `petugas` VALUES (000015, 'Suwanto', '0', '1');
INSERT INTO `petugas` VALUES (000016, 'Supardi', '0', '1');
INSERT INTO `petugas` VALUES (000017, 'Eko Pusbyantoro', '0', '1');
INSERT INTO `petugas` VALUES (000018, 'Usman Haryono', '0', '1');
INSERT INTO `petugas` VALUES (000019, 'Tasiran Iran', '0', '1');
INSERT INTO `petugas` VALUES (000020, 'Suheli', '0', '1');
INSERT INTO `petugas` VALUES (000021, 'Adi Riyanto', '0', '1');
INSERT INTO `petugas` VALUES (000022, 'Adi Setiawan', '0', '1');
INSERT INTO `petugas` VALUES (000023, 'Apriyanto Budi Santoso', '0', '1');
INSERT INTO `petugas` VALUES (000024, 'Junaetdi SR', '0', '1');
INSERT INTO `petugas` VALUES (000025, 'Endan Dahiri', '0', '1');
INSERT INTO `petugas` VALUES (000026, 'Koiril Anwar', '0', '1');
INSERT INTO `petugas` VALUES (000027, 'Khoirul Anam', '0', '1');
INSERT INTO `petugas` VALUES (000028, 'Aan Arianto', '0', '1');
INSERT INTO `petugas` VALUES (000029, 'Rudi', '0', '1');
INSERT INTO `petugas` VALUES (000030, 'Dimas Febry Setiawan', '0', '1');
INSERT INTO `petugas` VALUES (000031, 'Yadi Supriatna', '0', '1');
INSERT INTO `petugas` VALUES (000032, 'Abdul Latif', '0', '1');
INSERT INTO `petugas` VALUES (000033, 'Fuad Muhtarudin', '0', '1');
INSERT INTO `petugas` VALUES (000034, 'Rizal Faurizal', '0', '1');
INSERT INTO `petugas` VALUES (000035, 'Rizki Ramdani', '0', '1');
INSERT INTO `petugas` VALUES (000036, 'Khasan Nanda FIrmansyah', '0', '1');
INSERT INTO `petugas` VALUES (000037, 'Nurhudin Indrianto', '0', '1');
INSERT INTO `petugas` VALUES (000038, 'Yosep Misbahul Munir', '0', '1');
INSERT INTO `petugas` VALUES (000039, 'Nur Muhammad Adi WIbowo', '0', '1');
INSERT INTO `petugas` VALUES (000040, 'Joko Setya Budi', '0', '1');
INSERT INTO `petugas` VALUES (000041, 'Vito Restu Prasetyo', '0', '1');
INSERT INTO `petugas` VALUES (000042, 'Luthfi Andika Yudistira', '0', '1');
INSERT INTO `petugas` VALUES (000043, 'Fredy Ardiansyah', '0', '1');
INSERT INTO `petugas` VALUES (000044, 'Doni Ragil Rivanto', '0', '1');
INSERT INTO `petugas` VALUES (000045, 'Jupri', '0', '1');
INSERT INTO `petugas` VALUES (000046, 'Soni Ertanto', '0', '1');
INSERT INTO `petugas` VALUES (000047, 'Test', '0', '0');

-- ----------------------------
-- Table structure for point
-- ----------------------------
DROP TABLE IF EXISTS `point`;
CREATE TABLE `point`  (
  `id_point` int NOT NULL AUTO_INCREMENT,
  `description` varchar(255) CHARACTER SET latin1 COLLATE latin1_swedish_ci NULL DEFAULT NULL,
  `id_induk` int NOT NULL,
  PRIMARY KEY (`id_point`, `id_induk`) USING BTREE
) ENGINE = InnoDB AUTO_INCREMENT = 27 CHARACTER SET = latin1 COLLATE = latin1_swedish_ci ROW_FORMAT = Compact;

-- ----------------------------
-- Records of point
-- ----------------------------
INSERT INTO `point` VALUES (1, 'INK - PENYIMPANAN & PERSIAPAN TINTA', 2);
INSERT INTO `point` VALUES (2, 'TOOLING - PERSIAPAN KELENGKAPAN TOOLS', 2);
INSERT INTO `point` VALUES (3, 'PRINTING PROCESS - LINE CLEARANCE', 2);
INSERT INTO `point` VALUES (4, 'PRINTING PROCESS - SETUP MESIN', 2);
INSERT INTO `point` VALUES (5, 'PRINTING PROCESS - SETUP AVT', 2);
INSERT INTO `point` VALUES (6, 'PRINTING PROCESS - DEFECT HANDLING', 2);
INSERT INTO `point` VALUES (7, 'PRINTING PROCESS - PEMERIKSAAN KUALITAS', 2);
INSERT INTO `point` VALUES (8, 'INK - PENERIMAAN DAN PENYIMPANAN TINTA', 3);
INSERT INTO `point` VALUES (9, 'INK - PERSIAPAN TINTA', 3);
INSERT INTO `point` VALUES (10, 'TOOLING - PREPARATION DOKUMEN', 4);
INSERT INTO `point` VALUES (11, 'TOOLING - PERSIAPAN KELENGKAPAN TOOLS', 4);
INSERT INTO `point` VALUES (12, 'TOOLING - PENCUCIAN', 4);
INSERT INTO `point` VALUES (13, 'N/A', 4);
INSERT INTO `point` VALUES (14, 'DOKUMEN ACUAN KERJA - PRA CETAK', 5);
INSERT INTO `point` VALUES (15, 'METODE KERJA - SETUP MESIN', 5);
INSERT INTO `point` VALUES (16, 'METODE KERJA - SETUP AVT', 5);
INSERT INTO `point` VALUES (17, 'METODE KERJA - LINE CLEARANCE', 5);
INSERT INTO `point` VALUES (18, 'METODE KERJA - DEFECT HANDLING', 5);
INSERT INTO `point` VALUES (19, 'Sliting', 1);
INSERT INTO `point` VALUES (20, 'Cutting & schober', 1);
INSERT INTO `point` VALUES (21, 'Seaming', 1);
INSERT INTO `point` VALUES (22, 'Sortir roll', 1);
INSERT INTO `point` VALUES (23, 'Packing Roll', 1);
INSERT INTO `point` VALUES (24, 'Packing sheet', 1);
INSERT INTO `point` VALUES (25, 'DCM QR Code', 1);
INSERT INTO `point` VALUES (26, 'METODE KERJA - PEMERIKSAAN KUALITAS', 5);

SET FOREIGN_KEY_CHECKS = 1;
