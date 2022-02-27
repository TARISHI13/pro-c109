import statistics
import plotly.figure_factory as ff
import pandas as pd 
import csv
df = pd.read_csv('sp.csv')
heightList = df['reading score'].tolist()
weightList = df['writing score'].tolist()
mathList = df['math score'].tolist()

heightmean = statistics.mean(heightList)
heightmode = statistics.mode(heightList)
heightmedian = statistics.median(heightList)
print('mean,median,mode of reading score is{},{},{}'.format(heightmean,heightmedian,heightmode))
hstdev = statistics.stdev(heightList)
hstdevfirststart,hstdevfirstend = heightmean-hstdev,heightmean+hstdev
hstdevsecondstart,hstdevsecondend = heightmean-(2*hstdev),heightmean+(2*hstdev)
hstdevthreestart,hstdevthreeend = heightmean-(3*hstdev),heightmean+(3*hstdev)
heightListofdatawithin1stdev = [result for result in heightList if result > hstdevfirststart and result < hstdevfirstend]
heightListofdatawithin2stdev = [result for result in heightList if result > hstdevsecondstart and result < hstdevsecondend]
heightListofdatawithin3stdev = [result for result in heightList if result > hstdevthreestart and result < hstdevthreeend]
print('{}% of data for reading score lies within 1 stdev'.format(len(heightListofdatawithin1stdev)*100.0/len(heightList)))
print('{}% of data for reading score lies within 2 stdev'.format(len(heightListofdatawithin2stdev)*100.0/len(heightList)))
print('{}% of data for reading score lies within 3 stdev'.format(len(heightListofdatawithin3stdev)*100.0/len(heightList)))

weightmean = statistics.mean(weightList)
weightmode = statistics.mode(weightList)
weightmedian = statistics.median(weightList)
print('mean,median,mode of writing score is{},{},{}'.format(weightmean,weightmedian,weightmode))
wstdev = statistics.stdev(weightList)
wstdevfirststart,wstdevfirstend = weightmean-wstdev,weightmean+wstdev
wstdevsecondstart,wstdevsecondend = weightmean-(2*wstdev),weightmean+(2*wstdev)
wstdevthreestart,wstdevthreeend = weightmean-(3*wstdev),weightmean+(3*wstdev)
weightListofdatawithin1stdev = [result for result in weightList if result > wstdevfirststart and result < wstdevfirstend]
weightListofdatawithin2stdev = [result for result in weightList if result > wstdevsecondstart and result < wstdevsecondend]
weightListofdatawithin3stdev = [result for result in weightList if result > wstdevthreestart and result < wstdevthreeend]
print('{}% of data for writing score lies within 1 stdev'.format(len(weightListofdatawithin1stdev)*100.0/len(weightList)))
print('{}% of data for writing score lies within 2 stdev'.format(len(weightListofdatawithin2stdev)*100.0/len(weightList)))
print('{}% of data for writing score lies within 3 stdev'.format(len(weightListofdatawithin3stdev)*100.0/len(weightList)))

mathmean = statistics.mean(mathList)
mathmode = statistics.mode(mathList)
mathmedian = statistics.median(mathList)
print('mean,median,mode of math score is{},{},{}'.format(mathmean,mathmedian,mathmode))
mstdev = statistics.stdev(mathList)
mstdevfirststart,mstdevfirstend = mathmean-mstdev,mathmean+mstdev
mstdevsecondstart,mstdevsecondend = mathmean-(2*mstdev),mathmean+(2*mstdev)
mstdevthreestart,mstdevthreeend = mathmean-(3*mstdev),mathmean+(3*mstdev)
mathListofdatawithin1stdev = [result for result in mathList if result > mstdevfirststart and result < mstdevfirstend]
mathListofdatawithin2stdev = [result for result in mathList if result > mstdevsecondstart and result < mstdevsecondend]
mathListofdatawithin3stdev = [result for result in mathList if result > mstdevthreestart and result < mstdevthreeend]
print('{}% of data for math score lies within 1 stdev'.format(len(mathListofdatawithin1stdev)*100.0/len(mathList)))
print('{}% of data for math score lies within 2 stdev'.format(len(mathListofdatawithin2stdev)*100.0/len(mathList)))
print('{}% of data for math score lies within 3 stdev'.format(len(mathListofdatawithin3stdev)*100.0/len(mathList)))







