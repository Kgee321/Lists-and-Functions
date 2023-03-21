""" Working with dictionary's """

# Hero list
heroes = {
    "MAT":
        {"name": "Materdon",
         "power": "flight",
         "strength": 5},
    "ORA":
        {"name": "Orasy",
         "power": "x-ray vision",
         "strength": 2,
         "speed": 8}
}

# printing
for hero_id, hero_info in heroes.items():
    print(f"\nHero ID: {hero_id}")

    for key, value in hero_info.items():
        print(f"{key}: {value}")

