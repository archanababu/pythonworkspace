#-------------------------------------------------------------------------------------------------------
# Dictionary - Special structure in python which allows us to store information called key, value pairs
#            - All of the key values should be unique
#-------------------------------------------------------------------------------------------------------

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

print(monthConversions.get("Jan"))
print(monthConversions.get("Dec","Not a valid key"))
print(monthConversions.get("Luv","Not a valid key"))

monthConversions1 = {
    1: "January",
    2: "February",
    3: "March",
    4: "April",
    5: "May",
    6: "June",
    7: "July",
    8: "August",
    9: "September",
    10: "October",
    11: "November",
    12: "December"
}

print(monthConversions1.get(6))
print(monthConversions1.get(8,"Not a valid key"))
print(monthConversions1.get(67,"Not a valid key"))