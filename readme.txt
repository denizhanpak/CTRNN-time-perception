README


Brian Dahlberg & Denizhan Pak - Indiana University 2021


MOTIVATION:

    In progress. 
    Time perception isn't representational per se, but counting is. Can we show that a minimally
    cognitive agent (a CTRNN) can delay its action by some amount of time based on an input? Is the 
    input representational? Is it morphologically analogous to time and just needs scaling? Does this
    change how we interpret the results?


DESIGN:

Brian's version of the fitness function is meant to be scale-agnostic; the agent can respond in
whatever time-scale it wants so long as it is within the trial Duration. The agent's fitness is 
based on the ratio consistency of its response times.


Some experiment design questions:
    1) When assessing fitness and performing time task, should we do self-play or play with others?
    In other words, should we use N copies of the same agent, or use multiple agents?
        A) Actually, there's no reason why this game even needs to be multiplayer at all. Just give 
        the agents a stimulus and assess fitness based on accuracy of their action. 
    2) What should the input be? And what should be the shape of the input space? Should we let 
    input sensitivity be evolved or pre-given?  
    3) What should the output be? SHould we monitor one neuron and see if its voltage ever surpasses
    a threshold?
    4) If we don't do a multiplayer game, would this be an interesting extension? Is it an
    interesting corodination task?
    5) If we do a singleplayer version of the task, should fitness be assessed scale-free? IE, the
    agents can react in any time-scale they want, as long as they're consistent across varying 
    stimuli?


RESULTS:

Our first goalpost was to evolve for a very simple task to make sure there are no foundational bugs. 
For this first task, fitness is related not to the correct timing of the agent's first action, nor 
the first action at all - instead, more actions is more fitness. We expected this to be trivial to 
evolve, and indeed it was (Fig A). 

Next we evolved the agents to perform a simple delay task. In this task, agents must delay their
action by as much as possible on order to attain greater fitness. However, if an agent never takes an 
action, that is considered 0 fitness. Fig. B demonstrates proof-of-evolvability with toy parameters; 
Fig. C will be the same but with increased trial duration and population. 


TODO: 

Once this is achieved, we should show how agents' ability to accomplish this is related to CTRNN 
network size. 