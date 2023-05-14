"""The probabilities associated with rising or falling in degrees and if the heat is on or off
will be stored here for our program to use to calculate the optimal policy"""

heat_on = {"rising by 0.5": 0.5, "rising by 1": 0.2, "no change": 0.2, "falling by 0.5": .10}
heat_off = {"rising by 0.5": 0.10, "falling by 0.5": 0.7, "no change": 0.2}
