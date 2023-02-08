import numpy as np

b = np.uint8(124)
print(b)
# 124
print(type(b))
# <class 'numpy.uint8'>
np.iinfo(b)
# iinfo(min=0, max=255, dtype=uint8)

print(np.sctypeDict)
print(len(np.sctypeDict))
# 158, но может быть 135 или 139

print(*sorted(map(str, set(np.sctypeDict.values()))), sep='\n')

b = np.uint1(-456)
print(b)