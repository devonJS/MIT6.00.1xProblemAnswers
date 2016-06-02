'''
Wrapper function that does initial checks on the two strings,
these are cases in which the two strings are automatically not semordnilap
'''

def semordnilapWrapper(str1, str2):
    if len(str1) == 1 or len(str2) == 1:
        return False
    
    if len(str1) !=  len(str2):
        return False
        
    if str1 == str2:
        return False
    
    return semordnilap(str1, str2)

'''
Checks if two strings are semordnilap, meaning one word spells a different word backwards
'''
def semordnilap(str1, str2):
    '''
    str1: a string
    str2: a string
    
    returns: True if str1 and str2 are semordnilap;
             False otherwise.
    '''
    if len(str1) == 1 and len(str2) == 1:
        if str1 == str2:
            return True
        else:
            return False
            
    if str1[0] == str2[len(str2) - 1]:
        return semordnilap(str1[1:], str2[:len(str2) - 1])
    else: 
        return False

print(semordnilapWrapper('semordnilap', 'palindromes')) # Expects True 
print(semordnilapWrapper('desserts', 'stressed')) # Expects True
print(semordnilapWrapper('rats live on', 'no evil star')) # Expects True
print(semordnilapWrapper('utzqcls', 'ojuqhiea')) # Expects False
print(semordnilapWrapper('z', 'z')) # Expects False
print(semordnilapWrapper('b', 'n')) # Expects False