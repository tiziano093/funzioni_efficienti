import psutil
from memory_profiler import memory_usage
import numpy as np 

# Ottimizzazione con NumPy: Invece di utilizzare un loop per sommare gli elementi della lista, utilizziamo np.sum(lst). NumPy è una libreria ottimizzata per operazioni numeriche che utilizza implementazioni C sottostanti, risultando in esecuzioni molto più rapide per operazioni su array rispetto ai loop Python puri.
# Green Coding: Riducendo il numero di operazioni esplicite e sfruttando librerie ottimizzate, riduciamo il consumo energetico necessario per eseguire la funzione.
# concatenate_strings(lst)
def sum_list(lst):
    # Calcola la somma degli elementi di una lista usando NumPy, che è più veloce per grandi quantità di dati.
    return np.sum(lst)

# Efficienza delle Stringhe: L'operazione di concatenazione in un loop crea molte stringhe intermedie, consumando memoria e tempo di calcolo. Il metodo join esegue la concatenazione in un unico passaggio, riducendo l'overhead.
# Green Coding: Utilizzando una singola operazione per concatenare le stringhe, riduciamo il consumo di risorse computazionali e memoria.
# create_squares(n)
def concatenate_strings(lst):
    # Unisce una lista di stringhe in una singola stringa.
    return ''.join(lst)

# Utilizzo di NumPy: Generiamo una sequenza di numeri con np.arange(n) e calcoliamo i loro quadrati con np.square. NumPy esegue queste operazioni in modo vettoriale, risultando molto più veloce.
# Green Coding: Le operazioni vettoriali di NumPy riducono il numero di iterazioni e operazioni, risparmiando energia.
# find_max(lst)
def create_squares(n):
    # Crea una lista dei quadrati dei numeri da 0 a n-1 usando NumPy.
    return np.square(np.arange(n)).tolist()

#Ottimizzazione con NumPy: np.max(lst) utilizza algoritmi ottimizzati per trovare il valore massimo, risultando più efficiente del loop manuale.
# Green Coding: Riduciamo il numero di confronti e iterazioni, migliorando l'efficienza energetica.
# filter_evens(lst)
def find_max(lst):
    # Trova il valore massimo in una lista usando NumPy.
    return np.max(lst)

# List Comprehension: La list comprehension è una sintassi più concisa e spesso più veloce per creare nuove liste basate su condizioni.
# Green Coding: Utilizzando una sintassi più efficiente, riduciamo il consumo di risorse computazionali.
# sum_of_squares(lst)
def filter_evens(lst):
    # Restituisce una lista contenente solo i numeri pari dalla lista originale.
    return [num for num in lst if num % 2 == 0]

# Generator Expression: Utilizziamo una generator expression all'interno della funzione sum, che è più efficiente in termini di memoria poiché evita di creare una lista intermedia.
# Green Coding: Riduciamo l'uso della memoria, migliorando l'efficienza energetica.
# generate_evens(n)
def sum_of_squares(lst):
    # Calcola la somma dei quadrati di ogni elemento in una lista.
    return sum(number * number for number in lst)

# List Comprehension con Passo: Utilizziamo una list comprehension con un passo di 2 nel range, creando direttamente i numeri pari senza bisogno di condizioni aggiuntive.
# Green Coding: Evitiamo il controllo condizionale per ogni elemento, risparmiando risorse computazionali.
# duplicate_items(lst)
def generate_evens(n):
    # Genera una lista di numeri pari da 0 a n-1.
    return [i for i in range(0, n, 2)]

# Nested List Comprehension: Utilizziamo una nested list comprehension per duplicare ogni elemento in un'unica operazione, rendendo il codice più conciso e potenzialmente più veloce.
# Green Coding: Riduciamo il numero di chiamate alla funzione append, risparmiando risorse.
# count_occurrences(lst, element)
def duplicate_items(lst):
    # Duplica ogni elemento in una lista.
    return [item for item in lst for _ in range(2)]

# Metodo Integrato: Utilizziamo il metodo count delle liste, che è ottimizzato per contare le occorrenze di un elemento.
# Green Coding: Utilizziamo una funzione nativa ottimizzata, riducendo il numero di operazioni manuali.
# reverse_string(s)
def count_occurrences(lst, element):
    # Conta quante volte un elemento specifico appare in una lista.
    return lst.count(element)

# Slicing delle Stringhe: Utilizziamo il slicing [::-1] per invertire la stringa in un'unica operazione, che è molto più efficiente rispetto alla concatenazione in un loop.
# Green Coding: Riduciamo il numero di operazioni di concatenazione, risparmiando tempo e risorse.
# find_minimum(lst)
def reverse_string(s):
    # Inverte l'ordine dei caratteri in una stringa.
    return s[::-1]

#Funzione Integrata: Utilizziamo la funzione min, che è ottimizzata per trovare il valore minimo in una lista.
# Green Coding: Riduciamo il numero di confronti manuali, migliorando l'efficienza.
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
