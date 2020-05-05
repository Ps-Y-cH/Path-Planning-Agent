"""------------------
    RACHIT RATHORE
    2015HS120600P
------------------"""

class IdsNode:

    def __init__(self, state, parent,action, nodeCost,depth):

        self.state = state
        self.parent = parent
        self.nodeCost = nodeCost
        self.action = action
        self.depth=depth

    def __eq__(self, other):
        return self.__dict__ == other.__dict__