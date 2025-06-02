maximum = lambda a, b, c: max(a, b, c)
print("Maximum number:", maximum(12, 25, 17))


celsius = [0, 10, 20, 30, 40]
fahrenheit = list(map(lambda c: (c * 9/5) + 32, celsius))
print("Fahrenheit:", fahrenheit)
