# Section08
# 파이썬 모듈과 패키지
# 왜 패키지 모듈형태로 배포를 해야하는지 이해하기

# .py 파일 하나 하나 가 모듈이 될 수 있고,
# 파일들이 모여잇는 directory, ALL 이 패키지가 된다.

# 패키지 예제1
# 상대 경로
# ..:부모 디렉토리
# . : 현재 디렉터리


# 사용1(클래스)
import builtins
import Ch1.pkg.prints as p
from Ch1.pkg.calculations import div as d
import Ch1.pkg.calculations as c  # 클래스가 아닌 함수 단위이기 때문에 from 사용 하지 않는다.
from Ch1.pkg.fibonacci import Fibonacci as fb  # 앨리아스, 약어
from Ch1.pkg.fibonacci import *  # 모든 클래스, 메서드를 import 하겠다. 권장하지 않음. 불필요한 리소스낭비 문제
from Ch1.pkg.fibonacci import Fibonacci
# pkg 폴더 안에 fibonacci.py 파일 안에 있는 Fibonacci class를 import 하는 것이다.
# pkg라는 디렉터리가 실제로 있어야 된다. sys.path 경로안에..
# pkg 디렉터리 안에 fibonacci.py에서
# Fibonacci 클래스를 import 했다.
Fibonacci.fib(100)  # self 가 없으니 클래스 메서드로 바로 사용 가능
a = Fibonacci()

print("ex1 : ", Fibonacci.fib2(200))
print("ex1 : ", Fibonacci().title)
print(Fibonacci().__dict__)  # {'title': 'fibonacci'}
# 이렇게 되면 Fibonacci() 클래스의 self는 자기 자신이 된다.

# Fibonacci()클래스를 생성해서 title로 접근해야 되고
# 인스턴스화 시켜 줘야 __init__ 메서드가 호출된다.
# Fibonacci() 인스턴스 초기화
print("*"*20)
# ex1 :  fibonacci 이렇게 사용하면 클래스 변수 인가 ?
print("ex1 : ", a.title)  # fibonacci 인스턴스 변수를 self.title 출력 가능
# self 가 있으니 인스턴스 변수 같은데, title='fibonacci'로 고정이니
# 클래스변수로도 호출이 되는 것 같다.
# <pkg.fibonacci.Fibonacci object at 0x000001A8CB650FD0>
print("ex2 : ", Fibonacci(a).title)
print("ex3 : ", a.title)
print("ex3-1 : ", Fibonacci().title)
print()

# 사용2(클래스) # 메모리 많이 잡아먹음 권장하지 않음
Fibonacci.fib(150)  # 0 1 1 2 3 5 8 13 21 34 55 89 144


# 사용3(클래스)

fb.fib(300)  # 0 1 1 2 3 5 8 13 21 34 55 89 144 233

# 사용4(함수)

print("ex4 : ", c.add(10, 100))  # ex4 :  110
print("ex4 : ", c.mul(10, 100))  # ex4 :  1000
print("ex4 : ", c.div(10, 100))  # ex4 :  0.1

# 사용5(함수)
# from 절을 사용하여 원하는 함수만 불러와서 사용 할 수 있다.
# 필요한 것만 리소스에 올려서 사용하는것이 코드상의 효율성이 좋다.
print("ex5 : ", d(100, 10), type(d(100, 10)))
print("ex5-1 : ", int(d(100, 10)), type(int(d(100, 10))))

# 사용6

p.prt1()  # I'm NiceBoy!
p.prt2()  # I'm Goodboy!
print(p.__name__)  # pkg.prints 본인의 위치가 아닌 pkg.prints가 import 되어 실행 되고 있기 때문에
# __name__에는 pkg.prints가 들어가게 되고
# if __name__ == "__main__": 문은 실행 되지 않는다.
# 독립적으로 모듈안에 함수나 클래스가 작동하는지 확인 할 때 사용.

# print(dir(builtins))
# ['ArithmeticError', 'AssertionError', 'AttributeError', 'BaseException', 'BlockingIOError',
# 'BrokenPipeError', 'BufferError', 'BytesWarning', 'ChildProcessError',
# 'ConnectionAbortedError', 'ConnectionError', 'ConnectionRefusedError',
# 'ConnectionResetError', 'DeprecationWarning', 'EOFError', 'Ellipsis',
# 'EnvironmentError', 'Exception', 'False', 'FileExistsError', 'FileNotFoundError',
# 'FloatingPointError', 'FutureWarning', 'GeneratorExit', 'IOError', 'ImportError',
# 'ImportWarning', 'IndentationError', 'IndexError', 'InterruptedError', 'IsADirectoryError',
# 'KeyError', 'KeyboardInterrupt', 'LookupError', 'MemoryError', 'ModuleNotFoundError',
# 'NameError', 'None', 'NotADirectoryError', 'NotImplemented', 'NotImplementedError',
# 'OSError', 'OverflowError', 'PendingDeprecationWarning', 'PermissionError',
# 'ProcessLookupError', 'RecursionError', 'ReferenceError', 'ResourceWarning',
# 'RuntimeError', 'RuntimeWarning', 'StopAsyncIteration', 'StopIteration', 'SyntaxError',
# 'SyntaxWarning', 'SystemError', 'SystemExit', 'TabError', 'TimeoutError', 'True',
# 'TypeError', 'UnboundLocalError', 'UnicodeDecodeError', 'UnicodeEncodeError', 'UnicodeError'
# icodeTranslateError', 'UnicodeWarning', 'UserWarning', 'ValueError', 'Warning',
# 'WindowsError', 'ZeroDivisionError', '__build_class__', '__debug__', '__doc__',
# '__import__', '__loader__', '__name__', '__package__', '__spec__', 'abs', 'all',
# 'any', 'ascii', 'bin', 'bool', 'breakpoint', 'bytearray', 'bytes', 'callable',
# 'chr', 'classmethod', 'compile', 'complex', 'copyright', 'credits', 'delattr',
# 'dict', 'dir', 'divmod', 'enumerate', 'eval', 'exec', 'exit', 'filter', 'float',
# 'format', 'frozenset', 'getattr', 'globals', 'hasattr', 'hash', 'help', 'hex', 'id',
# 'input', 'int', 'isinstance', 'issubclass', 'iter', 'len', 'license', 'list', 'locals',
# 'map', 'max', 'memoryview', 'min', 'next', 'object', 'oct', 'open', 'ord', 'pow', 'print',
# 'property', 'quit', 'range', 'repr', 'reversed', 'round', 'set', 'setattr', 'slice',
# 'sorted', 'staticmethod', 'str', 'sum', 'super', 'tuple', 'type', 'vars', 'zip']
