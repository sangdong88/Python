class Fibonacci:
    def __init__(self, title="fibonacci"):
        # title이 따로 넘어오면 사용하고, 아니면 "fibonacci"를 기본 값으로 사용하겠다.
        self.title = title

    def fib(n):
        a, b = 0, 1
        while a < n:
            print(a, end=' ')
            a, b = b, a + b
        print()

    def fib2(n):
        result = []
        a, b = 0, 1
        while a < n:
            result.append(a)
            a, b = b, a + b
        return result
