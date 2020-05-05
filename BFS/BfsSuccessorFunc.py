"""------------------
    RACHIT RATHORE
    2015HS120600P
------------------"""

import copy

from BfsNode import *
from State import *


def bfsNextState(node,visited):
    childArray = []

    if node.state.dirt_tuples is not None and node.state.vc_coord in node.state.dirt_tuples:
        newDirtTuples = copy.deepcopy(node.state.dirt_tuples)
        newDirtTuples.remove(node.state.vc_coord)
        newVcCoord = copy.deepcopy(node.state.vc_coord)

        newNode = BfsNode(State(newVcCoord, newDirtTuples), node, "S", node.nodeCost+1)
        childArray.append(newNode)

    else:
        if node.state.vc_coord[0] != 0:
            newNode = BfsNode(State([node.state.vc_coord[0] - 1, node.state.vc_coord[1]], node.state.dirt_tuples), node, "MU", node.nodeCost+2)
            if newNode.state not in visited:
                childArray.append(newNode)
        if node.state.vc_coord[0] != 9:
            newNode = BfsNode(State([node.state.vc_coord[0] + 1, node.state.vc_coord[1]], node.state.dirt_tuples), node, "MD", node.nodeCost+2)
            if newNode.state not in visited:
                childArray.append(newNode)
        if node.state.vc_coord[1] != 0:
            newNode = BfsNode(State([node.state.vc_coord[0], node.state.vc_coord[1] - 1], node.state.dirt_tuples), node, "ML", node.nodeCost+2)
            if newNode.state not in visited:
                childArray.append(newNode)
        if node.state.vc_coord[1] != 9:
            newNode = BfsNode(State([node.state.vc_coord[0], node.state.vc_coord[1] + 1], node.state.dirt_tuples), node, "MR", node.nodeCost+2)
            if newNode.state not in visited:
                childArray.append(newNode)

    return childArray
