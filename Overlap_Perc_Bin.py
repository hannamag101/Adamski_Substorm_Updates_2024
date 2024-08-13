import numpy as np
import matplotlib.pyplot as plt
import pandas as pd
import os
import datetime
from datetime import datetime
from open_csv import *

# Plot overlap percentages across Forsyth, Newell, and Ohtani as a function of Bin Size
def generate_overlap_bin_plot():
    # Plot from 10 minutes to 3 hours - contents contained in GIVEN Summary Table .csv file
    x_vals1 = np.arange(10, 60, 10)
    x_vals2 = np.arange(60, 122, 2)
    x_vals = np.concatenate([x_vals1, x_vals2])
    x_vals3 = np.arange(150, 320, 30)
    x_vals = np.concatenate([x_vals, x_vals3])

    # Read in .csv file
    url = f"https://raw.githubusercontent.com/hannamag101/Adamski_Substorm_Updates_2024/main/Summary_Statistics_Indices/Summary_Table_10_300.csv"
    summary = pd.read_csv(url, index_col = 0)

    # Assign y values to various overlap regions
    y1 = np.array(summary['F+N'])
    y2 = np.array(summary['F+O'])
    y3 = np.array(summary['O+N'])
    y4 = np.array(summary['F+O+N'])

    # Plot 4 Subplots of Overlap evolution as a function of chosen bin increment size
    fig, ax = plt.subplots(2, 2, figsize = (10,10))
    ax[0,0].set_title("Forsyth + Newell Overlap")
    ax[0,0].set_xlabel("Bin Increment (min)")
    ax[0,0].set_ylabel("Count")
    ax[0,0].plot(x_vals, y1, label = 'F+N', linewidth = 0.75, color = 'black')
    ax[0,0].set_xticks(np.arange(10, 300, 10), minor = True)
    ax[0,0].set_xticks(np.arange(10, 300, 20))
    ax[0,0].set_xticklabels(np.arange(10, 300, 20), rotation = 45)
    ax[0,0].axvline(60, linestyle = "--", color = 'red', label = "Median Substorm Duration (Fogg et al. 2022)")
    for i in range(10, 310, 10):
        ax[0,0].axvline(i, linestyle = "--", color = 'lightgrey', alpha = 0.75, linewidth = 0.5)
    ax[0,0].set_xlim(10, 300)
    ax[0,0].legend(fontsize = 8)

    ax[0,1].set_title("Forsyth + Ohtani Overlap")
    ax[0,1].set_xlabel("Bin Increment (min)")
    ax[0,1].set_ylabel("Count")
    ax[0,1].plot(x_vals,  y2, label = 'F+O', linewidth = 0.75, color = 'black')
    ax[0,1].set_xticks(np.arange(10, 300, 10), minor = True)
    ax[0,1].set_xticks(np.arange(10, 300, 20))
    ax[0,1].set_xticklabels(np.arange(10, 300, 20), rotation = 45)
    ax[0,1].axvline(60, linestyle = "--", color = 'red', label = "Median Substorm Duration (Fogg et al. 2022)")
    for i in range(10, 310, 10):
        ax[0,1].axvline(i, linestyle = "--", color = 'lightgrey', alpha = 0.75, linewidth = 0.5)
    ax[0,1].set_xlim(10, 300)
    ax[0,1].legend(fontsize = 8)

    ax[1,0].set_title("Ohtani + Newell Overlap")
    ax[1,0].set_xlabel("Bin Increment (min)")
    ax[1,0].set_ylabel("Count")
    ax[1,0].plot(x_vals, y3, label = 'O+N', linewidth = 0.75, color = 'black')
    ax[1,0].set_xticks(np.arange(10, 300, 10), minor = True)
    ax[1,0].set_xticks(np.arange(10, 300, 20))
    ax[1,0].set_xticklabels(np.arange(10, 300, 20), rotation = 45)
    ax[1,0].axvline(60, linestyle = "--", color = 'red', label = "Median Substorm Duration (Fogg et al. 2022)")
    for i in range(10, 310, 10):
        ax[1,0].axvline(i, linestyle = "--", color = 'lightgrey', alpha = 0.75, linewidth = 0.5)
    ax[1,0].set_xlim(10, 300)
    ax[1,0].legend(fontsize = 8)

    ax[1,1].set_title("Forsyth + Ohtani + Newell Overlap")
    ax[1,1].set_xlabel("Bin Increment (min)")
    ax[1,1].set_ylabel("Count")
    ax[1,1].plot(x_vals, y4, label = 'F+O+N', linewidth = 0.75, color = 'black')
    ax[1,1].set_xticks(np.arange(10, 300, 10), minor = True)
    ax[1,1].set_xticks(np.arange(10, 300, 20))
    ax[1,1].set_xticklabels(np.arange(10, 300, 20), rotation = 45)
    ax[1,1].axvline(60, linestyle = "--", color = 'red', label = "Median Substorm Duration (Fogg et al. 2022)")
    for i in range(10, 310, 10):
        ax[1,1].axvline(i, linestyle = "--", color = 'lightgrey', alpha = 0.75, linewidth = 0.5)
    ax[1,1].set_xlim(10, 300)
    ax[1,1].legend(fontsize = 8)

    plt.tight_layout()
    plt.show()

# Actual code which plots overlap subplots
generate_overlap_bin_plot()