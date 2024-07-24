import math

def sieve(n, isPrime):
    """Generate a list of primes up to the given limit using the Sieve of Eratosthenes."""
    isPrime[0] = isPrime[1] = False
    for i in range(2,n+1):
        isPrime[i]=True
    for p in range(2, int(math.sqrt(n)) + 1):
       if isPrime[p] == True:
         for i in range(p*p, n+1, p):
             isPrime[i]=False
 


def findPrimePair(n):
    flag=0
    isPrime=[False] * (n + 1)
    sieve(n, isPrime)

    for i in range(2,n):
        x = n // i
        if (isPrime[i] & isPrime[x] and x!=i and x*i==n):
            print(i, x)
            flag=1
            break
    if not flag:
        print("No such pair found")


def main():
    """Main function to read input, process cases, and print results."""
    import sys
    if len(sys.argv) != 2:
     print("Usage: python PrimeLogic.py <input_file>")
     return
    input_file = sys.argv[1]
    
    try:
        with open(input_file, 'r') as file:
            data = list(map(int, file.read().split()))
    except FileNotFoundError:
        print(f"File not found: {input_file}")
        return
    except ValueError:
        print("Error in file format. Ensure the file contains only integers.")
        return
    
    P = data[0]
    test_cases = data[1:P + 1]
    for n in test_cases:
     findPrimePair(n)
    

if __name__ == "__main__":
    main()
