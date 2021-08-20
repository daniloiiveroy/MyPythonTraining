print("Imported new_module")

test_str = "Test String"

def find_by_index(to_search,target):
    '''find the index of a value in a sequence'''
    for i, value in enumerate(to_search):
        if value == target:
            return i
    
    return -1