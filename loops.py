# While loop
i = 1
while i <= 10:
    print(i)
    i += 1

print("Done with while loop")

# For loop
for letter in "Giraffe Academy":
    print(letter)

friends = ["Jim", "Karen", "Kevin"]
for friend in friends:
    print(friend)

for index in range(3, 10):
    print(index)

for index in range(len(friends)):
    print(friends[index])

for index in range(5):
    if index == 0:
        print("First iteration")
    else:
        print("Not First")

# 2D lists
number_grid = [
    [1, 2, 3],
    [4, 5, 6],
    [7, 8, 9],
    [0]
]

print(number_grid[3][0])

# Nested for loop
for row in number_grid:
    for column in row:
        print(column)
