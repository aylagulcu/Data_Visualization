import pandas as pd # pandas will be referred to as pd below

# Load the course files: Data comes from two different csv files: one for GDP data and one for Mortality Rate.
#Step1: 
# Loadind CSV files: imported into a DataFrame
print('GDP Data...')
data_GDP= pd.read_csv('GDP.csv')
#data_GDP.columns # output: Index(['Area', 'Year', 'GDP'], dtype='object')
print('GDP original length: '+ str(len(data_GDP)))
data_GDP_NoMissing= data_GDP.dropna() # Removes rows in which there are NaN values in any of the columns
print('Length when empty cells removed: '+str(len(data_GDP_NoMissing)))

print('MortalityRate Data...')
data_MortalityRate= pd.read_csv('MortalityRate.csv')
print('Mortality rate original length: '+ str(len(data_MortalityRate)))
data_MortalityRate_NoMissing= data_MortalityRate.dropna()

print('Length when empty cells removed: '+ str(len(data_MortalityRate_NoMissing)))

# Merge two data frames:
# Inner joins yield a DataFrame that contains only rows where the value being joins exists in BOTH tables. 
data = pd.merge(left= data_GDP, right= data_MortalityRate)
print('Length of the new merged data: '+ str(len(data)))
#setting variables you will be working with to numeric
data['Year'] = pd.to_numeric(data['Year'])
data['GDP'] = pd.to_numeric(data['GDP'])
data['Under_five_mortality'] = pd.to_numeric(data['Under_five_mortality'])

print('Number of columns in this data frame: '+ str(len(data.columns)))
print(data.columns)

# Area Column frequency distribution: using value_counts function
print('Area column...:')
print('Total number of observations for Area column...:')
print(len(data['Area'])) # number of observations for Area column

countAreaDistr= data['Area'].value_counts(sort= False, dropna=False)

print ('Number of Different Areas:')
print(len(countAreaDistr))
print('Number of observations for each Area...:')
print(countAreaDistr)

print('Percentages of observations for each Area...:')
perAreaDistr= data['Area'].value_counts(sort= False, dropna=False, normalize= True)
print(perAreaDistr)


# GDP Column frequency distribution: using value_counts function
print('GDP column...:')
print('Total number of observations for GDP column...:')
print(len(data['GDP'])) # number of observations for Area column

print ('Number of empty observations for the GDP column:')
sub1=data[(data['GDP']>0)]
print(len(data)-len(sub1))

countGDPDistr= data['GDP'].value_counts(sort= False, dropna=False)

print ('Number of Different GDP values:')
print(len(countGDPDistr))
print('Number of observations for each GDP...:')
print(countGDPDistr)

print('Percentages of observations for each GDP...:')
perGDPDistr= data['GDP'].value_counts(sort= False, dropna=False, normalize= True)
print(perGDPDistr)


# Under_five_mortality Column frequency distribution: using value_counts function
print('Under_five_mortality column...:')
print('Total number of observations for Under_five_mortality column...:')
print(len(data['Under_five_mortality'])) # number of observations for Area column

print ('Number of empty observations for the Under_five_mortality column:')
sub2=data[(data['Under_five_mortality']>0)]
print(len(data)-len(sub2))

countUnder_five_mortalityDistr= data['Under_five_mortality'].value_counts(sort= False, dropna=False)

print ('Number of Different Under_five_mortality values:')
print(len(countUnder_five_mortalityDistr))
print('Number of observations for each Under_five_mortality...:')
print(countUnder_five_mortalityDistr)

print('Percentages of observations for each Under_five_mortality...:')
perUnder_five_mortalityDistr= data['GDP'].value_counts(sort= False, dropna=False, normalize= True)
print(perUnder_five_mortalityDistr)



