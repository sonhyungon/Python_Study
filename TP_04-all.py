Python 3.7.4 (tags/v3.7.4:e09359112e, Jul  8 2019, 19:29:22) [MSC v.1916 32 bit (Intel)] on win32
Type "help", "copyright", "credits" or "license()" for more information.
>>> for i in range(0,5):
	print('*', end = '')

	
*****
>>> for i in range(0,4):
	for j in range(0,5):
		print('*', end = '')
	print('\n')

	
*****

*****

*****

*****

>>> for i in range(1,6):
	print('*' * i)

	
*
**
***
****
*****
>>> for i in range(5,0,-1):
	print('*' * i)

	
*****
****
***
**
*
>>> list(range(1,6))
[1, 2, 3, 4, 5]
>>> for i in range(1,6):
	for j in range(4,0,-1):
	    print(' ' * j, end = '')
	    print('*' * (i*2-1), end = '')
	    print(' ' * j, end = '')
	    print('\n')
	    i += 1
	break

    *    

   ***   

  *****  

 ******* 

>>> for i in range(1,6):
	for j in range(5,0,-1):
	    print(' ' * (j-1), end = '')
	    print('*' * (i*2-1), end = '')
	    print(' ' * (j-1), end = '')
	    print('\n')
	    i += 1
	break

    *    

   ***   

  *****  

 ******* 

*********

>>> for j in range(5,0,-1):
	for i in range(1,6):
	    print(' ' * (i-1), end = '')
	    print('*' * (j*2-1), end = '')
	    print(' ' * (i-1), end = '')
	    print('\n')
	    j -= 1
	break

*********

 ******* 

  *****  

   ***   

    *    

>>> for floor in apart:
	for room in floor:
		if room == 101 or room == 203 or room == 301 or room == 404:
                        print("배달구독료 미납부 세대 배달 불가: %s" % room)
		else:
			print("배달 가능 세대: %s" % room)

			
Traceback (most recent call last):
  File "<pyshell#16>", line 1, in <module>
    for floor in apart:
NameError: name 'apart' is not defined
>>> apart = [[101, 102, 103, 104],[201, 202, 203, 204],[301, 302, 303, 304], [401, 402, 403, 404]]
>>> arrears = [101, 203, 301, 404]
>>> for floor in apart:
	for room in floor:
		if room == 101 or room == 203 or room == 301 or room == 404:
                        print("배달구독료 미납부 세대 배달 불가: %s" % room)
		else:
			print("배달 가능 세대: %s" % room)

			
배달구독료 미납부 세대 배달 불가: 101
배달 가능 세대: 102
배달 가능 세대: 103
배달 가능 세대: 104
배달 가능 세대: 201
배달 가능 세대: 202
배달구독료 미납부 세대 배달 불가: 203
배달 가능 세대: 204
배달구독료 미납부 세대 배달 불가: 301
배달 가능 세대: 302
배달 가능 세대: 303
배달 가능 세대: 304
배달 가능 세대: 401
배달 가능 세대: 402
배달 가능 세대: 403
배달구독료 미납부 세대 배달 불가: 404
>>> 
