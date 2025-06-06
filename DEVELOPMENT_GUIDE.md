# Development Guide - Structural Engineering Jupiter Notebooks

## 🚀 Getting Started

### 1. Environment Setup

#### Virtual Environment Activation
```bash
# Windows
venv\Scripts\activate

# Verify activation
python --version
pip --version
```

#### Install Dependencies
```bash
# Install all required packages
pip install -r requirements.txt

# Verify handcalcs installation
python -c "import handcalcs; print('✅ handcalcs ready')"
```

#### Jupyter Setup
```bash
# Start Jupyter Lab
jupyter lab

# Or Jupyter Notebook
jupyter notebook
```

### 2. Project Initialization
```bash
# Initialize git (if not done)
git init
git add .
git commit -m "Initial commit: Professional structural engineering setup"
```

## 📓 Creating New Calculations

### 1. Using Template Notebook

#### Copy Template
```bash
# Copy template to appropriate folder
cp notebooks/templates/structural_calculation_template.ipynb notebooks/beam_design/2025-06-06_beam_design_project_name_v1.ipynb
```

#### Customize Template
1. Update project information in header cell
2. Modify input parameters section
3. Add specific calculations for your project
4. Update material properties and design codes

### 2. Using Creation Script
```bash
# Create new beam calculation
python scripts/utilities/create_new_calculation.py GC-2025-047 --description "Office Building Beam" --type beam

# Create new column calculation  
python scripts/utilities/create_new_calculation.py GC-2025-048 --description "High-rise Column" --type column
```

## 🔧 Development Workflow

### 1. Standard Development Process

#### Step 1: Create Calculation
```bash
# Start from template
cp notebooks/templates/structural_calculation_template.ipynb notebooks/beam_design/new_calculation.ipynb
```

#### Step 2: Develop in Jupyter
1. Open notebook in Jupyter Lab
2. Configure handcalcs for professional output
3. Implement calculations step by step
4. Test with simple cases first
5. Add professional plots and diagrams

#### Step 3: Generate Professional Report
```bash
# Generate PDF report
python scripts/pdf_generators/pdf_generator_system.py --notebook notebooks/beam_design/new_calculation.ipynb --template cambridge
```

#### Step 4: Review and Archive
1. Review calculations and outputs
2. Move to appropriate output folder
3. Commit changes to git
4. Archive if calculation is complete

### 2. Professional Calculation Standards

#### Handcalcs Setup
```python
# Standard imports for all notebooks
import numpy as np
import matplotlib.pyplot as plt
import handcalcs.render
from handcalcs import handcalc

# Configure handcalcs
%load_ext handcalcs.render

# Professional matplotlib settings
plt.style.use('default')
plt.rcParams.update({
    'font.size': 10,
    'axes.titlesize': 12,
    'figure.dpi': 300,
    'savefig.dpi': 300
})
```

#### Variable Naming Convention
```python
# Good examples
f_c_prime = 25.0    # Concrete compressive strength, MPa
f_y = 420.0         # Steel yield strength, MPa
M_u = 150.0         # Ultimate moment, kN⋅m
A_s_req = 1200.0    # Required steel area, mm²

# Include units in comments
length = 8.0        # Beam length, m
width = 300         # Beam width, mm
```

#### Professional Calculations
```python
%%render
# Use handcalcs decorator for professional output
@handcalc()
def calculate_moment_capacity(f_c, f_y, b, d, A_s):
    """Calculate moment capacity per ACI 318-19"""
    a = A_s * f_y / (0.85 * f_c * b)  # Depth of compression block
    M_n = A_s * f_y * (d - a/2)       # Nominal moment capacity
    return M_n, a
```

## 🎨 Professional Plotting

### 1. Structural Diagrams
```python
import matplotlib.pyplot as plt
from scripts.utilities.structural_plotting import plot_beam_diagram, plot_moment_diagram

# Create professional beam diagram
fig, (ax1, ax2, ax3) = plt.subplots(3, 1, figsize=(12, 8))

# Beam geometry
plot_beam_diagram(ax1, length=8.0, loads=[30, 40])

# Moment diagram
plot_moment_diagram(ax2, x_values, moment_values)

# Steel layout
plot_steel_layout(ax3, beam_width=300, beam_height=600, bars=[25, 25, 20])

plt.tight_layout()
plt.savefig('reports/figures/beam_analysis.png', dpi=300, bbox_inches='tight')
```

### 2. Professional Styling
```python
# Professional color scheme
colors = {
    'concrete': '#C0C0C0',
    'steel': '#FF6B35',
    'loads': '#2E86AB',
    'moments': '#A23B72'
}

# Professional annotations
plt.annotate('f\'c = 25 MPa', xy=(0.1, 0.9), xycoords='axes fraction',
            fontsize=10, bbox=dict(boxstyle="round,pad=0.3", facecolor='white'))
```

