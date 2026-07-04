import os
import banduppy
import pickle
import numpy as np
import matplotlib.pyplot as plt
from mpl_toolkits.axes_grid1 import make_axes_locatable



def read_energies_weights(filename):
    energies = []
    weights = []
    with open(filename, 'r') as f:
        for line in f:
            if line.strip().startswith('#') or not line.strip():
                continue
            cols = line.split()
            energies.append(float(cols[2]))
            weights.append(float(cols[3]))
    return np.array(energies), np.array(weights)

def lorentzian_dos(energies, weights, E_grid, eta, normalize=False):
    diff = E_grid[:, None] - energies[None, :]
    L = eta / (np.pi * (diff**2 + eta**2))
    dos = np.dot(L, weights)
    if normalize:
        dos /= np.sum(weights) * (E_grid[1] - E_grid[0])
    return dos








# Define the simulation folder and file prefix
sim_folder = '/storage/JOSIPDUJMENOVIC_STORAGE/graphene/bands_4x4/polaron'
prefix = os.path.join(sim_folder, 'graphene')

# Define the supercell size for graphene 4x4x1
super_cell_size = [[4, 0, 0], [0, 4, 0], [0, 0, 1]]

# Initialize the Unfolding object
band_unfold = banduppy.Unfolding(supercell=super_cell_size, print_log='high')

# Define a detailed k-path in the primitive Brillouin zone
PC_BZ_path = [
    [0.0, 0.0, 0.0],  # Γ
    [0.33333, 0.33333, 0.0],  # K
    [0, 0.5, 0.0],  # M
    [0.0, 0.0, 0.0]   # Γ
]
# Provide a label for each node in the detailed k-path.
# (You might use more labels if your path is divided into more segments.)
special_k_points = "GKMG"  # Adjust labels as needed

# Specify a detailed number of k-points for each segment to get a continuous path.
npoints_per_path_seg = (110, 80, 110)
###npoints_per_path_seg = (38, 29, 33) #100
###npoints_per_path_seg = (49, 31, 50) #130
###npoints_per_path_seg = (53, 40, 47) ##140
##npoints_per_path_seg = (84, 65, 51)  #200

# Save the SC k-points file so you can inspect it (set to True for debugging)
save_sc = True

# Generate the SC k-points from the primitive cell k-path.

kpointsPBZ_full, kpointsPBZ_unique, kpointsSBZ, SBZ_PBZ_kpts_mapping, special_kpoints_pos_labels = \
    band_unfold.generate_SC_Kpts_from_pc_k_path(
        pathPBZ=PC_BZ_path,
        nk=npoints_per_path_seg,
        labels=special_k_points,
        kpts_weights=1,
        save_all_kpts=True,
        save_sc_kpts=True,
        save_dir=sim_folder,
        file_name_suffix='',
        file_format='qe'
    )

#print("Generated kpline:", band_unfold.kpline)
#print("Number of kpoints in kpline:", len(band_unfold.kpline))

# Now, ensure your NSCF run used the same k-points.
# Read the band structure from the NSCF calculation.
bands = banduppy.BandStructure(code="espresso", spinor=False, prefix=prefix)
#pickle.dump(bands,open(f"{results_dir}/bandstructure.pickle","wb"))
print ("- Reading band structure - done")



# Perform the unfolding
results_dir = sim_folder
unfolded_bandstructure, kpline = band_unfold.Unfold(
    bands,
    kline_discontinuity_threshold=0.1,
    save_unfolded_kpts={'save2file': True, 'fdir': results_dir, 'fname': 'kpoints_unfolded'},
    save_unfolded_bandstr={'save2file': True, 'fdir': results_dir, 'fname': 'bandstructure_unfolded'}
)

print("Unfolding completed.")


