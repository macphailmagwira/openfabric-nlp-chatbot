class HashTable:
    def __init__(self, size=100, prehashed=None):
        self.size = size
        self.table = [[] for _ in range(self.size)]

        if prehashed is not None:
            for bucket in prehashed:
                for key, value in bucket:
                    index = self._hash(key)
                    self.table[index].append((key, value))

    def _hash(self, key):
        # Hash function implementation goes here
        return abs(hash(key)) % self.size

    def put(self, key, value):
        index = self._hash(key)
        self.table[index].append((key, value))

    def get(self, key):
        index = self._hash(key)
        for k, v in self.table[index]:
            if k == key:
                return v
        raise KeyError(key)
    
    def print_table(self):
        for i, bucket in enumerate(self.table):
            print(f"Bucket {i}: {bucket}")