## 📄 Report Generation

### 1. PDF Generation Options

#### Cambridge Style (Academic)
```bash
python scripts/pdf_generators/pdf_generator_system.py \
    --notebook notebooks/beam_design/calculation.ipynb \
    --template cambridge \
    --output output/beam_design/
```

#### Standard Professional
```bash
python scripts/pdf_generators/pdf_generator_system.py \
    --notebook notebooks/beam_design/calculation.ipynb \
    --template standard \
    --output output/beam_design/
```

#### ACI 318 Method C (Columns)
```bash
python scripts/pdf_generators/aci318_method_c_pdf_generator.py \
    --notebook notebooks/column_design/column_calc.ipynb \
    --output output/column_design/
```

### 2. Batch Processing
```bash
# Generate all reports for a project
scripts/batch_files/generate_all_reports.bat PROJECT_NAME

# Quick standard report
scripts/batch_files/generate_standard_pdf.bat
```

## 🔍 Quality Assurance

### 1. Calculation Verification
```python
# Always include verification
def verify_calculation(calculated_value, expected_value, tolerance=0.05):
    """Verify calculation against expected result"""
    error = abs(calculated_value - expected_value) / expected_value
    if error <= tolerance:
        print(f"✅ Verification PASSED: {error:.2%} error")
    else:
        print(f"❌ Verification FAILED: {error:.2%} error")
    return error <= tolerance
```

### 2. Unit Consistency
```python
# Use consistent units throughout
# Convert at input, calculate in consistent units, display with units

# Input conversion
length_m = 8.0          # Input in meters
length_mm = length_m * 1000  # Convert to mm for calculations

# Calculation in mm
moment_Nmm = force_N * length_mm

# Output conversion
moment_kNm = moment_Nmm / 1e6  # Convert to kN⋅m for display
```

### 3. Code Review Checklist
- [ ] All variables have clear names and units
- [ ] Calculations follow design codes (ACI 318-19, etc.)
- [ ] Handcalcs used for professional presentation
- [ ] Plots are professional quality with proper labels
- [ ] Results are verified against hand calculations
- [ ] Documentation is complete and clear

## 🛠️ Troubleshooting

### 1. Common Issues

#### Handcalcs Not Rendering
```python
# Reload handcalcs extension
%reload_ext handcalcs.render

# Check installation
pip install --upgrade handcalcs
```

#### LaTeX Compilation Errors
```bash
# Check LaTeX installation
pdflatex --version

# Install missing packages
tlmgr install [package-name]
```

#### Import Errors
```python
# Check virtual environment
import sys
print(sys.executable)

# Reinstall packages
pip install --force-reinstall -r requirements.txt
```

### 2. Performance Optimization

#### Large Calculations
```python
# Use numpy for vectorized operations
import numpy as np

# Efficient array operations
moments = np.array([M1, M2, M3])
capacities = np.array([Mn1, Mn2, Mn3])
ratios = moments / capacities
```

#### Memory Management
```python
# Clear large variables when done
del large_array
import gc
gc.collect()
```

## 📈 Advanced Features

### 1. Custom Templates
```python
# Create custom LaTeX template
template_content = """
\\documentclass[11pt]{article}
\\usepackage{your_custom_packages}
\\begin{document}
{{ calculation_content }}
\\end{document}
"""
```

### 2. Automated Testing
```python
# Create test cases for calculations
def test_beam_capacity():
    result = calculate_beam_capacity(fc=25, fy=420, b=300, d=550, As=1200)
    expected = 185.5  # kN⋅m
    assert abs(result - expected) < 1.0, f"Expected {expected}, got {result}"
```

### 3. Integration with External Tools
```python
# Export to Excel for further analysis
import pandas as pd

results_df = pd.DataFrame({
    'Parameter': ['Mu', 'Mn', 'Ratio'],
    'Value': [150.0, 185.5, 0.81],
    'Units': ['kN⋅m', 'kN⋅m', '-']
})

results_df.to_excel('output/beam_design/results.xlsx', index=False)
```

## 🎯 Best Practices Summary

1. **Always use handcalcs** for professional presentation
2. **Follow naming conventions** for files and variables
3. **Include units** in all calculations and comments
4. **Verify calculations** against hand calculations or known solutions
5. **Use professional plotting** with proper labels and styling
6. **Document assumptions** clearly in markdown cells
7. **Generate reports early** and review frequently
8. **Commit changes regularly** to git with meaningful messages
9. **Archive completed calculations** in appropriate folders
10. **Keep templates updated** with latest standards and practices 