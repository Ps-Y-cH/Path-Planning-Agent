"""------------------
    RACHIT RATHORE
    2015HS120600P
------------------"""

class BfsNode:

    def __init__(self, state, parent,action, nodeCost):

        self.state = state
        self.parent = parent
        self.nodeCost = nodeCost
        self.action = action

    def __eq__(self, other):
        return self.__dict__ == other.__dict__