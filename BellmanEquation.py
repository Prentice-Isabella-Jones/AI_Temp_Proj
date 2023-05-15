
class BellmanEquation:
        #0=16, 12=22, 17=24.5, 18=25
    def bellman_calculation(self, list_of_states, heat_on, heat_off):
        values = []
        cost_on = 3
        cost_off = .01

        for i in range(len(list_of_states)):
            if i == 0:
                #no falling
                values[i] = 0
            if i == 12:
                #value is always = 0
                values[list_of_states[i]] = 0
            if i == 17:
                #value only rises by .5
                values[list_of_states[i]] = 0
            if i == 18:
                #no rising
                values[list_of_states[i]] = 0

            else:
                value_on = cost_on + (heat_on["falling by 0.5"] * values[i - 1]
                                      + heat_on["no change"] * values[i]
                                      + heat_on["rising by 0.5"] * values[i + 1]
                                      + heat_on["rising by 1"] * values[i + 2])

                value_off = cost_off + (
                            heat_off["falling by 0.5"] * values[i - 1]
                            + heat_off["no change"] * values[i]
                            + heat_off["rising by 0.5"] * values[i + 1])

                val = min(value_on, value_off)

        return values















