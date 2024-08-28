import random
import sys

rzips = [90007, 10102, 23474, 90018, 61023]

n = int(sys.argv[1])
for i in range(n):
    # get one random choice from rzips
    print(random.choice(rzips))
print(0)