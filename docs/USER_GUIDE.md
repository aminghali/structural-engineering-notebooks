# User Guide
## Professional Concrete Beam Design System

### Table of Contents
1. [Quick Start](#quick-start)
2. [Installation](#installation)
3. [Using the Main Notebook](#using-the-main-notebook)
4. [Generating PDF Reports](#generating-pdf-reports)
5. [Customizing Calculations](#customizing-calculations)
6. [Troubleshooting](#troubleshooting)
7. [Advanced Features](#advanced-features)

---

## Quick Start

### 1. First-Time Setup
```bash
# Run the automated setup script
.\scripts\Setup_Environment.ps1

# Or install manually
pip install -r requirements.txt
```

### 2. Open the Main Notebook
```bash
jupyter notebook notebooks/professional_concrete_design_aci318.ipynb
```

### 3. Generate Professional PDF
```bash
# One-click generation
.\scripts\Quick_PDF_Generator.bat

# Or use the full script
.\scripts\Generate_Professional_PDF.ps1
```

---

## Installation

### System Requirements
- **Operating System**: Windows 10/11, macOS 10.14+, or Linux
- **Python**: Version 3.8 or higher
- **Memory**: 2GB RAM minimum (4GB recommended)
- **Storage**: 100MB free space

### Automated Installation
The easiest way to set up the environment:

```powershell
# Run the setup script (Windows)
.\scripts\Setup_Environment.ps1

# This will:
# - Check Python installation
# - Create virtual environment
# - Install all dependencies
# - Verify installation
```

### Manual Installation
If you prefer manual setup:

```bash
# 1. Create virtual environment (recommended)
python -m venv venv
venv\Scripts\activate  # Windows
# source venv/bin/activate  # macOS/Linux

# 2. Install core dependencies
pip install jupyter handcalcs forallpeople numpy matplotlib nbconvert

# 3. Install optional PDF dependencies
pip install weasyprint pdfkit nbconvert[webpdf]

# 4. Verify installation
jupyter --version
python -c "import handcalcs, forallpeople; print('Ready!')"
```

---

## Using the Main Notebook

### Opening the Notebook
1. Navigate to the project directory
2. Run: `jupyter notebook notebooks/professional_concrete_design_aci318.ipynb`
3. Your browser will open with the calculation sheet

### Notebook Structure
The notebook is organized like a professional calculation sheet:

#### 1. Project Information
- Project details and engineer information
- Calculation date and revision tracking
- ACI 318-19 code references

#### 2. Input Parameters
```python
# Beam Geometry
beam_width = 300 * mm      # Beam width
beam_depth = 600 * mm      # Total depth
clear_cover = 40 * mm      # Clear cover to reinforcement

# Material Properties
concrete_strength = 25 * MPa    # f'c
steel_yield = 420 * MPa         # fy
elastic_modulus = 200 * GPa     # Es

# Loading
dead_load = 15 * kN/m      # Dead load
live_load = 20 * kN/m      # Live load
span_length = 6.0 * m      # Clear span
```

#### 3. Calculations
Each calculation cell shows:
- **Symbolic equations** (LaTeX rendered)
- **Numeric substitutions** 
- **Final results** with proper units
- **ACI section references**

#### 4. Results Summary
- Design verification status
- Required reinforcement
- Safety factors and ratios
- Professional recommendations

### Running Calculations
1. **Modify Input Parameters**: Edit the input cells with your project values
2. **Execute Cells**: Run cells sequentially (Shift+Enter)
3. **Review Results**: Check calculations and design verification
4. **Generate Report**: Use PDF generation tools for documentation

---

## Generating PDF Reports

### Method 1: One-Click Generation (Recommended)
```bash
# Double-click or run from command line
.\scripts\Quick_PDF_Generator.bat
```

This automatically:
- Executes the notebook
- Generates professional PDF
- Opens the result
- Saves to `reports/` folder

### Method 2: Advanced PDF Generation
```powershell
# Full control with options
.\scripts\Generate_Professional_PDF.ps1 -InstallDependencies -OpenAfterGeneration
```

Options:
- `-InstallDependencies`: Install PDF tools if missing
- `-OpenAfterGeneration`: Open PDF when complete
- `-Verbose`: Show detailed progress

### Method 3: Manual Generation
```bash
# Convert notebook to PDF directly
jupyter nbconvert --to pdf --execute notebooks/professional_concrete_design_aci318.ipynb --output reports/My_Report.pdf
```

### PDF Features
Generated reports include:
- **Professional Header**: Project information and engineer details
- **ACI Compliance**: Section references and code requirements
- **LaTeX Equations**: Beautiful mathematical rendering
- **Engineering Precision**: 4-decimal accuracy throughout
- **Professional Format**: Industry-standard calculation sheet layout

---

## Customizing Calculations

### Modifying Input Parameters
The notebook uses a modular design for easy customization:

```python
# Example: Different beam size
beam_width = 400 * mm      # Change from 300mm to 400mm
beam_depth = 700 * mm      # Change from 600mm to 700mm

# Example: Different materials
concrete_strength = 30 * MPa    # Higher strength concrete
steel_yield = 500 * MPa         # Higher grade steel

# Example: Different loading
dead_load = 20 * kN/m      # Heavier dead load
live_load = 25 * kN/m      # Heavier live load
```

### Adding Custom Calculations
You can extend the notebook with additional calculations:

```python
# Example: Add deflection check
%%render
# Additional deflection calculation
delta_max = span_length / 250  # ACI 318-19 Table 7.3.1.1
delta_actual = 5 * total_load * span_length**4 / (384 * E_eff * I_eff)
deflection_ratio = delta_actual / delta_max
```

### Creating Project Templates
1. Modify the main notebook for your typical projects
2. Save as a new template (e.g., `my_template.ipynb`)
3. Update the PDF generation script to use your template

---

## Troubleshooting

### Common Issues

#### 1. Notebook Won't Open
**Problem**: Jupyter command not found
**Solution**: 
```bash
# Ensure Jupyter is installed
pip install jupyter notebook

# Check installation
jupyter --version
```

#### 2. Package Import Errors
**Problem**: `ModuleNotFoundError: No module named 'handcalcs'`
**Solution**:
```bash
# Install missing packages
pip install handcalcs forallpeople

# Or run full setup
.\scripts\Setup_Environment.ps1
```

#### 3. PDF Generation Fails
**Problem**: PDF conversion errors
**Solutions**:
```bash
# Try different methods
.\scripts\Generate_Professional_PDF.ps1 -InstallDependencies

# Manual HTML generation (always works)
jupyter nbconvert --to html --execute notebooks/professional_concrete_design_aci318.ipynb
```

#### 4. Unit Handling Issues
**Problem**: Unit conversion errors
**Solution**:
```python
# Always use .magnitude for numeric values
force_value = force_with_units.magnitude  # Extract numeric value
result = calculation(force_value) * kN    # Apply units to result
```

#### 5. Equation Rendering Problems
**Problem**: LaTeX equations not displaying
**Solution**:
```python
# Ensure handcalcs is properly imported
import handcalcs.render

# Use %%render magic command
%%render
# Your calculations here
```

### Getting Help

#### 1. Check Documentation
- `README.md`: Project overview and quick start
- `docs/PROJECT_INFO.md`: Technical details
- `docs/CHANGELOG.md`: Version history and updates

#### 2. Verify Installation
```bash
# Run diagnostic script
.\scripts\Setup_Environment.ps1 -Verbose

# Check package versions
pip list | findstr "handcalcs\|forallpeople\|jupyter"
```

#### 3. Test Environment
```python
# Test in Python console
import handcalcs.render
import forallpeople as u
u.environment('structural')
print("Environment ready!")
```

---

## Advanced Features

### 1. Custom Unit Systems
```python
# Create custom unit environment
import forallpeople as u
u.environment('structural', top_level=True)

# Define custom units
ksi = u.kilo * u.psi
ksf = u.kilo * u.psf
```

### 2. Batch Processing
Create scripts to process multiple designs:

```python
# Example: Multiple beam sizes
beam_sizes = [(300, 600), (400, 700), (500, 800)]
for width, depth in beam_sizes:
    # Run calculations
    # Generate individual reports
```

### 3. Integration with CAD
Export results for use in CAD software:

```python
# Export reinforcement details
reinforcement_data = {
    'top_bars': top_reinforcement,
    'bottom_bars': bottom_reinforcement,
    'stirrups': shear_reinforcement
}
# Save to JSON or CSV for CAD import
```

### 4. Custom Report Templates
Modify the LaTeX template for different report formats:

1. Edit `scripts/Generate_Professional_PDF.ps1`
2. Customize the LaTeX template section
3. Add company logos, headers, footers
4. Modify calculation sheet layout

### 5. Database Integration
Connect to material property databases:

```python
# Example: Load material properties from database
import sqlite3
conn = sqlite3.connect('materials.db')
concrete_props = conn.execute('SELECT * FROM concrete WHERE grade=?', (25,)).fetchone()
```

---

## Best Practices

### 1. Project Organization
- Keep input parameters in clearly marked cells
- Use descriptive variable names
- Add comments for complex calculations
- Save different versions for different projects

### 2. Quality Control
- Always verify results manually for critical calculations
- Check units throughout calculations
- Review ACI section references
- Validate against hand calculations

### 3. Documentation
- Update project information for each calculation
- Add notes for assumptions and limitations
- Include sketches and diagrams where helpful
- Maintain calculation revision history

### 4. Professional Standards
- Use 4-decimal precision for engineering accuracy
- Include proper ACI 318-19 section references
- Follow professional calculation sheet format
- Maintain consistent unit systems

---

**User Guide Version**: 1.0  
**Last Updated**: June 2025  
**For Technical Support**: See docs/ folder for additional resources 