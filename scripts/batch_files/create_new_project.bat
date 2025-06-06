@echo off
REM Ghali Consultants - New Project Creator
REM Interactive project creation

echo ========================================
echo   GHALI CONSULTANTS - NEW PROJECT
echo ========================================

cd /d "D:\R1\Jupiter Notebook"

REM Activate virtual environment if it exists
if exist "venv\Scripts\activate.bat" (
    echo Activating virtual environment...
    call venv\Scripts\activate.bat
)

REM Get project details
set /p PROJECT_ID="Enter Project ID (e.g., GC-2025-045): "
set /p DESCRIPTION="Enter Description (optional): "
set /p LENGTH="Enter Beam Length in meters (default 8.0): "
set /p DEAD_LOAD="Enter Dead Load in kN/m (default 20.0): "
set /p LIVE_LOAD="Enter Live Load in kN/m (default 25.0): "

REM Set defaults if empty
if "%LENGTH%"=="" set LENGTH=8.0
if "%DEAD_LOAD%"=="" set DEAD_LOAD=20.0
if "%LIVE_LOAD%"=="" set LIVE_LOAD=25.0

echo.
echo Creating new calculation notebook...

REM Create new calculation
if "%DESCRIPTION%"=="" (
    python scripts/create_new_calculation.py %PROJECT_ID% --length %LENGTH% --dead-load %DEAD_LOAD% --live-load %LIVE_LOAD%
) else (
    python scripts/create_new_calculation.py %PROJECT_ID% --description "%DESCRIPTION%" --length %LENGTH% --dead-load %DEAD_LOAD% --live-load %LIVE_LOAD%
)

echo.
echo ========================================
echo   PROJECT CREATED SUCCESSFULLY
echo ========================================
echo.
echo Next steps:
echo 1. Open Jupyter: jupyter notebook
echo 2. Edit your calculation notebook
echo 3. Generate PDF: Use batch files or command line
echo.

pause 