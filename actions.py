"""Used for defining actions which are made up of a name and probability"""

class Actions:
    def __init__(self, name: str, prob: float):
        # actions name will be a string and the probability will be type float to be used
        # to calculate the optimal policy
        self.name = name
        self.prob = prob

    def __eq__(self, other):
        return self.name == other.name, self.prob == other.prob
