import time


start_time = time.perf_counter()
l = [x**2 for x in range(10000000)]
end_time = time.perf_counter()
print(f'Time for List:\t\t{end_time-start_time}\n')


start_t = time.perf_counter()
g = (x**2 for x in range(10000000))
end_t = time.perf_counter()
print(f'Time for Generator:\t{end_t-start_t}')