# Define Fermi energy and energy range (choose these based on your SCF output)
Efermi = -4.5753     # Fermi energy from the 2x2 (unfolded) calculation
Emin = -5           # Minimum energy to plot (relative to Efermi)
Emax = 10            # Maximum energy to plot (relative to Efermi)
save_file_name = 'unfolded_bandstructure1.png'
with open(f'{results_dir}/KPOINTS_SpecialKpoints.pkl', 'rb') as handle:
    special_kpoints_pos_labels = pickle.load(handle)




plot_unfold = banduppy.Plotting(save_figure_dir=results_dir)


# You can call the built-in plot function from your Unfolding object
fig, ax, CountFig = band_unfold.plot_ebs(
    save_figure_dir=results_dir,
    save_file_name=save_file_name,
    CountFig=None, 
    Ef=Efermi,         # Here you pass the Fermi level of your 2x2 calculation
    Emin=Emin,
    Emax=Emax,
    pad_energy_scale=0.5, 
    mode="density",    # Use density mode
    special_kpoints=special_kpoints_pos_labels, 
    plotSC=True, 
    fatfactor=20, 
    nE=100,
    smear=0.1, 
    marker='o',
    threshold_weight=0.01, 
    show_legend=True,
    color='gray', 
    color_map='viridis'
)

save_file_name = 'unfolded_bandstructure2.png'

fig, ax, CountFig \
= plot_unfold.plot_ebs(kpath_in_angs=kpline,
                       unfolded_bandstructure=unfolded_bandstructure,
                       save_file_name=save_file_name, CountFig=None,
                       Ef=Efermi, Emin=Emin, Emax=Emax, pad_energy_scale=0.5,
                       mode="fatband", special_kpoints=special_kpoints_pos_labels,
                       plotSC=True, fatfactor=20, nE=100,smear=0.1,
                       color='red', color_map='viridis', show_colorbar=False)

save_file_name = 'unfolded_bandstructure_spectral.png'

fig, ax, CountFig \
= band_unfold.plot_ebs(save_figure_dir=results_dir, save_file_name=save_file_name, CountFig=None, 
                      Ef=Efermi, Emin=Emin, Emax=Emax, pad_energy_scale=0.5, 
                      mode="density", special_kpoints=special_kpoints_pos_labels, 
                      plotSC=True, fatfactor=20, nE=100,smear=0.1, marker='o',
                      threshold_weight=0.01, show_legend=True,
                      color='gray', color_map='viridis')



# Full path to the input file
input_file = "/storage/JOSIPDUJMENOVIC_STORAGE/graphene/bands_4x4/polaron/bandstructure_unfolded.dat"
# Desired output file path
output_file = "/storage/JOSIPDUJMENOVIC_STORAGE/graphene/bands_4x4/polaron/bandstructure_unfolded.txt"

# Read and write the file
with open(input_file, "r") as infile, open(output_file, "w") as outfile:
    data = infile.read()
    outfile.write(data)





# Define Fermi energy and energy range (choose these based on your SCF output)
Efermi = -4.5753     # Fermi energy from the 2x2 (unfolded) calculation
Emin = -5           # Minimum energy to plot (relative to Efermi)
Emax = 10            # Maximum energy to plot (relative to Efermi)
E_F1x1 = -1.4374



save_file_name = 'TEST_-5_10.png'


fig, ax, CountFig \
= plot_unfold.plot_ebs(kpath_in_angs=kpline,
                       unfolded_bandstructure=unfolded_bandstructure,
                       save_file_name=save_file_name, CountFig=None,
                       Ef=Efermi, Emin=Emin, Emax=Emax, pad_energy_scale=0.5,
                       mode="fatband", special_kpoints=special_kpoints_pos_labels,
                       plotSC=True, fatfactor=20, nE=100,smear=0.1,
                       color='red', color_map='viridis', show_colorbar=False)






data = np.loadtxt("/storage/JOSIPDUJMENOVIC_STORAGE/graphene/bands_1x1/graphene.band.gnu")


k_values11 = data[:, 0]  # First column: k-points
energies11 = data[:, 1:]  # Remaining columns: Energy levels

C = kpline.max()/k_values11.max()



