import math
import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
import plotly.express as px


pop = 1000
base_infected = 10
days = 0
infection_rate = 0.05
inf_dict = {'date':[0],'infected':[10]}

inf_df = pd.DataFrame(inf_dict)

while base_infected < 1000:
    infected = math.ceil((infection_rate*3)*base_infected*(pop - base_infected)/(pop))
    base_infected = base_infected + infected
    days = days + 1
    # Append values to dictionary
    inf_dict['date'].append(days)
    inf_dict['infected'].append(base_infected)

# Model generated data
df = pd.DataFrame(inf_dict)

# Model infected people first 3 days = 17:
d3_infected = df[df['date'] <= 3]
fig = px.line(d3_infected, x='date', y='infected', title='Number of Infected First 3 Days', labels=dict(date="Days", infected="Infected Persons"))
fig.show()

fig = px.line(df, x='date', y='infected', title='Number of Infected per Day', labels=dict(date="Days", infected="Infected Persons"))
fig.show()

'''
    Let's simulate a policy. Suposse we introduce vaccination at period 3.
    The implications of the vaccine are only for those that are still uninfected. For simplicity, 
    their inmunity is modeled as a reduction in the probability that they get infected of 0.01 pp.
    How many infections result in the 10th day?
'''

pop = 1000
base_infected = 10
days = 0
inf_dict = {'date':[0],'infected':[10]}
vax_rate = 0.01
infection_rate = 0.05


while base_infected < 1000:
     if days <= 3:
          infected = math.ceil((infection_rate*3)*base_infected*(pop - base_infected)/(pop))
          base_infected = base_infected + infected
          days = days + 1
          inf_dict['date'].append(days)
          inf_dict['infected'].append(base_infected)
     else:
         infected = math.ceil((vax_rate*3)*base_infected*(pop - base_infected)/(pop))
         base_infected = base_infected + infected
         days = days + 1
         inf_dict['date'].append(days)
         inf_dict['infected'].append(base_infected)


# Model generated data
df2 = pd.DataFrame(inf_dict)

# Model infected people first 10 days = 26:
d10_infected = df2[df2['date'] <= 10]
fig = px.line(d10_infected, x='date', y='infected', title='Number of Infected First 10 Days', labels=dict(date="Days", infected="Infected Persons"))
fig.show()

'''---------------------------------------------'''

new_rows = pd.DataFrame({"date":range(df.shape[0],df2.shape[0]), "infected":[df.infected.values[-1] for i in range(df.shape[0],df2.shape[0])]})
df = pd.concat([df, new_rows])

df["type"] = "Infected"
df2["type"] = "Infected with Vaccine"
## Join DataFrames
df_merge = pd.concat([df, df2])
'''---------------------------------------------'''
print(df_merge)
#plot both curves same chart
fig = px.line(df_merge, x='date', y='infected', color="type", title='Number of Infected per Day', labels=dict(date="Days", infected="Infected Persons"))
fig.show()




# identify inflection point 
# create change in slope graph 
# maximum infection slope 
df[""]


# stages of infection 
# stages of vaccination effect