import pandas as pd
import matplotlib.pyplot as plt


def data_Frames():
    Dy = pd.DataFrame()

    Dy['Colours'] = ['blue','yellow','red']

    Dy['Radius'] = [20,32,45]

    Dy['Diameter'] = Dy['Radius'] * 2

    Dy['area'] = Dy.eval('2*22/7*Radius') #Do maths with eval

    print(Dy.sort_values(by='Diameter', ascending=False))#sorting

    print(Dy['Diameter'].sum())

    print(Dy.query('Colours == "red"'))# Query about the Colour Red

    #print(Dy.query('area < area.mean()')) #Perform condition


    #print(Dy.groupby('Radius').mean().reset_index())# Allows grouping just like the sql

    #print(Dy)
#print(Dy['Diameter'].max())
#print(Dy.iloc[1]) #Rows
#print(Dy['Colours'])#Columns
#print(Dy.shape)# row numbers and columns

def c_sv():
    dy = pd.read_csv('earth.csv')
    print(dy['thickness'].sum())

def Cisco():
    df = pd.read_csv('bird-neck-bones.csv')
#print(df.query('species == "giraffe"'))
#print(df['neck_vertebrae'].mean())

    bird_coun= df['neck_vertebrae'].value_counts()
    bird_coun.sort_index()
    bird_coun.plot.bar()

def population():
    # coding sandbox
    internet = pd.read_csv('world-internet-users.csv')
    population = pd.read_csv('historical-world-population.csv')

    inpop = internet.merge(population,on ='year',how='left')#merging all values to be displayed in the left datasest which
#... is the internet and then display only results from the right which conjuginates with those in the left

    inpop = inpop.dropna()#Remove the rows which has nan columns


#print(inpop.eval('internet_users.sum()/population.sum()'))

    inpop['percent'] = inpop.eval('internet_users/population * 100')
    inpop['percent'] = inpop['percent'].round(2)

    #print(inpop)

    #plt.plot(inpop['year'], inpop['percent'])
    #plt.axhline(50,color = 'Green',linestyle='--') #dra hox line
    #print(internet.query('internet_users >= 100000000').head(1))#Print first result
    Above = inpop.query('percent >= 50')

    print(Above.head(1))


def Top_Song():
    Df = pd.read_csv('top-song-durations.csv')
    #print(Df)
    split_duration = Df['duration'].str.split(':',expand=True)
    Df[['h','m','s']]=split_duration.astype(int) #splitting to the h,m,s and assigninng with the respect to split_duration
    Df['seconds'] = Df.eval('m * 60 + s')
    Longest_song = Df['seconds'].max()
    plt.plot(Df['year'], Df['seconds'])
    plt.xlabel('Year')
    plt.ylabel('Duration in seconds')

    plt.axhline(Longest_song, color = 'Green')
   # plt.show()


  
    print(Df[['title','artist']])

Top_Song()