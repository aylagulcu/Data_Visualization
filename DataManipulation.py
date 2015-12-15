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

print('Number of columns in this data frame: '+ str(len(data.columns)))
print(data.columns)

# Area Column frequency distribution: value_counts ile
print('Number of rows for each Area...:')
countArea= data['Area'].value_counts(sort= False)
print(countArea)

print('Percentages for each Area...:')
perArea= data['Area'].value_counts(sort= False, normalize= True)
print(perArea)


#frequency distributions:
areaDistr= data.groupby('Area').size()
print(areaDistr)








