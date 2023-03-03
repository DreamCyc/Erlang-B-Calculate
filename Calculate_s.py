from func import func
import math
def calculate_s(a, Pb):
    temp_1 = [0]
    temp_2 = [0]
    temp_3 = [0]
    data = [100000]
    for m in range(1, 101):
        temp_1.append(a**m)
        temp_2.append(func(m))
        temp_3.append(temp_1[m]/temp_2[m])
        temp_4 = 0
        for k in range(m+1):
            temp_4 = temp_4 + (a**k)/func(k)
        data.append(abs(Pb-(temp_3[m]/temp_4)))
    m = data.index(min(data))
    return m

if __name__ == '__main__':
    s = calculate_s(8, 0.5)
    print(s)