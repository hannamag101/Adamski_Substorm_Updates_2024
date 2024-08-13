# Adamski_Substorm_Updates_2024
This repository contains python code which aids the user in the comparison of Earth substorm initialization events recorded across different datasets. We use onset data, further detailed in the following papers, to generate our visualizations in the form of Venn Diagrams. 

### References:
---
Ohtani, S., & Gjerloev, J. W. (2020). Is the substorm current wedge an ensemble of wedgelets?: Revisit to midlatitude positive bays. Journal of Geophysical Research: Space Physics, 125, e2020JA027902. https://doi.org/ 10.1029/2020JA027902

Newell, P. T., and J. W. Gjerloev (2011), Evaluation of SuperMAG auroral electrojet indices as indicators of substorms and auroral power, J. Geophys. Res., 116, A12211, doi:10.1029/2011JA016779.

Liou, K. (2010), Polar Ultraviolet Imager observation of auroral breakup, J. Geophys. Res., 115, A12219, doi:10.1029/2010JA015578.

Frey, H. U., S. B. Mende, V. Angelopoulos, and E. F. Donovan (2004), Substorm onset observations by IMAGE-FUV, J. Geophys. Res., 109, A10304, doi:10.1029/2004JA010607.

Frey HU, Mende SB (2006) Substorm onsets as observed by IMAGE-FUV, In: Syrjäsuo M, Donovan E (eds) Proceedings of eighth international conference on substorms (ICS-8), University of Calgary, Calgary, Alberta, pp 71–75

Forsyth, C., I. J. Rae, J. C. Coxon, M. P. Freeman, C. M. Jackman, J. Gjerloev, and A. N. Fazakerley (2015), A new technique for determining Substorm Onsets and Phases from Indices of the Electrojet (SOPHIE), J. Geophys. Res. Space Physics, 120, 10,592–10,606, doi:10.1002/ 2015JA021343.
 
### Packages: 
---
* numpy
* matplotlib, matplotlib_venn, matplotlib.colors, matplotlib.transforms
* pandas
* datetime
* os

### Sample Visualization:
----
For a more thorough description and analysis of progress made during project, as well as more figures, visit [a relative link](/Earth_Substorm_Updates_Final.pdf) file. Below is an example plot, Figure 7, from the final project report. 

![Image](/Sample_Visualizations/Optimal_Venns.jpeg)

**Figure 7:** Venn diagram representing the subdivision of simultaneous substorm onsets across the Forsyth, Newell, and Ohtani datasets using a 10 minute, 1 hour, 2 hour, and 24 hour increment. Based on Fogg et al. (2022), the median duration of a substorm event is estimated to be 60 minutes. This assumption lays the foundation for the choice of our optimal bin - 1 hour - whose data overlap is visualized in 7b.