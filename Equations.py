import pprint

import Equations


class BellmanEquation:
    #@staticmethod
    def bellman_equation(list_of_states, number_of_iterations, costs):
        heat_on = {"rising by 0.5": .5, "rising by 1": .2, "no change": .2, "falling by 0.5": .1}
        heat_off = {"rising by 0.5": .1, "falling by 0.5": .7, "no change": .2}
        #list_of_states = [16, 16.5, 17, 17.5, 18, 18.5, 19, 19.5, 20, 20.5, 21, 21.5, 22, 22.5, 23, 23.5, 24, 24.5, 25]
        #number_of_iterations = 5000
            #val = {0: [0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0]}
        val = {}
        #costs = {"on": 3, "off": .01}
        for i in range(number_of_iterations):
            if i == 0:
                val[i] = [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0]
            else:
                values = []
                for state in range(len(list_of_states)):
                    if state == 0:
                        val_on = (costs["on"] + .3 * val[i - 1][state] + .5 * val[i - 1][state + 1] + .2 * val[i - 1][state + 2])
                        val_off = (costs["off"] + .9 * val[i - 1][state] + .1 * val[i - 1][state + 1])
                        min_val = min(val_on, val_off)
                        values.append(min_val)

                    elif state == 12:
                        values.append(0)
                    elif state == 17:
                        val_on = (costs["on"] + .1 * val[i - 1][state - 1] + .2 * val[i - 1][state] + .7 * val[i - 1][state + 1])
                        val_off = (costs["off"] + .7*val[i - 1][state - 1] + heat_off["no change"] * val[i - 1][state] + heat_off["rising by 0.5"] * val[i - 1][state + 1])
                        min_val = min(val_on, val_off)
                        values.append(min_val)
                    elif state == 18:
                        val_on = (costs["on"] + .1 * val[i - 1][state - 1] + .9 * val[i - 1][state])
                        val_off = (costs["off"] + .7 * val[i - 1][state - 1] + .3 * val[i - 1][state])
                        min_val = min(val_on, val_off)
                        values.append(min_val)
                    else:
                        val_on = (costs["on"] + heat_on["falling by 0.5"] * val[i-1][state - 1] + heat_on["no change"] * val[i-1][state] + heat_on["rising by 0.5"]*val[i-1][state+1] + heat_on["rising by 1"] * val[i-1][state+2])
                        val_off = (costs["off"] + heat_off["falling by 0.5"] * val[i-1][state - 1] + heat_off["no change"] * val[i-1][state] + heat_off["rising by 0.5"]*val[i-1][state + 1])
                        min_val = min(val_on, val_off)
                        values.append(min_val)
                val[i] = values
                    #val[i][state] = min_val
        #pprint.pprint(val)
        return val
    #@staticmethod
    def optimal_policy(list_of_states, number_of_iterations, costs):
        #list_of_states = [16, 16.5, 17, 17.5, 18, 18.5, 19, 19.5, 20, 20.5, 21, 21.5, 22, 22.5, 23, 23.5, 24, 24.5, 25]
        #costs = {"on": 3, "off": .01}
        result = Equations.BellmanEquation.bellman_equation(list_of_states, number_of_iterations, costs)
        result_list = result[4999]
        # print(result_list)
        # need to pick out reocurring number from val table
        # plug probabilities and num above into eq for on and off and then return the min of the two
        optimal_min_values = []
        # based on what user pick
        for state in range(len(list_of_states)):

            if state == 0:
                opt_val_on = (costs["on"] + .3 * result_list[state] + .5 * (result_list[state + 1]) + .2 *
                              (result_list[state + 2]))
                opt_val_off = (costs["off"] + .9 * result_list[state] + .1 * (result_list[state + 1]))
                opt_min_val = min(opt_val_on, opt_val_off)
                if opt_min_val == opt_val_on:
                    optimal_min_values.append(str(list_of_states[state]) + " OP is ON")
                else:
                    optimal_min_values.append(str(list_of_states[state]) + " OP is OFF")
            elif state == 12:
                optimal_min_values.append(" OP is ON OR OFF")
            elif state == 17:
                opt_val_on = (costs["on"] + .1 * result_list[state-1] + .2 * result_list[state] + .7 *
                              result_list[state + 1])
                opt_val_off = (costs["off"] + .7 * result_list[state - 1] + .2 * result_list[state] + .5 * result_list[state + 1])
                opt_min_val = min(opt_val_on, opt_val_off)
                if opt_min_val == opt_val_on:
                    optimal_min_values.append(str(list_of_states[state]) + " OP is ON")
                else:
                    optimal_min_values.append(str(list_of_states[state]) + " OP is OFF")
            elif state == 18:
                opt_val_on = (costs["on"] + .1 * result_list[state - 1] + .9 * result_list[state])
                opt_val_off = (costs["off"] + .7 * result_list[state - 1] + .3 * result_list[state])
                opt_min_val = min(opt_val_on, opt_val_off)
                if opt_min_val == opt_val_on:
                    optimal_min_values.append(str(list_of_states[state]) + " OP is ON")
                else:
                    optimal_min_values.append(str(list_of_states[state]) + " OP is OFF")
            else:
                opt_val_on = (costs["on"] + .1 * result_list[state - 1] + .2 * result_list[state] + .5 * result_list[state + 1] +
                              .2 * result_list[state + 2])
                opt_val_off = (costs["off"] + .7 * result_list[state - 1] + .2 * result_list[state] + .1 * result_list[state + 1])
                opt_min_val = min(opt_val_on, opt_val_off)
                if opt_min_val == opt_val_on:
                    optimal_min_values.append(str(list_of_states[state]) + " OP is ON")
                else:
                    optimal_min_values.append(str(list_of_states[state]) + " OP is OFF")

        return optimal_min_values








