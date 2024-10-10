#!/usr/bin/python3
"""
Module to determine if all boxes can be opened
"""

def canUnlockAll(boxes):
    """
    Function to determine if all boxes can be opened
    """
    opened = [False] * len(boxes)
    opened[0] = True
    keys = [0]

    while keys:
        current_key = keys.pop()
        for key in boxes[current_key]:
            if key < len(boxes) and not opened[key]:
                opened[key] = True
                keys.append(key)
    
    return all(opened)
