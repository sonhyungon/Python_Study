#5-1 문제
def myaverage(a, b):
	return (a+b)/2

myaverage(5,5)


#5-2 문제
def get_max_min(data_list):
	return max(data_list), min(data_list)

mylist = [1,2,3,4,5,6,7,8,9]
get_max_min(mylist)

#5-3 문제
import os
def get_txt_list(path):
	mylist = []
	for x in os.listdir(path):
		if x.endswith('txt'):
			mylist.append(x)
		else:
			pass
	return mylist

get_txt_list('C:\ProgramData\Anaconda3\Lib\idlelib')

#5-4 문제
def bmi_check(weith, lenth):
	bmi = weith/pow(lenth*0.01,2)
	print('bmi 지수:%d' %bmi)
	if bmi == 18.5:
		print("마른체형입니다.")
	elif 18.5 <= bmi and bmi < 25.0 :
		print("표준입니다.")
	elif 25.0 <= bmi and bmi < 30.0:
		print("비만입니다.")
	elif bmi >= 30.0:
		print("고도비만입니다.")
	else:
		pass

bmi_check(75, 173)

#5-5 문제 
#while 1:
    weith, lenth = map(int,input("몸무계와 키를 띄어쓰기 구분으로 입력해주세요:").split())
    
    bmi = weith/pow(lenth*0.01,2)
    print('bmi 지수:%d' %bmi)
    if bmi == 18.5:
        print("마른체형입니다.")
    elif 18.5 <= bmi and bmi < 25.0 :
        print("표준입니다.")
    elif 25.0 <= bmi and bmi < 30.0:
        print("비만입니다.")
    elif bmi >= 30.0:
        print("고도비만입니다.")
    else:
        pass

#5-6 문제
def get_triangle_are(width, height):
	area= width * height * 0.5
	return area

get_triangle_are(3, 5)

#5-7 문제
def add_start_to_end(start, end):
	for x in range(start, end+1):
		x += x
	return x

add_start_to_end(1, 10)

#5-8 문제
def str_list_modify(mylist):
	for x in range(len(mylist)):
		mylist[x] = mylist[x][0:3]
	return mylist

mylist = ['Seoul', 'Daegu', 'Kwangju', 'Jeju']
str_list_modify(mylist)