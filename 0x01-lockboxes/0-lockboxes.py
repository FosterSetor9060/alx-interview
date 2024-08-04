#!/usr/bin/python3
"""
locked boxes in front of you.
Each box is numbered sequentially
from 0 to n - 1 and each box may
contain keys to the other boxes.
"""

def canUnlockAll(boxes):
    """
    The method that determines if all the boxes can be opened.

    :param boxes: A list of lists where each sublist contains keys to other boxes
    :return: True if all boxes can be opened, otherwise False
    """
    if not boxes or type(boxes) is not list:
        return False

    n = len(boxes)
    unlocked = set([0])  # Use a set for faster membership checks
    stack = [0]  # Use a stack (list) to explore the boxes

    while stack:
        box = stack.pop()
        for key in boxes[box]:
            if key not in unlocked and key < n:
                unlocked.add(key)
                stack.append(key)

    return len(unlocked) == n
