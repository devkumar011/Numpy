## reshape rows, col specify neew shape
## if dimensions match
## resshape does not create copy

import numpy as np

arr = np.array([1,2,3,4,5,6])
reshaped_Arr = arr.reshape(2,3)
print(reshaped_Arr)
