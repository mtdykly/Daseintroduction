import matplotlib.pyplot as plt
print(2**10)
print(2**20)
print(2**30)
print(2**40)
print(2**50)

exponents = [10, 20, 30, 40, 50]
results = [2 ** exp for exp in exponents]

plt.plot(exponents, results, marker='o', linestyle='-')
plt.title('2^x for Different Exponents')
plt.xlabel('Exponent (x)')
plt.ylabel('2^x')
plt.grid(True)
plt.show()