# set 1
# problem 1
def welcome():
    print("Welcome to the Hundred Acre Wood!")

welcome()

# problem 2
def greeting(name):
    print(f"Welcome to the Hundred Acre Wood {name}! My name is Christopher Robin.")

greeting("Michael")
greeting("Winnie the Pooh")

# problem 3
def print_catchphrase(character):
    if character == "Pooh":
        print("Oh brother!")
    elif character == "Tigger":
        print("TTFN: Ta-ta for now!")
    elif character == "Eeyore":
        print("Thanks for noticing me.")
    elif character == "Christopher Robin":
        print("Silly old bear.")
    else:
        print(f"Sorry! I don't {character}'s catchphrase!")

character = "Pooh"
print_catchphrase(character)
character = "Piglet"
print_catchphrase(character)

# problem 4
def get_item(items, x):
    if x < len(items):
        print(items[x])
    else: 
        print("None")

items = ["piglet", "pooh", "roo", "rabbit"]
x = 2
get_item(items, x)

items = ["piglet", "pooh", "roo", "rabbit"]
x = 5
get_item(items, x)

    
