# Lists in python (Data type insensitive)
friends = ["Kevin", "Karen", "Jim", "Oscar", "Oscar", "Tobi"]
lucky_numbers = [4, 8, 15, 16, 23, 42]

print(friends)
print(friends[1])
print(friends[-2])
# Grab element block
print(friends[1:])
print(friends[1:3])
# Change elements
friends[1] = "Mike"
print(friends)
# Add two lists
friends.extend(lucky_numbers)
print(friends)
# Append item to the list
friends.append("Creed")
# Insert item to the list
friends.insert(1, "Kelly")
print(friends)
# Removes a particular item
friends.remove("Jim")
print(friends)
# Removes last element from the end
friends.pop()
print(friends)
# Check for an element
print(friends.index("Kevin"))
# Count elements
print(friends.count("Oscar"))
# sort the list in ascending order
lucky_numbers.sort()
print(lucky_numbers)
lucky_numbers.reverse()
print(lucky_numbers)
friends2 = friends.copy()
print(friends2)
# Clears the whole list
friends.clear()
print(friends)

