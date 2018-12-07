import time
def con(name):
    print("%s 准备吃包子啦！"%name)
    while True:
        baozi = yield

        print("包子[%s]来了，被[%s]吃了！"%(baozi,name))


c = con("asd")
c.__next__()

def pro(name):
    c = con("A")
    c2 = con("B")
    c.__next__()
    c2.__next__()
    print("老子开始做包子了")
    for i in range(10):
        time.sleep(1)
        print("做了2个包子")
        c.send(i)
        c2.send(i)


pro('alex')