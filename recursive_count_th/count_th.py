'''
Your function should take in a single parameter (a string `word`)
Your function should return a count of how many occurences of ***"th"*** occur within `word`. Case matters.
Your function must utilize recursion. It cannot contain any loops.
'''
def count_th(word):
    
    # Base (if the word is too short)
    if len(word) <= 1:
        return 0
    # When found one, count and recurse
    if word[:2] == 'th':
        return 1 + count_th(word[2:])
    
    # Move right
    return count_th(word[1:])
