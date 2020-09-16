#  Hint:  You may not need all of these.  Remove the unused functions.

# Step 1: Create a hash table 
        # Create empty route
# Step 2: Store source as key, destination as value
# Step 3: Loop over every position in the table, starting from None
# Step 4: 
class Ticket:
    def __init__(self, source, destination):
        self.source = source
        self.destination = destination


def reconstruct_trip(tickets, length):
    """
    YOUR CODE HERE
    """
    dictionary = {}
    route =[]
    
    for ticket in tickets: 
        dictionary[ticket.source] = ticket.destination
    starting_point = dictionary["NONE"]

    while starting_point is not "NONE":
        route.append(starting_point)
        starting_point = dictionary[starting_point]
    
    route.append("NONE")

    return route
    
    
    
    
    
    
    
    
    
    
    
    
    
    # # Your code here
    # print(tickets)
    # saveTickets = dict()
    # route = []

    # for i in range(length):
    #     des = tickets.destination
    #     sor = tickets.source
    #     saveTickets[sor] = des
    #     print(saveTickets)
    
    # for i in range(length):
    #     if saveTickets.keys()[i] == "None":
    #         route.append(saveTickets.keys()[i])
    #         if saveTickets.values()[i] == saveTickets.keys()[i+1]:
    #             route.append(saveTickets.values()[i])
    #             route.append(saveTickets.key()[i+1])
    #             print(route)
    #     print(route)

    # return route
