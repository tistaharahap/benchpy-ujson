import ujson
import time


some_obj = {
    'string': 'Tista',
    'int': 113,
    'float': 0.091248129
}

test_runs = 10000000

start_time = time.time()
for x in range(test_runs):
    ujson.dumps(some_obj)
end_time = time.time()

elapsed_time = end_time - start_time

print(f'Total Runs: {test_runs} times')
print(f'Execution time: {elapsed_time} second')
print('Each Run Time: %.10f second' % (elapsed_time / test_runs))
