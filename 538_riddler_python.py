import numpy as np
import time
cards = np.tile([i for i in range(1, 14)], 4)
shuffled = cards.copy()
n, losses = 1000000, 0
start_time = time.time()
for i in range(n):
     losses += np.any(cards == np.random.permutation(shuffled)) 
print(time.time() - start_time)
