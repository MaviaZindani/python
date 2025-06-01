# Finding prime numbers

def is_prime_recursive(n, i=2):
    if n <= 1:
        return False
    if i * i > n:
        return True
    if n % i == 0:
        return False
    return is_prime_recursive(n, i + 1)

# Example
number = int(input('give a number: '))

isItPrimeNumber = is_prime_recursive(number)

if isItPrimeNumber:
    print('This Is A Prime Number')
else :
    print('This Is A Not Prime Number')
