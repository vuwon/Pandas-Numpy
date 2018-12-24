#We'll be working with data set from Fortune magazine's Global 500 list 2017, which ranks the top 500 corporations worldwide by revenue.
#1. Understanding pandas
import pandas as pd
f500 = pd.read_csv("f500.csv", index_col=0)
f500.index.name = None
f500_type = type(f500) 	#assign the type of f500 to f500_type
f500_shape = f500.shape 	#assign the shape of f500 to f500_shape
#2. Introducing DataFrames
f500_head=f500.head(6) 	#select the first 6 rows and assign the result to f500_head
f500_tail=f500.tail(8) 	#select the last 8 rows and assign the result to f500_tail
f500.info() 	#display information about the dataframe
#3. Selecting Columns From a DataFrame by Label
industries=f500.loc[:,"industry"] #Select the industry column, and assign the result to the variable name industries
previous=f500.loc[:,["rank","previous_rank","years_on_global_500_list"]]
financial_data=f500.loc[:,"revenues":"profit_change"] #Select all columns from revenues up to and including profit_change, in order, and assign the result to the variable name financial_data
#4. Column selection shortcuts
countries=f500.country #Select the country column, and assign the result to the variable name countries.
revenues_years=f500[["revenues","years_on_global_500_list"]]
ceo_to_sector=f500.loc[:,"ceo":"sector"] #Select all columns from ceo up to and including sector, in order, and assign the result to the variable name ceo_to_sector.
#5. Selecting Items from a Series by Label
ceos = f500["ceo"]  #From the pandas series ceos:
walmart=ceos["Walmart"] #Select the item at index label Walmart and assign the result to the variable name walmart.
apple_to_samsung=ceos["Apple":"Samsung Electronics"] #Select the items from index label Apple up to and including index label Samsung Electronics and assign the result to the variable name apple_to_samsung
oil_companies=ceos[["Exxon Mobil","BP","Chevron"]] #Select the items with index labels Exxon Mobil, BP, and Chevron, in order, and assign the result to the variable name oil_companies
#6. Selecting Rows From a DataFrame by Label
drink_companies=f500.loc[["Anheuser-Busch InBev","Coca-Cola","Heineken Holding"]] #Create a new variable, drink_companies, with:    Rows with indicies Anheuser-Busch InBev, Coca-Cola, and Heineken Holding, in that order.
big_movers=f500.loc[["Aviva","HP","JD.com","BHP Billiton"]] #Create a new variable big_movers, with:   Rows with indicies Aviva, HP, JD.com, and BHP Billiton, in that order.
big_movers=big_movers[["rank","previous_rank"]] #The rank and previous_rank columns, in that order.
middle_companies=f500["Tata Motors":"Nationwide"] #Create a new variable, middle_companies with: All rows with indicies from Tata Motorsto Nationwide, inclusive.
middle_companies=middle_companies.loc[:,"rank":"country"] #All columns from rank to country, inclusive
#7. Series and Dataframe Describe Methods
#Use the appropriate describe() method to
#Return a series of descriptive statistics for the profits column, and assign the result to profits_desc.
#Return a dataframe of descriptive statistics for the revenues and employees columns, in order, and assign the result to revenue_and_employees_desc.
#Return a dataframe of descriptive statistics for every column in the f500 dataframe, by checking the documentation for the correct value for the include parameter, and assign the result to all_desc.
profits_desc = f500["profits"].describe()
revenue_and_employees_desc = f500[["revenues","employees"]].describe()
all_desc = f500.describe(include['0'])
#8. More Data Exploration Methods
#Use Series.value_counts() and Series.head() to return the five most common values for the country column, and assign the results to top5_countries.
#Use Series.value_counts() and Series.head() to return the five most common values for the previous_rank column, and assign the results to top5_previous_rank.
#Use the appropriate max() method to find the maximum value for only the numeric columns from f500 (you may need to check the documentation), and assign the result to the variable max_f500.
top5_countries=f500["country"].value_counts().head()
top5_previous_rank=f500["previous_rank"].value_counts().head()
max_f500=f500.describe().max()
#9. Assignment with pandas
#Add a new column, revenues_b to the f500 dataframe by using vectorized division to divide the values in the existing revenues column by 1000 (converting them from millions to billions).
#The company 'Dow Chemical' have named a new CEO. Update the value where the index label is Dow Chemical and for the ceo column to Jim Fitterling.
f500["revenues_b"]=f500["revenues"]/1000
f500.loc["Dow Chemical","ceo"]="Jim Fitterling"
print(f500)
#10. Using Boolean Indexing with pandas Objects
#Create a boolean series, kr_bool, that compares whether the values in the country column from the f500 dataframe are equal to "South Korea"
kr_bool=f500["country"]=="South Korea"
top_5_kr=f500[kr_bool].head()
#11. Using Boolean Arrays to Assign Values
import numpy as np
prev_rank_before = f500["previous_rank"].value_counts(dropna=False).head()
f500.loc[f500["previous_rank"]==0,"previous_rank"]=np.nan
prev_rank_after = f500["previous_rank"].value_counts(dropna=False).head()
#12. Challenge: Top Performers by Country
top_3_countries = f500["country"].value_counts().head(3)
cities_usa1 = f500["country"]=="USA"
cities_usa=f500.loc[cities_usa1,"hq_location"].value_counts().head(5)
china= f500["country"]=="China"
sector_china= f500.loc[china,"sector"].value_counts().head(3)
employees_japan= f500["country"]=="Japan"
mean_employees_japan=f500[employees_japan].mean()