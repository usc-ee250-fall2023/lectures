
zips = {}
currzip = int(input())
while currzip != 0:
    # first occurrence
    if currzip not in zips:
        zips[currzip] = 1
    else:
        zips[currzip] += 1
    # get next number
    currzip = int(input())

for zip,occ in zips.items():
    print(zip, ":", occ)