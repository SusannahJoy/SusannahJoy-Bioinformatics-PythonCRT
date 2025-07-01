import numpy as np
prices=np.array([50,20,30])
quantities=np.array([2,5,3])
total_bill=np.sum(prices*quantities)
print("Total Bill: ",total_bill)