"""
we must know 3 step when performing a slicing
step 1: start
step 2: stop/end(excluted hota he)
step 3: step size


array[start:stop:step]

arr[start:end], start to end -1
negative step. -1 reverse
"""

import numpy as np

arr = np.array([10,20,30,40,50,60])
print(arr[1:5])#index 1 to 4
print(arr[:4])#index 0 to 3
print(arr[::2]) #every second element
print(arr[::-1])# array ko reverse kr dega