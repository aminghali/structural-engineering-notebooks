#!/usr/bin/env python3
"""
Ghali Consultants - Unified PDF Generation System
================================================
Complete system for generating professional calculation sheets from Jupyter notebooks.
Supports both Standard and Cambridge Academic templates.

Author: Ghali Consultants
Version: 2.0 Unified System
"""

import os
import sys
import json
import re
import subprocess
import tempfile
import shutil
from pathlib import Path
from typing import Dict, List, Optional, Union

# Add project root to Python path
script_dir = Path(__file__).parent
project_root = script_dir.parent
sys.path.append(str(project_root))

from scripts.structural_plotting import create_all_structural_plots

class GhaliPDFGenerator:
    """Unified PDF generator for structural calculations"""
    
    def __init__(self, template_style="standard"):
        """
        Initialize PDF generator
        
        Args:
            template_style (str): "standard" or "cambridge"
        """
        self.template_style = template_style.lower()
        self.project_root = project_root
        
        if self.template_style not in ["standard", "cambridge"]:
            raise ValueError("Template style must be 'standard' or 'cambridge'")
    
    def extract_from_notebook(self, notebook_path: str) -> Dict:
        """
        Extract calculation data from Jupyter notebook
        
        Args:
            notebook_path (str): Path to notebook file
            
        Returns:
            Dict: Extracted beam parameters and results
        """
        try:
            import nbformat
            
            notebook_path = Path(notebook_path)
            if not notebook_path.exists():
                raise FileNotFoundError(f"Notebook not found: {notebook_path}")
            
            with open(notebook_path, 'r', encoding='utf-8') as f:
                nb = nbformat.read(f, as_version=4)
            
            # Extract variables from code cells
            extracted_data = {}
            
            for cell in nb.cells:
                if cell.cell_type == 'code':
                    source = cell.source
                    
                    # Extract common beam parameters
                    patterns = {
                        'length': r'(?:L|length|beam_length)\s*=\s*([\d.]+)',
                        'dead_load': r'(?:w_d|dead_load|DL)\s*=\s*([\d.]+)', 
                        'live_load': r'(?:w_l|live_load|LL)\s*=\s*([\d.]+)',
                        'width': r'(?:b|width|beam_width)\s*=\s*([\d.]+)',
                        'height': r'(?:h|height|beam_height)\s*=\s*([\d.]+)',
                        'fc': r'(?:f_c|fc|concrete_strength)\s*=\s*([\d.]+)',
                        'fy': r'(?:f_y|fy|steel_strength)\s*=\s*([\d.]+)'
                    }
                    
                    for param, pattern in patterns.items():
                        match = re.search(pattern, source, re.IGNORECASE)
                        if match:
                            extracted_data[param] = float(match.group(1))
            
            # Set defaults if not found
            defaults = {
                'length': 8.0,
                'dead_load': 20.0,
                'live_load': 25.0,
                'width': 350,
                'height': 600,
                'fc': 25,
                'fy': 420
            }
            
            for key, default_value in defaults.items():
                if key not in extracted_data:
                    extracted_data[key] = default_value
            
            # Calculate derived values
            extracted_data['factored_load'] = 1.2 * extracted_data['dead_load'] + 1.6 * extracted_data['live_load']
            extracted_data['steel_area_req'] = int(extracted_data['length'] * 225)  # Approximate
            extracted_data['bar_diameter'] = 25
            
            return extracted_data
            
        except ImportError:
            print("Warning: nbformat not installed. Using default values.")
            return self._get_default_beam_data()
        except Exception as e:
            print(f"Warning: Could not extract from notebook: {e}")
            return self._get_default_beam_data()
    
    def _get_default_beam_data(self) -> Dict:
        """Get default beam data when notebook extraction fails"""
        return {
            'length': 8.0,
            'dead_load': 20.0,
            'live_load': 25.0,
            'factored_load': 64.0,
            'width': 350,
            'height': 600,
            'fc': 25,
            'fy': 420,
            'steel_area_req': 1800,
            'bar_diameter': 25
        }
    
    def generate_plots(self, beam_data: Dict) -> Dict:
        """Generate structural plots for beam data"""
        print("📊 Generating structural plots...")
        plots_data = create_all_structural_plots(beam_data)
        print("   ✓ Professional structural diagrams created")
        return plots_data
    
    def load_template(self) -> str:
        """Load the appropriate LaTeX template"""
        if self.template_style == "cambridge":
            template_file = "cambridge_style_template.tex"
        else:
            # Use the embedded standard template
            return self._get_standard_template()
        
        template_path = self.project_root / "templates" / template_file
        
        if not template_path.exists():
            raise FileNotFoundError(f"Template not found: {template_path}")
        
        with open(template_path, 'r', encoding='utf-8') as f:
            return f.read()
    
    def _get_standard_template(self) -> str:
        """Embedded standard template for reliability"""
        # Import from the existing ghali_pdf_generator
        try:
            from scripts.ghali_pdf_generator import create_latex_template
            return create_latex_template()
        except ImportError:
            raise ImportError("Could not load standard template")
    
    def populate_template(self, template: str, beam_data: Dict, project_info: Dict) -> str:
        """Populate template with beam data and project information"""
        
        # Calculate design forces
        L = beam_data['length']
        w_u = beam_data['factored_load']
        max_moment = w_u * L**2 / 8
        max_shear = w_u * L / 2
        
        # Common replacements for both templates
        replacements = {
            'BEAM_LENGTH_PLACEHOLDER': f"{beam_data['length']:.1f}",
            'DEAD_LOAD_PLACEHOLDER': f"{beam_data['dead_load']:.1f}",
            'LIVE_LOAD_PLACEHOLDER': f"{beam_data['live_load']:.1f}",
            'FACTORED_LOAD_PLACEHOLDER': f"{beam_data['factored_load']:.1f}",
            'BEAM_WIDTH_PLACEHOLDER': str(beam_data['width']),
            'BEAM_HEIGHT_PLACEHOLDER': str(beam_data['height']),
            'EFFECTIVE_DEPTH_PLACEHOLDER': str(beam_data['height'] - 50),
            'STEEL_AREA_PLACEHOLDER': str(beam_data['steel_area_req']),
            'MAX_MOMENT_PLACEHOLDER': f"{max_moment:.1f}",
            'MAX_SHEAR_PLACEHOLDER': f"{max_shear:.1f}",
            'PROJECT_ID_PLACEHOLDER': project_info.get('project_id', 'GC-2025-001'),
            'PROJECT_TITLE_PLACEHOLDER': project_info.get('title', f"{beam_data['length']:.1f}m RC Beam Design"),
            'ENGINEER_NAME_PLACEHOLDER': project_info.get('engineer', 'Ahmed Ghali, P.E.'),
            'REVIEWER_NAME_PLACEHOLDER': project_info.get('reviewer', 'Senior Engineer, P.E.')
        }
        
        # Apply replacements
        for placeholder, value in replacements.items():
            template = template.replace(placeholder, value)
        
        return template
    
    def compile_pdf(self, latex_content: str, output_name: str) -> Optional[str]:
        """Compile LaTeX content to PDF"""
        print(f"🔨 Compiling {self.template_style.title()} style PDF...")
        
        with tempfile.TemporaryDirectory() as temp_dir:
            temp_path = Path(temp_dir)
            tex_file = temp_path / f"{output_name}.tex"
            
            # Write LaTeX content
            with open(tex_file, 'w', encoding='utf-8') as f:
                f.write(latex_content)
            
            # Copy plot files
            reports_dir = self.project_root / "reports" / "figures"
            plot_files = ["beam_diagram.pdf", "bmd_sfd.pdf", "steel_layout.pdf"]
            
            for plot_file in plot_files:
                source = reports_dir / plot_file
                if source.exists():
                    shutil.copy2(source, temp_path)
            
            # Compile PDF
            try:
                result = subprocess.run([
                    'pdflatex', '-interaction=nonstopmode', tex_file.name
                ], cwd=temp_path, capture_output=True, text=True)
                
                if result.returncode == 0:
                    # Copy to output
                    output_dir = self.project_root / "output"
                    output_dir.mkdir(exist_ok=True)
                    
                    pdf_file = temp_path / f"{output_name}.pdf"
                    output_pdf = output_dir / f"{output_name}.pdf"
                    
                    if pdf_file.exists():
                        shutil.copy2(pdf_file, output_pdf)
                        print(f"   ✓ PDF created: {output_pdf}")
                        print(f"   📄 Size: {output_pdf.stat().st_size / 1024:.1f} KB")
                        return str(output_pdf)
                else:
                    print(f"   ❌ LaTeX compilation failed")
                    if result.stderr:
                        print(f"   Error: {result.stderr}")
                        
            except FileNotFoundError:
                print("   ❌ LaTeX not found. Install TinyTeX or MiKTeX.")
                
        return None
    
    def generate_pdf(self, 
                    notebook_path: Optional[str] = None,
                    beam_data: Optional[Dict] = None,
                    project_info: Optional[Dict] = None) -> Optional[str]:
        """
        Generate PDF calculation sheet
        
        Args:
            notebook_path (str, optional): Path to Jupyter notebook
            beam_data (Dict, optional): Beam parameters (if not using notebook)
            project_info (Dict, optional): Project information
            
        Returns:
            str: Path to generated PDF file
        """
        print(f"🏗️  GHALI CONSULTANTS - {self.template_style.title()} PDF Generator")
        print("=" * 60)
        
        # Step 1: Get beam data
        if notebook_path:
            print(f"📓 Extracting data from notebook: {notebook_path}")
            beam_data = self.extract_from_notebook(notebook_path)
        elif beam_data is None:
            print("📊 Using default beam parameters")
            beam_data = self._get_default_beam_data()
        
        # Step 2: Generate plots
        plots_data = self.generate_plots(beam_data)
        
        # Step 3: Load and populate template
        print(f"📄 Loading {self.template_style} template...")
        template = self.load_template()
        
        if project_info is None:
            project_info = {
                'project_id': f'GC-{self.template_style.upper()}-2025',
                'title': f"{beam_data['length']:.1f}m RC Beam Design",
                'engineer': 'Ahmed Ghali, P.E.',
                'reviewer': 'Senior Engineer, P.E.'
            }
        
        populated_template = self.populate_template(template, beam_data, project_info)
        
        # Step 4: Compile PDF
        output_name = f"Ghali_{self.template_style.title()}_Beam_Design"
        pdf_path = self.compile_pdf(populated_template, output_name)
        
        if pdf_path:
            print(f"\n🎉 SUCCESS! {self.template_style.title()} PDF generated")
            print(f"📁 {pdf_path}")
            
            if self.template_style == "cambridge":
                print("\n✨ Cambridge Academic Features:")
                print("   • Two-column professional layout")
                print("   • Academic table formatting")
                print("   • Narrow margins & condensed typography")
                print("   • Multiple beam analysis ready")
            else:
                print("\n✨ Standard Professional Features:")
                print("   • Single-column readable layout")
                print("   • Professional Ghali branding")
                print("   • Generous margins for review")
                print("   • Client presentation format")
        
        return pdf_path

