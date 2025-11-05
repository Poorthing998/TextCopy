@echo off
REM TextCopy Installation Script for Windows

echo ==================================
echo TextCopy Installation Script
echo ==================================
echo.

REM Check for Python
python --version >nul 2>&1
if %errorlevel% neq 0 (
    echo X Python is not installed or not in PATH.
    echo Please install Python 3.7 or higher from python.org
    echo Make sure to check "Add Python to PATH" during installation.
    pause
    exit /b 1
)

echo [OK] Python is installed
python --version

REM Check for pip
pip --version >nul 2>&1
if %errorlevel% neq 0 (
    echo X pip is not installed.
    echo Please reinstall Python with pip included.
    pause
    exit /b 1
)

echo [OK] pip is installed
echo.

REM Install dependencies
echo Installing dependencies...
pip install -r requirements.txt

if %errorlevel% eq 0 (
    echo [OK] Dependencies installed successfully
) else (
    echo X Failed to install dependencies
    pause
    exit /b 1
)

echo.
echo ==================================
echo [OK] Installation Complete!
echo ==================================
echo.
echo To start TextCopy, run:
echo   python src\textcopy.py
echo.
echo Or use the launcher:
echo   python run.py
echo.
echo Or double-click run.py in File Explorer
echo.
echo For quick start guide, see QUICKSTART.md
echo.
pause
