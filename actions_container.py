"""This is a container for actions"""


from actions import Actions


class Actions_Cont(Actions):
    def __init__(self, name: str, prob: float):
        super().__init__(name, prob)
        self.actions = None

    def __int__(self):
        """A container can be initialized empty"""

    def __len__(self):
        """Will return the number of actions in a container"""
        return len(self)

    def __iter__(self):
        """Will return an iterator over the actions in a container"""
        self.curr_index = 0
        return self

    def __next__(self):
        """Will return the next action in a container"""
        if self.curr_index < len(self.actions):
            val = self.actions[self.curr_index]
            self.curr_index = +1
            return val
        raise StopIteration

    def __iadd__(self, other):
        """Will add two operands and assign it to the left variable for actions"""
        self.actions += other.actions
        return self
