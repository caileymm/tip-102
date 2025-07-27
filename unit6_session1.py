# Set 1

# Problem 1
# class SongNode:
# 	def __init__(self, song, next=None):
# 		self.song = song
# 		self.next = next

# # For testing
# def print_linked_list(node):
#     current = node
#     while current:
#         print(current.song, end=" -> " if current.next else "")
#         current = current.next
#     print()
		
# top_hits_2010s = SongNode("Uptown Funk")
# node2 = SongNode("Party Rock Anthem")
# node3 = SongNode("Bad Romance")

# top_hits_2010s.next = node2
# node2.next = node3

# # Test
# print_linked_list(top_hits_2010s) # Output: Uptown Funk -> Party Rock Anthem -> Bad Romance


# # Problem 2
# class SongNode:
#     def __init__(self, song, artist, next=None):
#         self.song = song
#         self.artist = artist
#         self.next = next

# # For testing
# def print_linked_list(node):
#     current = node
#     while current:
#         print((current.song, current.artist), end=" -> " if current.next else "")
#         current = current.next
#     print()

# def get_artist_frequency(playlist):
# 	# create a dictionary to hold artist and frequency
#     frequency = {}

#     # traverse linked list
#     current = playlist
#     while(current is not None):
#         if current.artist in frequency:
#             frequency[current.artist] += 1
#         else:
#             frequency[current.artist] = 1
#         current = current.next

#     return frequency

# # Test
# playlist = SongNode("Saturn", "SZA", 
#                 SongNode("Who", "Jimin", 
#                         SongNode("Espresso", "Sabrina Carpenter", 
#                                 SongNode("Snooze", "SZA"))))

# print(get_artist_frequency(playlist))
# # Output: { "SZA": 2, "Jimin" : 1, "Sabrina Carpenter": 1}


# # Problem 3
# class SongNode:
#     def __init__(self, song, artist, next=None):
#         self.song = song
#         self.artist = artist
#         self.next = next

# # For testing
# def print_linked_list(node):
#     current = node
#     while current:
#         print((current.song, current.artist), end=" -> " if current.next else "")
#         current = current.next
#     print()


# # Function with a bug!
# def remove_song(playlist_head, song):
#     if not playlist_head:
#         return None
#     if playlist_head.song == song:
#         return playlist_head.next

#     current = playlist_head
#     previous = None
#     while current.next:
#         if current.song == song:
#             previous.next = current.next
#             return playlist_head
#         previous = current
#         current = current.next

#     return playlist_head

# playlist = SongNode("SOS", "ABBA", 
#                 SongNode("Simple Twist of Fate", "Bob Dylan",
#                     SongNode("Dreams", "Fleetwood Mac",
#                         SongNode("Lovely Day", "Bill Withers"))))

# print_linked_list(remove_song(playlist, "Dreams"))
# # Output: ('SOS', 'ABBA') -> ('Simple Twist of Fate', 'Bob Dylan') -> ('Lovely Day', 'Bill Withers')


# # Problem 4
# class SongNode:
#     def __init__(self, song, artist, next=None):
#         self.song = song
#         self.artist = artist
#         self.next = next

# def on_repeat(playlist_head):
#     slow = playlist_head
#     fast = playlist_head
    
#     while fast is not None and fast.next is not None:      
#         slow = slow.next
#         fast = fast.next.next

#         if slow == fast:
#             return True
    
#     return False


# # Test
# song1 = SongNode("GO!", "Common")
# song2 = SongNode("N95", "Kendrick Lamar")
# song3 = SongNode("WIN", "Jay Rock")
# song4 = SongNode("ATM", "J. Cole")
# song1.next = song2
# song2.next = song3
# song3.next = song4
# song4.next = song2

# print(on_repeat(song1))
# # Output: True


# Problem 5
class SongNode:
    def __init__(self, song, artist, next=None):
        self.song = song
        self.artist = artist
        self.next = next

# For testing
def print_linked_list(node):
    current = node
    while current:
        print((current.song, current.artist), end=" -> " if current.next else "")
        current = current.next
    print()

def loop_length(playlist_head):
    if not playlist_head:
        return 0
    
    slow = playlist_head
    fast = playlist_head

    cycle_head = None

    while fast is not None and fast.next is not None:
        slow = slow.next
        fast = fast.next.next

        if slow == fast:
            cycle_head = slow
            break

    if cycle_head is None:
        return 0

    print(cycle_head.song)
    current = cycle_head.next
    counter = 1
    while current != cycle_head:
        counter += 1
        current = current.next

    return counter

# Test
song1 = SongNode("Wein", "AL SHAMI")
song2 = SongNode("Si Ai", "Tayna")
song3 = SongNode("Qalbi", "Yasser Abd Alwahab")
song4 = SongNode("La", "DYSTINCT")
song1.next = song2
song2.next = song3
song3.next = song4
song4.next = song2

print(loop_length(song1))
# Output: 3