@echo off

echo ComicMetadataHub Test Runner

set PROJECT_ROOT=%~dp0

set PYTHON=%PROJECT_ROOT%runtime\python\python.exe


if not exist "%PYTHON%" (
    echo Embedded Python not found.
    echo Expected:
    echo %PYTHON%
    pause
    exit /b 1
)


"%PYTHON%" "%PROJECT_ROOT%run_tests.py"

pause