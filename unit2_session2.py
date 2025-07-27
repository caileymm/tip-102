# set 1

# problem 1
def most_endangered(species_list):
    # holds most endangered species name and population
    endangered = [
        species_list[0]["name"],
        species_list[0]["population"]
    ]

    for species in species_list:
        if species["population"] < endangered[1]:
            endangered[0] = species["name"]
            endangered[1] = species["population"]
    
    return endangered[0]

species_list = [
    {"name": "Amur Leopard",
     "habitat": "Temperate forests",
     "population": 84
    },
    {"name": "Javan Rhino",
     "habitat": "Tropical forests",
     "population": 72
    },
    {"name": "Vaquita",
     "habitat": "Marine",
     "population": 10
    }
]

print(most_endangered(species_list))

# problem 2
def count_endangered_species(endangered_species, observed_species):
    # set for endangered species ?
    # counter

    count = 0
    es_set = set(endangered_species)

    for index_i, char_i in enumerate(observed_species):
        for index_j, char_j in enumerate(es_set):
            if char_i == char_j:
                count += 1

    return count


endangered_species1 = "aA"
observed_species1 = "aAAbbbb"

endangered_species2 = "z"
observed_species2 = "ZZ"

print(count_endangered_species(endangered_species1, observed_species1)) 
print(count_endangered_species(endangered_species2, observed_species2))  