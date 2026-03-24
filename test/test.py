from collections import deque


def min_button_presses(target, buttons):
    n = len(target)
    start = tuple(0 for _ in range(n))  # starting counters (all zeros)

    # BFS queue: stores (state, distance)
    q = deque([(start, 0)])

    # visited states to avoid loops
    visited = {start}

    while q:
        state, steps = q.popleft()

        # success condition
        if state == target:
            return steps

        # try pressing each button
        for btn in buttons:
            new_state = list(state)
            for idx in btn:
                new_state[idx] += 1
                # OPTIONAL: clamp to target so BFS stays small
                if new_state[idx] > target[idx]:
                    new_state[idx] = target[idx]
            new_state = tuple(new_state)

            if new_state not in visited:
                visited.add(new_state)
                q.append((new_state, steps + 1))

    return None  # unreachable


target = (7, 5, 12, 7, 2)

buttons = [(0, 2, 3, 4), (2, 3), (0, 4), (0, 1, 2), (1, 2, 3, 4)]

print(min_button_presses(target, buttons))
