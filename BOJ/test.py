
spam = [["2021/07/01", "spam1"],
["2021/07/02", "spam2"],
["2021/06/29", "spam3"],
["2021/07/03", "spam4"]]

for data in sorted(spam, reverse=True): print(data[1])