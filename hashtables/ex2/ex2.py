#  Hint:  You may not need all of these.  Remove the unused functions.
from hashtables import (HashTable,
                        hash_table_insert,
                        hash_table_remove,
                        hash_table_retrieve,
                        hash_table_resize)


class Ticket:
    def __init__(self, source, destination):
        self.source = source
        self.destination = destination


def reconstruct_trip(tickets, length):
    hashtable = HashTable(length)
    route = [None] * (length-1)

    for ticket in tickets:
        hash_table_insert(hashtable, ticket.source, ticket.destination)
        # if ticket.source == "NONE":
        #     route[0] = ticket.destination
        #     # hash_table_remove(hashtable, ticket.source)
        # if ticket.destination == "NONE":
        #     route[-1] = ticket.source
        #     # hash_table_remove(hashtable, ticket.source)
    destination = hash_table_retrieve(hashtable, 'NONE')
    i = 0
    while destination != "None":
        try:
            route[i] = destination
        except:
            break
        destination = hash_table_retrieve(hashtable, destination)
        print(route)
        i+=1
    return route
        
