#!/usr/bin/python3
"""lockboxes
"""


def canUnlockAll(boxes):
    """return True if all unlockable"""
    unlocked = [0]
    for box, keys in enumerate(boxes):
        if not keys:
            continue
        for key in keys:
            if key < len(boxes) and key not in unlocked and key != box:
                unlocked.append(key)
    if len(unlocked) == len(boxes):
        return True
    return False
