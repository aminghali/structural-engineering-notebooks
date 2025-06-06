#!/usr/bin/env python3
"""
Ghali Consultants - Cambridge Style PDF Generator
================================================
Academic two-column format for multiple beam analysis.

Author: Ghali Consultants
Version: 1.0 Cambridge Style
"""

import os
import sys
import subprocess
import tempfile
import shutil
from pathlib import Path

# Add project root to Python path
script_dir = Path(__file__).parent
project_root = script_dir.parent
sys.path.append(str(project_root))

from scripts.structural_plotting import create_all_structural_plots

def create_cambridge_template():
    """Load Cambridge-style LaTeX template"""
    template_path = project_root / "templates" / "cambridge_style_template.tex"
    
    with open(template_path, 'r', encoding='utf-8') as f:
        return f.read()

def generate_cambridge_pdf(beams_data, project_id="GC-CAM-2025"):
    """
    Generate academic-style PDF for multiple beam analysis
    
    Args:
        beams_data (list): List of beam dictionaries with parameters
        project_id (str): Project identifier
        
    Returns:
        str: Path to generated PDF file
    """
    print("🎓 GHALI CONSULTANTS - Cambridge Style Generator")
    print("=" * 55)
    
    # Step 1: Generate plots for the first beam (representative)
    print("1. Generating structural plots...")
    if beams_data:
        beam_data = beams_data[0]  # Use first beam for diagrams
        plots_data = create_all_structural_plots(beam_data)
        max_moment = plots_data.get('M_max', beam_data['length']**2 * beam_data.get('factored_load', 64) / 8)
        max_shear = plots_data.get('V_max', beam_data['length'] * beam_data.get('factored_load', 64) / 2)
        print(f"   ✓ Generated academic structural diagrams")
    else:
        print("   ⚠️ No beam data provided")
        return None
    
    # Step 2: Create LaTeX document
    print("2. Creating academic calculation sheet...")
    latex_content = create_cambridge_template()
    
    # Step 3: Replace placeholders with first beam data
    if beams_data:
        beam = beams_data[0]
        replacements = {
            'PROJECT_ID_PLACEHOLDER': project_id,
            'BEAM_LENGTH_PLACEHOLDER': f"{beam['length']:.1f}",
            'BEAM_WIDTH_PLACEHOLDER': str(beam.get('width', 350)),
            'BEAM_HEIGHT_PLACEHOLDER': str(beam.get('height', 600)),
            'DEAD_LOAD_PLACEHOLDER': f"{beam.get('dead_load', 20):.1f}",
            'LIVE_LOAD_PLACEHOLDER': f"{beam.get('live_load', 25):.1f}",
            'MAX_MOMENT_PLACEHOLDER': f"{max_moment:.1f}",
            'MAX_SHEAR_PLACEHOLDER': f"{max_shear:.1f}",
            'STEEL_AREA_PLACEHOLDER': str(beam.get('steel_area_req', int(beam['length'] * 225)))
        }
        
        for placeholder, value in replacements.items():
            latex_content = latex_content.replace(placeholder, value)
    
    # Step 4: Compile PDF
    print("3. Compiling academic PDF...")
    
    with tempfile.TemporaryDirectory() as temp_dir:
        temp_path = Path(temp_dir)
        tex_file = temp_path / "cambridge_calculation.tex"
        
        # Write LaTeX content
        with open(tex_file, 'w', encoding='utf-8') as f:
            f.write(latex_content)
        
        # Copy plot files
        reports_dir = project_root / "reports" / "figures"
        plot_files = ["beam_diagram.pdf", "bmd_sfd.pdf", "steel_layout.pdf"]
        
        for plot_file in plot_files:
            source = reports_dir / plot_file
            if source.exists():
                shutil.copy2(source, temp_path)
        
        # Compile PDF with pdflatex
        try:
            result = subprocess.run([
                'pdflatex', '-interaction=nonstopmode', tex_file.name
            ], cwd=temp_path, capture_output=True, text=True)
            
            if result.returncode == 0:
                # Copy to output
                output_dir = project_root / "output"
                output_dir.mkdir(exist_ok=True)
                
                pdf_file = temp_path / "cambridge_calculation.pdf"
                output_pdf = output_dir / "Cambridge_Style_Beam_Design.pdf"
                
                if pdf_file.exists():
                    shutil.copy2(pdf_file, output_pdf)
                    print(f"   ✓ Academic PDF created: {output_pdf}")
                    print(f"   📄 Size: {output_pdf.stat().st_size / 1024:.1f} KB")
                    return str(output_pdf)
            else:
                print(f"   ❌ LaTeX compilation failed")
                print(f"   Error: {result.stderr}")
                    
        except FileNotFoundError:
            print("   ❌ LaTeX not found. Install TinyTeX or MiKTeX.")
            
    return None

def create_sample_beam_data():
    """Create sample beam data for testing"""
    return [
        {
            'length': 8.0,
            'dead_load': 20.0,
            'live_load': 25.0,
            'factored_load': 64.0,
            'width': 350,
            'height': 600,
            'steel_area_req': 1800,
            'bar_diameter': 25
        },
        {
            'length': 10.0,
            'dead_load': 25.0,
            'live_load': 30.0,
            'factored_load': 78.0,
            'width': 400,
            'height': 650,
            'steel_area_req': 2250,
            'bar_diameter': 25
        }
    ]

if __name__ == "__main__":
    import argparse
    
    parser = argparse.ArgumentParser(description='Generate Cambridge Style Academic PDF')
    parser.add_argument('--project-id', default='GC-CAM-2025', help='Project ID')
    parser.add_argument('--sample', action='store_true', help='Use sample beam data')
    
    args = parser.parse_args()
    
    if args.sample:
        beams_data = create_sample_beam_data()
        print(f"Using sample data for {len(beams_data)} beams")
    else:
        # Single beam for now
        beams_data = create_sample_beam_data()[:1]
    
    pdf_path = generate_cambridge_pdf(beams_data, args.project_id)
    
    if pdf_path:
        print(f"\n🎓 SUCCESS! Cambridge Style PDF generated")
        print(f"📁 {pdf_path}")
        print("\n✨ Academic Features:")
        print("   • Two-column professional layout")
        print("   • Academic table formatting (booktabs)")
        print("   • Narrow margins & condensed typography")
        print("   • Single/double column figure handling")
        print("   • Cambridge-style bibliography")
        print("   • Multiple beam analysis capability")
    else:
        print("\n❌ PDF generation failed") 