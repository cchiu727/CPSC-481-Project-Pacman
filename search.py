# search.py
# ---------
# Licensing Information:  You are free to use or extend these projects for
# educational purposes provided that (1) you do not distribute or publish
# solutions, (2) you retain this notice, and (3) you provide clear
# attribution to UC Berkeley, including a link to http://ai.berkeley.edu.
# 
# Attribution Information: The Pacman AI projects were developed at UC Berkeley.
# The core projects and autograders were primarily created by John DeNero
# (denero@cs.berkeley.edu) and Dan Klein (klein@cs.berkeley.edu).
# Student side autograding was added by Brad Miller, Nick Hay, and
# Pieter Abbeel (pabbeel@cs.berkeley.edu).


"""
In search.py, you will implement generic search algorithms which are called by
Pacman agents (in searchAgents.py).
"""

import util

class SearchProblem:
    """
    This class outlines the structure of a search problem, but doesn't implement
    any of the methods (in object-oriented terminology: an abstract class).

    You do not need to change anything in this class, ever.
    """

    def getStartState(self):
        """
        Returns the start state for the search problem.
        """
        util.raiseNotDefined()

    def isGoalState(self, state):
        """
          state: Search state

        Returns True if and only if the state is a valid goal state.
        """
        util.raiseNotDefined()

    def getSuccessors(self, state):
        """
          state: Search state

        For a given state, this should return a list of triples, (successor,
        action, stepCost), where 'successor' is a successor to the current
        state, 'action' is the action required to get there, and 'stepCost' is
        the incremental cost of expanding to that successor.
        """
        util.raiseNotDefined()

    def getCostOfActions(self, actions):
        """
         actions: A list of actions to take

        This method returns the total cost of a particular sequence of actions.
        The sequence must be composed of legal moves.
        """
        util.raiseNotDefined()


def tinyMazeSearch(problem):
    """
    Returns a sequence of moves that solves tinyMaze.  For any other maze, the
    sequence of moves will be incorrect, so only use this for tinyMaze.
    """
    from game import Directions
    s = Directions.SOUTH
    w = Directions.WEST
    return  [s, s, w, s, w, w, s, w]

def depthFirstSearch(problem):
    open = util.Stack()
    closed = []
    actionsList = []
    
    # push root node on stack, and empty actions list
    open.push((problem.getStartState(), actionsList))

    while not open.isEmpty():
        currentState, currentActionsList = open.pop() # unpack
        if problem.isGoalState(currentState): # returns actions if goal state reached
            return currentActionsList
        elif currentState not in closed: # if state is unvisited
            closed.append(currentState) # add state to closed
            for successor, action, stepCount in problem.getSuccessors(currentState): # unpack
                newActionsList = currentActionsList.copy() # take copy of actions list
                newActionsList.append(action) # append new action
                open.push((successor, newActionsList)) # push successor and actions list on stack
    return currentActionsList # FAIL
    util.raiseNotDefined()

def breadthFirstSearch(problem):
    open = util.Queue()
    closed = []
    actionsList = []
    
    # push root node on queue, and empty actions list
    open.push((problem.getStartState(), actionsList))

    while not open.isEmpty():
        currentState, currentActionsList = open.pop() # unpack
        if problem.isGoalState(currentState): # returns actions if goal state reached
            return currentActionsList
        elif currentState not in closed: # if state is unvisited
            closed.append(currentState) # add state to closed
            for successor, action, stepCount in problem.getSuccessors(currentState): # unpack
                newActionsList = currentActionsList.copy() # take copy of actions list
                newActionsList.append(action) # append new action
                open.push((successor, newActionsList)) # push successor and actions list on queue
    return currentActionsList # FAIL
    util.raiseNotDefined()

def uniformCostSearch(problem):
    """Search the node of least total cost first."""
    "*** YOUR CODE HERE ***"
    util.raiseNotDefined()
    
def nullHeuristic(state, problem=None):
    """
    A heuristic function estimates the cost from the current state to the nearest
    goal in the provided SearchProblem.  This heuristic is trivial.
    """

    # x1, y1 = state[0], state[1]
    # x2, y2 = problem.getStartState()[0], problem.getStartState()[1]
    # return min((x1-x2),(y1-y2))
    return 0

def aStarSearch(problem, heuristic=nullHeuristic):
    """Search the node that has the lowest combined cost and heuristic first."""
    "*** YOUR CODE HERE ***"

    # open = util.Stack()
    # closed = []

    # start = []

    # # push starting state onto stack
    # open.push((problem.getStartState(), start))

    # while not open.isEmpty():
    #     X, currentActionsList= open.pop()
    #     if problem.isGoalState(X):
    #         return currentActionsList
    #     elif X not in closed:
    #         while (len(X) > 0):
    #             n = len(X)

    #         while (n > 0):
    #             if (n not in open and n not in closed):
    #                 #assign the child a heuristic value
    #                 #X.append(n)
    #                 n.append("Heurstistic Value")

    #             elif n in open:
    #                 # IGNORE THIS TEMP RETURN
    #                 #return "TEMP"
    #                 #if child is reached by shorter path
    #                 if n < len(X):
    #                     #give state on open the shorter path
    #                     open.append(n)
    #             elif n in closed:
    #                 #if child is reached by shorter path then
    #                 if n < len(X):
    #                     closed.remove(X)
    #                     open.append(n)


    #         closed.append(X)


    # TEST CODE FROM STACKOVERFLOW
    fringe = util.PriorityQueue()
    visited = {} # Visited nodes

    if problem.isGoalState(problem.getStartState()):
        return []

    fringe.push((problem.getStartState(),[]),0)

    while not fringe.isEmpty():
        currentState, pathToCurrent = fringe.pop()
        currentCost = problem.getCostOfActions(pathToCurrent)

        if problem.isGoalState(currentState):
            return pathToCurrent

        if currentState not in visited or currentCost<visited[currentState]:
            visited[currentState]=currentCost
            for successor,action,stepCost in problem.getSuccessors(currentState):
                currentTotalCost = currentCost + stepCost + heuristic(successor,problem)
                fringe.push((successor, pathToCurrent+[action]),currentTotalCost)
    return []

            # closed.append(currentState)
            # for successor, action, stepCount in problem.getSuccessors(currentState):
            #     #newAction = currentActionsList + [action]
            #     newAction = currentActionsList.copy()
            #     newAction.append(action)
            #     open.push((successor, newAction))


    #Best-First search pseudocode algorithm on page 5 of LO4 slides
    util.raiseNotDefined()


# Abbreviations
bfs = breadthFirstSearch
dfs = depthFirstSearch
astar = aStarSearch
ucs = uniformCostSearch
