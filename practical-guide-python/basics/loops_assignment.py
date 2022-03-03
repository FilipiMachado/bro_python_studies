# 1) Create a list of names and use a for loop to output the length of each name (len()).
# 2) Add an if check inside the loop to only output names longer than 5 characters.
# 3) Add another if check to see whether a name includes a “n” or “N” character.
# 4) Use a while loop to empty the list of names (via pop())

names = ['fil', 'banzo', 'funil', 'willy smith', 'aero will']

for name in names:
    while len(names) >= 1:
        print("Names: " + names.pop())

print('Final list: ' + str(names))
""" print(name) """
""" if len(name) > 5:
        print(len(name)) """
""" if name[-1] == 'l' or 'L' or 'll' or 'LL':
         print("Name with l: " + name) """