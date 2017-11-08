# encoding: utf-8

# coding=utf-8
import time

'''
函数嵌套
装饰器参数 相关，如果函数有不确定参数 需要在装饰函数中添加 *args  **kwargs

装饰器带有 参数的情况。
'''

def  timer(func):
    def wrapper(*args,**kwargs):
        start=time.time()
        func(*args,**kwargs)
        end=time.time()
        print("the %s run time is %s" %(func.__name__,end-start))
    return wrapper





if __name__ == '__main__':
    pass