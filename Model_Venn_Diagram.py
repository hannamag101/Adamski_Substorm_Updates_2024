import numpy as np
import matplotlib.pyplot as plt
import pandas as pd
import os
import datetime
from datetime import datetime
from matplotlib_venn import venn3, venn3_circles
import matplotlib.colors as colors
from matplotlib.transforms import ScaledTranslation
import matplotlib as mpl
from open_csv import *

# Create venn diagrams of 10, 20, 30, ... 60 minute increments
def create_model_venn_diagram():
    # Read in Provided Summary Statistics Table 
    url = f"https://raw.githubusercontent.com/hannamag101/Adamski_Substorm_Updates_2024/main/Summary_Statistics_Indices/Summary_Table_10_300.csv"
    summary = pd.read_csv(url, index_col = 0)
    
    # Shape of data
    forsyth = open_csv("Forsyth")
    ohtani = open_csv("Ohtani")
    ng = open_csv("NG")

    # Create Venn Diagrams for 10, 20, 30, 40, 50, 60 minute increments
    figure, axes = plt.subplots(2, 3, figsize = (20,10), layout = 'constrained')
    colormap = plt.cm.get_cmap('inferno')
    norm5 = colors.Normalize(vmin=0, vmax=0.5) # matplotlib.colors
    sm5 = plt.cm.ScalarMappable(cmap=colormap, norm = norm5)

    sizes10 = [int(summary.loc[0, 'F']), int(summary.loc[0, 'O']), int(summary.loc[0, 'N']), int(summary.loc[0, 'F+O']), int(summary.loc[0, 'F+N']), int(summary.loc[0, 'O+N']), int(summary.loc[0, 'F+O+N'])]
    sizes20 = [int(summary.loc[1, 'F']), int(summary.loc[1, 'O']), int(summary.loc[1, 'N']), int(summary.loc[1, 'F+O']), int(summary.loc[1, 'F+N']), int(summary.loc[1, 'O+N']), int(summary.loc[1, 'F+O+N'])]
    sizes30 = [int(summary.loc[2, 'F']), int(summary.loc[2, 'O']), int(summary.loc[2, 'N']), int(summary.loc[2, 'F+O']), int(summary.loc[2, 'F+N']), int(summary.loc[2, 'O+N']), int(summary.loc[2, 'F+O+N'])]
    sizes40 = [int(summary.loc[3, 'F']), int(summary.loc[3, 'O']), int(summary.loc[3, 'N']), int(summary.loc[3, 'F+O']), int(summary.loc[3, 'F+N']), int(summary.loc[3, 'O+N']), int(summary.loc[3, 'F+O+N'])]
    sizes50 = [int(summary.loc[4, 'F']), int(summary.loc[4, 'O']), int(summary.loc[4, 'N']), int(summary.loc[4, 'F+O']), int(summary.loc[4, 'F+N']), int(summary.loc[4, 'O+N']), int(summary.loc[4, 'F+O+N'])]
    sizes60 = [int(summary.loc[5, 'F']), int(summary.loc[5, 'O']), int(summary.loc[5, 'N']), int(summary.loc[5, 'F+O']), int(summary.loc[5, 'F+N']), int(summary.loc[5, 'O+N']), int(summary.loc[5, 'F+O+N'])]

    # df10 - info
    size10_result = [x/summary.loc[0, 'Total'] for x in sizes10]
    total = summary.loc[0, 'Total']
    axes[0,0].set_title('10 Minute Binning ')
    axes[0,0].text(0.0, 1.0, 'a)', transform=(
                axes[0,0].transAxes + ScaledTranslation(-20/72, +7/72, figure.dpi_scale_trans)),
            fontsize=15, va='bottom', fontfamily='serif')
    one = venn3(subsets = (int(summary.loc[0, 'F']), int(summary.loc[0, 'O']), int(summary.loc[0, 'F+O']), int(summary.loc[0, 'N']),
                    int(summary.loc[0, 'F+N']), int(summary.loc[0, 'O+N']), int(summary.loc[0, 'F+O+N'])), 
                    set_labels = (f'Forsyth: \n N = {np.shape(forsyth)[0]}', f'Ohtani: \n N = {np.shape(ohtani)[0]}', f'Newell: \n N = {np.shape(ng)[0]}'), 
                    alpha = 0.7, ax = axes[0,0],
                    subset_label_formatter = lambda x: f"{(x/total):1.0%} \n({x})")

    # Order in set(100,010,110,001,101,011,111) format
    one.get_patch_by_id('100').set_color(colormap(norm5(size10_result)[0]))
    one.get_patch_by_id('010').set_color(colormap(norm5(size10_result)[1]))
    one.get_patch_by_id('110').set_color(colormap(norm5(size10_result)[2]))
    one.get_patch_by_id('001').set_color(colormap(norm5(size10_result)[3]))
    one.get_patch_by_id('101').set_color(colormap(norm5(size10_result)[4]))
    one.get_patch_by_id('011').set_color(colormap(norm5(size10_result)[5]))
    one.get_patch_by_id('111').set_color(colormap(norm5(size10_result)[6]))

    # Subset text fontsize
    for text in one.subset_labels:
        text.set_fontsize(9)

    venn3_circles(subsets = (int(summary.loc[0, 'F']), int(summary.loc[0, 'O']),  int(summary.loc[0, 'F+O']), int(summary.loc[0, 'N']),
                    int(summary.loc[0, 'F+N']), int(summary.loc[0, 'O+N']), int(summary.loc[0, 'F+O+N'])),
                    linestyle = "dashed", linewidth = 0.5, ax = axes[0,0])

    # df20 - info
    size20_result = [x/summary.loc[1, 'Total'] for x in sizes20]
    axes[0,1].set_title('20 Minute Binning')
    axes[0,1].text(0.0, 1.0, 'b)', transform=(
                axes[0,1].transAxes + ScaledTranslation(-20/72, +7/72, figure.dpi_scale_trans)),
            fontsize=15, va='bottom', fontfamily='serif')
    two = venn3(subsets = (int(summary.loc[1, 'F']), int(summary.loc[1, 'O']),int(summary.loc[1, 'F+O']),  int(summary.loc[1, 'N']),
                    int(summary.loc[1, 'F+N']), int(summary.loc[1, 'O+N']), int(summary.loc[1, 'F+O+N'])), 
                    set_labels = (f'Forsyth: \n N = {np.shape(forsyth)[0]}', f'Ohtani: \n N = {np.shape(ohtani)[0]}', f'Newell: \n N = {np.shape(ng)[0]}'), 
                    alpha = 0.7, ax = axes[0,1],
                    subset_label_formatter = lambda x: f"{(x/total):1.0%}\n ({x})")

    # Order in set(100,010,110,001,101,011,111) format
    two.get_patch_by_id('100').set_color(colormap(norm5(size20_result)[0]))
    two.get_patch_by_id('010').set_color(colormap(norm5(size20_result)[1]))
    two.get_patch_by_id('110').set_color(colormap(norm5(size20_result)[2]))
    two.get_patch_by_id('001').set_color(colormap(norm5(size20_result)[3]))
    two.get_patch_by_id('101').set_color(colormap(norm5(size20_result)[4]))
    two.get_patch_by_id('011').set_color(colormap(norm5(size20_result)[5]))
    two.get_patch_by_id('111').set_color(colormap(norm5(size20_result)[6]))

    # Subset text fontsize
    for text in two.subset_labels:
        text.set_fontsize(9)

    venn3_circles(subsets = (int(summary.loc[1, 'F']), int(summary.loc[1, 'O']), int(summary.loc[1, 'F+O']), int(summary.loc[1, 'N']),
                    int(summary.loc[1, 'F+N']),  int(summary.loc[1, 'O+N']), int(summary.loc[1, 'F+O+N'])),
                    linestyle = "dashed", linewidth = 0.5, ax = axes[0,1])

    # df30 - info
    size30_result = [x/summary.loc[2, 'Total'] for x in sizes30]
    axes[0,2].set_title('30 Minute Binning')
    axes[0,2].text(0.0, 1.0, 'c)', transform=(
                axes[0,2].transAxes + ScaledTranslation(-20/72, +7/72, figure.dpi_scale_trans)),
            fontsize=15, va='bottom', fontfamily='serif')
    three = venn3(subsets = (int(summary.loc[2, 'F']), int(summary.loc[2, 'O']), int(summary.loc[2, 'F+O']), int(summary.loc[2, 'N']),
                    int(summary.loc[2, 'F+N']), int(summary.loc[2, 'O+N']), int(summary.loc[2, 'F+O+N'])), 
                    set_labels = (f'Forsyth: \n N = {np.shape(forsyth)[0]}', f'Ohtani: \n N = {np.shape(ohtani)[0]}', f'Newell: \n N = {np.shape(ng)[0]}'), 
                    alpha = 0.7, ax = axes[0,2],
                    subset_label_formatter = lambda x: f"{(x/total):1.0%}\n ({x})")

    # Order in set(100,010,110,001,101,011,111) format
    three.get_patch_by_id('100').set_color(colormap(norm5(size30_result)[0]))
    three.get_patch_by_id('010').set_color(colormap(norm5(size30_result)[1]))
    three.get_patch_by_id('110').set_color(colormap(norm5(size30_result)[2]))
    three.get_patch_by_id('001').set_color(colormap(norm5(size30_result)[3]))
    three.get_patch_by_id('101').set_color(colormap(norm5(size30_result)[4]))
    three.get_patch_by_id('011').set_color(colormap(norm5(size30_result)[5]))
    three.get_patch_by_id('111').set_color(colormap(norm5(size30_result)[6]))

    # Subset text fontsize
    for text in three.subset_labels:
        text.set_fontsize(9)

    venn3_circles(subsets = (int(summary.loc[2, 'F']), int(summary.loc[2, 'O']), int(summary.loc[2, 'F+O']), int(summary.loc[2, 'N']),
                    int(summary.loc[2, 'F+N']), int(summary.loc[2, 'O+N']), int(summary.loc[2, 'F+O+N'])),
                    linestyle = "dashed", linewidth = 0.5, ax = axes[0,2])


    # df40 - info
    size40_result = [x/summary.loc[3, 'Total'] for x in sizes40]
    axes[1,0].set_title('40 Minute Binning ')
    axes[1,0].text(0.0, 1.0, 'd)', transform=(
                axes[1,0].transAxes + ScaledTranslation(-20/72, +7/72, figure.dpi_scale_trans)),
            fontsize=15, va='bottom', fontfamily='serif')
    four = venn3(subsets = (int(summary.loc[3, 'F']), int(summary.loc[3, 'O']), int(summary.loc[3, 'F+O']), int(summary.loc[3, 'N']),
                    int(summary.loc[3, 'F+N']), int(summary.loc[3, 'O+N']), int(summary.loc[3, 'F+O+N'])), 
                    set_labels = (f'Forsyth: \n N = {np.shape(forsyth)[0]}', f'Ohtani: \n N = {np.shape(ohtani)[0]}', f'Newell: \n N = {np.shape(ng)[0]}'), 
                    alpha = 0.7, ax = axes[1,0],
                    subset_label_formatter = lambda x: f"{(x/total):1.0%} \n({x})")

    # Order in set(100,010,110,001,101,011,111) format
    four.get_patch_by_id('100').set_color(colormap(norm5(size40_result)[0]))
    four.get_patch_by_id('010').set_color(colormap(norm5(size40_result)[1]))
    four.get_patch_by_id('110').set_color(colormap(norm5(size40_result)[2]))
    four.get_patch_by_id('001').set_color(colormap(norm5(size40_result)[3]))
    four.get_patch_by_id('101').set_color(colormap(norm5(size40_result)[4]))
    four.get_patch_by_id('011').set_color(colormap(norm5(size40_result)[5]))
    four.get_patch_by_id('111').set_color(colormap(norm5(size40_result)[6]))

    # Subset text fontsize
    for text in one.subset_labels:
        text.set_fontsize(9)

    venn3_circles(subsets = (int(summary.loc[3, 'F']), int(summary.loc[3, 'O']), int(summary.loc[3, 'F+O']), int(summary.loc[3, 'N']),
                    int(summary.loc[3, 'F+N']), int(summary.loc[3, 'O+N']), int(summary.loc[3, 'F+O+N'])),
                    linestyle = "dashed", linewidth = 0.5, ax = axes[1,0])

    # df50 - info
    size50_result = [x/summary.loc[4, 'Total'] for x in sizes50]
    axes[1,1].set_title('50 Minute Binning')
    axes[1,1].text(0.0, 1.0, 'e)', transform=(
                axes[1,1].transAxes + ScaledTranslation(-20/72, +7/72, figure.dpi_scale_trans)),
            fontsize=15, va='bottom', fontfamily='serif')
    five = venn3(subsets = (int(summary.loc[4, 'F']), int(summary.loc[4, 'O']),int(summary.loc[4, 'F+O']),  int(summary.loc[4, 'N']),
                    int(summary.loc[4, 'F+N']), int(summary.loc[4, 'O+N']), int(summary.loc[4, 'F+O+N'])), 
                    set_labels = (f'Forsyth: \n N = {np.shape(forsyth)[0]}', f'Ohtani: \n N = {np.shape(ohtani)[0]}', f'Newell: \n N = {np.shape(ng)[0]}'), 
                    alpha = 0.7, ax = axes[1,1],
                    subset_label_formatter = lambda x: f"{(x/total):1.0%}\n ({x})")

    # Order in set(100,010,110,001,101,011,111) format
    five.get_patch_by_id('100').set_color(colormap(norm5(size50_result)[0]))
    five.get_patch_by_id('010').set_color(colormap(norm5(size50_result)[1]))
    five.get_patch_by_id('110').set_color(colormap(norm5(size50_result)[2]))
    five.get_patch_by_id('001').set_color(colormap(norm5(size50_result)[3]))
    five.get_patch_by_id('101').set_color(colormap(norm5(size50_result)[4]))
    five.get_patch_by_id('011').set_color(colormap(norm5(size50_result)[5]))
    five.get_patch_by_id('111').set_color(colormap(norm5(size50_result)[6]))

    # Subset text fontsize
    for text in two.subset_labels:
        text.set_fontsize(9)

    venn3_circles(subsets = (int(summary.loc[4, 'F']), int(summary.loc[4, 'O']),int(summary.loc[4, 'F+O']),  int(summary.loc[4, 'N']),
                    int(summary.loc[4, 'F+N']), int(summary.loc[4, 'O+N']), int(summary.loc[4, 'F+O+N'])),
                    linestyle = "dashed", linewidth = 0.5, ax = axes[1,1])

    # df60 - info
    size60_result = [x/summary.loc[5, 'Total'] for x in sizes60]
    axes[1,2].set_title('1 Hour Binning')
    axes[1,2].text(0.0, 1.0, 'f)', transform=(
                axes[1,2].transAxes + ScaledTranslation(-20/72, +7/72, figure.dpi_scale_trans)),
            fontsize=15, va='bottom', fontfamily='serif')
    six = venn3(subsets = (int(summary.loc[5, 'F']), int(summary.loc[5, 'O']), int(summary.loc[5, 'F+O']), int(summary.loc[5, 'N']),
                    int(summary.loc[5, 'F+N']), int(summary.loc[5, 'O+N']), int(summary.loc[5, 'F+O+N'])), 
                    set_labels = (f'Forsyth: \n N = {np.shape(forsyth)[0]}', f'Ohtani: \n N = {np.shape(ohtani)[0]}', f'Newell: \n N = {np.shape(ng)[0]}'), 
                    alpha = 0.7, ax = axes[1,2],
                    subset_label_formatter = lambda x: f"{(x/total):1.0%}\n ({x})")

    # Order in set(100,010,110,001,101,011,111) format
    six.get_patch_by_id('100').set_color(colormap(norm5(size60_result)[0]))
    six.get_patch_by_id('010').set_color(colormap(norm5(size60_result)[1]))
    six.get_patch_by_id('110').set_color(colormap(norm5(size60_result)[2]))
    six.get_patch_by_id('001').set_color(colormap(norm5(size60_result)[3]))
    six.get_patch_by_id('101').set_color(colormap(norm5(size60_result)[4]))
    six.get_patch_by_id('011').set_color(colormap(norm5(size60_result)[5]))
    six.get_patch_by_id('111').set_color(colormap(norm5(size60_result)[6]))

    # Subset text fontsize
    for text in three.subset_labels:
        text.set_fontsize(9)

    venn3_circles(subsets = (int(summary.loc[5, 'F']), int(summary.loc[5, 'O']), int(summary.loc[5, 'F+O']), int(summary.loc[5, 'N']),
                    int(summary.loc[5, 'F+N']), int(summary.loc[5, 'O+N']), int(summary.loc[5, 'F+O+N'])),
                    linestyle = "dashed", linewidth = 0.5, ax = axes[1,2])

    p0 = axes[1,0].get_position().get_points().flatten()
    p1 = axes[1,1].get_position().get_points().flatten()
    p2 = axes[1,2].get_position().get_points().flatten()
    ax_cbar = figure.add_axes([p0[0], -.1 , p2[2]-p0[0], 0.05]) # [a,b,c,d] (a,b) = southwest point, c = width, d = height
    cb = figure.colorbar(sm5, cax=ax_cbar, orientation='horizontal', pad = 10.2)
    cb.set_label('Percentage of Total Classifed Earth Substorms')
    cb.set_ticks([0, 0.1, 0.2, 0.3, 0.4, 0.5])
    cb.set_ticklabels(['0%', '10%', '20%', '30%', '40%', '50%'])

    #plt.savefig("./visualizations/venn_diag_final.jpeg", dpi = 300)
    plt.show()


# Actual code to generate MODEL Venn Diagrams
create_model_venn_diagram()