energies11 = (energies11-E_F1x1) 
k_values11 = k_values11*C

# --- 3) Overlay your 1×1 scatter ---
# energies11 is shape (Nk, Nbands); pick the band index you want, here band 0
ax.scatter(
    k_values11,
    energies11[:, 0],    # first band
    s     = 5,
    color = 'black',
    label = "1×1 band",
    zorder = 100         # make sure it sits on top
)




# --- 4) Final touches and save/show ---
ax.set_ylim(Emin, Emax)
ax.legend(loc='best')

# If plot_ebs already saved the figure, you may need to overwrite or just call:
fig.savefig('Graphene_4x4_P_1x1_-5_10.png', dpi=300, bbox_inches='tight')
plt.show()














file_pristine = "/storage/JOSIPDUJMENOVIC_STORAGE/graphene/bands_4x4/TEST1/stari/bandstructure_unfolded.txt"
file_vacancy  = "/storage/JOSIPDUJMENOVIC_STORAGE/graphene/bands_4x4/TEST1/stari/stariji/bandstructure_unfolded.txt"

E_F_prist = -4.8202
E_F_vac   = -3.0177



E_min, E_max, delta_E = -20, 9, 0.01
E_grid = np.arange(E_min, E_max, delta_E)

eta = 0.2  # eV
normalize = False  # ← Turn this ON or OFF as needed

# ——— Read & shift ———
E_prist, w_prist = read_energies_weights(file_pristine)
E_vac,   w_vac   = read_energies_weights(file_vacancy)

E_prist -= E_F_prist
E_vac   -= E_F_vac

# ——— Compute DOS ———
dos_prist = lorentzian_dos(E_prist, w_prist, E_grid, eta, normalize=False)
dos_vac   = lorentzian_dos(E_vac,   w_vac,   E_grid, eta, normalize=False)



mask_prist = E_grid >= 2.8
mask_vac = E_grid <= 2.8






E_min = [-19,-5,0]
E_max = 10




for i, Emin in enumerate(E_min):

    save_file_name = f'TEST2_{Emin}_10.png'

    fig, ax, CountFig \
    = band_unfold.plot_ebs(save_figure_dir=results_dir, save_file_name=save_file_name, CountFig=None, 
                          Ef=Efermi, Emin=Emin, Emax=E_max, pad_energy_scale=0.5, 
                          mode="density", special_kpoints=special_kpoints_pos_labels, 
                          plotSC=True, fatfactor=20, nE=100, smear=0.1, marker='o',
                          threshold_weight=0.01, show_legend=True,
                          color='gray', color_map='viridis')

    data = np.loadtxt("/storage/JOSIPDUJMENOVIC_STORAGE/graphene/bands_1x1/graphene.band.gnu")

    k_values11 = data[:, 0]
    energies11 = data[:, 1:]

    C = kpline.max() / k_values11.max()

    energies11 = (energies11 - E_F1x1)
    k_values11 = k_values11 * C

    ax.scatter(
        k_values11,
        energies11[:, 0],
        s=5,
        color='black',
        zorder=100
    )

    ax.set_ylim(Emin, Emax)

    divider = make_axes_locatable(ax)
    ax_dos = divider.append_axes("right", size="30%", pad=0.05, sharey=ax)

# Plot DOS (with aligned y-axis)
    ax_dos.plot(dos_prist[mask_prist], E_grid[mask_prist], color='blue')
    ax_dos.plot(dos_vac[mask_vac], E_grid[mask_vac], color='blue', label='bez smetnji')

# Add the z-polaron DOS
    file_vacancy = "/storage/JOSIPDUJMENOVIC_STORAGE/graphene/bands_4x4/TEST1/stari/stari_z_BZ/bandstructure_unfolded.txt"
    E_F_vac = -4.5781
    E_vac, w_vac = read_energies_weights(file_vacancy)
    E_vac -= E_F_vac
    dos_vac_z = lorentzian_dos(E_vac, w_vac, E_grid, eta, normalize=False)
    ax_dos.plot(dos_vac_z, E_grid, color='red', linestyle='--', label='z_polaron')

