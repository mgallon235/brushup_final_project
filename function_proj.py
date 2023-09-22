import math
import numpy as np
import pandas as pd
import matplotlib.pyplot as plt


def model_1(pop = 1000, base_infected = 10, infection_rate = 0.05):
    """
    function to project the infection rate of a disease
    :param int pop: total population
    :param int base_infected: initial infected population
    :param float infection_rate: infection rate of the disease

    """
    
    inf_dict = {'date':[0],'infected':[10]}
    days = 0

    inf_df = pd.DataFrame(inf_dict)

    while base_infected < 1000:
        infected = math.ceil((infection_rate*3)*base_infected*(pop - base_infected)/(pop))
        base_infected = base_infected + infected
        days += 1
        # Append values to dictionary
        inf_dict['date'].append(days)
        inf_dict['infected'].append(base_infected)
        
    return pd.DataFrame(inf_dict)


## Model vaccination

def model_2(pop = 1000, base_infected = 10, infection_rate = 0.05, vax_rate=0.01):
    """
    function to project the infection rate of a disease when a vaccine is introduced
    :param int pop: total population
    :param int base_infected: initial infected population
    :param float infection_rate: infection rate of the disease
    :param float vax_rate: effective rate of the vaccine
    """
    days = 0
    inf_dict = {'date':[0],'infected':[10]}


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

def sir_model(pop = 1000, base_infected = 10, infection_rate = 0.05, recovery_rate=0.9, death_rate=0.1):
    """
    function to project the infection rate of a disease when deaths and recoveries are accounted for
    :param int pop: total population
    :param int base_infected: initial infected population
    :param float infection_rate: infection rate of the disease
    :param float recovery_rate: recovery rate of the disease
    :param float death_rate: death rate of the disease
    """
    days = 7
    inf_diction = {'date':[0,1,2,3,4,5,6],'recovers':[0,0,0,0,0,0,10],'dead':[0,0,0,0,0,0,1]}
    recovers = 9
    dead = 1

    while recovers <= 1000 :
        infected = math.ceil((infection_rate*3)*base_infected*(pop - base_infected)/(pop))
        recovery = math.ceil((infection_rate*3)*base_infected*(pop - base_infected)/(pop)*0.90)
        recovers = recovers + recovery
        deads  = math.ceil((infection_rate*3)*base_infected*(pop - base_infected)/(pop)*0.10)
        dead = dead + deads
        base_infected = base_infected + infected - deads
        days = days + 1
        inf_diction['date'].append(days)
        inf_diction['recovers'].append(recovers)
        inf_diction['dead'].append(dead)

    return pd.DataFrame(inf_diction)