def main():
    """Command line interface"""
    import argparse
    
    parser = argparse.ArgumentParser(description='Ghali Consultants PDF Generation System')
    parser.add_argument('--template', choices=['standard', 'cambridge'], default='standard',
                      help='Template style: standard or cambridge')
    parser.add_argument('--notebook', help='Path to Jupyter notebook')
    parser.add_argument('--length', type=float, default=8.0, help='Beam length (m)')
    parser.add_argument('--dead-load', type=float, default=20.0, help='Dead load (kN/m)')
    parser.add_argument('--live-load', type=float, default=25.0, help='Live load (kN/m)')
    parser.add_argument('--project-id', help='Project ID')
    
    args = parser.parse_args()
    
    # Create generator
    generator = GhaliPDFGenerator(template_style=args.template)
    
    # Prepare data
    beam_data = None
    project_info = None
    
    if not args.notebook:
        # Use command line parameters
        beam_data = {
            'length': args.length,
            'dead_load': args.dead_load,
            'live_load': args.live_load,
            'factored_load': 1.2 * args.dead_load + 1.6 * args.live_load,
            'width': 350,
            'height': 600,
            'fc': 25,
            'fy': 420,
            'steel_area_req': int(args.length * 225),
            'bar_diameter': 25
        }
    
    if args.project_id:
        project_info = {'project_id': args.project_id}
    
    # Generate PDF
    pdf_path = generator.generate_pdf(
        notebook_path=args.notebook,
        beam_data=beam_data,
        project_info=project_info
    )
    
    if not pdf_path:
        sys.exit(1)

if __name__ == "__main__":
    main() 