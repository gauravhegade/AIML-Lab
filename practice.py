def print_states(state):
    for row in state:
        print(", ".join(map(str, row)))


def find_blank_state(state):
    for i in range(3):
        for j in range(3):
            if state[i][j] == 0:
                return i, j


def make_move(state, di, dj):
    i, j = find_blank_state(state)

    if 0 <= i + di < 3 and 0 <= j + dj < 3:
        new_state = [row.copy() for row in state]
        new_state[i][j], new_state[i + di][j + dj] = (
            new_state[i + di][j + dj],
            new_state[i][j],
        )

        return new_state
    else:
        return None


def calculate_heuristic(initial_state, goal_state):
    return sum(
        1 for i in range(3) for j in range(3) if initial_state[i][j] != goal_state[i][j]
    )


def a_star(initial_state, goal_state):
    open_set = [(calculate_heuristic(initial_state, goal_state), 0, initial_state, [])]
    closed_set = set()

    while open_set:
        open_set.sort()
        f, g, current_state, moves = open_set.pop(0)
        closed_set.add(tuple(map(tuple, current_state)))

        print_states(current_state)
        print()

        if current_state == goal_state:
            print("Goal state reached", moves)
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


initial_state = [[2, 8, 1], [0, 4, 3], [7, 6, 5]]
goal_state = [[1, 2, 3], [8, 0, 4], [7, 6, 5]]
a_star(initial_state, goal_state)
