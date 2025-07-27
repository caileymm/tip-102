# Set 1

class Villager:
    def __init__(self, name, species, personality, catchphrase):
        self.name = name
        self.species = species
        self.personality = personality
        self.catchphrase = catchphrase
        self.furniture = []

    def greet_player(self, player_name):
        return f"{self.name}: Hey there, {player_name}! How's it going, {self.catchphrase}!"
    
    def set_catchphrase(self, new_catchphrase):
        if len(new_catchphrase) < 20 and (new_catchphrase.isalpha() or " " in new_catchphrase):
            self.catchphrase = new_catchphrase
            print("Catchphrase updated")
        else:
            print("Invalid catchphrase")

    def add_item(self, item_name):
        if item_name in ["acoustic guitar", "ironwood kitchenette", "rattan armchair", "kotatsu", "cacao tree"]:
            self.furniture.append(item_name)

    def print_inventory(self):
        if not self.furniture:
            print("Inventory empty")
            return
        
        inventory_dict = {}

        for f in self.furniture:
            if f not in inventory_dict:
                inventory_dict[f] = 1
            else:
                inventory_dict[f] += 1
        
        for furniture, count in inventory_dict.items():
            print(f"{furniture} : {count}, ", end="")
    
'''
# Problem 1
apollo = Villager("Apollo", "Eagle", "pah")

print(apollo.name)  
print(apollo.species)  
print(apollo.catchphrase) 
print(apollo.furniture) 

# Problem 2
bones = Villager("Bones", "Dog", "yip yip")
print(bones.greet_player("Cailey"))

# Problem 3
bones.catchphrase = "ruff it up"
print(bones.greet_player("Samia"))

# Problem 4
alice = Villager("Alice", "Koala", "guvnor")

alice.set_catchphrase("sweet dreams")
print(alice.catchphrase)
alice.set_catchphrase("#?!")
print(alice.catchphrase)

# Problem 5
alice = Villager("Alice", "Koala", "guvnor")
print(alice.furniture)

alice.add_item("acoustic guitar")
print(alice.furniture)

alice.add_item("cacao tree")
print(alice.furniture)

alice.add_item("nintendo switch")
print(alice.furniture)

# Problem 6
alice = Villager("Alice", "Koala", "guvnor")

alice.print_inventory()

alice.furniture = ["acoustic guitar", "ironwood kitchenette", "kotatsu", "kotatsu"]
alice.print_inventory()
'''
# Problem 7
def of_personality_type(townies, personality_type):
    personality_list = []
    for townie in townies:
        if townie.personality == personality_type:
            personality_list.append(townie.name)

    return personality_list

isabelle = Villager("Isabelle", "Dog", "Normal", "what's up?")
bob = Villager("Bob", "Cat", "Lazy", "pthhhpth")
stitches = Villager("Stitches", "Cub", "Lazy", "stuffin'")

print(of_personality_type([isabelle, bob, stitches], "Lazy"))
print(of_personality_type([isabelle, bob, stitches], "Cranky"))

# Problem 8
