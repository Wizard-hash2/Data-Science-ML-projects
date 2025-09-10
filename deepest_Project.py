#How deep can air-breathing animals dive into the ocean? Do whales go deeper than seals? Which animals go the deepest?

#In this project, we'll harness the power of data visualization to compare the diving depths of the ocean's deepest divers. Along the way, we'll transform Matplotlib's default bar charts into compelling visuals that tell a story.

import pandas as pd
import matplotlib.pyplot as plt

def Deepest():
    Df = pd.read_csv('deepest-diving-animals.csv')
    # print(Df['category'].value_counts())#Value counts
   # print(Df.groupby('category')['depth'].max()) #find maximum in each category
    Max_depth= Df.groupby('category')['depth'].max()
    New_Dataset = Max_depth.reset_index(name = 'max_depth')
   
    #print(Df.merge(New_Dataset, on = 'category', how = 'left'))
    #print(New_Dataset)
    names ={"category":"Cat",
    "max_depth": "MaxDep"}

    New_Dataset.rename(columns=names,inplace= True)
    New_Dataset = New_Dataset.sort_values('MaxDep')

    New_Dataset['Color'] = 'C0'
    New_Dataset.loc['ref_0'] = ['submarine implosion', 750, 'C1'] #Add Point of reference
    New_Dataset = New_Dataset.sort_values('MaxDep')


    print(New_Dataset)



    plt.barh(New_Dataset['Cat'],New_Dataset['MaxDep'], color = New_Dataset['Color'])
    clean_bar_axes()



    plt.show()


def clean_bar_axes():
    ax =plt.gca()
    ax.spines[['top','bottom','left','right']].set_visible(False)
    ax.grid(axis='x',color = 'black',alpha = 0.5)
    ax.tick_params(axis='both',length = 0)
    #Swapping ticks and spines for faded grid lines.


Deepest()