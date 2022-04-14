"""s, a, b = (input() for _ in range(3))


def change_str(s, a, b, count=0):
    if s == s.replace(a, b):
        print(count)
    else:
        count += 1
        s = s.replace(a, b)
        return change_str(s, a, b, count)
    if count > 1000 or a in b and a in s:
        print('Impossible')



change_str(s, a, b)
"""


s, t = ('cvcabacvcaba', 'aba')


def find_result(s, t):
    result = len([i for i in range(len(s)) if s.startswith(t, i)])
    return result


print(find_result(s, t))
