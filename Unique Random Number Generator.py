#unique random number generator in a ranges
import random
import time
start = time.time()
print(random.sample(range(0,999999999),999999999)) #define the range of numbers, # of #s to print
time.sleep(1)
end = time.time()
print(f"Time taken by this program is : {end-start} seconds")