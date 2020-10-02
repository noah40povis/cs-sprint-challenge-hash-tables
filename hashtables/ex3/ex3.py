def intersection(arrays):
    result = []
    cache = {}
    arr = []
    #add elements from arrays to arr empty list 
    for array in arrays:
        arr = arr + array
        #iterate through new list then if item in cache add a plus one 
    for item in arr:
        if item in cache:
            #set value to add to one 
            cache[item] += 1
        else:
            #else just set to one one 
            cache[item] = 1

       # iterate through the keys of the dic 
    for key in cache.keys():
        #if any given key (actual number) equals the length arrays (which is number of arrays)
        if cache[key] == len(arrays):
            # append to result 
            result.append(key)

    return result

if __name__ == "__main__":
    arrays = []

    arrays.append(list(range(1000000, 2000000)) + [1, 2, 3])
    arrays.append(list(range(2000000, 3000000)) + [1, 2, 3])
    arrays.append(list(range(3000000, 4000000)) + [1, 2, 3])

    print(intersection(arrays))
