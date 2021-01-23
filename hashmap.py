class HashMap:
    def __init__(self):
        self.arr = [None for i in range(10)]
    def get_hash(self, key):
        h = 0
        for ha in key:
            h += ord(ha)
        return h % 10
    def __getitem__(self, item):
        for i in range(len(self.arr)):
            if self.arr[i] != None and self.arr[i][0] == item:
                return self.arr[i][1]

        print("Item not found")
    def __setitem__(self, key, value):
        h = self.get_hash(key)
        free_space = self.find_free_space(key)

        self.arr[free_space] = (key, value)

    def get_range(self, index):
        return [*range(index, len(self.arr))] + [*range(0, index)]
    # Function

    def find_free_space(self, key):
        h = self.get_hash(key)
        range = self.get_range(h)
        for index in range:
            if self.arr[index] is None:
                return index
            if self.arr[index][0] == key:
                return index
        raise Exception("Array is full")

h = HashMap()
h['march 6'] = 15

print(h['march 6'], h.arr)