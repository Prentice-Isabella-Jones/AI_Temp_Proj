"""Used for defining states"""


class States:

    def __int__(self, state):
        self.state = state

    def __eq__(self, other):
        return self.state == other.state
