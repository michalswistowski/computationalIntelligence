# a
def prime(n):
    for i in range(2, n):
        if n % i == 0:
            return False
    return True

print(prime(9))
print(prime(11))
print(prime(8))
print(prime(2))

# b

def select_primes(x):
    primes_list = []
    for i in x:
        if prime(i):
            primes_list.append(i)
    print(primes_list)

select_primes([2,3,4,5,6,7,8,9,10,11])