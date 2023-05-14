
class BellmanEquation:
    def BellmanCalculation(self, cost, initial_state, end_state):
        #V(end_state) = min(c(action) + sum(P(initial_state|end_state, action) * V(initial_state))

        #for loop to find sum of the probabilities between the initial_state and the end_state
        #store value in variable and += that after each iteration
        #once every state has been calculated add the cost to that value
        #then find all the costs depending on the actions taken
        #calulate the minimum (most optimal actions to take)
        #return the V(end_state) value
        total_probability = 0
        #actions are just on and off
        #
        for MDPState in range(initial_state, end_state):



