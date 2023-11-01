height = int(input('What is the height?(1-8): '))
while height < 1 or height > 8:
    height = int(input('What is the height?(1-8): '))
    
for i in range(height):
    for j in range(height - i):
        print(' ', end= '')
    for j in range(0,i+1):
        print('#', end = '')
    print()