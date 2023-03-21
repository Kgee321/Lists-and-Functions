""" Working with dictionary's """


# Hero list
hero_0 = {
    "name": "Materdon",
    "power": "flight",
    "strength": 5
}
# adding speed
hero_0["Speed"] = 12

# Changing speed
hero_0["strength"] = 8

# popping power
popped_item = hero_0.pop("power")

# outputting
print("\nSuperhero 1 stat\n")
for value, key in hero_0.items():
    print(f"{value}: {key}")







