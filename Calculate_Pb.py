from func import func
import sys
import math
sys.setrecursionlimit(100000)
def calculate_Pb(a, s):
    temp_1 = a**s
    temp_2 = func(s)
    temp_3 = 0
    for k in range(s+1):
        temp_3 = temp_3 + (math.pow(a, k))/func(k)
    Pb = (temp_1/temp_2)/temp_3
    return Pb

if __name__ == '__main__':
    Pb = calculate_Pb(2, 2)
    print(Pb)