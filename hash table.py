"""
### Hash Table ###
- Hash table are similar to dictionary in python store key and values.
- faster.

(Dictionaries in Python are implemented using a data structure called hash table.
A hash table uses a list/array to store the key-value pairs, and uses a hashing function to determine
the index for storing or retrieving the data associated with a given key.)

- Use ord inbuilt function to get the number for a specific character for eg:- "A" ord("A").
"""


class BasicHashTable:

    def __init__(self, max_size=4093):
        self.data_list = [None] * max_size

    @staticmethod
    def get_index(data_list, string):
        result = 0
        for i in string:
            number_ord = ord(i)
            result += number_ord

        index = result % len(data_list)
        return index

    def insert(self, key, value):
        idx = self.get_index(self.data_list, key)
        self.data_list[idx] = key, value

    def find(self, key):
        idx = self.get_index(self.data_list, key)
        kv = self.data_list[idx]

        if kv is None:
            return None
        else:
            key, value = kv
            return value

    def update(self, key, value):
        v = self.find(key)
        idx = self.get_index(self.data_list, key)
        if v is not None:
            self.data_list[idx] = key, value

    def list_all(self):
        return self.data_list

    def show(self, index):
        return self.data_list[index]


basic_table = BasicHashTable()
basic_table.insert('Aakash', '9999999999')
print(basic_table.find("Aakash"))
lst = [None] * 4093
print(basic_table.get_index(lst, "Aakash"))
print(basic_table.show(585))
basic_table.update("Aakash", "777")
print(basic_table.find("Aakash"))

"""
- While using hash table the problem can occur that if the key is same.
- We use Linear Probing Hash table.
(Linear probing is a scheme in computer programming for resolving collisions in hash tables,
data structures for maintaining a collection of key–value pairs and looking up the value
associated with a given key.)

- Re-sizing hash table
- we resize hash table if we want to store more data we double it in some condition.
for eg:- doubling the size if list when list stores or contain 70% of data.

- Time complexity :- O(1)
"""
# def get_index(data_list, string):
#     result = 0
#     for i in string:
#         number_ord = ord(i)
#         result += number_ord
#
#     index = result % len(data_list)
#     return index
