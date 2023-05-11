
class BellmanEquation:
    def BellmanCalculation(self, cost, probability, transition: MDPTransition, ):
        #V(end_state) = min(c(action) + sum(P(initial_state|end_state, action) * V(initial_state))