#!/usr/bin/python3
"""check if all doors can be opened"""


def canUnlockAll(boxes):
    if len(boxes) == 0:
        return False

    keys = [x for x in boxes[0]]
    openedBoxes = set()
    openedBoxes.add(0)

    while keys:
        key = keys.pop(0)
        if key not in openedBoxes and key < len(boxes):
            if len(boxes[key]) == 0:
                openedBoxes.add(key)
            keys.extend(boxes[key])
            openedBoxes.add(key)

            if check_if_opened(len(boxes), openedBoxes):
                return True

    return (len(boxes) == len(openedBoxes))


def check_if_opened(count, listB):
    if count == len(listB):
        return True
    return False
