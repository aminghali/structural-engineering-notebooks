# Structural Engineering Jupiter Notebooks
**Professional Calculation System with Handcalcs Integration**

---

## 🏗️ Project Overview

A comprehensive, professionally organized system for structural engineering calculations using Jupiter notebooks with handcalcs for mathematical presentation and LaTeX templates for professional reports.

### ✨ Key Features

- **📓 Professional Notebooks**: Organized by calculation type (beam, column, etc.)
- **🎨 Handcalcs Integration**: Beautiful mathematical presentation with symbolic calculations
- **📄 LaTeX Templates**: Cambridge style and professional report templates
- **🔄 Automated PDF Generation**: One-click professional report creation
- **📊 Professional Plotting**: High-quality structural diagrams and plots
- **🎯 Code Standards**: Following structural engineering best practices

---

## 🚀 Quick Start

### 1. Environment Setup
```bash
# Activate virtual environment
venv\Scripts\activate

# Install dependencies
pip install -r requirements.txt

# Start Jupyter Lab
jupyter lab
```

### 2. Create New Calculation
```bash
# Copy template for beam design
copy notebooks\templates\structural_calculation_template.ipynb notebooks\beam_design\2025-06-06_my_beam_calc_v1.ipynb

# Or use creation script
python scripts\utilities\create_new_calculation.py GC-2025-049 --description "My Beam Project" --type beam
```

### 3. Generate Professional Report
```bash
# Cambridge style report
python scripts\pdf_generators\pdf_generator_system.py --notebook notebooks\beam_design\my_calculation.ipynb --template cambridge

# Standard professional report
python scripts\pdf_generators\pdf_generator_system.py --notebook notebooks\beam_design\my_calculation.ipynb --template standard
```

---

## 📁 Project Structure

```
Jupiter Notebook/
├── 📓 notebooks/                    # Organized by calculation type
│   ├── beam_design/                 # Beam calculations
│   ├── column_design/               # Column calculations
│   ├── templates/                   # Template notebooks
│   └── archive/                     # Archived calculations
├── 🔧 scripts/                      # Automation and utilities
│   ├── pdf_generators/              # PDF generation scripts
│   ├── utilities/                   # Helper utilities
│   └── batch_files/                 # Batch automation
├── 🎨 templates/                    # LaTeX report templates
├── 📄 output/                       # Generated reports (organized by type)
├── 📊 reports/figures/              # Generated plots and diagrams
├── 📋 .cursor/rules/                # Professional development rules
└── 📚 docs/                         # Documentation
```

---

## 🎯 Professional Standards

### Handcalcs Integration
```python
import handcalcs.render
from handcalcs import handcalc

%load_ext handcalcs.render

%%render
# Professional calculation presentation
f_c_prime = 25.0    # Concrete strength, MPa
f_y = 420.0         # Steel yield strength, MPa
M_u = 150.0         # Ultimate moment, kN⋅m
```

### Variable Naming Convention
- Use descriptive names: `f_c_prime`, `A_s_req`, `M_u`
- Include units in comments: `# MPa`, `# mm²`, `# kN⋅m`
- Follow engineering notation standards

### Professional Plotting
```python
import matplotlib.pyplot as plt
from scripts.utilities.structural_plotting import plot_beam_diagram

# Professional styling with proper labels and units
plt.style.use('default')
plt.rcParams.update({'font.size': 10, 'figure.dpi': 300})
```

---

## 📄 Available Templates

### 1. Cambridge Style Template
- **File**: `templates/cambridge_style_template.tex`
- **Use**: Academic presentations, journal submissions
- **Features**: Two-column layout, professional typography

### 2. Standard Professional Template  
- **File**: `templates/structural_calculation_template.tex`
- **Use**: Client reports, professional calculations
- **Features**: Single-column, generous margins

### 3. ACI 318-19 Method C Template
- **File**: `templates/aci318_method_c_template.tex`
- **Use**: Column slenderness analysis
- **Features**: Code-compliant format, technical presentation

---

## 🔧 Development Workflow

### 1. Standard Process
1. **Create**: Copy template or use creation script
2. **Develop**: Implement calculations with handcalcs
3. **Test**: Verify against hand calculations
4. **Generate**: Create professional PDF report
5. **Review**: Check calculations and presentation
6. **Archive**: Store in appropriate folder

### 2. Quality Assurance
- ✅ Use handcalcs for all mathematical presentations
- ✅ Include proper units and dimensional analysis
- ✅ Follow ACI 318-19, AISC 360, IBC standards
- ✅ Verify calculations against known solutions
- ✅ Generate professional plots with proper labels

---

## 📊 Calculation Types

### Beam Design
- **Location**: `notebooks/beam_design/`
- **Templates**: Cambridge and Standard styles
- **Features**: Flexural design, shear design, deflection analysis

### Column Design
- **Location**: `notebooks/column_design/`
- **Templates**: ACI 318-19 Method C
- **Features**: Slenderness analysis, moment magnification

### Custom Calculations
- **Templates**: Extensible template system
- **Standards**: Professional engineering format
- **Integration**: Handcalcs and LaTeX compatibility

---

## 🛠️ Advanced Features

### Automated PDF Generation
```bash
# Batch processing
scripts\batch_files\generate_cambridge_pdf.bat

# Custom parameters
python scripts\pdf_generators\pdf_generator_system.py --template cambridge --length 10.0 --fc 30.0
```

### Professional Plotting System
```python
from scripts.utilities.structural_plotting import (
    plot_beam_diagram,
    plot_moment_diagram, 
    plot_steel_layout
)
```

### Version Control Integration
- Git repository with professional .gitignore
- Organized commit structure
- Clear branching for features

---

## 📚 Documentation

- **[Project Structure](PROJECT_STRUCTURE.md)**: Detailed organization guide
- **[Development Guide](DEVELOPMENT_GUIDE.md)**: Complete development workflow
- **[System Summary](SYSTEM_SUMMARY.md)**: Technical overview
- **[Cursor Rules](.cursor/rules/)**: Professional development standards

---

## 🎯 Getting Help

### Common Issues
1. **Handcalcs not rendering**: `%reload_ext handcalcs.render`
2. **LaTeX errors**: Check template compatibility
3. **Import errors**: Verify virtual environment activation

### Best Practices
1. Always use handcalcs for mathematical presentation
2. Include units in all calculations and comments
3. Follow professional naming conventions
4. Generate reports early and often
5. Verify calculations against hand calculations

---

## 📈 Future Enhancements

- [ ] Additional calculation types (foundations, connections)
- [ ] Integration with structural analysis software
- [ ] Automated code compliance checking
- [ ] Enhanced plotting capabilities
- [ ] Multi-language support for international codes

---

**Professional structural engineering calculations made simple and beautiful.**

*Last Updated: June 2025* 