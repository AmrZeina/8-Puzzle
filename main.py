from collections import deque   #Queue properties

#Define possible moves in dictionary
moves = {
    'Up': -3,
    'Down': 3,
    'Left': -1,
    'Right': 1
}


def getChildren(currentState):
    """
    A function called to calculate all possible transitions from a given state.

    Args:
        currentState (int) : the state wanted to get transitions from
    
    Returns:
        states (tupple) : list of all possible transitions with move associated to each
    """

    strState=list(str(currentState)) #Converting int state to string and make it list to swap chars
    states = [] #List to be returned
    freeTileIndex = strState.index('0') #Get index of 0 element which represents free tile to be moved
    
    for move, steps in moves.items():
        newTilePlace = freeTileIndex + steps

        #Prevent non-possible moves, conditions arranged so that smaller states 'alphabitically' appear first
        if move == 'Up' and freeTileIndex < 3 : continue
        if move == 'Left' and freeTileIndex%3 == 0: continue
        if move == 'Right' and freeTileIndex%3 == 2: continue
        if move == 'Down' and freeTileIndex > 5: continue

        #Generate the new state and append it with the move happened. No two moves shall happens at a time
        childState = strState.copy()
        childState[freeTileIndex] , childState[newTilePlace] = childState[newTilePlace] , childState[freeTileIndex]
        states.append((childState, move)) #Append as a tupple to insert move with the state

    return states

"""
def DFS(initialState, goalState):
    
    A function called to reach the goal state using Depth First Search.

    Args:
        initialState (int) : the state where searching begin from
        goalState (int) : solution of the buzzle problem
    
    Returns:
        pathToGoal (list) : List include moves happened from initial to goal 
        pathCost (int) : Cost spent to reach the goal
        nodesExpanded (list) : List include all moves expanded from initial to goal
        searchDepth (int) 
        runningTime (float) : time in seconds
    
def BFS():
    pass

def IDS():
    pass

def AStar():
    pass
"""