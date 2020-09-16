# Step 1: Get the length of the arrays, to check how many items are in it 
# Step 2: Loop over each item in the first array
# Step 3: Add the items to the hash table as keys, and values as 1
# Step 4: Continue for all arrays

def intersection(arrays):
    """
    YOUR CODE HERE
    """
    list_length = len(arrays)
    dictionary = {}
    result = []

    # Adding first array to dictionary
    for item in arrays[0]:
        dictionary[item] = 1

    # Loop over two other arrays, and check to see if number is in array
    for item2 in range(1,list_length):
        for num in arrays[item2]:
            if num in dictionary:
                dictionary[num] += 1

    for key in dictionary:
        if dictionary[key] ==  list_length:
            result.append(key)

    return result







    # Your code here
    # dictionary = dict()
    # result = []
    # # iterate through the arrays list, add the item from each list to the dictionary as key
    # # if the ket is already in the dictionary add the 1 to the value of that key else the 
    # # value is equal to one
    # for i in len(arrays):
    #     for item in arrays[i]:
    #         if item in dictionary:
    #             dictionary[item] += 1
    #         else:
    #             dictionary[item] = 1
                
    # length = len(arrays)
    
    # # Check if the value of a key is equal to the length of the array, add the key to result if they are equal
    # for key,value in dictionary.items():
    #     if length == value:
    #         result.append(key)
    
    


if __name__ == "__main__":
    arrays = []

    arrays.append(list(range(1000000, 2000000)) + [1, 2, 3])
    arrays.append(list(range(2000000, 3000000)) + [1, 2, 3])
    arrays.append(list(range(3000000, 4000000)) + [1, 2, 3])

    print(intersection(arrays))
