# Basic Dictionary
info = {
    "name": "Vinit",
    "Roll no": 46
}
print(info)
print(info["name"])

# nested dict
nested_dict = {
    "name": "Vinit",
    "Roll no": 46,
    "Subjects": {
        "math": 20,
        "chem": 30,
        "phy": 40
    }
}
print("Nested dict")
print(nested_dict["Subjects"]["math"])
print("\n")

# Methods

# .keys()
print(".keys()")
print(nested_dict.keys()) # prints all keys
print("\n")

# to typecast into list
print(".keys() typecasted into list")
print(list(nested_dict.keys()))
print("\n")

# .values()
print(".values()")
print(nested_dict.values()) # print all values
print("\n")

# .items()
# returns all (key, val) in pairs of tuples
print(".items()")
print(nested_dict.items())
print("\n")

# typecasted into list
print(".items() typecasted into list")
pairs = list(nested_dict.items())
print(pairs[0])
print("\n")

# .get()
# doesnt return error
print(".get() doesnt return error and can set default val")
print(nested_dict.get("surname"))
print(nested_dict.get("surname", "patil"))
print("\n")