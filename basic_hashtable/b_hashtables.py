

# '''
# Basic hash table key/value pair
# '''
class Pair:
    def __init__(self, key, value):
        self.key = key
        self.value = value


# '''
# Basic hash table
# Fill this in.  All storage values should be initialized to None

# '''
class BasicHashTable:
    def __init__(self, capacity):
        self.capacity = capacity
        self.count = 0
        self.elements = [None] * capacity


# '''
# Fill this in.
# Research and implement the djb2 hash function
# '''
def hash(string, max):
    hash_const = 5381
    for x in range(0, len(string)):
        hash_const = ((hash_const << 5) + hash_const)
    return hash_const % max


# '''
# Fill this in.

# If you are overwriting a value with a different key, print a warning.
# '''
def hash_table_insert(hash_table, key, value):
    # take key value and make a pair
    new_pair = Pair(key, value)
    index = hash(key, hash_table.capacity)

    if hash_table.elements[index]:
        print(f"warning, this is overwriting")

    hash_table.elements[index] = new_pair

# '''
# Fill this in.

# If you try to remove a value that isn't there, print a warning.
# '''
def hash_table_remove(hash_table, key):
    # this is the bucket
    index = hash(key, hash_table.capacity)

    if hash_table.elements[index] and hash_table.elements[index].key == key:
        hash_table.elements[index] = None
    else:
        print(f"that key/value pair doesn't exist")


# '''
# Fill this in.

# Should return None if the key is not found.
# '''
def hash_table_retrieve(hash_table, key):

    index = hash(key, hash_table.capacity)

    if hash_table.elements[index] and hash_table.elements[index].key == key:

        return hash_table.elements[index]
    else:
        return None


def Testing():
    ht = BasicHashTable(16)

    hash_table_insert(ht, "line", "Here today...\n")

    hash_table_remove(ht, "line")

    if hash_table_retrieve(ht, "line") is None:
        print("...gone tomorrow (success!)")
    else:
        print("ERROR:  STILL HERE")


Testing()
