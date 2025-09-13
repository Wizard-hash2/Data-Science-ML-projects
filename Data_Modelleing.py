import pandas as pd
import matplotlib.pyplot as plt
from sklearn.linear_model import LinearRegression
from sklearn.metrics import r2_score
from sklearn.preprocessing import PolynomialFeatures

class LinearModel:
    def __init__(self, model_name=""):
        self.model_name = model_name
        
    def fit(self, x, y):
        x = pd.DataFrame(x)
        linear_model = LinearRegression().fit(x, y)
        y_pred = linear_model.predict(x)
        self.slope = linear_model.coef_[0]
        self.intercept = linear_model.intercept_
        self.rsquared = r2_score(y, y_pred)
        
    def predict(self, x):
        return self.slope * x + self.intercept
    

    def plot_model(self, x_min, x_max, color="black"):
        y_min = self.predict(x_min)
        y_max = self.predict(x_max)
        plt.plot([x_min, x_max], [y_min, y_max], color=color)
        
    def print_model_info(self):
        m = self.slope
        b = self.intercept
        rsquared = self.rsquared
        model_name = self.model_name
        print(f'LinearModel({model_name}):')
        print(f'Parameters: slope = {m:.2f}, intercept = {b:.2f}')
        print(f'Equation: y = {m:.2f}x + {b:.2f}')
        print(f'Goodness of Fit (R²): {rsquared:.3f}')

class QuadraticModel:
    def fit(self, x, y):
        x = pd.DataFrame(x)
        quadratic = PolynomialFeatures(degree=2)
        quad_features = quadratic.fit_transform(x)
        quad_model = LinearRegression().fit(quad_features, y)
        y_pred = quad_model.predict(quad_features)
        self.a = quad_model.coef_[2]
        self.b = quad_model.coef_[1]
        self.c = quad_model.intercept_
        self.rsquared = r2_score(y, y_pred)
        
    def predict(self, x):
        return self.a*x**2 + self.b*x + self.c
    
    
    def plot_model(self, xmin, xmax):
        xvals = range(xmin, xmax+1)
        yvals = [self.predict(x) for x in xvals]
        plt.plot(xvals, yvals, color='black')
        
    def print_model_info(self):
        a = self.a
        b = self.b
        c = self.c
        rsquared = self.rsquared
        print('QuadraticModel')
        print(f'Parameters: a = {a:.2f}, b = {b:.2f}, c = {c:.2f}')
        print(f'Equation: y = {self.a:.2f}x² + {self.b:.2f}x + {self.c:.2f}')
        print(f'Goodness of Fit (R²): {rsquared:.3f}')

def elepahnts():
    Df = pd.read_csv('Data-Science-ML-projects/male-elephant-tusk-size.csv')
    pre_poaching = Df.query('period == "1966-68"')
    post_poaching = Df.query('period == "2005-13"')

    average_pre = pre_poaching.eval('tusk_length.mean()')

    plt.scatter(pre_poaching['shoulder_height'],pre_poaching['tusk_length'], marker='s', color = "green") #plot the with square

    plt.scatter(post_poaching['shoulder_height'], post_poaching['tusk_length'], marker='^',color = "red")#plot with rectangular
    Remove_axis()

    plt.xlabel("shoulder_height legth")
    plt.ylabel("tusk_length height")

    plt.text(x = 60, y = 260, s = "Post poaching" , color = "C0")
    plt.text(x = 100, y = 160 ,s = "Pre", color = "C1" )
    
    pre_mdl = LinearModel("pre_poaching")

    pre_mdl.fit(x=pre_poaching["shoulder_height"], y=pre_poaching["tusk_length"])

    pre_mdl.plot_model(140,270, color = "C1")
    
    POST_mdl = LinearModel("post_poaching")

    POST_mdl.fit(x=post_poaching["shoulder_height"], y=post_poaching["tusk_length"])

    POST_mdl.plot_model(140,270, color = "C1")

    POST_mdl.print_model_info()
    pre_mdl.print_model_info()

    plt.show()
    


    
    #print(average_pre)

