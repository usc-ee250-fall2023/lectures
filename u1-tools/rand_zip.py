import random
import sys

rzips = [10012, 90007, 90201, 91324, 95613]
n = int(sys.argv[1])
for i in range(n):
    print(random.choice(rzips))
print(0)