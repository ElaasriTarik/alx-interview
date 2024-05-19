#!/usr/bin/python3
import time
canUnlockAll = __import__('0-lockboxes').canUnlockAll


boxes = [[1], [2], [3], [4], []]
start = time.time()
print(canUnlockAll(boxes))
end = time.time()
print(f"The code took {end - start} seconds to run")

boxes = [[1, 4, 6], [2], [0, 4, 1], [5, 6, 2], [3], [4, 1], [6], [2, 5, 8, 0], [9, 7], [4, 1], [6], [2, 5, 8, 0], [9, 7]]
start = time.time()
print(canUnlockAll(boxes))
end = time.time()
print(f"The code took {end - start} seconds to run")

boxes = [[1, 4], [2], [0, 4, 1], [3], [], [4, 1], [5, 6]]
start = time.time()
print(canUnlockAll(boxes))
end = time.time()
print(f"The code took {end - start} seconds to run")

