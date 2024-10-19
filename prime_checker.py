# prime_checker.py
def is_prime(n):
    if n <= 1:
        return False
    for i in range(2, int(n ** 0.5) + 1):
        if n % i == 0:
            return False
    return True

def generate_primes(limit):
    primes = []
    for num in range(2, limit + 1):
        if is_prime(num):
            primes.append(num)
    return primes

def count_primes_in_range(start, end):
    count = 0
    for num in range(start, end + 1):
        if is_prime(num):
            count += 1
    return count

if __name__ == "__main__":
    num = int(input("Enter a number to check if it's prime: "))
    print(f"{num} is a prime number: {is_prime(num)}")
    
    limit = int(input("Enter a limit to generate prime numbers: "))
    primes_list = generate_primes(limit)
    print(f"Prime numbers up to {limit}: {primes_list}")
    
    start = int(input("Enter the start of the range: "))
    end = int(input("Enter the end of the range: "))
    prime_count = count_primes_in_range(start, end)
    print(f"Number of prime numbers between {start} and {end}: {prime_count}")
