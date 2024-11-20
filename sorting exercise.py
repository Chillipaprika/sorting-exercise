import random
import numpy as np

boxes = [145, 687, 58, 68, 278, 149, 296, 382, 398, 426, 827, 654, 257, 12, 16, 8, 147, 1028, 283, 647, 2, 48, 12]
#boxes = [random.randint(0, 1000000) for i in range(10000)]
boxes = sorted(boxes)
count = 0
for pokus in boxes :
    indexhigh = (len(boxes) - 1)
    indexlow = (0)
    while indexhigh != indexlow: 
        count += 1
        index = (indexhigh + indexlow) / (2)
        print(index)
        hledam = boxes[int(index)]
        if hledam == pokus:
            break
        elif hledam > pokus:
            indexhigh = index
        else:
            indexlow = index
print(count/len(boxes))