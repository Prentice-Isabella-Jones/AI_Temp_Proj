from states_container import States_Cont


#creating new states_cont obj which has list of states
list_of_states = States_Cont()
#heat_on and off probs will be imported to BellmanEquation.py so can call cal
cost_on = 3
cost_off = .01


heat_on = {"rising by 0.5": 0.5, "rising by 1": 0.2, "no change": 0.2, "falling by 0.5": .10}
heat_off = {"rising by 0.5": 0.10, "falling by 0.5": 0.7, "no change": 0.2}