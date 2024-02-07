#!/usr/bin/python3
""" Lockboxes """


def canUnlockAll(boxes):
    """
      Function to determine if all boxes can be unlocked.
      :param boxes: List of lists, where each sub-list contains keys
                    to other boxes.
      :return: True if all boxes can be unlocked, False otherwise.
    """

    keys = [0]
    i = 0

    for key in keys:
        for i in range(len(boxes[key])):
            if boxes[key][i] < len(boxes) and boxes[key][i] not in keys:
                keys.append(boxes[key][i])

    return(len(keys) == len(boxes))