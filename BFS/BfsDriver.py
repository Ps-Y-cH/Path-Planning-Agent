"""------------------
    RACHIT RATHORE
    2015HS120600P
------------------"""

import queue
import time
import sys
sys.path.append('../')

from BfsNode import *
from DirtGenerator import *
from GoalTest import goalTest
from State import State
from BfsSuccessorFunc import bfsNextState


def bfsRootNode(state):
    root = BfsNode(state, None, None, 0)
    return root


def doNothingFunction(vc_position, final_position):
    x = vc_position[0]
    y = vc_position[1]

    actionSequence = []
    pathCostAdd = 0
    if x >= 0 and x<5:
        pathCostAdd+=2*x
        for i in range(x):
            actionSequence.append("MU")

    else:
        pathCostAdd+=2*(9-x)
        for i in range((9-x)):
            actionSequence.append("MD")

    if y >= 0 and y<5:
        pathCostAdd+=2*y
        for i in range(y):
            actionSequence.append("ML")

    else:
        pathCostAdd+=(2*(9-y))
        for i in range((9-y)):
            actionSequence.append("MR")

    return actionSequence, pathCostAdd

    # x = vc_position[0] - final_position[0]
    # y = vc_position[1] - final_position[1]
    #
    # actionSequence = []
    # pathCostAdd = (abs(x) + abs(y)) * 2
    # if x > 0:
    #     for i in range(x):
    #         actionSequence.append("MU")
    #
    # else:
    #     for i in range(abs(x)):
    #         actionSequence.append("MD")
    #
    # if y > 0:
    #     for i in range(y):
    #         actionSequence.append("ML")
    #
    # else:
    #     for i in range(abs(y)):
    #         actionSequence.append("MR")
    #
    # return actionSequence, pathCostAdd


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


def bfs(initialState, finalState):
    noOfNodes = 0
    auxiliaryQueueSize = 0

    rootNode = bfsRootNode(initialState)
    if rootNode == finalState:
        return [], 0

    noOfNodes += 1

    bfsQueue = queue.Queue(maxsize=0)
    visited = set()

    bfsQueue.put(rootNode)

    auxiliaryQueueSize += 1

    while (True):
        if bfsQueue.empty():
            return [], 0
        currNode = bfsQueue.get()

        if currNode.state not in visited:
            if (goalTest(currNode.state)):
                temp1, temp2 = actionSeq(currNode, finalState)
                anslist = [temp1, temp2, noOfNodes, auxiliaryQueueSize]
                return anslist

        visited.add(currNode.state)

        childNodes = bfsNextState(currNode,visited)
        noOfNodes += len(childNodes)

        for x in childNodes:
            bfsQueue.put(x)
            if bfsQueue.qsize() >= auxiliaryQueueSize:
                auxiliaryQueueSize = bfsQueue.qsize()


# if __name__ == "__main__":
#     time_start = time.process_time()
#
#     initialDirtTuple = [[9,0]]#dirt_gen(2)
#     print(initialDirtTuple)
#     finalDirtTuple = []
#     initalState = State([0, 0], initialDirtTuple)
#     finalState = State([9, 9], finalDirtTuple)
#     anslist = bfs(initalState, finalState)
#     print(anslist)
#     time_elapsed = time.process_time() - time_start
#     print(time_elapsed)