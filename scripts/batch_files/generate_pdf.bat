@echo off
REM Ghali Consultants - PDF Generator
REM Quick execution script

echo.
echo ================================
echo  GHALI CONSULTANTS PDF GENERATOR
echo ================================

REM Activate virtual environment if it exists
if exist "venv\Scripts\activate.bat" (
    echo Activating virtual environment...
    call venv\Scripts\activate.bat
)

REM Generate PDF with default 8m beam
echo Generating professional calculation sheet...
python scripts\ghali_pdf_generator.py --length 8.0 --dead-load 20.0 --live-load 25.0

echo.
echo Complete! Check output folder for PDF.
pause 