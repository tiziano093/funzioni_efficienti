import psutil
from memory_profiler import memory_usage
import numpy as np 

def sum_list(lst):
    # Calcola la somma degli elementi di una lista usando NumPy, che è più veloce per grandi quantità di dati.
    return np.sum(lst)

def concatenate_strings(lst):
    # Unisce una lista di stringhe in una singola stringa.
    return ''.join(lst)

def create_squares(n):
    # Crea una lista dei quadrati dei numeri da 0 a n-1 usando NumPy.
    return np.square(np.arange(n)).tolist()

def find_max(lst):
    # Trova il valore massimo in una lista usando NumPy.
    return np.max(lst)

def filter_evens(lst):
    # Restituisce una lista contenente solo i numeri pari dalla lista originale.
    return [num for num in lst if num % 2 == 0]

def sum_of_squares(lst):
    # Calcola la somma dei quadrati di ogni elemento in una lista.
    return sum(number * number for number in lst)

def generate_evens(n):
    # Genera una lista di numeri pari da 0 a n-1.
    return [i for i in range(0, n, 2)]

def duplicate_items(lst):
    # Duplica ogni elemento in una lista.
    return [item for item in lst for _ in range(2)]

def count_occurrences(lst, element):
    # Conta quante volte un elemento specifico appare in una lista.
    return lst.count(element)

def reverse_string(s):
    # Inverte l'ordine dei caratteri in una stringa.
    return s[::-1]

def find_minimum(lst):
    # Trova il valore minimo in una lista, restituisce None se la lista è vuota.
    return min(lst) if lst else None


def profile_function(func, *args):
    p = psutil.Process()
    p.cpu_percent(interval=None)      
    mem_usage = memory_usage((func, args), max_usage=True)
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
    profile_function(sum_of_squares, lst)
    profile_function(generate_evens, 5000)
    profile_function(duplicate_items, lst)
    profile_function(count_occurrences, lst, 2500)
    profile_function(reverse_string, concatenate_strings(str_lst))
    profile_function(find_minimum, lst)

if __name__ == "__main__":
    test_functions()
