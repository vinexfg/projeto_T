import time

def increment(x):
    return x + 1

# Medir o tempo de execução com chamadas de função
start_time = time.time()
result = 0
for i in range(1000000):
    result = increment(result)
end_time = time.time()
print(f"Tempo com chamadas de função: {end_time - start_time:.6f} segundos")

# Medir o tempo de execução sem chamadas de função
start_time = time.time()
result = 0
for i in range(1000000):
    result += 1
end_time = time.time()
print(f"Tempo sem chamadas de função: {end_time - start_time:.6f} segundos")
