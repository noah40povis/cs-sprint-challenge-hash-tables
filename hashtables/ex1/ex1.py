
def get_indices_of_item_weights(weights, length, limit):
    #create empty dictionary 
    dic = {}
    #enumerate through weights , subtract limit from weight to get remainder which would be the second value we would search for 
    possible_combination = [[limit-weight, index] for index, weight in enumerate(weights)]
    #check 
    print(possible_combination)
    #add weight and index key value pairs
    for index, weight in enumerate(weights):
        #set weights as the index 
        dic[weight] = index
        #iterate through possible combinations
    print(dic)
    for combination in possible_combination:
        #if combination is in dic return tuple 
        if combination[0] in dic:
            return (dic[combination[0]], combination[1])

weights = [ 4, 6, 10, 15, 16 ]
print(get_indices_of_item_weights(weights, 5, 10))
