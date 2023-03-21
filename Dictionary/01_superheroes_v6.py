""" Working with dictionary's """


# Hero list
hero_0 = {
    "name": "Materdon",
    "power": "flight",
    "strength": 5
}

hero_1 = {
    "name": "Orasy",
    "power": "x-ray vision",
    "strength": 2,
    "speed": 8

}

# adding list togeth
hero_list = [hero_0, hero_1]
print(hero_list, f"\n")

# for list to print values
for i in hero_list:
    print(f"{i['name']}'s superpower is {i['power']} and their strength value is "
          f"{i['strength']}")







