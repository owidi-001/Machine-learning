import numpy as np
import time
import sys

items=np.array([23,34,35,5,42,21,342,4,343])

listItems=range(1000)
# get size of items
print(sys.getsizeof(5)*len(listItems))

numpyList=np.arange(1000)
print(numpyList.size*numpyList.itemsize)