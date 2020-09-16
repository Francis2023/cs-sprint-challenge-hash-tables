class HashTable:
    """
    A hash table that with `capacity` buckets
    that accepts string keys

    Implement this.
    """

    def __init__(self, capacity):
        # Your code here
        self.array = [None] * capacity
      

    def get_num_slots(self):
        """
        Return the length of the list you're using to hold the hash
        table data. (Not the number of items stored in the hash table,
        but the number of slots in the main list.)

        One of the tests relies on this.

        Implement this.
        """
        # Your code here
        return len(self.array)


    def get_load_factor(self):
        """
        Return the load factor for this hash table.

        Implement this.
        """
        # Your code here
        
        return self.size / self.capacity


    def fnv1(self, key):
        """
        FNV-1 Hash, 64-bit

        Implement this, and/or DJB2.
        """

        # Your code here
        encodedStr = key.encode()

        total = 0
        for element in encodedStr:
            total += element
            total &= 0xffffffff
        
        return total


    def djb2(self, key):
        """
        DJB2 hash, 32-bit

        Implement this, and/or FNV-1.
        """
        # Your code here
        hash = 5381
        for x in key:
            hash = (hash << 5) + hash + ord(x)
        return (hash  & 0xfffffff)

    def hash_index(self, key):
        """
        Take an arbitrary key and return a valid integer index
        between within the storage capacity of the hash table.
        """
        #return self.fnv1(key) % self.capacity
        return self.djb2(key) % self.capacity

    def put(self, key, value):
        """
        Store the value with the given key.

        Hash collisions should be handled with Linked List Chaining.

        Implement this.
        """
        # Your code here
        index = self.hash_index(key)


        if self.array[index] != None:
            print(f"Collision! Overwriting {repr(self.array[index])}!")
        self.array[index] = value
       
       


    def delete(self, key):
        """
        Remove the value stored with the given key.

        Print a warning if the key is not found.

        Implement this.
        """
        # Your code here
        
        index = self.hash_index(key)
        self.array[index] = None
        

        # if self.array[index] is None:
        #     print('Key not found!')
        # else:
        #     self.array[index] = None
        #     print(self.array)

    def get(self, key):
        """
        Retrieve the value stored with the given key.

        Returns None if the key is not found.

        Implement this.
        """
        # Your code here
        index = self.hash_index(key)
        
        return self.array[index]
          
            

    def resize(self, new_capacity):
        """
        Changes the capacity of the hash table and
        rehashes all key/value pairs.

        Implement this.
        """
        # Your code here
        self.newArray = self.HastTable(new_capacity)

        for i in range(len(self.array)):
            if self.array[i] is None:
                continue

            for val in self.array[i]:
                self.newArray.put()
