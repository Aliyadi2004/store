-- phpMyAdmin SQL Dump
-- version 5.2.1
-- https://www.phpmyadmin.net/
--
-- Host: 127.0.0.1
-- Generation Time: Oct 19, 2024 at 10:26 AM
-- Server version: 10.4.32-MariaDB
-- PHP Version: 8.2.12

SET SQL_MODE = "NO_AUTO_VALUE_ON_ZERO";
START TRANSACTION;
SET time_zone = "+00:00";


/*!40101 SET @OLD_CHARACTER_SET_CLIENT=@@CHARACTER_SET_CLIENT */;
/*!40101 SET @OLD_CHARACTER_SET_RESULTS=@@CHARACTER_SET_RESULTS */;
/*!40101 SET @OLD_COLLATION_CONNECTION=@@COLLATION_CONNECTION */;
/*!40101 SET NAMES utf8mb4 */;

--
-- Database: `aybeyrag`
--

-- --------------------------------------------------------

--
-- Table structure for table `anbar`
--

CREATE TABLE `anbar` (
  `ID` int(127) NOT NULL,
  `userID` varchar(127) CHARACTER SET utf32 COLLATE utf32_persian_ci NOT NULL,
  `UserName` varchar(127) CHARACTER SET utf32 COLLATE utf32_persian_ci NOT NULL,
  `Phonumber` varchar(127) CHARACTER SET utf32 COLLATE utf32_persian_ci NOT NULL,
  `Adress` varchar(127) CHARACTER SET utf32 COLLATE utf32_persian_ci NOT NULL,
  `PruductID` varchar(127) CHARACTER SET utf32 COLLATE utf32_persian_ci NOT NULL,
  `Produckt` varchar(127) CHARACTER SET utf32 COLLATE utf32_persian_ci NOT NULL,
  `SellPrice` int(127) NOT NULL,
  `Count` int(127) NOT NULL,
  `Datei` varchar(127) CHARACTER SET utf32 COLLATE utf32_persian_ci NOT NULL,
  `GamPrice` int(127) NOT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_general_ci;

--
-- Dumping data for table `anbar`
--

INSERT INTO `anbar` (`ID`, `userID`, `UserName`, `Phonumber`, `Adress`, `PruductID`, `Produckt`, `SellPrice`, `Count`, `Datei`, `GamPrice`) VALUES
(41, '37391', 'Aliyadi', '09145888580', 'maralan', '65593', 'خیار', 24000, 10, '1401', 240000),
(43, '53461', 'امیر حیسن', '09584955852', 'فقیتغفبرغع', '78688', 'نوتلا', 64153, 930, '2014', 59662290),
(44, '74582', 'قلی یدی', '09141001369', 'ذلغعتلعغ', '48492', 'موز', 12000, 500, '1300', 6000000),
(46, '74582', 'قلی یدی', '09141001369', 'ذلغعتلعغ', '16936', 'کیک', 12, 298, '555', 3576);

-- --------------------------------------------------------

--
-- Table structure for table `cg`
--

CREATE TABLE `cg` (
  `Id` int(127) NOT NULL,
  `ProductID` int(127) NOT NULL,
  `Product` varchar(127) CHARACTER SET utf32 COLLATE utf32_persian_ci NOT NULL,
  `BuyPrice` int(127) NOT NULL,
  `SelePrice` int(127) NOT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_general_ci;

--
-- Dumping data for table `cg`
--

INSERT INTO `cg` (`Id`, `ProductID`, `Product`, `BuyPrice`, `SelePrice`) VALUES
(97658, 48492, 'موز', 10000, 12000),
(97659, 65593, 'خیار', 20000, 24000),
(97660, 78688, 'نوتلا', 53461, 64153),
(97661, 39589, 'انبه', 100, 120),
(97662, 16936, 'کیک', 10, 12);

-- --------------------------------------------------------

--
-- Table structure for table `cpr`
--

CREATE TABLE `cpr` (
  `Id` int(127) NOT NULL,
  `Userid` int(127) NOT NULL,
  `BuyersName` varchar(127) CHARACTER SET utf32 COLLATE utf32_persian_ci NOT NULL,
  `PhoneNumber` varchar(127) CHARACTER SET utf32 COLLATE utf32_persian_ci NOT NULL,
  `Adress` varchar(127) CHARACTER SET utf32 COLLATE utf32_persian_ci NOT NULL,
  `Dati` varchar(127) CHARACTER SET utf16 COLLATE utf16_persian_ci NOT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_general_ci;

--
-- Dumping data for table `cpr`
--

INSERT INTO `cpr` (`Id`, `Userid`, `BuyersName`, `PhoneNumber`, `Adress`, `Dati`) VALUES
(23, 44715, 'rdyh', 'hgcgh', 'hvhg', 'hgfcgfc'),
(24, 71868, 'yeabchbcs', '095488', 'uaywc', '1400/8/5'),
(27, 37391, 'Aliyadi', '09145888580', 'maralan', '2004/5/14'),
(28, 43785, 'yashar ', '01433360634', 'darvazeh', '2004/1/1'),
(29, 56142, 'ansar', '088888', 'valeasr', '2003/3/3'),
(30, 74582, 'قلی یدی', '09141001369', 'ذلغعتلعغ', '10215'),
(31, 53461, 'امیر حیسن', '09584955852', 'فقیتغفبرغع', '10.5'),
(32, 78377, 'یاشار', '10203040', 'اضتزذباصث', '2003');

-- --------------------------------------------------------

--
-- Table structure for table `historysales`
--

CREATE TABLE `historysales` (
  `Id` varchar(12) NOT NULL,
  `Product Code` varchar(20) NOT NULL,
  `Produckt` varchar(20) NOT NULL,
  `price` varchar(30) NOT NULL,
  `count` varchar(20) NOT NULL,
  `totalprice` varchar(20) NOT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_general_ci;

--
-- Dumping data for table `historysales`
--

INSERT INTO `historysales` (`Id`, `Product Code`, `Produckt`, `price`, `count`, `totalprice`) VALUES
('15', '48492', 'موز', '12000', '15', '180000'),
('16', '65593', 'خیار', '24000', '50', '1200000'),
('17', '78688', 'نوتلا', '64153', '', '0'),
('18', '78688', 'نوتلا', '64153', '100', '6415300'),
('20', '48492', 'موز', '12000', '50', '600000'),
('21', '78688', 'نوتلا', '64153', '50', '3207650'),
('22', '48492', 'موز', '12000', '50', '600000'),
('23', '65593', 'خیار', '24000', '100', '2400000'),
('24', '78688', 'نوتلا', '64153', '1', '64153'),
('25', '16936', 'کیک', '12', '1', '12'),
('26', '78688', 'نوتلا', '64153', '8', '513224'),
('27', '48492', 'موز', '12000', '8', '96000'),
('28', '65593', 'خیار', '24000', '8', '192000'),
('29', '16936', 'کیک', '12', '8', '96'),
('30', '78688', 'نوتلا', '64153', '100', '6415300'),
('31', '78688', 'نوتلا', '64153', '60', '3849180'),
('32', '78688', 'نوتلا', '64153', '10', '641530'),
('33', '78688', 'نوتلا', '64153', '10', '641530'),
('34', '78688', 'نوتلا', '64153', '20', '1283060'),
('35', '78688', 'نوتلا', '64153', '20', '1283060'),
('36', '78688', 'نوتلا', '64153', '50', '3207650'),
('37', '78688', 'نوتلا', '64153', '20', '1283060'),
('38', '16936', 'کیک', '12', '2', '24'),
('39', '16936', 'کیک', '12', '200', '2400'),
('40', '16936', 'کیک', '12', '500', '6000'),
('41', '78688', 'نوتلا', '64153', '50', '3207650'),
('42', '65593', 'خیار', '24000', '10', '240000');

-- --------------------------------------------------------

--
-- Table structure for table `sales`
--

CREATE TABLE `sales` (
  `ID` int(127) NOT NULL,
  `ProductCode` varchar(127) CHARACTER SET utf32 COLLATE utf32_persian_ci NOT NULL,
  `ProductName` varchar(127) CHARACTER SET utf32 COLLATE utf32_persian_ci NOT NULL,
  `Price` int(127) NOT NULL,
  `Count` int(127) NOT NULL,
  `TotalPrice` int(127) NOT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_general_ci;

--
-- Dumping data for table `sales`
--

INSERT INTO `sales` (`ID`, `ProductCode`, `ProductName`, `Price`, `Count`, `TotalPrice`) VALUES
(43, '65593', 'خیار', 24000, 10, 240000);

--
-- Indexes for dumped tables
--

--
-- Indexes for table `anbar`
--
ALTER TABLE `anbar`
  ADD PRIMARY KEY (`ID`);

--
-- Indexes for table `cg`
--
ALTER TABLE `cg`
  ADD PRIMARY KEY (`Id`);

--
-- Indexes for table `cpr`
--
ALTER TABLE `cpr`
  ADD PRIMARY KEY (`Id`);

--
-- Indexes for table `sales`
--
ALTER TABLE `sales`
  ADD PRIMARY KEY (`ID`);

--
-- AUTO_INCREMENT for dumped tables
--

--
-- AUTO_INCREMENT for table `anbar`
--
ALTER TABLE `anbar`
  MODIFY `ID` int(127) NOT NULL AUTO_INCREMENT, AUTO_INCREMENT=50;

--
-- AUTO_INCREMENT for table `cg`
--
ALTER TABLE `cg`
  MODIFY `Id` int(127) NOT NULL AUTO_INCREMENT, AUTO_INCREMENT=97663;

--
-- AUTO_INCREMENT for table `cpr`
--
ALTER TABLE `cpr`
  MODIFY `Id` int(127) NOT NULL AUTO_INCREMENT, AUTO_INCREMENT=35;

--
-- AUTO_INCREMENT for table `sales`
--
ALTER TABLE `sales`
  MODIFY `ID` int(127) NOT NULL AUTO_INCREMENT, AUTO_INCREMENT=44;
COMMIT;

/*!40101 SET CHARACTER_SET_CLIENT=@OLD_CHARACTER_SET_CLIENT */;
/*!40101 SET CHARACTER_SET_RESULTS=@OLD_CHARACTER_SET_RESULTS */;
/*!40101 SET COLLATION_CONNECTION=@OLD_COLLATION_CONNECTION */;
