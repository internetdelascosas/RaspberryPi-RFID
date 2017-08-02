-- phpMyAdmin SQL Dump
-- version 3.4.11.1deb2+deb7u8
-- http://www.phpmyadmin.net
--
-- Servidor: localhost
-- Tiempo de generación: 03-08-2017 a las 00:16:28
-- Versión del servidor: 5.5.55
-- Versión de PHP: 5.4.45-0+deb7u8

SET SQL_MODE="NO_AUTO_VALUE_ON_ZERO";
SET time_zone = "+00:00";

--
-- Base de datos: `accesscontrol`
--

-- --------------------------------------------------------

--
-- Estructura de tabla para la tabla `lectorRFID`
--

CREATE TABLE IF NOT EXISTS `lectorRFID` (
  `id` bigint(20) NOT NULL AUTO_INCREMENT,
  `nombre` varchar(200) NOT NULL,
  `uid` varchar(16) NOT NULL,
  PRIMARY KEY (`id`),
  UNIQUE KEY `uid` (`uid`)
) ENGINE=InnoDB  DEFAULT CHARSET=utf8 AUTO_INCREMENT=2 ;

--
-- Volcado de datos para la tabla `lectorRFID`
--

INSERT INTO `lectorRFID` (`id`, `nombre`, `uid`) VALUES
(1, 'Jose Zorrilla', '136.4.78.91');
