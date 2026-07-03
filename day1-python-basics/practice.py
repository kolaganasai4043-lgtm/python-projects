def is_palindrome(s):
    s = s.lower().replace(" ", "")
    return s == s[::-1]

def fibonacci(n):
    fib = [0, 1]
    for i in range(2, n):
        fib.append(fib[-1] + fib[-2])
    return fib[:n]

print("Palindrome check:", is_palindrome("Madam"))
print("Fibonacci:", fibonacci(10))
