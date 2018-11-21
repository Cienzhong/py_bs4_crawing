'''
#这是一个python的类
'''
class Idog:
    '创建Idog类，她具备一些属性、函数'

    # 这是一个类变量，它的值将在这个类的所有实例之间共享，你可以在内部类或外部类使用 Idog.passStatus 访问
    passStatus = True

    # __init__()方法是一种特殊的方法，被称为类的构造函数或初始化方法，当创建了这个类的实例时就会调用该方法
    def __init__(self):
        self.key = "dog"
        self.path = "/src/py/"
        Idog.passStatus = False

    def subkey(self):
        return self.key + ":" + self.path

    def subNum(self, x, y):
        self.__primed()
        return x * y

    def __primed(self):
        print("这是一个私有方法，不能在类外部调用，类内部调用方式：self.__primed()")

t = Idog()
text = t.subkey()
print(text)
s = t.subNum(88, 23)
print(str(s))