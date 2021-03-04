# It is a special structure.
# It allows us to store information as key-value pairs
# Keys are always unique
# Convert 3 alphabet month name to a full month name
monthConversions = {
    "Jan": "January",
    "Feb": "February",
    "Mar": "March",
    "Apr": "April",
    "May": "May",
    "Jun": "June",
    "Jul": "July",
    "Aug": "August",
    "Sep": "September",
    "Oct": "October",
    "Nov": "November",
    "Dec": "December"
}

# Ways to get the value associated to a key
print(monthConversions["Nov"])
# Gives "None" when the key is not found
print(monthConversions.get("Dec"))
print(monthConversions.get("Luv", "Not a valid key"))
