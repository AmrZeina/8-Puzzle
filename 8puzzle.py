from collections import deque
import heapq
import time
from math import sqrt

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


def manhattan_distance(state):
    """Manhattan distance heuristic for 8-puzzle."""
    distance = 0
    for i in range(9):
        tile = int(state[i])
        if tile != 0:
            goal_row, goal_col = divmod(tile, 3)
            current_row, current_col = divmod(i, 3)
            distance += abs(current_row - goal_row) + abs(current_col - goal_col)
    return distance


def euclidean_distance(state):
    """Euclidean distance heuristic for 8-puzzle."""
    distance = 0
    for i in range(9):
        tile = int(state[i])
        if tile != 0:
            goal_row, goal_col = divmod(tile, 3)
            current_row, current_col = divmod(i, 3)
            dx = current_row - goal_row
            dy = current_col - goal_col
            distance += sqrt(dx * dx + dy * dy)
    return distance

def AStar(initialState, goalState="012345678", heuristic="manhattan"):
    start_time = time.time()

    if isinstance(initialState, int):
        initialState = str(initialState)

    open_heap = [] 
    heapq.heappush(open_heap, (0, 0, initialState, []))
    visited = set()
    nodesExpanded = 0

    while open_heap:
        f, g, currentState, path = heapq.heappop(open_heap)
        if currentState in visited:
            continue
        visited.add(currentState)
        nodesExpanded += 1
        if currentState == goalState:
            end_time = time.time()
            return {
                "pathToGoal": path,
                "pathCost": len(path),
                "nodesExpanded": nodesExpanded,
                "searchDepth": len(path),
                "runningTime": round(end_time - start_time, 5)
            }

        for childState, move in getChildren(currentState):
            childState = ''.join(childState)   # convert list to string before using it
            if childState not in visited:
                g_new = g + 1
                if heuristic == "manhattan":
                    h = manhattan_distance(childState)
                else:
                    h = euclidean_distance(childState)
                f_new = g_new + h
                new_path = path + [move]
                heapq.heappush(open_heap, (f_new, g_new, childState, new_path))


    return None  


initial = "125340678"  # Example starting state

print("Initial State:", initial)
print("\n--- Running A* with Manhattan Heuristic ---")
result1 = AStar(initial, heuristic="manhattan")
print(result1)

print("\n--- Running A* with Euclidean Heuristic ---")
result2 = AStar(initial, heuristic="euclidean")
print(result2)