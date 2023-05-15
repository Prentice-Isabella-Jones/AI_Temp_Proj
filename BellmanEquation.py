
class BellmanEquation:
    def bellman_equation():
        heat_on = {"rising by 0.5": .5, "rising by 1": .2, "no change": .2, "falling by 0.5": .1}
        heat_off = {"rising by 0.5": .1, "falling by 0.5": .7, "no change": .2}
        list_of_states = [16, 16.5, 17, 17.5, 18, 18.5, 19, 19.5, 20, 20.5, 21, 21.5, 22, 22.5, 23, 23.5, 24, 24.5, 25]
        number_of_iterations = 50
            #val = {0: [0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0]}
        val = {}
        costs = {"on": 3, "off": .01}
        for i in range(number_of_iterations):
            if i == 0:
                val[i] = [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0]
            else:
                for state in range(len(list_of_states)+1):
                    #print(val)
                    values = []
                    if state == 0:
                        val_on = (costs["on"] + .3 * val[i - 1][state] + .5 * val[i - 1][state + 1] + .2 * val[i - 1][state + 2])
                        val_off = (costs["off"] + .9 * val[i - 1][state] + .1 * val[i - 1][state + 1])
                        min_val = min(val_on, val_off)
                        values.append(min_val)
                        #print(state)
                    elif state == 12:
                        values.append(0)
                    elif state == 17:
                        #print(list_of_states[state])
                        val_on = (costs["on"] + .1 * val[i - 1][state - 1] + .2 * val[i - 1][state] + .7 * val[i - 1][state + 1])
                        val_off = (costs["off"] + .7*val[i - 1][state - 1] + heat_off["no change"] * val[i - 1][state] + heat_off["rising by 0.5"] * val[i - 1][state + 1])
                        min_val = min(val_on, val_off)
                        values.append(min_val)
                    elif state == 18:
                        #print(list_of_states[state])
                        val_on = (costs["on"] + .1 * val[i-1][state-1] + .9 * val[i-1][state])
                        val_off = (costs["off"] + .7 * val[i-1][state - 1] + .3 * val[i-1][state])
                        min_val = min(val_on, val_off)
                        values.append(min_val)
                    else:
                        #print(list_of_states[state])
                        val_on = (costs["on"] + heat_on["falling by 0.5"]*(val[i-1][state - 1]) + heat_on["no change"] * val[i-1][state] + heat_on["rising by 0.5"]*val[i-1][state+1] + heat_on["rising by 1"] * val[i-1][state+2])
                        val_off = (costs["off"] + heat_off["falling by 0.5"] * val[i-1][state - 1] + heat_off["no change"] * val[i-1][state] + heat_off["rising by 0.5"]*val[i-1][state + 1])
                        min_val = min(val_on, val_off)
                        values.append(min_val)
                print(values)
                val[i] = values
                print(val)
                    #val[i][state] = min_val
        return val

    if __name__ == "__main__":
        print(bellman_equation())












