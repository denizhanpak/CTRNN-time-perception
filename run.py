from agent import Agent
from ctrnn import CTRNN
from mga import Microbial
import numpy as np
import matplotlib.pyplot as plt

#TASK PARAMETERS ---------------------------------------------------------------
Duration = 1000    # Duration of simulation, in steps
Dt = 0.01
N_task_agents = 2 # Number of copies of agent for the time task

#CTRNN PARAMETERS --------------------------------------------------------------
Size = 10
WeightRange = 15
BiasRange = 15
TimeConstMin = Dt*10
TimeConstMax = 5.0
InputWeightRange = 15

#EA PARAMETERS -----------------------------------------------------------------
Trials = 10    # N of trials of self-play
GenotypeLength = Size*Size + Size*3    # Slightly longer because of incoding the input weight vector
Population = 50
RecombProb = 0.5
MutatProb = 0.1
Generations = 200
Tournaments = Generations * Population

# ==============================================================================

def fitness_function(genotype):

    agents = []
    for i in range(len(agents)): 
        agents[i] = Agent(Size)
        agents[i].setParameters(genotype,WeightRange,BiasRange,TimeConstMin,TimeConstMax,InputWeightRange)
    nn = CTRNN(Size)



    fitness = np.zeros(Trials)
    for t in range(Trials):    # This loops run all trials of task
        pass

    return np.average(fitness)