# Set 1

# Problem 1
# You're curating a large collection of NFTs for a digital art gallery,
# and your first task is to extract the names of these NFTs from a given list of dictionaries.
# Each dictionary in the list represents an NFT, and contains information such as the name, creator, and current value.

# Write the extract_nft_names() function, which takes in this list and returns a list of all NFT names.

# Evaluate the time and space complexity of your solution.
# Define your variables and provide a rationale for why you believe your solution has the stated time and space complexity.

def extract_nft_names(nft_collection):
    pass

def extract_nft_names(nft_collection):
    nft_names = []
    for nft in nft_collection:
        nft_names.append(nft["name"])
    return nft_names

# Example usage:
nft_collection = [
    {"name": "Abstract Horizon", "creator": "ArtByAlex", "value": 5.4},
    {"name": "Pixel Dreams", "creator": "DreamyPixel", "value": 7.2},
    {"name": "Future City", "creator": "UrbanArt", "value": 3.8}
]

nft_collection_2 = [
    {"name": "Crypto Kitty", "creator": "CryptoPets", "value": 10.5},
    {"name": "Galactic Voyage", "creator": "SpaceArt", "value": 6.7}
]

nft_collection_3 = [
    {"name": "Golden Hour", "creator": "SunsetArtist", "value": 8.9}
]

print(extract_nft_names(nft_collection))
print(extract_nft_names(nft_collection_2))
print(extract_nft_names(nft_collection_3))


# Problem 2
# You're responsible for ensuring the quality of the NFT collection before it is displayed in the virtual gallery. 
# One of your tasks is to review and debug the code that extracts the names of NFTs from the collection.
# A junior developer wrote the initial version of this function, but it contains some bugs that prevent it from working correctly.

# Task:
# Review the provided code and identify the bug(s).
# Explain what the bug is and how it affects the output.
# Refactor the code to fix the bug(s) and provide the correct implementation.

def extract_nft_names(nft_collection):
    nft_names = []
    for nft in nft_collection:
        nft_names.append(nft["name"]) # nft_names += nft["name"]
    return nft_names

# Tests
nft_collection = [
    {"name": "Abstract Horizon", "creator": "ArtByAlex", "value": 5.4},
    {"name": "Pixel Dreams", "creator": "DreamyPixel", "value": 7.2}
]

nft_collection_2 = [
    {"name": "Golden Hour", "creator": "SunsetArtist", "value": 8.9}
]

nft_collection_3 = []

print()
print("-"*50)
print()
print(extract_nft_names(nft_collection))

print()
print("-"*50)
print()
print(extract_nft_names(nft_collection_2))

print()
print("-"*50)
print()
print(extract_nft_names(nft_collection_3))


# Problem 3
# You have been tasked with identifying the most popular NFT creators in your collection. 
# A creator is considered "popular" if they have created more than one NFT in the collection.
# Write the identify_popular_creators() function, which takes a list of NFTs and returns a list 
# of the names of popular creators.
# Evaluate the time and space complexity of your solution. Define your variables and provide 
# a rationale for why you believe your solution has the stated time and space complexity.

def identify_popular_creators(nft_collection):
    creator_count = {
        # creator name : count
    }

    for nft in nft_collection: # O(n)
        creator = nft["creator"]
        if creator in creator_count:
            creator_count[creator] += 1
        else:
            creator_count[creator] = 1
    
    pop_creators = []
    for name, count in creator_count.items(): 
        if count > 1:
            pop_creators.append(name)
    
    return pop_creators

def find_duplicates(arr):
    seen = set()
    duplicates = set()
    for item in arr:
        if item in seen:
            duplicates.add(item)
        else:
            seen.add(item)
    return list(duplicates)

# Tests
nft_collection = [
    {"name": "Abstract Horizon", "creator": "ArtByAlex", "value": 5.4},
    {"name": "Pixel Dreams", "creator": "DreamyPixel", "value": 7.2},
    {"name": "Urban Jungle", "creator": "ArtByAlex", "value": 4.5}
]

nft_collection_2 = [
    {"name": "Crypto Kitty", "creator": "CryptoPets", "value": 10.5},
    {"name": "Galactic Voyage", "creator": "SpaceArt", "value": 6.7},
    {"name": "Future Galaxy", "creator": "SpaceArt", "value": 8.3}
]

nft_collection_3 = [
    {"name": "Golden Hour", "creator": "SunsetArtist", "value": 8.9}
]

print(identify_popular_creators(nft_collection)) # ['ArtByAlex']
print(identify_popular_creators(nft_collection_2)) # ['SpaceArt']
print(identify_popular_creators(nft_collection_3)) # []