def Remove_axis():
    ax = plt.gca()
    ax.spines[["left","right","top"]].set_visible(False)

    ax.tick_params(axis = 'both', length = 0)

    ax.grid(axis='y',alpha = 0.5)

#elepahnts()

def Lions():
    Lio = pd.read_csv('Data-Science-ML-projects/lion-attacks-lunar-cycle.csv')

    plt.scatter(Lio['evening_moonlight'], Lio['attacks'])
    

    #Lets fit in the data with the linear model

    Linemod = LinearModel("Attacks")

    Linemod.fit(x = Lio["evening_moonlight"], y = Lio["attacks"])

    Linemod.plot_model(0,1.0, color = "C1")
    plt.show()

    print(Lio) 

    #Linemod.print_model_info()
    #Based on the output it seems that during moonlight the numeber of attacks reduce decisively

    Lion_Belly = pd.read_csv('Data-Science-ML-projects/lion-belly-sizes.csv')

    plt.scatter(Lion_Belly['moonlight'], Lion_Belly['belly_size'], alpha= 0.5)

    Bellymod = LinearModel('Belly')

    Bellymod.fit(x = Lion_Belly['moonlight'],y = Lion_Belly['belly_size'])
    Bellymod.plot_model(0,1.0,color="C2")

    plt.show()

    print(Lion_Belly)




def Ebike():
    Ebi = pd.read_csv('Data-Science-ML-projects/ebike-stopping-distances.csv')
    #print(Ebi)


    #lets draw scatter 
    plt.scatter(Ebi['speed'],Ebi['distance'])
    
    line_model = LinearModel("Stopping distance")

    line_model.fit(x = Ebi["speed"], y = Ebi["distance"])

    
      
    df_low = pd.read_csv('Data-Science-ML-projects/ebike-data-low-speed.csv')

    #print(df_low)
    plt.scatter(df_low['speed'],df_low['distance'], color = "C3")
    

    Format_graphs_ebike() 
    #line_model.plot_model(0, 40, color = "C2")# Crafting the plot model forlinear equation


#Lets switch to qudratc 

    #plt.show()
   # This one doesnt work lemme use pd.concat
   # df_all = Ebi.merge(df_low, on = "speed", how="left")

    df_all = pd.concat([Ebi, df_low])

    plt.scatter(df_all['speed'], df_all['distance'] )
    quadMeth = QuadraticModel()

    quadMeth.fit(x = df_all['speed'], y = df_all['distance'])

    quadMeth.plot_model(0,65)
    
    quadMeth.print_model_info()

    Format_graphs_ebike()

    df_high = pd.read_csv("Data-Science-ML-projects/ebike-data-high-speed.csv")

    #print(df_high)

    # lets try predicting the distance at the speed of 61

  

    plt.scatter(df_high["speed"], df_high["distance"], color = "C4")

   # plt.axvline(x = 61, color = "purple", linestyle ="--", label = "Lets see the distance at the 61")
   # plt.axhline(y = distance, color = "purple", linestyle ="--", label = "Lets see the distance at the 61")

    
    plt.show()

    

#Summary
#In this Ebike() function project, we started with a linear model. While this provided a good fit for the initial data, it deviated from our physical intuition at zero speed.

#We brought in some low-speed data and changed to a quadratic model. The quadratic model provided a better fit to the curved relationship.

#Finally we tested our quadratic model on high-speed data. Using visual inspection of the graph, the model was able to predict the high-speed data with reasonable accuracy.


def Format_graphs_ebike():
    plt.xlabel("speed")
    plt.ylabel("Distance")
    plt.axhline(color = "black", alpha = 0.5, linestyle = "--")
    plt.axvline(color = "black", alpha = 0.5, linestyle = "--")

Ebike()