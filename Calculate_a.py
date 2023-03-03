from func import func
import sys
import math
sys.setrecursionlimit(100000)
def calculate_a(s, Pb):
    temp_1 = [0]
    temp_2 = [0]
    temp_3 = [0]
    data = [100000]
    for a in range(1, 101):
        temp_1.append(a**s)
        temp_2.append(func(s))
        temp_3.append(temp_1[a]/temp_2[a])
        temp_4 = 0
        for k in range(s+1):
            temp_4 = temp_4 + (a**k)/func(k)
        data.append(abs(Pb-temp_3[a]/temp_4))
    a = data.index(min(data))
    return a

if __name__ == '__main__':
    aa = calculate_a(100, 0.2)
    print(aa)
