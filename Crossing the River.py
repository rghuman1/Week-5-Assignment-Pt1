def is_valid_state(state):
    missionaries_left = state[0]
    cannibals_left = state[1]
    missionaries_right = 3 - missionaries_left
    cannibals_right = 3 - cannibals_left
    if missionaries_left > 0 and missionaries_left < cannibals_left:
        return False
    if missionaries_right > 0 and missionaries_right < cannibals_right:
        return False
    return True

def is_goal_state(state):
    return state == (0, 0, 1)

def get_next_states(state):
    boat = state[2]
    next_states = []
    for m in range(3):
        for c in range(3):
            if m + c == 0:
                continue
            if m + c > 2:
                continue
            if boat == 1 and (state[0] - m < state[1] - c):
                continue
            if boat == 0 and ((3 - state[0]) - m < (3 - state[1]) - c):
                continue
            new_state = (
                state[0] - boat * m + (1 - boat) * m,
                state[1] - boat * c + (1 - boat) * c,
                1 - boat
            )
            if is_valid_state(new_state):
                next_states.append(new_state)
    return next_states

def breadth_first_search(initial_state):
    visited = set()
    queue = [initial_state]
    while queue:
        state = queue.pop(0)
        if state not in visited:
            visited.add(state)
            if is_goal_state(state):
                return state
            for next_state in get_next_states(state):
                if next_state not in visited:
                    queue.append(next_state)
                    return None

print("\tGame Start\nNow the task is to move all of them to right side of the river")
print("rules:\n1. The boat can carry at most two people\n2. If cannibals num greater than missionaries then the cannibals would eat the missionaries\n3. The boat cannot cross the river by itself with no people on board")
print("\n")
initial_state = (3, 3, 0)
solution = breadth_first_search(initial_state)
print(solution)