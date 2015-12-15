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
# Inner joins yield a DataFrame that contains only rows where the value being joins exists in BOTH tables. 
data = pd.merge(left= data_GDP, right= data_MortalityRate)
data['Year']= pd.to_numeric(data['Year'])
data['GDP']= pd.to_numeric(data['GDP'])

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
print ('GDP ranges from '+ str(data['GDP'].min())+' and to '+ str(data['GDP'].max()) )
countGDP= data['GDP'].value_counts(sort= False, dropna=False) # dropna=False  required, otherwise python does not show mising values
print('GDP counts:')
print(countGDP.head(5))
print('GDP percentages:')
perGDP= data['GDP'].value_counts(sort= False, dropna=False, normalize=True)
print(perGDP.head(5))
print ('Number of Different GDP values: '+ str(len(countGDP)))

print('Under_five_mortality data...:')
print ('Under_five_mortality ranges from '+ str(data['Under_five_mortality'].min())+' and to '+ str(data['Under_five_mortality'].max()) )
countMortality= data['Under_five_mortality'].value_counts(sort= False, dropna=False)
print('Mortality counts:')
print(countMortality.head(5))
print('Mortality percentages:')
perMortality= data['Under_five_mortality'].value_counts(sort= False, dropna=False, normalize=True)
print(perMortality.head(5))
print ('Number of Different mortality rates: '+ str(len(countMortality)))

















