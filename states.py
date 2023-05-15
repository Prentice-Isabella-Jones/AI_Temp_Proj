"""Used for defining states"""


class States:

    def __int__(self, state: int) -> int:
        self.state = state

    def __eq__(self, other: int) -> int:
        return self.state == other.state
