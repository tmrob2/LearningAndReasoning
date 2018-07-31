import time

def time_it(f):
    def inner(*args, **kwargs):
        start = time.time()
        result = f(*args, **kwargs)
        end = time.time()
        print(f.__name__+' took: '+str((end-start)*1000)+' ms')
    return inner

@time_it
def calc_square(numbers):
    result = []
    for number in numbers:
        result.append(number**2)
    return result

@time_it
def calc_cube(numbers):
    result = []
    for number in numbers:
        result.append(number**3)
    return result

array = range(1, 100000)
out_sq = calc_square(array)

out_cu = calc_cube(array)