def test(x):
    tempRes = 0
    for i in range(0, x + 1):
        tempRes += i
    print(tempRes)

n = int(input())
test(n)