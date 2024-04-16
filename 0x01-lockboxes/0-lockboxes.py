def canUnlockAll(boxes):
    # Initialize a set to keep track of visited boxes
    visited = set()
    # Initialize a queue with the first box (boxes[0]) as the starting point
    queue = [0]

    while queue:
        # Get the current box from the queue
        current_box = queue.pop(0)
        # Mark the current box as visited
        visited.add(current_box)
        # Iterate through the keys in the current box
        for key in boxes[current_box]:
            # If the key opens a box that hasn't been visited yet
            if key not in visited:
                # Add the box to the queue to explore its keys later
                queue.append(key)

    # Check if all boxes have been visited
    return len(visited) == len(boxes)
