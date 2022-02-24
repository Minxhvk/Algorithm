# group-anagrams

import collections


a = ["eat", "tea", "tan", "ate", "nat", "bat"]

anagrams = collections.defaultdict(list)

for word in a:
    anagrams[''.join(sorted(word))].append(word)
print(list(anagrams.values()))
