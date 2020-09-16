class HashTable:
    def __init__(self, capacity):
       
        self.array = [None] * capacity
      
    def get_num_slots(self):
       
        return len(self.array)

    def get_load_factor(self):
        
        return self.size / self.capacity

    def fnv1(self, key):
       
        encodedStr = key.encode()

        total = 0
        for element in encodedStr:
            total += element
            total &= 0xffffffff
        
        return total

    def djb2(self, key):
       
        hash = 5381
        for x in key:
            hash = (hash << 5) + hash + ord(x)
        return (hash  & 0xfffffff)

    def hash_index(self, key):
       
        return self.djb2(key) % self.capacity

    def put(self, key, value):
       
        index = self.hash_index(key)

        if self.array[index] != None:
            print(f"Collision! Overwriting {repr(self.array[index])}!")
        self.array[index] = value
       
    def delete(self, key):
        
        index = self.hash_index(key)
        self.array[index] = None

    def get(self, key):
        
        index = self.hash_index(key)
        
        return self.array[index]
          
    def resize(self, new_capacity):
        
        self.newArray = self.HastTable(new_capacity)

        for i in range(len(self.array)):
            if self.array[i] is None:
                continue

            for val in self.array[i]:
                self.newArray.put()


def has_negatives(a):
    """
    YOUR CODE HERE
    """
    # Your code here
    length = len(a)
    newA = abs(a)
    result = []
    table = HashTable(length)

    for i in length:
        if newA[i] in table:
            result.append(newA[i])
            key = newA[i]
            table.put(key,i)
        else:
            table.put(newA[i],i)

    return result


if __name__ == "__main__":
    print(has_negatives([-1, -2, 1, 2, 3, 4, -4]))
