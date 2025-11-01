"""
np.insert(array, index,value, aXix=NONE)
Araay-> original aray
index
value
axis
axis-> row wise
1 coloumn wise


"""

import numpy as np
arr = np.array([10,20,30,40,50])
print (arr)
new_arr = np.insert(arr,2,100)
print(new_arr)

