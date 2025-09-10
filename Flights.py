## Flight Delays


#Millions of people fly every day, and flight delays can be an unwelcome aspect of air travel. Just how often do flight delays occur?

#In this project, you will work with airport flight data and explore how the day of week affects the likelihood of a delayed departure.

import pandas as pd
import matplotlib.pyplot as mlt

def flight():
    df = pd.read_csv('flights.csv')
    #print(df)
    time = ["scheduled","actual"]

    act_time = df[time].copy()  # steps above shows how I extracted schedule and actual
    act_time['scheduled'] = pd.to_datetime(act_time['scheduled'])# convert to date time
    act_time['actual'] = pd.to_datetime(act_time['actual'])# convert to date time

    act_time['delay'] = act_time.eval('actual - scheduled')
    #act_time['delay'] = act_time['actual'] - act_time['scheduled']  # Correct way for datetime subtraction
    act_time['is_late'] = act_time['delay'].dt.total_seconds() > 900
    act_time['dayname'] = act_time['actual'].dt.strftime('%a')#convery to day name 

    proportion_delay= act_time.groupby('dayname')['is_late'].mean()
    proportion_delay = proportion_delay * 100

    new_order = ['Sun','Mon','Tue','Wed','Thu','Fri','Sat']# rearrange in this order
    proportion_delay = proportion_delay.reindex(new_order)

    #print(proportion_delay)

    mlt.bar(proportion_delay.index, proportion_delay)
    mlt.show()
    

flight()

