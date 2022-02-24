
a = int(input())

word = []

for _ in range(a):
    word.append(input())

word = list(set(word)) # 중복 제거
word.sort(key=lambda x : (len(x), x))

print("\n".join(word))

