#  Hint:  You may not need all of these.  Remove the unused functions.
class Ticket:
    def __init__(self, source, destination):
        self.source = source
        self.destination = destination


def reconstruct_trip(tickets, length):
    #create dictionary 
    ticket_dic = {}
    #for ticket in tickets add them to dictionary as keyvalue pair 
    for ticket in tickets:
        ticket_dic[ticket.source] = ticket.destination
    #create an empty list for the routes 
    route = []
    #loop through length of length 
    for i in range(length):
        # if i == 0 then set it to none to indicate beginning / end 
        if i == 0:
            route.append(ticket_dic["NONE"])
        else:
            #otherwise append key of tickets dic to route list 
            route.append(ticket_dic[route[i-1]])
    return route

