import os


# 5-1 문제
def my_average(a, b):
    return (a + b) / 2


print(my_average(20, 5))


# 5-2 문제
def get_max_min(data_list):
    return max(data_list), min(data_list)


my2_list = [1, 2, 3, 4, 5, 6, 7, 8, 9]
print(get_max_min(my2_list))


# 5-3 문제
def get_txt_list(path):
    my3_list = []
    for x in os.listdir(path):
        if x.endswith('txt'):
            my3_list.append(x)
        else:
            pass
    return my3_list


print(get_txt_list("C:\\ProgramData\\Anaconda3\\Lib\\idlelib"))


#5-4 문제
def bmi_check(weight, length):
    bmi = weight / pow(length * 0.01, 2)
    print('bmi 지수:%d' % bmi)
    if bmi == 18.5:
        print("마른체형입니다.")
    elif 18.5 <= bmi < 25.0:
        print("표준입니다.")
    elif 25.0 <= bmi < 30.0:
        print("비만입니다.")
    elif bmi >= 30.0:
        print("고도비만입니다.")
    else:
        pass


print(bmi_check(75, 173))

# 5-5 문제
# while 1:
weight, length = map(int, input("몸무계와 키를 띄어쓰기 구분으로 입력해주세요:").split())

bmi = weight / pow(length * 0.01, 2)
print('bmi 지수:%d' % bmi)
if bmi == 18.5:
    print("마른체형입니다.")
elif 18.5 <= bmi < 25.0:
    print("표준입니다.")
elif 25.0 <= bmi < 30.0:
    print("비만입니다.")
elif bmi >= 30.0:
    print("고도비만입니다.")
else:
    pass


#5-6 문제
def get_triangle_are(width, height):
    area = width * height * 0.5
    return area


print(get_triangle_are(3, 5))


#5-7 문제
def add_start_to_end(start, end):
    for x in range(start, end+1):
        x += x
    return x


print(add_start_to_end(1, 10))


#5-8 문제
def str_list_modify(my8_list):
    for x in range(len(my8_list)):
        my8_list[x] = my8_list[x][0:3]
    return my8_list


my8_list = ['Seoul', 'Daegu', 'Kwangju', 'Jeju']
print(str_list_modify(my8_list))

