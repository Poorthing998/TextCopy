@echo off
REM TextCopy launcher for Windows
REM This runs TextCopy as a Python module

echo Starting TextCopy...
echo.

REM Run as a module from the parent directory
python -m src.textcopy %*

REM If that fails, try the alternative method
if %errorlevel% neq 0 (
    echo.
    echo Failed to start with module method, trying alternative...
    python src\textcopy.py %*
)
