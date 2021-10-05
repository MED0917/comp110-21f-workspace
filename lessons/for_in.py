"""Example of for-in syntax."""

names: list[str] = ["Morgan", "Jess", "Grace", "Liz"]

# Example of interating through names using a while loop
print("while output: ")
i: int = 0
while i < len(names):
    name: str = names[i]
    print(name)
    i += 1

print("for-in output: ")
# The following for-in loop is the same as while loop above
for name in names: 
    print(name)