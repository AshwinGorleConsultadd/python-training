

# Prime numbers upto 50 using generator
def prime_generator():
    for num in range(2, 51):
        for i in range(2, num):
            if num % i == 0:
                break
        else:
            yield num

for prime in prime_generator():
    print("Prime:", prime)







# infinite generator
def even_numbers():
    n = 2
    while True:
        yield n
        n += 2

gen = even_numbers()
for _ in range(5):
    print("Even:", next(gen))


# class based iterator
class Fibonacci:
    def __init__(self, n):
        self.n = n
        self.a = 0
        self.b = 1
        self.count = 0

    def __iter__(self):
        return self

    def __next__(self):
        if self.count >= self.n:
            raise StopIteration
        self.count += 1
        result = self.a
        self.a, self.b = self.b, self.a + self.b
        return result

fib = Fibonacci(10)
for num in fib:
    print("Fibonacci:", num)
