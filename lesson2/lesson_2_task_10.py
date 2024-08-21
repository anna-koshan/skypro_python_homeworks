def bank(x, y):
    for year in range(y):
        x = (x * 1.1)
    print(x)
x = int(input())
y = int(input())
bank(x,y)