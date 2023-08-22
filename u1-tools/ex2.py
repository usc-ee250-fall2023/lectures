import sys

cnt = 0
quitVal = int(sys.argv[1])
curr = int(input())
while curr != quitVal:
    if curr >= 0:
        cnt += 1
    curr = int(input())
print(cnt)
