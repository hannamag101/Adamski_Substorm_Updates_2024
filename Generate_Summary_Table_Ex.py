import numpy as np
import matplotlib.pyplot as plt
import pandas as pd
import os
import datetime
from datetime import datetime
from matplotlib_venn import venn3, venn3_circles, venn3_unweighted
import matplotlib.colors as colors
from matplotlib.transforms import ScaledTranslation
import matplotlib as mpl
from open_csv import *

# Template to generate your own Index Initialization Dataframe (IID) + Venn Diagram
# We are going to use the example of the EXTREME 24 Hour Binning Increment
# Takes approximately ~ 2 min to sort onsets into dataframe

def generate_iid(frequency = 'D', save_ind = False): # Can replace with values such as '10min' or '50min'
    # Generate list of indices (24 hour increments)
    index24 = pd.date_range('1/1/1970', '1/1/2024', freq = frequency)

    # Shape of data
    forsyth = open_csv("Forsyth")
    ohtani = open_csv("Ohtani")
    ng = open_csv("NG")

    # Create Index Initialization Dataframe (IID)
    ind24 = pd.DataFrame(index = index24, columns = ['Forsyth', 'NG', 'Ohtani'])
    ind24['Forsyth'] = 0
    ind24['NG'] = 0
    ind24['Ohtani'] = 0

    # Fill out (+1) Counts in IID
    file_names = ['Forsyth', 'NG', 'Ohtani']
    files = [forsyth, ng, ohtani]
    for name, data in zip(file_names, files):
        data['Date_UTC'] = pd.to_datetime(data['Date_UTC'])
        for i in range(np.shape(data)[0]):
            # 1 day increments
            ind24[f'{name}'].iloc[ind24.index.get_indexer([data['Date_UTC'].iloc[i]], method = 'ffill')[0]] += 1

    if save_ind == True: # If you want to save the IID to your local machine
        ind24.to_csv('ind24.csv')

    # Reassign variable name with new index values (i.e. 0, ... # of rows)
    df24 = ind24.reset_index()
    df24.columns = ['Index', 'F', 'N', 'O']

    df24['F+N'] = np.zeros(np.shape(df24)[0])
    df24['F+O'] = np.zeros(np.shape(df24)[0])
    df24['O+N'] = np.zeros(np.shape(df24)[0])
    df24['F+O+N'] = np.zeros(np.shape(df24)[0])

    for i in range(np.shape(df24)[0]):
        if df24.loc[i, 'F'] >= 1 and df24.loc[i, 'N'] >= 1 and df24.loc[i, 'O'] == 0:
            df24.loc[i, 'F+N'] = df24.loc[i, 'F'] + df24.loc[i, 'N']
        else:
            df24.loc[i, 'F+N'] = 0
        
        if df24.loc[i, 'F'] >= 1 and df24.loc[i, 'O'] >= 1 and df24.loc[i, 'N'] == 0:
            df24.loc[i, 'F+O'] = df24.loc[i, 'F'] + df24.loc[i, 'O']
        else:
            df24.loc[i, 'F+O'] = 0

        if df24.loc[i, 'O'] >= 1 and df24.loc[i, 'N'] >= 1 and df24.loc[i, 'F'] == 0:
            df24.loc[i, 'O+N'] = df24.loc[i, 'O'] + df24.loc[i, 'N']
        else:
            df24.loc[i, 'O+N'] = 0

        if df24.loc[i, 'F'] >= 1 and df24.loc[i, 'N'] >= 1 and df24.loc[i, 'O'] >= 1:
            df24.loc[i, 'F+O+N'] = df24.loc[i, 'F'] + df24.loc[i, 'O'] + df24.loc[i, 'N']
        else:
            df24.loc[i, 'F+O+N'] = 0

    # FIND F, O, and N ONLY indices
    f24 = (np.where(df24['F']>0))[0]
    o24 = (np.where(df24['O']>0))[0]
    n24 = (np.where(df24['N']>0))[0]

    fn_24 = (np.where(df24['F+N']>0))[0]
    on_24 = (np.where(df24['O+N']>0))[0]
    fo_24 = (np.where(df24['F+O']>0))[0]
    fon24 = (np.where(df24['F+O+N']>0))[0]

    fcon = np.concatenate([fn_24, fo_24], axis = 0)
    fcon = np.concatenate([fcon, fon24], axis = 0)

    ocon = np.concatenate([on_24, fo_24], axis = 0)
    ocon = np.concatenate([ocon, fon24], axis = 0)

    ncon = np.concatenate([on_24, fn_24], axis = 0)
    ncon = np.concatenate([ncon, fon24], axis = 0)

    f24_solo = []
    for element in f24:
        if element not in fcon:
            f24_solo.append(element)

    o24_solo = []
    for element in o24:
        if element not in ocon:
            o24_solo.append(element)

    n24_solo = []
    for element in n24:
        if element not in ncon:
            n24_solo.append(element)

    f_n_24 = sum(df24['F+N'])
    o_n_24 = sum(df24['O+N'])
    f_o_24 = sum(df24['F+O'])
    fon_24 = sum(df24['F+O+N'])

    summary24 = pd.DataFrame(list(), columns = ['Dataset Index', 'F+N', 'F+O', 'O+N', 'F+O+N', 'F', 'O', 'N'])
    summary24['Dataset Index'] = ['df24']
    summary24.loc[0, 'F+N'] = f_n_24
    summary24.loc[0, 'F+O'] = f_o_24
    summary24.loc[0, 'O+N'] = o_n_24
    summary24.loc[0, 'F+O+N'] = fon_24
    summary24.loc[0, 'F'] = sum(df24.iloc[f24_solo]['F'])
    summary24.loc[0, 'O'] = sum(df24.iloc[o24_solo]['O'])
    summary24.loc[0, 'N'] = sum(df24.iloc[n24_solo]['N'])
    summary24['Total'] = sum(summary24.iloc[0, 1:8])

    # Create unweighted Venn Diagram for Bin Increment - 24 Hours
    figure, axes = plt.subplots(1, figsize = (14,8), layout = 'constrained')
    colormap = plt.cm.get_cmap('inferno')
    norm = colors.Normalize(vmin=0, vmax=1) # matplotlib.colors
    sm = plt.cm.ScalarMappable(cmap=colormap, norm = norm)

    sizes24 = [int(summary24.loc[0, 'F']), int(summary24.loc[0, 'O']), int(summary24.loc[0, 'F+O']), 
                int(summary24.loc[0, 'N']), int(summary24.loc[0, 'F+N']), int(summary24.loc[0, 'O+N']), 
                int(summary24.loc[0, 'F+O+N'])]

    # df24 - info
    total = summary24.loc[0, 'Total']
    size24_result = [x/summary24.loc[0, 'Total'] for x in sizes24]
    axes.set_title('24 Hour Binning ')

    one = venn3_unweighted(subsets = (int(summary24.loc[0, 'F']), int(summary24.loc[0, 'O']), int(summary24.loc[0, 'F+O']), 
                int(summary24.loc[0, 'N']), int(summary24.loc[0, 'F+N']), int(summary24.loc[0, 'O+N']), 
                int(summary24.loc[0, 'F+O+N'])), 
                    set_labels = (f'Forsyth: \n N = {np.shape(forsyth)[0]}', f'Ohtani: \n N = {np.shape(ohtani)[0]}', f'Newell: \n N = {np.shape(ng)[0]}'), 
                    alpha = 0.7, ax = axes,
                    subset_label_formatter = lambda x: f"{(x/total):1.0%} \n({x})")

    # Order in set(100,010,110,001,101,011,111) format
    one.get_patch_by_id('100').set_color(colormap(norm(size24_result)[0]))
    one.get_patch_by_id('010').set_color(colormap(norm(size24_result)[1]))
    one.get_patch_by_id('110').set_color(colormap(norm(size24_result)[2]))
    one.get_patch_by_id('001').set_color(colormap(norm(size24_result)[3]))
    one.get_patch_by_id('101').set_color(colormap(norm(size24_result)[4]))
    one.get_patch_by_id('011').set_color(colormap(norm(size24_result)[5]))
    one.get_patch_by_id('111').set_color(colormap(norm(size24_result)[6]))

    # Subset text fontsize
    for text in one.subset_labels:
        text.set_fontsize(9)

    venn3_circles(subsets=(1, 1, 1, 1, 1, 1, 1), linestyle='dashed')
    #venn3_circles(subsets = (int(summary24.loc[0, 'F']), int(summary24.loc[0, 'O']), int(summary24.loc[0, 'F+O']), 
                #int(summary24.loc[0, 'N']), int(summary24.loc[0, 'F+N']), int(summary24.loc[0, 'O+N']), 
                #int(summary24.loc[0, 'F+O+N'])), linestyle = "dashed", linewidth = 0.5, ax = axes)


    p0 = axes.get_position().get_points().flatten()

    ax_cbar = figure.add_axes([p0[0], -0.1, p0[2]-p0[0], 0.05])
    cb = plt.colorbar(sm, cax=ax_cbar, orientation='horizontal')
    cb.set_label('Percentage of Total Classifed Earth Substorms')
    cb.set_ticks([0, 0.25, 0.5, 0.75, 1])
    cb.set_ticklabels(['0%', '25%','50%','75%','100%'])

    #plt.savefig("./visualizations/venn_diag_final.jpeg", dpi = 300)
    plt.show()

    return summary24

# Actual Code - 24 Hour increment
summary_table = generate_iid()
# If we want to change the bin increment size we simply change the frequency argument
                    
