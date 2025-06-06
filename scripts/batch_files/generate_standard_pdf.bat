@echo off
REM Ghali Consultants - Standard Template PDF Generator
REM Quick generation using unified system

echo ========================================
echo   GHALI CONSULTANTS - STANDARD PDF
echo ========================================

cd /d "D:\R1\Jupiter Notebook"

REM Activate virtual environment if it exists
if exist "venv\Scripts\activate.bat" (
    echo Activating virtual environment...
    call venv\Scripts\activate.bat
)

REM Generate Standard PDF
echo Generating Standard template PDF...
python scripts/pdf_generator_system.py --template standard --length 8.0 --dead-load 20.0 --live-load 25.0 --project-id GC-STD-2025

echo.
echo ========================================
echo   PDF GENERATION COMPLETE
echo ========================================

pause 