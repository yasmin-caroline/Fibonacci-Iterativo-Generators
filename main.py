import time 
def fibonacci(n):
    a, b, counter = 0, 1, 0
    while True:
        if (counter > n): return
        yield a
        a, b = b, a + b
        counter += 1
        
f = fibonacci(1000)

for i in range(30):
  ini = time.time()
  for x in f:
    """print(x)"""
  fim = time.time()
  print (fim-ini)

print("\n Fim do algoritmo iterativo/generators com 1000 elementos. \n")

f = fibonacci(5000)

for i in range(30):
  ini = time.time()
  for x in f:
    """print(x)"""
  fim = time.time()
  print (fim-ini)

print("\n Fim do algoritmo iterativo/generators com 5000 elementos. \n")

f = fibonacci(10000)

for i in range(30):
  ini = time.time()
  for x in f:
    """print(x)"""
  fim = time.time()
  print (fim-ini)

print("\n Fim do algoritmo iterativo/generators com 10000 elementos. \n")