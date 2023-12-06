#!/usr/bin/python3
"""Boxes containing keys"""


def canUnlockAll(boxes):
    if not boxes or not boxes[0]:
        # If there are no boxes or the first box is empty, return False
        return False

    n = len(boxes)
    visited = [False] * n
    visited[0] = True

    stack = [0]

    while stack:
        current_box = stack.pop()

        # Check each key in the current box
        for key in boxes[current_box]:
            if 0 <= key < n and not visited[key]:
                visited[key] = True
                stack.append(key)

    return all(visited)
