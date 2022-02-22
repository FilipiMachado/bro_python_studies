# Exercise 1
""" for i in range(1, 11):
    print(i) """
    
# Exercise 2
""" for i in range(1, 6, 1):
    for j in range(1, i + 1):
        print(j, end=' ')
    print() """
    
# Exercise 3
j = 0
n = int(input('Enter a value: '))

for i in range(1, n + 1, 1):
    j += i
print(j)