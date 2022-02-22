### super () ###
# 자식 클래스에서 부모클래스의 내용을 사용하고 싶은 경우
# super().부모 클래스의 내용

class Father():
    def __init__(self, name):
        self.name = name


class Son(Father):
    pass


a = Son('james')
print(a.name)


class Daughter(Father):
    def __init__(self, name, age):
        super().__init__(name)
        self.age = age


b = Daughter('kathy', 19)
print(b.name, b.age)


class Daughter1(Father):
    pass


c = Daughter1('Dorothy')
print(c.name)
