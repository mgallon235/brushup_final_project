# Notice that in this code the .csv documents are supposed to be situated in the same directory as this .py project.

#_______________________________________________________________________________________

# EXERCISE 1:

import pandas as pd
import matplotlib.pyplot as plt
import matplotlib.dates as mdates

df2 = pd.read_csv('us_states_covid19_daily.csv') #Importing the second data set, with State as a variable

df2['date_formatted'] = pd.to_datetime(df2['date'], format='%Y%m%d')

categories = df2['state'].unique()

plt.figure(figsize = (10, 6))

for category in categories:
    subset = df2[df2['state'] == category]
    plt.plot(subset['date_formatted'], subset['positive'], label=category)

plt.xlabel('Date')
plt.ylabel('Positives')
plt.title('Line Plot by State')
#plt.legend()

date_format = mdates.DateFormatter('%Y-%m-%d')
plt.gca().xaxis.set_major_formatter(date_format)

plt.xticks(rotation=45)

plt.show()

'''

Here we can observe that, for every State, the number of positive cases of Covid was growing as the time passed.
That being said, the variable 'date' could be affected by the number of tests that each State is realizing.
We could solve part of that by doing a ratio of positive cases in relation to the number of tests of each State.

'''

categories = df2['state'].unique()

df2['ratio_tests'] = df2['positive'] / df2['totalTestResults']

plt.figure(figsize = (10, 6))

for category in categories:
    subset = df2[df2['state'] == category]
    plt.plot(subset['date_formatted'], subset['ratio_tests'], label=category)

plt.xlabel('Date')
plt.ylabel('Ratio of Positives to Num. of Tests')
plt.title('Line Plot by State')
#plt.legend()

date_format = mdates.DateFormatter('%Y-%m-%d')
plt.gca().xaxis.set_major_formatter(date_format)

plt.xticks(rotation=45)

plt.show()

'''

Here, on the other hand, we can observe that it doesn't seem as obvious that positive cases increase as time passes.
It could as well be that the positive cases had been the same during the period covered (2020) but due to a more intensive testing to the end of the year
more cases were discovered. 
We cannot be as sure anymore that actual Covid cases increased over time during 2020.

'''

#_______________________________________________________________________________________

# EXERCISE 2:

import pandas as pd
import matplotlib.pyplot as plt

df1 = pd.read_csv('COVID19_state.csv') #Importing the first data set, with data separated by states (not with state as a variable, but separated by them)

#print(df1.head)

x1 = df1['Tested']
y1 = df1['Deaths']

plt.scatter(x1, y1)

plt.xlabel('Tests')
plt.ylabel('Deaths')
plt.title('Deaths in relation to number of Tests')
plt.show()

'''
Here we can observe that the resulting plot seems to show a strong correlation between Tests and Deaths, but we might be missing an important bias.
It is entirely possible that States with more Testing have also more Deaths due to both being explained by a higher population.
Therefore, in the next steps we are going to project the same plot but with variables being converted to a ratio between the variable itself and
the population of the State.
'''

#print(df1['Tested'].describe())
#print(df1.dtypes)

df1['test_pop_ratio'] = df1['Tested'] / df1['Population']
df1['deaths_pop_ratio'] = df1['Deaths'] / df1['Population']

x = df1['test_pop_ratio']
y = df1['deaths_pop_ratio']

plt.scatter(x, y)

plt.xlabel('Ratio of Tests to Population of the State')
plt.ylabel('Ratio of Deaths to Population of the State')
plt.title('Deaths in relation to number of Tests')
plt.show()

'''
In this second case we can observe that the apparent correlation shown before has mostly disappeared.
It no longer seems that more tests lead to a higher death count.
'''
