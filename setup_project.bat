@echo off
title ComicMetadataHub - Initial Project Setup

echo.
echo ===========================================
echo   ComicMetadataHub Project Setup
echo ===========================================
echo.

REM Change to the directory where this script lives
cd /d "%~dp0"

echo Creating project folders...

mkdir "docs\Metadata" 2>nul

mkdir "src\hub\models" 2>nul
mkdir "src\hub\merge" 2>nul
mkdir "src\hub\rules" 2>nul
mkdir "src\hub\io" 2>nul
mkdir "src\hub\providers" 2>nul

mkdir "tests\models" 2>nul
mkdir "tests\merge" 2>nul
mkdir "tests\providers" 2>nul
mkdir "tests\io" 2>nul

echo.

echo Creating __init__.py files...

type nul > "src\hub\__init__.py"
type nul > "src\hub\models\__init__.py"
type nul > "src\hub\merge\__init__.py"
type nul > "src\hub\rules\__init__.py"
type nul > "src\hub\io\__init__.py"
type nul > "src\hub\providers\__init__.py"

type nul > "tests\__init__.py"
type nul > "tests\models\__init__.py"
type nul > "tests\merge\__init__.py"
type nul > "tests\providers\__init__.py"
type nul > "tests\io\__init__.py"

echo.

echo ===========================================
echo Setup Complete
echo ===========================================
echo.

tree src
echo.

pause