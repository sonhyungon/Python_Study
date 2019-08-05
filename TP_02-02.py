Python 3.7.4 (tags/v3.7.4:e09359112e, Jul  8 2019, 19:29:22) [MSC v.1916 32 bit (Intel)] on win32
Type "help", "copyright", "credits" or "license()" for more information.
>>> daum_stock = 89000
>>> naver_stock = 751000
>>> man_stock = (daum_stock * 100) + (naver_stock * 20)
>>> man_stock
23920000
>>> daum_stock_lower = 89000 * 0.7
>>> naver_stock_lower = 751000 * 0.7
>>> man_stock_lower = (daum_stock_lower * 100) + (naver_stock_lower * 20)
>>> man_stock_lower
16744000.0
>>> int(man_stock_lower)
16744000
>>> man_loss = man_stock - man_stock_lower
>>> man_loss
7176000.0
>>> 
