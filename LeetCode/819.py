import collections
import re

para = "Bob. hIt, ball"
ban = ["bob", "hit"]

words = [word for word in re.sub(
    r'[^\w]', " ", para).lower().split() if word not in ban]

counts = collections.Counter(words)

print(counts.most_common(1)[0][0])
