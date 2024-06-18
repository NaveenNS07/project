def count_beautiful_partitions(s, k, minLength):
    MOD = 10**9 + 7
    primes = {'2', '3', '5', '7'}
    
    def is_prime_digit(digit):
        return digit in primes
    
    def is_prime(num):
        if num < 2:
            return False
        for i in range(2, int(num ** 0.5) + 1):
            if num % i == 0:
                return False
        return True
    
    def count_partitions(s, k, minLength, start, end, memo):
        if k == 0:
            return 1 if start == end else 0
        if (k, start, end) in memo:
            return memo[(k, start, end)]
        
        total = 0
        for i in range(start + minLength, end):
            if is_prime_digit(s[start]) and not is_prime(int(s[i])):
                total = (total + count_partitions(s, k - 1, minLength, i, end, memo)) % MOD
        
        memo[(k, start, end)] = total
        return total
    
    return count_partitions(s, k, minLength, 0, len(s), {})
    
s = "23542185131"
k = 3
minLength = 2
print(count_beautiful_partitions(s, k, minLength)) 