import time


def time_it(foo):

    """
    Outputs time taken by a function to execute
    """

    def wrapper():
        t1 = time.time()
        foo()
        t2 = time.time()
        return "Time it took to run the function: " + str((t2 - t1)) + "\n"
    return wrapper


@time_it
def sum_nums():
    num_list = []
    for num in (range(0, 10000)):
        num_list.append(num)
    print("\nSum of all the numbers: " + str((sum(num_list))))


print(sum_nums())
