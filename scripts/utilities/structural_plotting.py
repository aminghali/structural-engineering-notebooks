"""
GHALI CONSULTANTS - STRUCTURAL PLOTTING MODULE
Professional structural engineering plots for LaTeX reports
Follows structural engineering conventions: BMD positive downward
"""

import numpy as np
import matplotlib.pyplot as plt
import matplotlib.patches as mpatches
from matplotlib import rcParams
import os
from pathlib import Path

# Configure matplotlib for professional plots
rcParams.update({
    'font.family': 'serif',
    'font.serif': ['Times New Roman', 'Times', 'DejaVu Serif'],
    'font.size': 11,
    'axes.labelsize': 12,
    'axes.titlesize': 14,
    'xtick.labelsize': 10,
    'ytick.labelsize': 10,
    'legend.fontsize': 10,
    'figure.titlesize': 16,
    'figure.dpi': 300,
    'savefig.dpi': 300,
    'savefig.bbox': 'tight',
    'savefig.pad_inches': 0.1,
    'text.usetex': False,  # Set to True if LaTeX is available
    'axes.grid': True,
    'grid.alpha': 0.3,
    'axes.linewidth': 0.8,
    'grid.linewidth': 0.5
})

# Ghali Consultants color scheme
GHALI_COLORS = {
    'blue': '#1f4e79',      # Professional blue
    'red': '#c5504b',       # Accent red
    'green': '#4caf50',     # Success green
    'gray': '#424242',      # Text gray
    'light_blue': '#e3f2fd', # Light blue background
    'dark_blue': '#0d47a1'   # Dark blue for emphasis
}

