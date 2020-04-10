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

# tests

#   def test_ex1_1(self):
#         weights_1 = [9]
#         answer_1 = get_indices_of_item_weights(weights_1, 1, 9)
#         self.assertTrue(answer_1 is None)

#     def test_ex1_2(self):
#         weights_2 = [4, 4]
#         answer_2 = get_indices_of_item_weights(weights_2, 2, 8)
#         self.assertTrue(answer_2[0] == 1)
#         self.assertTrue(answer_2[1] == 0)

#     def test_ex1_3(self):
#         weights_3 = [4, 6, 10, 15, 16]
#         answer_3 = get_indices_of_item_weights(weights_3, 5, 21)
#         self.assertTrue(answer_3[0] == 3)
#         self.assertTrue(answer_3[1] == 1)

#     def test_ex1_4(self):
#         weights_4 = [12, 6, 7, 14, 19, 3, 0, 25, 40]
#         answer_4 = get_indices_of_item_weights(weights_4, 9, 7)
#         self.assertTrue(answer_4[0] == 6)
#         self.assertTrue(answer_4[1] == 2)
