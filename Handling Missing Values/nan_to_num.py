import numpy as np

arr = np.aray([1,2,np.nan,4, np.nan,6])

cleaned_arr = np.nan_to_num(arr,nan=100)
print(cleaned_arr)


#np.nan_to_num(arr,nan=100 if we were dont put 100 value will be 0
               