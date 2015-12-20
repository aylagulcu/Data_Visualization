import pandas as pd # pandas will be referred to as pd below

# Load the course files: Data comes from two different csv files: one for GDP data and one for Mortality Rate.
#Step1: 
# Loadind CSV files: imported into a DataFrame
print('GDP Data...')
data_GDP= pd.read_csv('GDP.csv')
#data_GDP.columns # output: Index(['Area', 'Year', 'GDP'], dtype='object')
print('GDP original length: '+ str(len(data_GDP)))
data_GDP_NoMissing= data_GDP.dropna() # Removes rows in which there are NaN values in any of the columns
#print('Length when empty cells removed: '+str(len(data_GDP_NoMissing)))

print('MortalityRate Data...')
data_MortalityRate= pd.read_csv('MortalityRate.csv')
#print('Mortality rate original length: '+ str(len(data_MortalityRate)))
data_MortalityRate_NoMissing= data_MortalityRate.dropna()
#print('Length when empty cells removed: '+ str(len(data_MortalityRate_NoMissing)))

# Merge two data frames:
# Inner joins yield a DataFrame that contains only rows where the value being joined (acc to column names) exists in BOTH tables. 
data = pd.merge(left= data_GDP, right= data_MortalityRate)
data['Year']= pd.to_numeric(data['Year'])
data['GDP']= pd.to_numeric(data['GDP'])
data['Under_five_mortality']= pd.to_numeric(data['Under_five_mortality'])

print ('Data looks like the following:')
print (data.head(5))

print('Area counts:')
countArea= data['Area'].value_counts(sort= False, dropna=False)
print(countArea.head(5))
print('Area percentages:')
perArea= data['Area'].value_counts(sort= False, dropna=False, normalize=True)
print(perArea.head(5))
print ('Number of Different Areas: '+ str(len(countArea)))
print ('Number of observations for the Area column:'+ str(len(data['Area'])))

print ('Year data...:')
print ('Year ranges from '+ str(data['Year'].min())+' and to '+ str(data['Year'].max()) )
print('Year counts:')
countYear= data['Year'].value_counts(sort= False, dropna=False)
print(countYear.head(5))
print('Year percentages:')
perYear= data['Year'].value_counts(sort= False, dropna=False, normalize=True)
print(perYear.head(5))
print ('Number of Different Years: '+ str(len(countYear)))

print ('GDP data...:')
countGDP= data['GDP'].value_counts(sort= False, dropna=False) # dropna=False  required, otherwise python does not show mising values
print('GDP counts:')
print(countGDP.head(5))
print('GDP percentages:')
perGDP= data['GDP'].value_counts(sort= False, dropna=False, normalize=True)
print(perGDP.head(5))
print ('Number of Different GDP values: '+ str(len(countGDP)))

print('Under_five_mortality data...:')
countMortality= data['Under_five_mortality'].value_counts(sort= False, dropna=False)
print('Mortality counts:')
print(countMortality.head(5))
print('Mortality percentages:')
perMortality= data['Under_five_mortality'].value_counts(sort= False, dropna=False, normalize=True)
print(perMortality.head(5))
print ('Number of Different mortality rates: '+ str(len(countMortality)))

# remove rows where either GDP or Under_five_mortality column is NaN:
data2= data.dropna(subset =['GDP','Under_five_mortality'], how='any')
#data2.sort_values(['Year'], ascending=[True], inplace=True)
data2= data2.reset_index(drop=True) # not to save old index as a column

#data2['index']= range(len(data2))  # in this case index is kept as another column.

# Create a group for GDP:
print ('GDP ranges from '+ str(data['GDP'].min())+' and to '+ str(data['GDP'].max()) )
data2['GDPGroup']= pd.cut(data2.GDP, [280,1000,2000,5000,10000,50000,120000]) # no need to sort the data frame.
GDPGroupP2= data2['GDPGroup'].value_counts(sort= False, normalize= True)
print('GDP percentage counts for the groups:')
print(GDPGroupP2)
#print(pd.crosstab(data2['GDPGroup'], data2['GDP'])) # shows which GDP valus were put into which GDP group

#consider only years before 2000:
data3= data2[data2['Year']<2000]
data3['GDPGroup']= pd.cut(data3.GDP, [280,1000,2000,5000,10000,50000,120000]) # no need to sort the data frame.
GDPGroupP3= data3['GDPGroup'].value_counts(sort= False, normalize= True)
print('GDP percentage counts for the years before 2000 for the following groups:')
print(GDPGroupP3)

data4= data2[data2['Year']>=2000]
data4['GDPGroup']= pd.cut(data4.GDP, [280,1000,2000,5000,10000,50000,120000]) # no need to sort the data frame.
GDPGroupP4= data4['GDPGroup'].value_counts(sort= False, normalize= True)
print('GDP percentage counts for the years after 2000 for the following groups:')
print(GDPGroupP4)

# Create a group for Under_five_mortality:
print ('Under_five_mortality ranges from '+ str(data['Under_five_mortality'].min())+' and to '+ str(data['Under_five_mortality'].max()) )
data2['MortalityGroup']= pd.cut(data2.Under_five_mortality, [2,50,100,200,500,800]) # no need to sort the data frame.
MortalityGroupP2= data2['MortalityGroup'].value_counts(sort= False, normalize= True)
print('MortalityGroup percentage counts for the groups:')
print(MortalityGroupP2)

#consider only years before 2000:
data5= data2[data2['Year']<2000]
data5['MortalityGroup']= pd.cut(data5.Under_five_mortality, [2,50,100,200,500,800]) # no need to sort the data frame.
MortalityGroupP5= data5['MortalityGroup'].value_counts(sort= False, normalize= True)
print('MortalityGroup percentage counts for the years before 2000 for the groups:')
print(MortalityGroupP5)

#consider only years after 2000:
data6= data2[data2['Year']>=2000]
data6['MortalityGroup']= pd.cut(data6.Under_five_mortality, [2,50,100,200,500,800]) # no need to sort the data frame.
MortalityGroupP6= data6['MortalityGroup'].value_counts(sort= False, normalize= True)
print('MortalityGroup percentage counts for the years after 2000 for the groups:')
print(MortalityGroupP6)


