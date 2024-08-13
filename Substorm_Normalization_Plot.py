from open_csv import *
import numpy as np
import matplotlib.pyplot as plt
import pandas as pd
import os
import datetime
from datetime import datetime

def substorm_norm_visual():
    # Mean sunspot count from 1749 to 2022
    url_monthly_sunspot = "https://raw.githubusercontent.com/hannamag101/Adamski_Substorm_Updates_2024/main/Sunspot_Data/Sophie_Substorm_Lists/SN_13monthsmoothed_1749_now.txt"
    sunspot_df = pd.DataFrame(np.loadtxt(url_monthly_sunspot), columns = ["Year", "Month", "Fraction Date", "Smoothed Sunspot Number", "Monthly Mean STD of input sunspot numbers", "Total observations"])

    # Smoothed Sunspot Number >= 0 
    sunspot_df = sunspot_df.iloc[np.where(sunspot_df["Smoothed Sunspot Number"]>=0)]

    # Find average sunspot number for SPECIFIC year
    mean_sunspot = pd.DataFrame(list(), columns = ["Year", "Mean Sunspot Number"])
    for i, year in enumerate(np.unique(sunspot_df['Year'])):
        if i == 0:
            val = round(np.sum(sunspot_df[sunspot_df['Year'] == year]['Smoothed Sunspot Number']), 2)
            df_new = pd.DataFrame([[year, val]], columns = ["Year", "Mean Sunspot Number"])
            df_prev = pd.concat([df_new, mean_sunspot])
        else:
            val = round(np.sum(sunspot_df[sunspot_df['Year'] == year]['Smoothed Sunspot Number']), 2)
            df_new = pd.DataFrame([[year, val]], columns = ["Year", "Mean Sunspot Number"])
            df_prev = pd.concat([df_new, df_prev])

    # Plot Normalization of Substorm Onsets as a function of Dataset + Overlaid Solar Sunspot Cycle
    fig, ax = plt.subplots(1, figsize = (13,8))
    ax.set_title("Substorm Onset Normalization per Dataset ")

    color = 'tab:red'
    colo = ['tab:blue', 'tab:orange', 'tab:green', 'tab:red', 'tab:purple', 'tab:brown']
    ax.set_xlabel('Time (Yrs)')
    ax.set_ylabel('Substorm Normalization', color=color)
    xmin = []
    xmax = []
    all_vals = []

    j = 0
    for key in file_dict:
        if key == 'Soph50' or key == 'Soph75':
            pass        
        else:
            data = open_csv(key)
            year = [data.iloc[i, 0].year for i in range(np.shape(data)[0])]
            xmin.append(min(np.unique(year, return_counts = True)[0]))
            xmax.append(max(np.unique(year, return_counts = True)[0]))
            ax.hist(year, alpha = 0.4, density = True, color = colo[j], bins = (max(np.unique(year, return_counts = True)[0]) - min(np.unique(year, return_counts = True)[0])), range = [min(np.unique(year, return_counts = True)[0]), max(np.unique(year, return_counts = True)[0])], label = f'{file_dict[key]}')
            ax.legend(loc = 'upper left')
            all_vals.append(year)
            j += 1

    ax.tick_params(axis='y', length = 3, labelcolor=color)
    ax.tick_params(axis = 'x', length = 3, which = 'minor')
    ax.set_xticks(np.arange(1970, 2023, 1), minor = True)
    ax.set_yticks(np.arange(0, 0.3, 0.01), minor = True)

    # Plot Sunspot Number
    ax1 = ax.twinx() # Sunspot number axis
    color = 'tab:blue'
    ax1.set_ylabel('Sunspot Number', color=color)  # we already handled the x-label with ax1
    p1, = ax1.plot(df_prev['Year'], df_prev['Mean Sunspot Number'], color = 'tab:blue', linestyle = '-', label = 'Mean Smoothed Sunspot Number')
    ax1.set_xlim([1970, max(xmax)]) # Manually set

    ax1.tick_params(axis='y', length = 3, labelcolor=color)
    ax1.set_yticks(np.arange(0, 3000, 100), minor = True)
    ax1.set_ylim(bottom = 0, top = 3000)
    ax1.legend()

    fig.tight_layout()  # otherwise the right y-label is slightly clipped
    plt.show()


# Actual Code which runs visualization
substorm_norm_visual()