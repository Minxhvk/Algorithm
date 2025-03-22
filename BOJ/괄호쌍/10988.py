import sys

def get():
  return sys.stdin.readline().rstrip()


str_input = get()
stack = []

str_len = len(str_input)
result = "1"
for left in range(str_len // 2):
  right = str_len - left - 1

  if str_input[left] != str_input[right]:
    result = "0"
    break 

print(result)