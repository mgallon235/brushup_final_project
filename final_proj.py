import math
import numpy as np
import pandas as pd
import matplotlib.pyplot as plt

pop = 1000
base = 10
days = 0
inf_dict = {'date':[0],'infected':[10]}
while base < 1000:
    infected = math.ceil((0.05*3)*base*(pop - base)/(pop))
    base = base + infected
    days = days + 1
    # Append values to dictionary
    inf_dict['date'].append(days)
    inf_dict['infected'].append(base)

# Model generated data
df = pd.DataFrame(inf_dict)

# Model infected people first 3 days = 17:
d3_infected = df[df['date'] <= 3]
d3_infected.plot.line(x='date',y='infected')
plt.show()

# Improve graph [Days to infect full population = 65]
df.plot.line(x='date',y='infected')
plt.show()

'''Let's simulate a policy. Suposse we introduce vaccination at period 3.
   The implications of the vaccine are only for those that are still uninfected. For simplicity, 
   their inmunity is modeled as a reduction in the probability that they get infected of 0.01 pp.
   How many infections result in the 10th day?
'''

pop = 1000
base = 10
days = 0
inf_dict = {'date':[0],'infected':[10]}
while base < 1000:
     if days <= 3:
          infected = math.ceil((0.05*3)*base*(pop - base)/(pop))
          base = base + infected
          days = days + 1
          inf_dict['date'].append(days)
          inf_dict['infected'].append(base)
     else:
         infected = math.ceil((0.01*3)*base*(pop - base)/(pop))
         base = base + infected
         days = days + 1
         inf_dict['date'].append(days)
         inf_dict['infected'].append(base)


# Model generated data
df2 = pd.DataFrame(inf_dict)

# Model infected people first 10 days = 26:
d10_infected = df2[df2['date'] <= 10]
d10_infected.plot.line(x='date',y='infected')
plt.show()

'''---------------------------------------------'''
## Join DataFrames
df_merge = pd.merge(df, df2, on='date')

#change column names
df_merge= df_merge.rename(columns={'infected_x':'infected','infected_y':'infected_vaccine'})

'''---------------------------------------------'''

#plot both curves same chart
plt.plot(df_merge['date'], df_merge['infected'], color='r', label='infected')
plt.plot(df_merge['date'], df_merge['infected_vaccine'], color='g', label='infected_vaccine')

# Naming the x-axis and y-axis
plt.xlabel("Date")
plt.ylabel("infected")

# Adding a title to the graph
plt.title("Infection and Vaccination Over Time")

# Adding a legend, which helps recognize the curve according to its color
plt.legend()

# Displaying the plot
plt.show()