# Project Structure - Structural Engineering Jupiter Notebooks

## 📁 Directory Organization

```
Jupiter Notebook/
├── 📓 notebooks/                    # All Jupiter notebooks organized by type
│   ├── beam_design/                 # Beam design calculations
│   │   └── GC-DEMO-2025_20250605_beam_design.ipynb
│   ├── column_design/               # Column design calculations  
│   │   └── aci318_column_design_method_c.ipynb
│   ├── templates/                   # Template notebooks for new calculations
│   │   └── structural_calculation_template.ipynb
│   └── archive/                     # Archived/old notebooks
│       └── professional_concrete_design_aci318.ipynb
│
├── 🔧 scripts/                      # All automation and utility scripts
│   ├── pdf_generators/              # PDF generation scripts
│   │   ├── aci318_method_c_direct_pdf.py
│   │   ├── aci318_method_c_html_generator.py
│   │   ├── aci318_method_c_pdf_generator.py
│   │   ├── cambridge_pdf_generator.py
│   │   ├── ghali_pdf_generator.py
│   │   └── pdf_generator_system.py
│   ├── utilities/                   # Utility scripts
│   │   ├── create_new_calculation.py
│   │   └── structural_plotting.py
│   └── batch_files/                 # Batch automation files
│       ├── create_new_project.bat
│       ├── generate_aci318_method_c_pdf.bat
│       ├── generate_cambridge_pdf.bat
│       ├── generate_pdf.bat
│       └── generate_standard_pdf.bat
│
├── 🎨 templates/                    # LaTeX templates for professional reports
│   ├── cambridge_style_template.tex
│   ├── structural_calculation_template.tex
│   └── aci318_method_c_template.tex
│
├── 📄 output/                       # Generated outputs organized by type
│   ├── beam_design/                 # Beam calculation outputs
│   │   ├── Cambridge_Style_Beam_Design.pdf
│   │   ├── Ghali_Cambridge_Beam_Design.pdf
│   │   ├── Ghali_Standard_Beam_Design.pdf
│   │   └── Ghali_Beam_Design.pdf
│   ├── column_design/               # Column calculation outputs
│   │   ├── ACI318_Method_C_Column_Design_Direct.pdf
│   │   └── ACI318_Method_C_Column_Design.html
│   └── archive/                     # Archived outputs
│       └── Professional_Beam_Design_Report.tex
│
├── 📊 reports/                      # Final professional reports
│   └── figures/                     # Generated plots and diagrams
│
├── 📚 docs/                         # Project documentation
├── 🎯 assets/                       # Images, diagrams, supporting files
├── 🔄 examples/                     # Example calculations and references
├── 🔧 venv/                         # Python virtual environment
├── 📋 .cursor/                      # Cursor IDE rules and configuration
│   └── rules/                       # MDC rule files
│       ├── structural_engineering_always_active.mdc
│       ├── notebook_development_standards.mdc
│       ├── handcalcs_usage_guidelines.mdc
│       ├── project_organization.mdc
│       └── environment_setup.mdc
│
├── 📄 README.md                     # Main project documentation
├── 📄 PROJECT_STRUCTURE.md          # This file - project organization
├── 📄 SYSTEM_SUMMARY.md             # System overview and capabilities
├── 📄 requirements.txt              # Python dependencies
└── 📄 .gitignore                    # Git ignore rules
```

## 🎯 File Naming Conventions

### Notebooks
- **Format**: `YYYY-MM-DD_CalculationType_Description_vX.ipynb`
- **Example**: `2025-06-05_beam_design_office_building_v1.ipynb`

### Templates
- **Format**: `[code]_[type]_template.tex`
- **Example**: `aci318_method_c_template.tex`

### Outputs
- **Format**: `YYYY-MM-DD_HHMM_CalculationName_Report.pdf`
- **Example**: `2025-06-05_1430_Beam_Design_Report.pdf`

### Scripts
- **Format**: `descriptive_name_purpose.py`
- **Example**: `aci318_method_c_pdf_generator.py`

## 🔄 Workflow Organization

### 1. Development Workflow
```
notebooks/templates/ → notebooks/[type]/ → output/[type]/ → reports/
```

### 2. Script Organization
- **PDF Generators**: Scripts that convert notebooks to professional PDFs
- **Utilities**: Helper scripts for calculations and plotting
- **Batch Files**: One-click automation for common tasks

### 3. Output Management
- **Type-based Organization**: Separate folders for beam, column, etc.
- **Archive System**: Old outputs moved to archive folders
- **Version Control**: Clear versioning and timestamps

## 🛠️ Professional Standards

### Code Quality
- All scripts follow PEP 8 standards
- Comprehensive error handling
- Professional documentation
- Type hints where appropriate

### Calculation Standards
- Follow ACI 318-19, AISC 360, IBC standards
- Use handcalcs for professional presentation
- Include proper units and dimensional analysis
- Provide clear variable definitions

### Documentation Standards
- Comprehensive README files
- Inline code documentation
- Professional calculation reports
- Clear project structure documentation

## 🔧 Development Environment

### Virtual Environment
- Located in `venv/` folder
- All dependencies in `requirements.txt`
- Professional package versions pinned

### IDE Configuration
- Cursor rules in `.cursor/rules/`
- Always-active structural engineering standards
- Automated code quality checks

### Version Control
- Git repository with proper .gitignore
- Organized commit structure
- Clear branching strategy for features

## 📈 Scalability

### Adding New Calculation Types
1. Create new subfolder in `notebooks/`
2. Create corresponding output subfolder
3. Add specific templates if needed
4. Update documentation

### Template System
- Modular LaTeX templates
- Consistent formatting across calculations
- Easy customization for different projects

### Automation
- Batch files for common operations
- Script-based PDF generation
- Automated report formatting

## 🎯 Quality Assurance

### Testing
- Calculation verification against hand calculations
- Template compatibility testing
- Output format validation

### Documentation
- Keep all documentation current
- Update structure documentation with changes
- Maintain professional standards

### Backup and Archive
- Regular archiving of completed calculations
- Version control for all changes
- Backup of important templates and outputs 