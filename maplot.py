import matplotlib.pyplot as plt
import pandas as pd

def Visualizing():
    x = [1,2,3,4]
    y = [4,2,1,3]
    plt.scatter(x,y,color='red')# Can replace scatter with bar, barh, plot
    plt.show()


def Drawing():
    df = pd.read_csv('earth.csv')
    x = df['layer']
    y = df['thickness']
    plt.bar(x,y, color = 'green' )
    plt.title('Layers OF the Earth')
    
    plt.ylabel('Thicknes')
    plt.show()
    


Drawing()
