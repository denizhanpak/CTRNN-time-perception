README

MOTIVATION:
    In progress. 
    Time perception isn't representational per se, but counting is. Can we show that a minimally
    cognitive agent (a CTRNN) can delay its action by some amount of time based on an input? Is the 
    input representational? Is it morphologically analogous to time and just needs scaling? Does this
    change how we interpret the results?


Brian Dahlberg, Indiana University 2021

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