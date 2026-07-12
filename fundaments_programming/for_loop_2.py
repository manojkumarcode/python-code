dates = [1982, 1980, 1973]

n = len(dates)

for i in range(n):
    print(dates[i])

print("")
for year in dates:
    print(year)

squares = ['red', 'yellow', 'green', 'purple', 'blue']

for i in range(0, 5):
    print("Before square ", i, 'is',  squares[i])
    squares[i] = 'white'

print("")
for i in range(0, 5):  
    print("After square ", i, 'is',  squares[i])