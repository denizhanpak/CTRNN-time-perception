from agent import Agent
from ctrnn import CTRNN
from mga import Microbial
import numpy as np
import matplotlib.pyplot as plt

#TASK PARAMETERS ---------------------------------------------------------------
Duration = 100    # Duration of simulation, in steps
Dt = 0.01
#N_task_agents = 2 # Number of copies of agent for the time task
Stimuli = [0.1, 0.2]    # External input/stimuli for the time task

#CTRNN PARAMETERS --------------------------------------------------------------
Size = 5
WeightRange = 15
BiasRange = 15
TimeConstMin = Dt*10
TimeConstMax = 5.0
InputWeightRange = 15

#EA PARAMETERS -----------------------------------------------------------------
Trials = 5   # N of trials of self-play
GenotypeLength = Size*Size + Size*3    # Slightly longer because of incoding the input weight vector
Population = 20
RecombProb = 0.5
MutatProb = 0.1
Generations = 200
Tournaments = Generations * Population

def fitnessFunction(genotype):
    """This version of the fitness function is meant to be scale-agnostic; the agent can respond in
    whatever time-scale it wants so long as it is within the trial Duration. The agent's fitness is 
    based on the ratio consistency of its response times."""
    
    agent = Agent(genotype, Size, WeightRange, BiasRange, TimeConstMin, TimeConstMax, InputWeightRange, Dt)
    first_actions = np.empty((len(Stimuli), Trials))
    for s in range(len(Stimuli)):    # This loops runs each stimulus condition
            for t in range(Trials):    # This loops run all trials of task
                actions = np.empty(Duration)
                agent.sense(Stimuli[s])    # Initial stimulus
                for step in range(Duration):    # Runtime
                    agent.think()
                    actions[step] = agent.act()    # Record agent action
                    agent.sense(0)    # Under current experimental design, no stimulus available for rest of 
                    
    #            first_actions[s, t] = np.where((actions==1))[0][0]    # Record when the agent's first action was   
    #Calculate ratio of stimuli to each other
    #Calculate ration of first action/response time to each other
    #Pass these through some loss function, returning fitness                
                    
                first_actions[s, t] = np.count_nonzero(actions)  # TEMP
    return np.average(first_actions)/Duration # TEMP


# ============================= RUNTIME ========================================
    

test = Microbial(fitnessFunction, Population, GenotypeLength, RecombProb, MutatProb)
test.run(Tournaments)
test.showFitness()



