#!/usr/bin/python3
""" Lockboxes """


boxes = [[1, 2], [2, 3], [], [4], [5], []]

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
        print(key)
        for i in range(len(boxes[key])):
            if boxes[key][i] < len(boxes) and boxes[key][i] not in keys:
                print(boxes[key][i])
                keys.append(boxes[key][i])
        print(keys)

    return len(keys) == len(boxes)