class StructuralPlotter:
    """Professional structural engineering plotting class for Ghali Consultants"""
    
    def __init__(self, output_dir="reports/figures"):
        """Initialize the plotter with output directory"""
        self.output_dir = Path(output_dir)
        self.output_dir.mkdir(parents=True, exist_ok=True)
        
    def plot_beam_diagram(self, L, w_d, w_l, beam_width, beam_height, save_name="beam_diagram"):
        """
        Plot beam geometry and loading diagram
        
        Args:
            L: Beam length (m)
            w_d: Dead load (kN/m)
            w_l: Live load (kN/m)
            beam_width: Beam width (mm)
            beam_height: Beam height (mm)
            save_name: Name for saved figure
        """
        fig, (ax1, ax2) = plt.subplots(2, 1, figsize=(12, 8))
        
        # Beam geometry
        x_beam = np.array([0, L, L, 0, 0])
        y_beam = np.array([0, 0, beam_height/1000, beam_height/1000, 0])  # Convert mm to m
        
        ax1.plot(x_beam, y_beam, 'k-', linewidth=2)
        ax1.fill(x_beam, y_beam, color=GHALI_COLORS['light_blue'], alpha=0.7, 
                label=f'Concrete Beam: {beam_width}×{beam_height} mm')
        
        # Support symbols
        support_size = L * 0.05
        # Left support (pin)
        ax1.plot([0, -support_size/2, support_size/2, 0], 
                [0, -support_size, -support_size, 0], 'k-', linewidth=2)
        # Right support (roller)
        ax1.plot([L, L-support_size/2, L+support_size/2, L], 
                [0, -support_size, -support_size, 0], 'k-', linewidth=2)
        # Add roller circles
        circle = plt.Circle((L, -support_size*0.7), support_size*0.2, 
                          color='white', ec='black', linewidth=2)
        ax1.add_patch(circle)
        
        ax1.set_xlim(-L*0.1, L*1.1)
        ax1.set_ylim(-support_size*1.5, beam_height/1000*1.3)
        ax1.set_xlabel('Length (m)')
        ax1.set_ylabel('Height (m)')
        ax1.set_title('Beam Geometry and Support Conditions', 
                     fontweight='bold', color=GHALI_COLORS['blue'])
        ax1.legend()
        ax1.grid(True, alpha=0.3)
        ax1.set_aspect('equal')
        
        # Loading diagram
        x_load = np.linspace(0, L, 100)
        w_total = w_d + w_l
        
        # Draw distributed load arrows
        n_arrows = 8
        x_arrows = np.linspace(L*0.1, L*0.9, n_arrows)
        arrow_height = max(w_d, w_l, w_total) * 0.3
        
        for x in x_arrows:
            ax2.annotate('', xy=(x, 0), xytext=(x, arrow_height),
                        arrowprops=dict(arrowstyle='->', color=GHALI_COLORS['red'], lw=1.5))
        
        # Load distribution rectangles
        ax2.fill_between([0, L], [0, 0], [w_d, w_d], 
                        color=GHALI_COLORS['green'], alpha=0.6, 
                        label=f'Dead Load: {w_d:.1f} kN/m')
        ax2.fill_between([0, L], [w_d, w_d], [w_total, w_total], 
                        color=GHALI_COLORS['red'], alpha=0.6, 
                        label=f'Live Load: {w_l:.1f} kN/m')
        
        # Beam outline
        ax2.plot([0, L], [0, 0], 'k-', linewidth=3, label='Beam')
        
        ax2.set_xlim(-L*0.05, L*1.05)
        ax2.set_ylim(0, w_total*1.4)
        ax2.set_xlabel('Length (m)')
        ax2.set_ylabel('Load Intensity (kN/m)')
        ax2.set_title(f'Loading Diagram - Total: {w_total:.1f} kN/m', 
                     fontweight='bold', color=GHALI_COLORS['blue'])
        ax2.legend()
        ax2.grid(True, alpha=0.3)
        
        plt.tight_layout()
        plt.savefig(self.output_dir / f"{save_name}.png", dpi=300, bbox_inches='tight')
        plt.savefig(self.output_dir / f"{save_name}.pdf", dpi=300, bbox_inches='tight')
        plt.close()
        
        return str(self.output_dir / f"{save_name}.pdf")
    
    def plot_bmd_sfd(self, L, w_u, save_name="bmd_sfd"):
        """
        Plot Bending Moment and Shear Force Diagrams
        BMD follows structural convention: positive moments shown downward
        
        Args:
            L: Beam length (m)
            w_u: Factored distributed load (kN/m)
            save_name: Name for saved figure
        """
        fig, (ax1, ax2, ax3) = plt.subplots(3, 1, figsize=(12, 10))
        
        # Define x coordinates
        x = np.linspace(0, L, 100)
        
        # Calculate maximum values
        M_max = w_u * L**2 / 8  # Maximum moment at midspan
        V_max = w_u * L / 2     # Maximum shear at supports
        
        # 1. Beam diagram
        ax1.plot([0, L], [0, 0], 'k-', linewidth=4, label='Simply Supported Beam')
        
        # Support symbols
        support_size = L * 0.03
        # Left support (pin)
        ax1.plot([0, -support_size, support_size, 0], 
                [0, -support_size*1.5, -support_size*1.5, 0], 'k-', linewidth=2)
        ax1.fill([0, -support_size, support_size], [0, -support_size*1.5, -support_size*1.5], 
                color='black')
        # Right support (roller)
        ax1.plot([L, L-support_size, L+support_size, L], 
                [0, -support_size*1.5, -support_size*1.5, 0], 'k-', linewidth=2)
        circle = plt.Circle((L, -support_size), support_size*0.4, 
                          color='white', ec='black', linewidth=2)
        ax1.add_patch(circle)
        
        # Load arrows
        n_arrows = 6
        x_arrows = np.linspace(L*0.15, L*0.85, n_arrows)
        for x_arr in x_arrows:
            ax1.annotate('', xy=(x_arr, 0), xytext=(x_arr, L*0.1),
                        arrowprops=dict(arrowstyle='->', color=GHALI_COLORS['red'], lw=2))
        
        ax1.text(L/2, L*0.12, f'w = {w_u:.1f} kN/m', ha='center', va='bottom',
                fontweight='bold', color=GHALI_COLORS['red'])
        ax1.text(L/2, -support_size*2.5, f'L = {L:.1f} m', ha='center', va='top',
                fontweight='bold')
        
        ax1.set_xlim(-L*0.1, L*1.1)
        ax1.set_ylim(-support_size*3, L*0.15)
        ax1.set_title('Simply Supported Beam with Uniform Load', 
                     fontweight='bold', color=GHALI_COLORS['blue'], fontsize=14)
        ax1.set_ylabel('Load')
        ax1.grid(True, alpha=0.3)
        ax1.legend()
        
        # 2. Shear Force Diagram
        V = w_u * L / 2 - w_u * x  # Shear force equation
        
        ax2.plot(x, V, 'b-', linewidth=2.5, color=GHALI_COLORS['blue'])
        ax2.fill_between(x, 0, V, alpha=0.3, color=GHALI_COLORS['blue'])
        ax2.axhline(y=0, color='black', linewidth=1)
        ax2.axvline(x=L/2, color='gray', linestyle='--', alpha=0.7)
        
        # Add key values
        ax2.plot(0, V_max, 'ro', markersize=8, color=GHALI_COLORS['red'])
        ax2.plot(L, -V_max, 'ro', markersize=8, color=GHALI_COLORS['red'])
        ax2.plot(L/2, 0, 'go', markersize=8, color=GHALI_COLORS['green'])
        
        ax2.text(0.05*L, V_max*0.8, f'+{V_max:.1f} kN', 
                fontweight='bold', color=GHALI_COLORS['red'])
        ax2.text(0.95*L, -V_max*0.8, f'-{V_max:.1f} kN', 
                fontweight='bold', color=GHALI_COLORS['red'], ha='right')
        ax2.text(L/2, V_max*0.15, '0', ha='center', fontweight='bold', 
                color=GHALI_COLORS['green'])
        
        ax2.set_xlim(0, L)
        ax2.set_ylabel('Shear Force (kN)')
        ax2.set_title('Shear Force Diagram', fontweight='bold', color=GHALI_COLORS['blue'])
        ax2.grid(True, alpha=0.3)
        
        # 3. Bending Moment Diagram (POSITIVE DOWNWARD - Structural Convention)
        M = w_u * x * (L - x) / 2  # Moment equation
        
        # Plot with positive moments downward (structural convention)
        ax3.plot(x, -M, 'r-', linewidth=2.5, color=GHALI_COLORS['red'])
        ax3.fill_between(x, 0, -M, alpha=0.3, color=GHALI_COLORS['red'])
        ax3.axhline(y=0, color='black', linewidth=1)
        ax3.axvline(x=L/2, color='gray', linestyle='--', alpha=0.7)
        
        # Add maximum moment annotation
        ax3.plot(L/2, -M_max, 'ro', markersize=10, color=GHALI_COLORS['red'])
        ax3.text(L/2, -M_max*1.15, f'M_max = {M_max:.1f} kN·m\n(at midspan)', 
                ha='center', va='top', fontweight='bold', 
                color=GHALI_COLORS['red'], fontsize=11,
                bbox=dict(boxstyle="round,pad=0.3", facecolor='white', alpha=0.8))
        
        # Zero moments at supports
        ax3.plot([0, L], [0, 0], 'go', markersize=6, color=GHALI_COLORS['green'])
        
        ax3.set_xlim(0, L)
        ax3.set_xlabel('Distance from Left Support (m)')
        ax3.set_ylabel('Bending Moment (kN·m)')
        ax3.set_title('Bending Moment Diagram (Positive Downward - Structural Convention)', 
                     fontweight='bold', color=GHALI_COLORS['blue'])
        ax3.grid(True, alpha=0.3)
        
        # Add note about sign convention
        ax3.text(0.02*L, -M_max*0.1, 'Note: Positive moments shown downward\n(structural engineering convention)', 
                va='top', fontsize=9, style='italic', color=GHALI_COLORS['gray'],
                bbox=dict(boxstyle="round,pad=0.3", facecolor='lightyellow', alpha=0.8))
        
        plt.tight_layout()
        plt.savefig(self.output_dir / f"{save_name}.png", dpi=300, bbox_inches='tight')
        plt.savefig(self.output_dir / f"{save_name}.pdf", dpi=300, bbox_inches='tight')
        plt.close()
        
        return str(self.output_dir / f"{save_name}.pdf"), M_max, V_max
    
    def plot_steel_layout(self, beam_width, beam_height, As_req, bar_diameter, 
                         cover=40, save_name="steel_layout"):
        """
        Plot reinforcement steel layout
        
        Args:
            beam_width: Beam width (mm)
            beam_height: Beam height (mm)
            As_req: Required steel area (mm²)
            bar_diameter: Rebar diameter (mm)
            cover: Concrete cover (mm)
            save_name: Name for saved figure
        """
        fig, ax = plt.subplots(1, 1, figsize=(10, 8))
        
        # Calculate number of bars needed
        bar_area = np.pi * (bar_diameter/2)**2
        n_bars = int(np.ceil(As_req / bar_area))
        
        # Beam outline
        beam_outline = mpatches.Rectangle((0, 0), beam_width, beam_height, 
                                        linewidth=2, edgecolor='black', 
                                        facecolor=GHALI_COLORS['light_blue'], 
                                        alpha=0.7)
        ax.add_patch(beam_outline)
        
        # Steel bars positioning
        clear_width = beam_width - 2*cover
        if n_bars == 1:
            bar_spacing = 0
            bar_positions = [beam_width/2]
        else:
            bar_spacing = clear_width / (n_bars - 1)
            bar_positions = [cover + i*bar_spacing for i in range(n_bars)]
        
        # Draw steel bars
        bar_y = cover
        for i, x_pos in enumerate(bar_positions):
            circle = plt.Circle((x_pos, bar_y), bar_diameter/2, 
                              color=GHALI_COLORS['red'], alpha=0.8)
            ax.add_patch(circle)
            # Add bar label
            ax.text(x_pos, bar_y, f'#{int(bar_diameter)}', ha='center', va='center', 
                   fontsize=8, fontweight='bold', color='white')
        
        # Dimensions
        # Cover dimensions
        ax.annotate('', xy=(0, bar_y), xytext=(cover, bar_y),
                   arrowprops=dict(arrowstyle='<->', color='green', lw=1.5))
        ax.text(cover/2, bar_y + bar_diameter, f'{cover}mm', ha='center', va='bottom',
               fontsize=9, color='green', fontweight='bold')
        
        ax.annotate('', xy=(beam_width-cover, bar_y), xytext=(beam_width, bar_y),
                   arrowprops=dict(arrowstyle='<->', color='green', lw=1.5))
        ax.text(beam_width-cover/2, bar_y + bar_diameter, f'{cover}mm', ha='center', va='bottom',
               fontsize=9, color='green', fontweight='bold')
        
        # Overall dimensions
        ax.annotate('', xy=(0, -beam_height*0.1), xytext=(beam_width, -beam_height*0.1),
                   arrowprops=dict(arrowstyle='<->', color='black', lw=2))
        ax.text(beam_width/2, -beam_height*0.15, f'{beam_width}mm', ha='center', va='top',
               fontsize=11, fontweight='bold')
        
        ax.annotate('', xy=(-beam_width*0.05, 0), xytext=(-beam_width*0.05, beam_height),
                   arrowprops=dict(arrowstyle='<->', color='black', lw=2))
        ax.text(-beam_width*0.1, beam_height/2, f'{beam_height}mm', ha='right', va='center',
               fontsize=11, fontweight='bold', rotation=90)
        
        # Steel information table
        info_text = f"""Steel Layout Information:
Required As: {As_req:.0f} mm²
Bar Size: #{bar_diameter}mm
Bar Area: {bar_area:.1f} mm²
Number of Bars: {n_bars}
Provided As: {n_bars * bar_area:.0f} mm²
Cover: {cover}mm"""
        
        ax.text(beam_width*1.05, beam_height*0.7, info_text, 
               fontsize=10, va='top', ha='left',
               bbox=dict(boxstyle="round,pad=0.5", facecolor='white', 
                        edgecolor=GHALI_COLORS['blue'], linewidth=1.5))
        
        ax.set_xlim(-beam_width*0.2, beam_width*1.4)
        ax.set_ylim(-beam_height*0.25, beam_height*1.1)
        ax.set_xlabel('Width (mm)')
        ax.set_ylabel('Height (mm)')
        ax.set_title(f'Reinforcement Steel Layout - {n_bars}#{bar_diameter}mm Bars', 
                    fontweight='bold', color=GHALI_COLORS['blue'], fontsize=14)
        ax.set_aspect('equal')
        ax.grid(True, alpha=0.3)
        
        plt.tight_layout()
        plt.savefig(self.output_dir / f"{save_name}.png", dpi=300, bbox_inches='tight')
        plt.savefig(self.output_dir / f"{save_name}.pdf", dpi=300, bbox_inches='tight')
        plt.close()
        
        return str(self.output_dir / f"{save_name}.pdf"), n_bars, n_bars * bar_area

