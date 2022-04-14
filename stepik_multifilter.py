"""class multifilter:
    def judge_half(pos, neg):  # допускает элемент, если его допускает хотя бы половина фукнций (pos >= neg)
        return pos >= neg

    def judge_any(pos, neg):  # допускает элемент, если его допускает хотя бы одна функция (pos >= 1)
        return pos >= 1

    def judge_all(pos, neg):  # допускает элемент, если его допускают все функции (neg == 0)
        return neg == 0

    def __init__(self, iterable, *funcs, judge=judge_any):
        self.iterable = iterable                            # iterable - исходная последовательность,\
        self.funcs = funcs                                  # funcs - допускающие функции
        self.judge = judge                                  # judge - решающая функция

    def __iter__(self):  # возвращает итератор по результирующей последовательности
        for i in self.iterable:
            pos = 0
            neg = 0
            for func in self.funcs:
                if func(i):
                    pos += 1
                else:
                    neg += 1
            if self.judge(pos, neg):
                yield i

def mul2(x):
    return x % 2 == 0


def mul3(x):
    return x % 3 == 0


def mul5(x):
    return x % 5 == 0


a = [i for i in range(31)]  # [0, 1, 2, ... , 30]

multifilter1 = multifilter(a, mul2, mul3, mul5)
# Здесь и дальше создаем разные экземпляры класса. iterable=a, *funcs=[mul2,mul3,mul4]
multifilter2 = multifilter(a, mul2, mul3, mul5, judge=multifilter.judge_half)
multifilter3 = multifilter(a, mul2, mul3, mul5, judge=multifilter.judge_all)

print(list(multifilter1))
# [0, 2, 3, 4, 5, 6, 8, 9, 10, 12, 14, 15, 16, 18, 20, 21, 22, 24, 25, 26, 27, 28, 30]

print(list(multifilter2))
# [0, 6, 10, 12, 15, 18, 20, 24, 30]

print(list(multifilter3))
# [0, 30]"""


"""def is_prime(a):
    if a == 2:
        return True
    if a % 2 == 0:
        return False
    for _ in range(3, a//2, 2):
        if a % _ == 0:
            return False
    return True


def primes():
    a = 2
    while True:
        if is_prime(a):
            yield a
        a += 1"""

with open('dataset_24465_4.txt') as r, open('output.txt', 'w') as w:
    lines = r.read().splitlines()
    for line in lines[::-1]:
        w.write('%s\n' % line)
