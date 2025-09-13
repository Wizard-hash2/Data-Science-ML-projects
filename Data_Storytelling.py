import pandas as pd
import matplotlib.pyplot as plt


def animal_trend_forma(animal,Def):
    tend = Def.query('word == @animal')

    plt.plot(tend["year"], tend["frequency"])

    plt.ylabel("Frequnce Per year")
   


def animal_world_trends():
    Def = pd.read_csv("Data-Science-ML-projects/animal-word-trends-intro.csv")
    #print(Def)
    animal_trend_forma("horse",Def)
    animal_trend_forma("lobster",Def)
   # animal_trend_forma(Def["word"],Def)
    plt.axvline(x = 1996, color = "green", ls = "--")
    
    plt.show()