# Tidy up the DOS axis
    ax_dos.axhline(0, color='k', linestyle='--', linewidth=0.5)
    ax_dos.legend(loc='upper right', fontsize=8, frameon=False)
    ax_dos.set_xlim(left=0)
    ax_dos.set_xticks([])
#    ax_dos.set_yticks([])

# Optional: add label
    ax_dos.set_xlabel("DOS")

    fig.savefig(f'Graphene_4x4_P_{Emin}_10.png', dpi=300, bbox_inches='tight')
    plt.show()















######################################
# Define Fermi energy and energy range (choose these based on your SCF output)
Efermi = -4.5753     # Fermi energy from the 2x2 (unfolded) calculation
Emin = 2           # Minimum energy to plot (relative to Efermi)
Emax = 10            # Maximum energy to plot (relative to Efermi)
E_F1x1 = -1.4374



save_file_name = 'TEST_2_10.png'


fig, ax, CountFig \
= plot_unfold.plot_ebs(kpath_in_angs=kpline,
                       unfolded_bandstructure=unfolded_bandstructure,
                       save_file_name=save_file_name, CountFig=None,
                       Ef=Efermi, Emin=Emin, Emax=Emax, pad_energy_scale=0.5,
                       mode="fatband", special_kpoints=special_kpoints_pos_labels,
                       plotSC=True, fatfactor=20, nE=100,smear=0.1,
                       color='red', color_map='viridis', show_colorbar=False)






data = np.loadtxt("/storage/JOSIPDUJMENOVIC_STORAGE/graphene/bands_1x1/graphene.band.gnu")


k_values11 = data[:, 0]  # First column: k-points
energies11 = data[:, 1:]  # Remaining columns: Energy levels

C = kpline.max()/k_values11.max()



energies11 = (energies11-E_F1x1)
k_values11 = k_values11*C

# --- 3) Overlay your 1×1 scatter ---
# energies11 is shape (Nk, Nbands); pick the band index you want, here band 0
ax.scatter(
    k_values11,
    energies11[:, 0],    # first band
    s     = 5,
    color = 'black',
    label = "1×1 band",
    zorder = 100         # make sure it sits on top
)




# --- 4) Final touches and save/show ---
ax.set_ylim(Emin, Emax)
ax.legend(loc='best')

# If plot_ebs already saved the figure, you may need to overwrite or just call:
fig.savefig('Graphene_4x4_P_1x1_2_10.png', dpi=300, bbox_inches='tight')
plt.show()






for smear_value  in [0.1, 0.2, 0.5]:
    save_file_name = f'TEST2_smear_{smear_value}_2_10.png'

    fig, ax, CountFig \
    = band_unfold.plot_ebs(save_figure_dir=results_dir, save_file_name=save_file_name, CountFig=None,
                          Ef=Efermi, Emin=Emin, Emax=Emax, pad_energy_scale=0.5,
                          mode="density", special_kpoints=special_kpoints_pos_labels,
                          plotSC=True, fatfactor=20, nE=100, smear=smear_value, marker='o',
                          threshold_weight=0.01, show_legend=True,
                          color='gray', color_map='viridis')

    data = np.loadtxt("/storage/JOSIPDUJMENOVIC_STORAGE/graphene/bands_1x1/graphene.band.gnu")

    k_values11 = data[:, 0]
    energies11 = data[:, 1:]

    C = kpline.max() / k_values11.max()

    energies11 = (energies11 - E_F1x1)
    k_values11 = k_values11 * C

    ax.scatter(
        k_values11,
        energies11[:, 0],
        s=5,
        color='black',
        zorder=100
    )

    ax.set_ylim(Emin, Emax)

    fig.savefig(f'Graphene_4x4_P_smear_{smear_value}_2_10.png', dpi=300, bbox_inches='tight')
    plt.show()
