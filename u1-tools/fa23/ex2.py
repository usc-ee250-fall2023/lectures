import sys

f1()
print("Hi")
def f1():
    quitval = int(sys.argv[1])
    num =  int(input("Enter an integer: "))
    sum = 0
    while quitval != num:
        if num >= 0:
            sum += num
        # get the next input
        num =  int(input("Enter an integer: "))
    print("Sum is", sum)
print("Bye")
