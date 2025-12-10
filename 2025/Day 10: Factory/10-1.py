from collections import deque

def lights_to_int(lights_tag):
    value = 0
    for light in reversed(lights_tag):
        value <<= 1
        if light == "#":
            value |= 1
    return value

def parse_button_mask(token):
    inner = token[1:-1].strip()
    if not inner:
        return 0

    mask = 0
    for idx in inner.split(","):
        mask |= (1 << int(idx))
    return mask

def min_presses_bfs(target_state, button_masks):
    visited = {0}
    queue = deque([(0, 0)])
    while queue:
        state, steps = queue.popleft()
        if state == target_state:
            return steps

        for mask in button_masks:
            next_state = state ^ mask
            if next_state not in visited:
                visited.add(next_state)
                queue.append((next_state, steps + 1))
    return -1

def min_button_presses(lines):
    total = 0
    for line in lines:
        parts = line.strip().split()

        lights_pattern = parts[0][1:-1]
        target_state = lights_to_int(lights_pattern)

        button_tokens = parts[1:-1]
        button_masks = [parse_button_mask(tok) for tok in button_tokens]

        presses = min_presses_bfs(target_state, button_masks)
        total += presses
    return total

if __name__ == "__main__":
    with open("10.txt") as f:
        data = f.read().splitlines()
    result = min_button_presses(data)
    print("Result:", result)
