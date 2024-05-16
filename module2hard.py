# n число от 3 до 20
# нужно подобрать пароль используя числа от 1 до 20

# как реализовать условие, что если n делится на сумму какойто пары из набора чисел, как создать и реализовать подбор
# этих пар из данного набора? чтобы не прописывать ответы вручную, чтобы алгоритм сам их просчитывал и выдавал.

import random
def code():
    code = range(1, 21)
    n = random.choice(code)
    return n
n = code()

string_ = ''

for i in range(1, n + 1):
    for j in range(1, n + 1):
        if n % (i + j) == 0 and i != j and i < j:
            string_ += str(i) + str(j)



print(n)
print(string_)