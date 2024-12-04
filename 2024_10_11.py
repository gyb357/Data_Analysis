# %%
import numpy as np
# %%
mid_scores = np.array([10, 20, 30])
final_scores = np.array([60, 70, 80])
total = mid_scores + final_scores

print('total:', total)
print('average: ', total / 2)
# %%
a = np.array(range(1, 11))
b = np.array(range(10, 101, 10))
c = a + b
c = a - b
c = a*b
c = a/b
# %%
a = np.array([1, 2, 3])
a.shape
a.ndim
a.dtype
a.itemsize
# %%
