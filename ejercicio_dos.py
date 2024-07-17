"""
crear una funcion que haciendo uso del metodo filter me filtre los numeros primos de una lista pasada por parametros
"""
def is_prime(n):
    if n <= 1:
        return False
    if n <= 3:
        return True
    if n % 2 == 0 or n % 3 == 0:
        return False
    i = 5
    while i * i <= n:
        if n % i == 0 or n % (i + 2) == 0:
            return False
        i += 6
    return True

def filter_prime_numbers(lst):
    return list(filter(is_prime, lst))

numbers1 = [52, 22, 58, 16, 10, 20, 60, 17, 12, 6]
prime_numbers1 = filter_prime_numbers(numbers1)
print(prime_numbers1)