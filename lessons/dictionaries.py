"""Demonstrations of dictionary capabilities."""


# Declaring the type of a dictionary
schools: dict[str, int]

# Initialize to an empty dictionary
schools = dict()

# Set a key-value pairing in the dictionary
schools["UNC"] = 19_400
schools["Duke"] = 6_717
schools["NCSU"] = 26_150

# Print a dictionary literal representation
print(schools)

# Access a key-val by its key -- lookup
print(f"UNC has {schools['UNC']} students")

# Removing a key-value pair from dict 
# by its key
schools.pop("Duke")

# Test for existence of a key
is_duke_present: bool = "Duke" in schools
print(f"Duke is present: {is_duke_present}")

# Reassign a key-value pair
schools["UNC"] = 20000
schools["NCSU"] += 200

print(schools)

# Demonstration of dictionary literals
# Empty dict literal
schools = {}  # Same as dict()
print(schools)

# Alternatively, initialize key-value pairs
schools = {"UNC": 19400, "Duke": 6717, "NCSU": 26150}
print(schools)

# What happens when a key does not exist
# print(schools["UNCC"])

# Example looping over the keys of a dict
for school in schools:
    print(f"Key: {schools} -> Value: {schools[school]}")
    