import math
import numpy as np
import pandas as pd
import matplotlib.pyplot as plt


def model_1():
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
        
    return pd.DataFrame(inf_dict)


## Model vaccination

def model_2():
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

    return pd.DataFrame(inf_dict)

def sir_model():
    pop = 1000
    days = 7
    inf_diction = {'date':[0,1,2,3,4,5,6],'recovers':[0,0,0,0,0,0,10],'dead':[0,0,0,0,0,0,1]}
    recovers = 9
    base = 10
    dead = 1
    while recovers <= 1000 :
        infected = math.ceil((0.05*3)*base*(pop - base)/(pop))
        recovery = math.ceil((0.05*3)*base*(pop - base)/(pop)*0.90)
        recovers = recovers + recovery
        deads  = math.ceil((0.05*3)*base*(pop - base)/(pop)*0.10)
        dead = dead + deads
        base = base + infected - deads
        days = days + 1
        inf_diction['date'].append(days)
        inf_diction['recovers'].append(recovers)
        inf_diction['dead'].append(dead)

    return pd.DataFrame(inf_diction)