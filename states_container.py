"""This is a container for states"""

from states import MDPStates


class MDPStates_Container(MDPStates):
    def __init__(self):
        self.states = None

    def __int__(self):
        """A container can be initialized empty"""


    def __len__(self):
        """Will return the number of states in a container"""
        return len(self)

    def __iter__(self):
        """Will return an iterator over the states in a container"""
        self.curr_index = 0
        return self

    def __next__(self):
        """Will return the next states in a container"""
        if self.curr_index < len(self.state):
            val = self.state[self.curr_index]
            self.curr_index = +1
            return val
        raise StopIteration

    def __iadd__(self, other):
        """Will add two operands and assign it to the left variable for states"""
        self.states += other.states
        return self
