import pandas as pd
import matplotlib.pyplot as plt
from sklearn.linear_model import LinearRegression
from sklearn.metrics import r2_score

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

def elepahnts():
    Df = pd.read_csv('male-elephant-tusk-size.csv')
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

elepahnts()