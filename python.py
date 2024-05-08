import psutil
from memory_profiler import memory_usage
import numpy as np 


def sum_list(lst):
    return np.sum(lst)  # Utilizzo di NumPy per un'operazione più veloce

def concatenate_strings(lst):
    return ''.join(lst)

def create_squares(n):
    return np.square(np.arange(n)).tolist()  # Utilizzo di NumPy

def find_max(lst):
    return np.max(lst)  # Utilizzo di NumPy

def filter_evens(lst):
    return [num for num in lst if num % 2 == 0]

def profile_function(func, *args):
    p = psutil.Process()
    p.cpu_percent(interval=None)      
    mem_usage = memory_usage((func, args), max_usage=True)
    result = func(*args)
    cpu_percent = p.cpu_percent(interval=None)
    
    print(f"Codice {func.__name__}:")
    print(f"Utilizzo percentuale della CPU: {cpu_percent}%")
    print(f"Uso massimo della memoria: {mem_usage:.2f} MiB\n")

def test_functions():
    lst = list(range(5000))
    str_lst = ["hello" for _ in range(5000)]

    profile_function(sum_list, lst)
    
    profile_function(concatenate_strings, str_lst)
    
    profile_function(create_squares, 5000)

    profile_function(find_max, lst)

    profile_function(filter_evens, lst)

if __name__ == "__main__":
    test_functions()
