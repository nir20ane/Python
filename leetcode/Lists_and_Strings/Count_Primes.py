"""Count the number of prime numbers less than a non-negative number, n.
Example:
Input: 10
Output: 4
Explanation: There are 4 prime numbers less than 10, they are 2, 3, 5, 7.
"""
#Method: count primes - Sieve of Eratosthenes
class Count_Primes(object):
    primes = []
    def count_prime(self,n):
        primes = [0,0]+[1]*(n-2)
        for i in range(2,int(n**0.5)+1):
            if primes[i] == 1:
                for j in range(i**2,n,i):
                   primes[j] = 0
        return sum(primes)
c=Count_Primes()
print(c.count_prime(10))