"""------------------
    RACHIT RATHORE
    2015HS120600P
------------------"""

import queue
import time
import sys
sys.path.append('../')

from GoalTest import goalTest
from IdsNode import *
from IdsSuccessorFunc import idsNextState


def idsRootNode(state):
    root = IdsNode(state, None, None, 0, 0)
    return root


def doNothingFunction(vc_position, final_position):
    x = vc_position[0]
    y = vc_position[1]

    actionSequence = []
    pathCostAdd = 0
    if x >= 0 and x < 5:
        pathCostAdd += 2 * x
        for i in range(x):
            actionSequence.append("MU")

    else:
        pathCostAdd += 2 * (9 - x)
        for i in range((9 - x)):
            actionSequence.append("MD")

    if y >= 0 and y < 5:
        pathCostAdd += 2 * y
        for i in range(y):
            actionSequence.append("ML")

    else:
        pathCostAdd += (2 * (9 - y))
        for i in range((9 - y)):
            actionSequence.append("MR")

    return actionSequence, pathCostAdd


def actionSeq(currNode, finalState):
    actionSequence = []
    pathCost = currNode.nodeCost
    coord = currNode.state.vc_coord

    while (currNode.parent is not None):
        actionSequence.append(currNode.action)
        currNode = currNode.parent

    actionSequence.reverse()

    directPath, directCost = doNothingFunction(coord, finalState.vc_coord)
    finalactionsequence = actionSequence + directPath
    pathCost = pathCost + directCost

    return finalactionsequence, pathCost


def idsUtil(initalState, finalState, depth):
    if (initalState == finalState):
        return [], 0

    noOfNodes = 0
    auxiliaryQueueSize = 0
    visited = {}
    visited[initalState] = 0

    rootNode = idsRootNode(initalState)
    auxiliaryQueueSize += 1
    noOfNodes += 1

    idsQueue = queue.Queue(maxsize=0)

    idsQueue.put(rootNode)

    while not idsQueue.empty():
        currnode = idsQueue.get()
        childNodes = idsNextState(currnode,visited)
        noOfNodes += len(childNodes)
        for x in childNodes:
            if x.state not in visited:
                if goalTest(x.state):
                    temp1, temp2 = actionSeq(x, finalState)
                    anslist = [temp1, temp2, noOfNodes, auxiliaryQueueSize]
                    return anslist  # actionSeq(x, finalState), noOfNodes, auxiliaryQueueSize
                elif x.depth <= depth:
                    visited[x.state] = x.nodeCost
                    idsQueue.put(x)
                    if idsQueue.qsize() > auxiliaryQueueSize:
                        auxiliaryQueueSize = idsQueue.qsize()

            else:
                if x.depth <= depth:
                    if visited[x.state] >= x.nodeCost:
                        visited[x.state] = x.nodeCost
                        idsQueue.put(x)
                        if idsQueue.qsize() > auxiliaryQueueSize:
                            auxiliaryQueueSize = idsQueue.qsize()

    return None


def ids(initialState, finalState):
    depth = 0

    while (True):
        anslist = idsUtil(initialState, finalState, depth)
        if anslist is not None:
            return anslist  # actionS, pathcst, noOfNode, auxiliaryQueueSize
        else:
            depth += 1


# if __name__ == "__main__":
#     time_start = time.process_time()
#
#     initialDirtTuple = [[1,7],[0,8]]  # list_to_xy_coord(dirt_gen(3))      #dirt_gen(2)
#     print(initialDirtTuple)
#     finalDirtTuple = []
#     initalState = State([0, 0], initialDirtTuple)
#     finalState = State([9, 9], finalDirtTuple)
#     # actionSequence, pathc = ids(initalState, finalState)
#     a = ids(initalState, finalState)
#     print(a[0], a[1], a[2], a[3])  # , noOfNode, auxQueueSize)
#
#     time_elapsed = time.process_time() - time_start
#     print(time_elapsed)
