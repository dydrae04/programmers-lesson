'''x = int(input('Input number: '))
epsilon=0.01

low=0
high=max(0, x)

ans=0

while abs(ans**2-x)>epsilon:
    ans=(low+high)/2.0
    print('low={}, high={}, ans={}'.format(low, high, ans))
    if ans**2<x:
        low=ans
    else:
        high=ans'''

x=int(input("Input number: "))
epsilon=0.01
ans=0
low=0
high=max(0,x)

while abs(ans**2-x)>epsilon:
    ans=(low+high)/2.0
    print("low={}, high={}, x_sqrt={}".format(low, high,ans))
    if ans**2<x:
        low=ans
    else:
        high=ans

print("{}'s square root is {}".format(x, ans))

    