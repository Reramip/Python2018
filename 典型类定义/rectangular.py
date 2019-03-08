###典型类定义：一个长方形
class Rectangle:
    def __init__(self, width=1, height=1):#构造方法
        self._width=width##实例变量
        self._height=height##实例变量

    def setWidth(self, width):#赋值方法
        self._width=width

    def segHeight(self, height):#赋值方法
        self._height=height

    def getWidth(self):#取值方法
        return self._width

    def getHeight(self):#取值方法
        return self._height

    def area(self):#其他方法
        return self._width*self._height

    def perimeter(self):#其他方法
        return 2*(self._width+self._height)

    def __str__(self):#状态表示方法
        return ("Width: "+str(self._width)+"\nHeight: "+str(self._height))