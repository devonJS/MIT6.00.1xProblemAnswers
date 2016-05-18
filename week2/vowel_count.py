'''
Counts number of vowels in a string
'''

def vowel_counter(s):
    vowel_count = 0
    for j in xrange(len(s)):
        if s[j] in "aeiou":
            vowel_count += 1
    return vowel_count