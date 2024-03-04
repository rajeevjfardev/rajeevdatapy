

#practiceagain

def sort_tuples(tuples):
    
    def last_element(tuple):
        return tuple[-1]

    sorted_tuples = sorted(tuples, key=last_element)
    return sorted_tuples

tuples = [(2, 5), (1, 2), (4, 4), (2, 3), (2, 1)]

sorted_tuples = sort_tuples(tuples)
print(sorted_tuples)