def create_all_structural_plots(beam_data, output_dir="reports/figures"):
    """
    Create all structural plots for the calculation sheet
    
    Args:
        beam_data: Dictionary containing all beam parameters
        output_dir: Output directory for figures
        
    Returns:
        Dictionary with figure paths and calculated values
    """
    plotter = StructuralPlotter(output_dir)
    
    # Extract parameters
    L = beam_data['length']  # m
    w_d = beam_data['dead_load']  # kN/m
    w_l = beam_data['live_load']  # kN/m
    w_u = beam_data['factored_load']  # kN/m
    beam_width = beam_data['width']  # mm
    beam_height = beam_data['height']  # mm
    As_req = beam_data['steel_area_req']  # mm²
    bar_diameter = beam_data.get('bar_diameter', 20)  # mm
    
    results = {}
    
    # 1. Beam geometry and loading
    beam_fig = plotter.plot_beam_diagram(L, w_d, w_l, beam_width, beam_height)
    results['beam_diagram'] = beam_fig
    
    # 2. BMD and SFD
    bmd_sfd_fig, M_max, V_max = plotter.plot_bmd_sfd(L, w_u)
    results['bmd_sfd_diagram'] = bmd_sfd_fig
    results['M_max'] = M_max
    results['V_max'] = V_max
    
    # 3. Steel layout
    steel_fig, n_bars, As_provided = plotter.plot_steel_layout(
        beam_width, beam_height, As_req, bar_diameter)
    results['steel_layout'] = steel_fig
    results['n_bars'] = n_bars
    results['As_provided'] = As_provided
    
    return results

if __name__ == "__main__":
    # Example usage
    sample_beam = {
        'length': 6.0,  # m
        'dead_load': 15.0,  # kN/m
        'live_load': 20.0,  # kN/m
        'factored_load': 49.0,  # kN/m (1.2*15 + 1.6*20)
        'width': 300,  # mm
        'height': 500,  # mm
        'steel_area_req': 1200,  # mm²
        'bar_diameter': 20  # mm
    }
    
    results = create_all_structural_plots(sample_beam)
    print("Generated plots:")
    for key, value in results.items():
        print(f"  {key}: {value}") 