pi4 = 0
sign = 1
for num in range(1,100,2):
    print(sign,'/', num)
    pi4 = pi4 + sign * 1/num
    sign = sign * -1

print(4*pi4)