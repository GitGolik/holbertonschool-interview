#!/usr/bin/python3
"""Module that checks if all the lockboxes can be opened"""


def canUnlockAll(boxes):
    """determine if all boxes can be opened"""

    opened_boxes = set([0])
    boxes_to_check = [0]

    while boxes_to_check:
        current_box = boxes_to_check.pop()

        for key in boxes[current_box]:
            if key < len(boxes) and key not in opened_boxes:
                opened_boxes.add(key)
                boxes_to_check.append(key)

    return len(opened_boxes) == len(boxes)
