# Sunspot numbers downloaded by A R Fogg on 11/08/2023
# 
# Obtained from:
http://www.sidc.be/silso/datafiles
# By the Solar Influences Data analysis Centre (SIDC) at the Royal
#	Observatory of Belgium
#
# Datafiles:
SN_monthly_1749_now.txt
SN_13monthsmoothed_1749_now.txt

# NOTE: I commented out any not definitive values (indicated with a star at the end) with a #

#------------------------------------------
# SN_monthly_1749_now.txt
#------------------------------------------
#
Monthly mean total sunspot number obtained by taking a simple arithmetic mean of the daily total sunspot number over all days of each calendar month. Monthly means are available only since 1749 because the original observations compiled by Rudolph Wolf were too sparse before that year. (Only yearly means are available back to 1700)
A value of -1 indicates that no number is available (missing value).

Error values:
The monthly standard deviation of individual data is derived from the daily values by: sigma(m)=sqrt(SUM(N(d)*sigma(d)^2)/SUM(N(d)))
where sigma(d) is the standard deviation for a single day and N(d) is the
number of observations for that day.
The standard error on the monthly mean values can be computed by:
sigma/sqrt(N) where sigma is the listed standard deviation and N the total number of observations in the month.

NB: February 1824 does not contain any daily value. As it is the only month without data after 1749, the monthly mean value was interpolated by R. Wolf between the adjacent months.

Format: plain ASCII text

Contents:
Column 1-2: Gregorian calendar date
- Year
- Month
Column 3: Date in fraction of year for the middle of the corresponding month
Column 4: Monthly mean total sunspot number.
Column 5: Monthly mean standard deviation of the input sunspot numbers from individual stations.
Column 6: Number of observations used to compute the monthly mean total sunspot number.
Column 7: Definitive/provisional marker. A blank indicates that the value is definitive. A '*' symbol indicates that the monthly value is still provisional and is subject to a possible revision (Usually the last 3 to 6 months)

Line format [character position]:
- [1-4] Year
- [6-7] Month
- [9-16] Decimal date
- [19-23] Monthly total sunspot number
- [25-29] Standard deviation
- [32-35] Number of observations
- [37] Definitive/provisional indicator

-------------------------------------------------------------------------------

#------------------------------------------
# SN_13monthsmoothed_1749_now.txt
#------------------------------------------
#

Time range: 1/1749 - last elapsed month (provisional values)

Data description:
The 13-month smoothed monthly sunspot number is derived by a "tapered-boxcar" running mean of monthly sunspot numbers over 13 months centered on the corresponding month (Smoothing function: equal weights = 1, except for first and last elements (-6 and +6 months) = 0.5, Normalization by 1/12 factor). There are no smoothed values for the first 6 months and last 6 months of the data series: columns 4, 5 and 6 are set to -1 (no data).

Choice of smoothing:
This 13-month smoothed series is provided only for backward compatibility with a large number of past publications and methods resting on this smoothed series. It has thus become a base standard (e.g. for the conventional definition of the times of minima and maxima of solar cycles).

However, a wide range of other smoothing functions can be used, often with better low-pass filtering and anti-aliasing properties. As the optimal filter choice depends on the application, we thus invite users to start from the monthly mean Sunspot Numbers and apply the smoothing function that is most appropriate for their analyses. The classical smoothed series included here should only be used when direct comparisons with past published analyses must be made.

Error values:
The standard deviations in this files are obtained from the weighted mean of the variances of the 13 months in the running mean value:
sigma(ms)=sqrt(SUM(weigth(M)*sigma(M)^2)/SUM(weight(M))
where sigma(M) is the standard deviation for a single month, weight(M) is 1 or 0.5 and M=13 in this case.

As successive monthly means are highly correlated, the standard error on the smoothed values can be estimated by the same formula as for a single month: sigma/sqrt(N) where sigma is the listed standard deviation and N the total number of observations in the month.
The number of observations given in column 6 is the number of observations of the corresponding (middle) month: same value SUM N(d) as in the monthly mean file.
This thus gives a smoothed mean of monthly standard deviations, i.e. with the samme low-pass filtering as the data value itself. Further autocorrelation analyses will be needed to derive a conversion of this standard deviation to a standard error of the 13-month smoothed number.

Format: plain ASCII text

Contents:
Column 1-2: Gregorian calendar date
- Year
- Month
Column 3: Date in fraction of year for the middle of the corresponding month
Column 4: Monthly smoothed total sunspot number.
Column 5: Monthly mean standard deviation of the input sunspot numbers.
Column 6: Number of observations used to compute the corresponding monthly mean total sunspot number.
Column 7: Definitive/provisional marker. A blank indicates that the value is definitive. A '*' symbol indicates that the monthly value is still provisional and is subject to a possible revision (Usually the last 3 to 6 months)

Line format [character position]:
- [1-4] Year
- [6-7] Month
- [9-16] Decimal date
- [19-23] Smoothed total sunspot number
- [25-29] Standard deviation
- [32-35] Number of observations
- [37] Definitive/provisional indicator
