# Prints the sequence of moves to reach the goal state from the initial state
def print_data(state):
    for row in state:
        print(",".join(map(str, row)))


# Finds the blank tile in the current state
def find_blank(state):
    for i in range(3):
        for j in range(3):
            if state[i][j] == 0:
                return i, j


def make_move(state, di, dj):
    """
    Finds the next state by moving the blank tile in the direction specified by di and dj

    Args:
        state: The current state of the system
        di: The change to be made to the row index of the blank tile
        dj: The change to be made to the column index of the blank tile

    Returns:
        The next state of the system
    """

    i, j = find_blank(state)

    # i is the row index and j is the column index of the blank tile
    # di and dj are the changes to be made to i and j respectively
    # di and dj are the direction in which the blank tile is to be moved
    if 0 <= i + di < 3 and 0 <= j + dj < 3:
        new_state = [row.copy() for row in state]
        new_state[i][j], new_state[i + di][j + dj] = (
            new_state[i + di][j + dj],
            new_state[i][j],
        )
        return new_state
    else:
        return None


def calculate_heuristic(state, goal):
    """
    Calculates the heuristic value of the current state.
    Heuristic value is the number of tiles that are not in their goal position.

    Args:
        state: The current state of the system
        goal: The goal state of the system

    Returns:
        The heuristic value of the current state
    """
    return sum(1 for i in range(3) for j in range(3) if state[i][j] != goal[i][j])


def a_star(initial_state, goal_state):
    """
    This algorithm uses a priority queue to store the states.
    The priority of a state is the heuristic value of the state.
    The algorithm terminates when the goal state is reached.

    Args:
        initial_state: The initial state of the system
        goal_state: The goal state of the system

    Calculates:
        The sequence of moves to reach the goal state from the initial state
    """

    # The open set is a priority queue which has the elements in the following format:
    # (f, g, current_state, moves)
    # it contains those states that are scheduled for exploration
    open_set = [(calculate_heuristic(initial_state, goal_state), 0, initial_state, [])]

    # closed set is the set of states that have already been visited
    # these states are not revisited
    closed_set = set()

    while open_set:
        open_set.sort()  # Sort the open set based on the heuristic value

        # f is the heuristic value of the state
        # g is the cost to reach the current state from the initial state
        # current_state is the current state of the system
        # moves is the sequence of moves to reach the current state from the initial state
        f, g, current_state, moves = open_set.pop(0)
        closed_set.add(tuple(map(tuple, current_state)))

        print_data(current_state)
        print()

        if current_state == goal_state:
            print("System has reached the goal state")
            print("Sequence of moves:", moves)
            return

        successors = [
            (make_move(current_state, -1, 0), "up"),
            (make_move(current_state, 1, 0), "down"),
            (make_move(current_state, 0, -1), "left"),
            (make_move(current_state, 0, 1), "right"),
        ]

        successors = [
            (state, move)
            for state, move in successors
            if state is not None and tuple(map(tuple, state)) not in closed_set
        ]

        for successor, move in successors:
            h = calculate_heuristic(successor, goal_state)
            g_successor = g + 1
            f_successor = g_successor + h
            open_set.append((f_successor, g_successor, successor, moves + [move]))


# Example usage:
initial_state = [[2, 8, 1], [0, 4, 3], [7, 6, 5]]
goal_state = [[1, 2, 3], [8, 0, 4], [7, 6, 5]]
a_star(initial_state, goal_state)
