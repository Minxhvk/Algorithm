def solution(s):
    answer = 0
    num_str = []
    res = []
    table = {
        'zero': '0',
        'one': '1',
        'two': '2',
        'three': '3',
        'four': '4',
        'five': '5',
        'six': '6',
        'seven': '7',
        'eight': '8',
        'nine': '9'
    }

    for i in s:
        try:
            int(i)
            res.append(i)
        except:
            num_str.append(i)
            if ''.join(num_str) in table:
                res.append(table["".join(num_str)])
                num_str.clear()
    answer = ''.join(res)
    return int(answer)
