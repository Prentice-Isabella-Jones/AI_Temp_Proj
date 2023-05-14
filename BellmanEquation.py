
class BellmanEquation:
    @staticmethod
    def bellman_equation(cost_on, cost_off, heat_on, heat_off, iteratn, values):
        #V(end_state) = min(c(action) + sum(P(initial_state|end_state, action) * V(initial_state))

        value_on = cost_on + (heat_on["falling by 0.5"] * values[iteratn - 1] + heat_on["no change"] * values[iteratn] +
                              heat_on["rising by 0.5"] * values[iteratn + 1] + heat_on["rising by 1"] * values[iteratn + 2])

        value_off = cost_off + (heat_off["falling by 0.5"] * values[iteratn - 1] + heat_off["no change"] * values[iteratn] +
                                heat_off["rising by 0.5"] * values[iteratn + 1])

        return min(value_on, value_off)
        #0=16, 12=22, 17=24.5, 18=25
    @staticmethod
    def bellman_calculation(list_of_states, heat_on, heat_off):
        values = {}
        #list_of_states = [16, 16.5, 17, 17.5, 18, 18.5, 19, 19.5, 20, 20.5, 21, 21.5, 22, 22.5, 23, 23.5, 24, 24.5, 25]
        #heat_on = {"rising by 0.5": 0.5, "rising by 1": 0.2, "no change": 0.2, "falling by 0.5": .10}
        #heat_off = {"rising by 0.5": 0.10, "falling by 0.5": 0.7, "no change": 0.2}

        for i in range(len(list_of_states)):
            if i == 0:
                #no falling

            if i == 12:
                #value is always = 0
                values[list_of_states[i]] = 0
            if i == 17:
                #value only rises by .5

            if i == 18:
                #no rising

            else:
                BellmanEquation.bellman_equation(3, .01, heat_on, heat_off, i, values)

        return values















