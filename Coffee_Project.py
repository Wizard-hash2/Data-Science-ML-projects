#Coffee is a global phenomenon. Across the world, thousands of new coffee shops open each year, with specialty shops becoming increasingly popular.

#In this project you will analyze a survey dataset of approximately 1000 coffee enthusiasts to identify the most popular dairy choices. Based on your findings, you will recommend which dairy alternatives should be stocked by a new specialty coffee shop planning to offer only plant-based beverages.

### Loading the Data
#The `coffee-survey-results.csv` file contains information about people's coffee preferences, including which dairy they prefer. Load up the data and take a look.

#Activity Goals:- Import pandas.- Load the coffee survey data.- Display the dataframe.

import pandas as Pd
import matplotlib.pyplot as plt

def Coffee():
    Df = Pd.read_csv('coffee-survey-results.csv')
    
    
   
    needed_columns = [
    "What kind of dairy? (Whole milk)",
    "What kind of dairy? (Skim milk)",
    "What kind of dairy? (Half and half)",
    "What kind of dairy? (Coffee creamer)",
    "What kind of dairy? (Flavored creamer)",
    "What kind of dairy? (Oat milk)",
    "What kind of dairy? (Almond milk)",
    "What kind of dairy? (Soy milk)"]

    dairy = Df[needed_columns]#extract columns woth the above specifications
    #print(dairy)
    name_map = {
    'What kind of dairy? (Whole milk)': 'Whole milk',
    'What kind of dairy? (Skim milk)': 'Skim milk',
    'What kind of dairy? (Half and half)': 'Half and half',
    'What kind of dairy? (Coffee creamer)': 'Coffee creamer',
    'What kind of dairy? (Flavored creamer)': 'Flavored creamer',
    'What kind of dairy? (Oat milk)': 'Oat milk',
    'What kind of dairy? (Almond milk)': 'Almond milk',
    'What kind of dairy? (Soy milk)': 'Soy milk',}
    dairy = dairy.rename(columns=name_map) #rename With shorter acronyms as shown above
    
   # print(dairy.dropna())
    dairy = dairy.dropna()#remove nan
   # print(dairy.isna().sum())#do sume of na
    daily_preferences = dairy.mean()*100
    daily_preferences = daily_preferences.sort_values(ascending = True )
    plt.barh(daily_preferences.index, daily_preferences)
    plt.show()
    #Conclusion
    #The most popular plant based choice is oat milk
    #he most popular plant based dairy choice is oat milk. This might be a great choice for the default dairy option in a specialty coffee shop.
    




Coffee()

