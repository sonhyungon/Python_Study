# 10미만의 자연수에서 3과 5의 배수를 구하면 3,5,6,9이다. 이들의 총합은 23이다.
# 1000미만의 자연수에서 3,5의 배수의 총합을 구하라.

def multiple2(x):
    Increase = 1
    result = 0
    while 1:
        Mul = x * Increase

        if Mul < 1000:
            result += Mul
            Increase += 1
        else:
            break

    return result


print(multiple2(3) + multiple2(5))
