def get_indices_of_item_weights(weights, length, limit):
    """
    YOUR CODE HERE
    """
    # Step 1: Create a function
    # Step 2: Find two items whose sum of wieghts equals the weight limit
            # Create a hashtable/dict
            # Store the weight as key and index as value
            # 
    # Step 3: return a tuple of integers that has the following form: (zero,one)
    # Step 4: if we find nothing, return None

    # Constraints: Your solution should run in linear time.

    dictionary = {}

    for i in range(length):
        dictionary[weights[i]] = i

    for i in range(length):
        weight_limit = limit - weights[i]
        
        if weight_limit in dictionary:
            return ([max(i, dictionary[weight_limit]), min(i, dictionary[weight_limit])])
        
    return None




    
   
   
   
   
   
#     # Your code here
#     hashDict = dict()
#     indices = tuple()

#     for i in range(length):
#         val = weights[i]
#         hashDict[val] = i
    
#     if length == 1:
#         return None
   
#     else:
#         for i in range(length):
#             findWeight = limit - weights[i]
#             index = hashDict.get(findWeight)
        
#             if index > weights[i]:
#                 indices = indices + (index,)
#                 indices = indices + (weights[i],)
#                 return indices
#             else: 
#                 indices = indices + (weights[i],)
#                 indices = indices + (index,)
#         return indices      
          

# get_indices_of_item_weights([0,2], 2, 2)