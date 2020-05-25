#difflib is used to match closest character

from difflib import get_close_matches
a = get_close_matches("abc",["abcd","aacd","abcdd"])
print(a)   # ['abcd', 'abcdd']

a = get_close_matches("abc",["abcd","abc","ade"],cutoff=0.5)
print(a) # ['abc', 'abcd']