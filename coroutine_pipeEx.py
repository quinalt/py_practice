# Coroutine Pipeline Example... producer, intermediate , sink 

# producer, intermdiate coroutine, sink 

def producer(nums, next_co):
    nums_transformed = []
    for i in nums:
        nums_transformed.append(i * 5)
    for num in nums_transformed:
        next_co.send(num)
    next_co.close()

# modulo finder 
def mod_finder(next_co=None):
    print('searching for numbers divisible by 4')

    try:
        while True:
            num = (yield)
            if num % 4 == 0:
                next_co.send(num)
    except GeneratorExit:
        print('no more numbers to look at, exiting')

# the sink printer 

def print_final_nums():
    print('My name is Sink, I will print for you')

    try:
        while True:
            num = (yield)
            print(num)
    except GeneratorExit:
        print('goodbye, Sink\'s job is done')

pt = print_final_nums()
pt.__next__()
mf = mod_finder(next_co= pt)
mf.__next__()

nums = [i for i in range(1, 100)]
producer(nums, mf)

  
