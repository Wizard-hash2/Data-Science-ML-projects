import pandas as pd
import matplotlib.pyplot as plt



def add_end_labels(Df, x, Column_names,alpha ):
    for z in Column_names:
        y = Df[z].iloc[-1]
        label = " " + z
        plt.text(x,y,label, va ="center",alpha = alpha)




def Dating():
    Df = pd.read_csv('how-couples-met.csv')
    print(Df)
    Df=Df.set_index('decade')

    back_color =[
        'college','at work', 'restaurant', 'neighbors'
    ]
    back_cal = ['C1', 'C2','C3','C4']

    focus_color = 'online'

    focus_cal = 'C5'


    Df[back_color].plot(color = back_cal)


    plt.plot(Df.index,Df['online'], color = focus_cal)
    plt.legend().set_visible(False)
    add_end_labels(Df,2010,back_color,alpha= 0.5)
    add_end_labels(Df, 2010, [focus_color], alpha = 1)
    clean_Graph()
    add_axes_label()
    plt.show()


def clean_Graph():
    ax = plt.gca()
    ax.spines[['left','top','right']].set_visible(False)
    ax.tick_params(axis='y',length = 0) # remove tick lines(-)
    ax.grid(axis='y' , alpha =0.5)

def add_axes_label():
    y_tick = [0,10,20,30,40,50]
    y_tick_percent = ['0%','10%','20%','30%','40%','50%']

  #  x_tick = [0,10,20,30,40,50]

    plt.yticks(y_tick,y_tick_percent)
    #plt.xticks(y_tick,y_tick_percent)
    plt.xlabel('Decade')



Dating()