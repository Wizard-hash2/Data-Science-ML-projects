import pandas as pd
import matplotlib.pyplot as plt

def Plot_Line():
    x= [0,100]
    y= [0,100]
    plt.plot(x,y,color="green",alpha = 0.5, linestyle = "--")
    plt.xlim(0,100)
    plt.ylim(0,100)
    ax = plt.gca()
    ax.set_aspect(1)


def add_labels(df, x_col, y_col, label_col):
    for (i, row) in df.iterrows():
        x = row[x_col]
        y = row[y_col]
        offset_spacing = "  "
        label = offset_spacing + row[label_col]
        plt.text(x, y, label, va='center', ha='left')

        
def Healthy_Food():
    Df_public = pd.read_csv('healthy-food-survey-public.csv')
   # Df['Yes_percent'] = Df.eval('yes.sum()/(no.sum()+no_opinion.sum()+yes.sum()) * 100').round(1)
    
    Df_public['Yes_percent'] = Df_public.eval('yes/(no+no_opinion+yes) * 100').round(0)

    Df_public = Df_public[['food', 'Yes_percent']]

    Df_private = pd.read_csv('healthy-food-survey-experts.csv')

    Df_private['Expe_OP'] = Df_private.eval('yes/(yes+no+no_opinion) * 100').round(0)

    Df_private = Df_private[['food','Expe_OP']]

    Df = Df_private.merge(Df_public, on = 'food', how='left')

    Df['Disagreement'] = Df.eval('Yes_percent-Expe_OP')


    print(Df.sort_values(by = 'Disagreement', ascending=False).head(4))

    Highes_Disagre = Df['Expe_OP'],Df['Yes_percent']

    plt.scatter( Df['Expe_OP'],Df['Yes_percent'])
    Plot_Line()
    add_labels(Highes_Disagre,'Expe_OP','Yes_percent','food')
    plt.show()

Healthy_Food()