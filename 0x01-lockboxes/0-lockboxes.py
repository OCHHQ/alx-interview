#!/usr/bin/python3
"""
Module for the canUnlockAll function.
"""

def canUnlockAll(boxes):
    """
    Determines if all boxes can be opened.
    
    Args:
    boxes (list of lists): A list of lists where each inner list represents a box
                           and contains keys to other boxes.
    
    Returns:
    bool: True if all boxes can be opened, False otherwise.
    """
    n = len(boxes)
    visited = set([0])  # Start with the first box opened
    stack = [0]  # Stack for DFS

    while stack:
        current_box = stack.pop()
        for key in boxes[current_box]:
            if key < n and key not in visited:
                visited.add(key)
                stack.append(key)
    
    return len(visited) == n
