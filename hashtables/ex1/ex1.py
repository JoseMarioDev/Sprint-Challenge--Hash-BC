#  Hint:  You may not need all of these.  Remove the unused functions.
from hashtables import (HashTable,
                        hash_table_insert,
                        hash_table_remove,
                        hash_table_retrieve,
                        hash_table_resize)


def get_indices_of_item_weights(weights, length, limit):
    ht = HashTable(16)

    """
    YOUR CODE HERE
    """
    
    # loop through weights, add to ht
    for index in range(length):
        hash_table_insert(ht, weights[index], index)

    # loop through ht, retrieve pair
    for index in range(length):
        key = limit - weights[index]
        second_index = hash_table_retrieve(ht, key)

        # sort by index of higher weight
        if second_index:
            if second_index > index:
                return [second_index, index]
            else:
                return [index, second_index]

    # if a pair does not exist then return None
    return None


def print_answer(answer):
    if answer is not None:
        print(str(answer[0] + " " + answer[1]))
    else:
        print("None")

