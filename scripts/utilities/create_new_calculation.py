#!/usr/bin/env python3
"""
Ghali Consultants - New Calculation Creator
===========================================
Creates new structural calculation notebooks from template.

Author: Ghali Consultants
Version: 1.0
"""

import os
import sys
import shutil
import argparse
from pathlib import Path
from datetime import datetime

# Add project root to Python path
script_dir = Path(__file__).parent
project_root = script_dir.parent
sys.path.append(str(project_root))

def create_new_calculation(project_id: str, 
                         description: str = "",
                         engineer: str = "Ahmed Ghali, P.E.",
                         length: float = 8.0,
                         dead_load: float = 20.0,
                         live_load: float = 25.0) -> str:
    """
    Create a new calculation notebook from template
    
    Args:
        project_id (str): Project identifier (e.g., "GC-2025-045")
        description (str): Project description
        engineer (str): Engineer name
        length (float): Initial beam length
        dead_load (float): Initial dead load
        live_load (float): Initial live load
        
    Returns:
        str: Path to created notebook
    """
    
    template_path = project_root / "notebooks" / "structural_calculation_template.ipynb"
    if not template_path.exists():
        raise FileNotFoundError("Template notebook not found!")
    
    # Create filename
    date_str = datetime.now().strftime("%Y%m%d")
    notebook_name = f"{project_id}_{date_str}_beam_design.ipynb"
    notebook_path = project_root / "notebooks" / notebook_name
    
    # Copy template
    shutil.copy2(template_path, notebook_path)
    
    # Read and modify notebook
    with open(notebook_path, 'r', encoding='utf-8') as f:
        content = f.read()
    
    # Update project information
    current_date = datetime.now().strftime("%Y-%m-%d")
    
    replacements = {
        'GC-2025-NEW': project_id,
        'Ahmed Ghali, P.E.': engineer,
        '2025': current_date,
        'RC Beam Design Calculation': description or f"{project_id} - RC Beam Design",
        'length = 8.0': f'length = {length}',
        'dead_load = 20.0': f'dead_load = {dead_load}',
        'live_load = 25.0': f'live_load = {live_load}'
    }
    
    for old, new in replacements.items():
        content = content.replace(old, new)
    
    # Write modified notebook
    with open(notebook_path, 'w', encoding='utf-8') as f:
        f.write(content)
    
    return str(notebook_path)

def main():
    """Command line interface"""
    parser = argparse.ArgumentParser(description='Create new structural calculation notebook')
    parser.add_argument('project_id', help='Project ID (e.g., GC-2025-045)')
    parser.add_argument('--description', '-d', help='Project description')
    parser.add_argument('--engineer', '-e', default='Ahmed Ghali, P.E.', help='Engineer name')
    parser.add_argument('--length', '-l', type=float, default=8.0, help='Beam length (m)')
    parser.add_argument('--dead-load', type=float, default=20.0, help='Dead load (kN/m)')
    parser.add_argument('--live-load', type=float, default=25.0, help='Live load (kN/m)')
    parser.add_argument('--generate-pdf', choices=['standard', 'cambridge'], 
                       help='Generate PDF immediately after creation')
    
    args = parser.parse_args()
    
    print("🏗️  GHALI CONSULTANTS - NEW CALCULATION CREATOR")
    print("=" * 60)
    
    try:
        # Create notebook
        print(f"📓 Creating calculation notebook for: {args.project_id}")
        notebook_path = create_new_calculation(
            project_id=args.project_id,
            description=args.description,
            engineer=args.engineer,
            length=args.length,
            dead_load=args.dead_load,
            live_load=args.live_load
        )
        
        print(f"✅ Notebook created: {notebook_path}")
        print(f"📊 Initial parameters:")
        print(f"   • Length: {args.length} m")
        print(f"   • Dead Load: {args.dead_load} kN/m")
        print(f"   • Live Load: {args.live_load} kN/m")
        print(f"   • Engineer: {args.engineer}")
        
        # Generate PDF if requested
        if args.generate_pdf:
            print(f"\n🔨 Generating {args.generate_pdf} PDF...")
            from scripts.pdf_generator_system import GhaliPDFGenerator
            
            generator = GhaliPDFGenerator(template_style=args.generate_pdf)
            pdf_path = generator.generate_pdf(notebook_path=notebook_path)
            
            if pdf_path:
                print(f"✅ PDF generated: {pdf_path}")
            else:
                print("❌ PDF generation failed")
        
        print(f"\n🎯 NEXT STEPS:")
        print(f"1. Open notebook: jupyter notebook {notebook_path}")
        print(f"2. Modify calculations as needed")
        print(f"3. Generate Standard PDF: python scripts/pdf_generator_system.py --notebook {notebook_path} --template standard")
        print(f"4. Generate Cambridge PDF: python scripts/pdf_generator_system.py --notebook {notebook_path} --template cambridge")
        
    except Exception as e:
        print(f"❌ Error: {e}")
        sys.exit(1)

if __name__ == "__main__":
    main() 