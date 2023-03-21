""" Working with dictionary's """


# Finding item in the hero_0 dictionary
def finding_item(dic, item):

    # outputting the hero 0's strength
    if item in dic["name"]:
        print(f"That is a superhero name")
    else:
        print(f"That isn't a superhero name")


# Hero list
hero_0 = {
    "name": "Materdon",
    "power": "flight",
    "strength": 5
}

# if materdon in name
finding_item(hero_0, "Materdon")

# if katelyn in name
finding_item(hero_0, "Katelyn")





