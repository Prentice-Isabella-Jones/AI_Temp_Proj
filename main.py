import Equations
from states_container import States_Cont


#creating new states_cont obj which has list of states
list_of_states = States_Cont()
#heat_on and off probs will be imported to BellmanEquation.py so can call cal
#call


if __name__ == "__main__":
    # print(bellman_equation())
    list_of_states = [16, 16.5, 17, 17.5, 18, 18.5, 19, 19.5, 20, 20.5, 21, 21.5, 22, 22.5, 23, 23.5, 24, 24.5, 25]
    costs = {"on": 3, "off": .01}
    number_of_iterations = 5000

    print(Equations.BellmanEquation.optimal_policy(list_of_states, number_of_iterations, costs))