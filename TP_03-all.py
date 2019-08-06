Python 3.7.4 (tags/v3.7.4:e09359112e, Jul  8 2019, 19:29:22) [MSC v.1916 32 bit (Intel)] on win32
Type "help", "copyright", "credits" or "license()" for more information.
>>> naver_closing_price = [474500, 461500, 501000, 500500, 488500]
>>> type(naver_closing_price)
<class 'list'>
>>> print(max(naver_closing_price))
501000
>>> print(min(naver_closing_price))
461500
>>> print(max(naver_closing_price) - min(naver_closing_price))
39500
>>> print(naver_closing_price[2])
501000
>>> naver_closing_price2 = {'09/07': 474500, '09/08' : 461500, '09/09' : 501000, '09/10' : 500500, '09/11' : 488500}
>>> type(naver_closing_price2)
<class 'dict'>
>>> naver_closing_price2
{'09/07': 474500, '09/08': 461500, '09/09': 501000, '09/10': 500500, '09/11': 488500}
>>> naver_closing_price2['09/09']
501000
>>> 
