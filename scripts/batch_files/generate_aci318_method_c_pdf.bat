@echo off
REM ===================================================================
REM GHALI CONSULTANTS - ACI 318-19 METHOD C PDF GENERATOR
REM Academic Cambridge-style PDF generation for column design
REM ===================================================================

echo.
echo ===============================================================
echo     GHALI CONSULTANTS - ACI 318-19 Method C PDF Generator
echo ===============================================================
echo.

REM Change to project root directory
cd /d "%~dp0\.."

REM Activate virtual environment if it exists
if exist "venv\Scripts\activate.bat" (
    echo 🐍 Activating virtual environment...
    call venv\Scripts\activate.bat
    echo    ✓ Virtual environment activated
    echo.
) else (
    echo ⚠️  Virtual environment not found - using system Python
    echo.
)

REM Run the ACI 318-19 Method C PDF generator
echo 🏗️  Generating ACI 318-19 Method C Column Design PDF...
python scripts\aci318_method_c_pdf_generator.py %*

REM Check if PDF was generated successfully
if exist "output\ACI318_Method_C_Column_Design.pdf" (
    echo.
    echo ✅ SUCCESS! PDF generated successfully
    echo 📁 Location: output\ACI318_Method_C_Column_Design.pdf
    echo.
    echo 📋 To open the PDF:
    echo    start output\ACI318_Method_C_Column_Design.pdf
    echo.
) else (
    echo.
    echo ❌ PDF generation failed
    echo 💡 Check the error messages above
    echo.
)

echo 🎓 ACI 318-19 Method C PDF Features:
echo    • Academic two-column Cambridge style
echo    • Complete ACI 318-19 Section 6.6 compliance
echo    • Critical buckling direction analysis
echo    • Method comparison (conservative vs refined)
echo    • Professional engineering calculations
echo    • Column cross-section diagrams
echo.

pause 