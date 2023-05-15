"""This is a container for states"""


class States_Cont:
    def __int__(self, list):
        """A container can be initialized empty"""
        self.list = [16, 16.5, 17, 17.5, 18, 18.5, 19, 19.5, 20, 20.5, 21, 21.5, 22, 22.5, 23, 23.5, 24, 24.5, 25]

    def __len__(self):
        """Will return the number of states in a container"""
        return len(self)

    def __iter__(self):
        """Will return an iterator over the states in a container"""
        return self
