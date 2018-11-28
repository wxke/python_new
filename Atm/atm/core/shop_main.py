#!/usr/bin/env python

shop_product = {
    'python':500,
    'mac':400,
    'iphone':300
}
shop_car={}
def shopping(func):
    def wap(*args):
        print("q退出 or 继续")
        for i in range(1000):
            a =input()
            if a is not 'q':
                func(a)
            else:
                print("qqqqqq")
                break
    return wap


def print_shop():
    print("welcome shopping!")
    print("select product!")
    for key,value in shop_product.items():
        print(key,value)
@shopping
def shop_car_1(name):
    shop_car[name] = shop_product[name]
    print("%s 加入购物车" %name)


def print_shop_cat():
    for key,value in shop_car.items():
        print(key,value)

print_shop()
shop_car_1()
print_shop_cat()
