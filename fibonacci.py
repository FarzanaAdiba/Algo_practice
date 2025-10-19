
#naive approach - T(n) = O(2^n)
def fib_func(n):
    if n<=1:
        return n
    else:
        return fib_func(n-1) + fib_func(n-2)
    
if __name__ == "__main__":
    num = 4
    print(f"Fibonacci of {num} is {fib_func(num)}")
    
#optimized approach using memoization - T(n) = O(n)
#creating memo dictionary
def fib_memo(n, memo={}):
    if n in memo:
        return memo[n]
    if n<=1:
        return n
    memo[n] = fib_memo(n-1, memo) + fib_memo(n-2, memo)
    return memo[n]

if __name__ == "__main__":
    num = 1
    print(f"Fibonacci of {num} using memoization is {fib_memo(num)}")
    
#for printing the sequences:
def fib_seq(n):
    memo={}
    seq=[fib_memo(i, memo) for i in range(n)]
    print(", ".join(map(str, seq)))
        
val=int(input("val = "))
fib_seq(val)
        