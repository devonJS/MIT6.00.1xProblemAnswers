''' 
Counts number of 'bob' found in a given string
'''

def bob_count(str):
    bob_counter = 0
    search_index = 0
    
    while str.find('bob', search_index) != -1:
        bob_counter += 1
        search_index = str.find('bob', search_index) + 1
        
    return bob_counter

print bob_count("azcbobobegghakl")