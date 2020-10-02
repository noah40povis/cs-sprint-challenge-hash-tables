def has_negatives(a):
    """
    YOUR CODE HERE
    """
    b = {}
    result = []
    #for every element of a we are going to cache the key as the number and the value as the negative of that number
    for number in a:
        b[number] = -number
        #
    for number in a:
        #for every number in a 
        if -number in b:
            #and if that number has a negative in cache b 
            if number > 0:
                #and if the number in a is greater than 0(positive) add that to the results 
                result.append(number)

    return result


if __name__ == "__main__":
    print(has_negatives([-1, -2, 1, 2, 3, 4, -4]))
